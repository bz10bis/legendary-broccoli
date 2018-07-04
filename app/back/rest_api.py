# -*- coding: UTF-8 -*-

import json as simplejson
import socket
import json
from kafka import KafkaConsumer
from kafka import TopicPartition

import cherrypy
import sys
from cherrypy import _cperror
from datetime import datetime
from datetime import timedelta
import random
import sys
from threading import Thread
import time

_demo = False

_flag_init = False
__version__ = '1.0'


meteo_datas = {}

class Consumer_meteo(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        global meteo_datas
        topic = TopicPartition('meteo', 0)
        c = KafkaConsumer(bootstrap_servers='10.33.1.131:29092')
        c.assign([topic])

        for msg in c:
            row = json.loads(msg.value)
            meteo_datas[row['IDOMMstation']] = row

# ----------- gestion de jsonp callback -----------------#
def jsonp(func):
    def ftemp(self, *args, **kwargs):
        callback, _ = None, None
        if 'callback' in kwargs and '_' in kwargs:
            callback, _ = kwargs['callback'], kwargs['_']
            del kwargs['callback'], kwargs['_']
        ret = func(self, *args, **kwargs)
        # cherrypy.response.headers['Content-Type'] = "APPLICATION/JSON"
        if callback is not None:
            ret = '%s(%s)' % (callback, simplejson.dumps(ret))
        return ret

    return ftemp


# Récupère les msg envoyés par un broker kafka
class get_meteo(object):
    @jsonp
    def index(self, args):
        data = {"test": {"reponse": meteo_datas}}
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        return simplejson.dumps(data)

    index.exposed = True


# gestion des requ�tes
class RacineServeur(object):
    meteo = get_meteo()


if True:  # demarrage serveur
    try:
        ip = socket.gethostbyname(socket.gethostname())
        _ipServeur = socket.gethostbyname(socket.gethostname())
    except:
        ip = '127.0.0.1'

    port = 8000
    requette = 10

    for i in sys.argv:
        if i.upper().find('-IP:') == 0:
            ip = i.split(':')[1]
        if i.upper().find('-REQUEST:') == 0:
            requette = int(i.split(':')[1])
        if i.upper().find('-PORT:') == 0:
            try:
                port = int(i.split(':')[1])
            except:
                port = 8000

    print("**   Server xxxxxxx  **")
    print("* Version Server: " + __version__)
    print("")
    print("* Serveur IP: " + ip, "   Port: ", port)
    print("* Nombre de requettes: ", requette)
    print("")

    if True:  # (Licence!=None):
        print("--> demarrage en cours... ")
        try:

            server_config = {
                'server.socket_host': ip,
                'server.socket_port': port,
                'server.numthreads': requette,
                'server.thread_pool': requette,
                # 'log.error_file': 'SingleLine.log',
                'environment': 'production'
            }

            cherrypy.config.update(server_config)

            print("Lancement du serveur json")
            try:
                print("--> SERVEUR PRET")
                cherrypy.tree.mount(RacineServeur())
                print("--> OK")
                cherrypy.engine.start()

                # Création des threads consumer
                thread_1 = Consumer_meteo()
                # Lancement des threads
                thread_1.start()

                cherrypy.engine.block()
            finally:
                print("****** SERVEUR KO **********")
                cherrypy.engine.stop()
                cherrypy.engine.block()

        except Exception:
            print("--> probleme de demarrage du serveur ---")

            print("erreur=", Exception)
