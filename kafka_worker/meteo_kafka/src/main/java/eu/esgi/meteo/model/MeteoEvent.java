package eu.esgi.meteo.model;

public class MeteoEvent {

    public String IDOMMstation;
    public String Dateprelevement;
    public String Pressionauniveaumer;
    public String Temperature;
    public String Pointderosee;
    public String Humidite;
    public String Coordonnees;
    public String  Nom;
    public String codePos;
    public String[] codesPostaux;

    public String getIDOMMstation() {
        return IDOMMstation;
    }

    public String getDateprelevement() {
        return Dateprelevement;
    }

    public String getPressionauniveaumer() {
        return Pressionauniveaumer;
    }

    public String getTemperature() {
        return Temperature;
    }

    public String getPointderosee() {
        return Pointderosee;
    }

    public String getHumidite() {
        return Humidite;
    }

    public String getCoordonnees() {
        return Coordonnees;
    }

    public String getNom() {
        return Nom;
    }

    public String getCodePos() { return codePos; }

    public String[] getCodesPostaux() {
        return codesPostaux;
    }

    public void setCodesPostaux(String[] codesPostaux) {
        this.codesPostaux = codesPostaux;
    }

    public String getLat() {
        return this.Coordonnees.split(",")[0].trim();
    }

    public String getLon() {
        return this.Coordonnees.split(",")[1].trim();
    }

}
