package eu.esgi.meteo.model;

public class MeteoEvent {

    public String IDOMMstation;
    public String Dateprelevement;
    public String Pressionauniveaumer;
    public Double Temperature;
    public Double Pointderosee;
    public Double Humidite;
    public String Coordonnees;
    public String  Nom;
    public String codeDep;
    //public String[] codesPostaux;

    public String getIDOMMstation() {
        return IDOMMstation;
    }

    public String getDateprelevement() {
        return Dateprelevement;
    }

    public String getPressionauniveaumer() {
        return Pressionauniveaumer;
    }

    public Double getTemperature() {
        return Temperature;
    }

    public Double getPointderosee() {
        return Pointderosee;
    }

    public Double getHumidite() {
        return Humidite;
    }

    public String getCoordonnees() {
        return Coordonnees;
    }

    public String getNom() {
        return Nom;
    }

    public String getCodeDep() { return codeDep; }

    /*public String[] getCodesPostaux() {
        return codesPostaux;
    }

    public void setCodesPostaux(String[] codesPostaux) {
        this.codesPostaux = codesPostaux;
    }
*/
    public String getLat() {
        return this.Coordonnees.split(",")[0].trim();
    }

    public String getLon() {
        return this.Coordonnees.split(",")[1].trim();
    }

    public void setCodeDep(String codeDep) {
        this.codeDep = codeDep;
    }

}
