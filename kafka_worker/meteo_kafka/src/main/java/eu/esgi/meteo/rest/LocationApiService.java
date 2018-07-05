package eu.esgi.meteo.rest;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

import eu.esgi.meteo.model.LocationModel;

public class LocationApiService {
    private WebTarget locationApi;

    public LocationApiService(String baseUrl) {
        Client client = ClientBuilder.newClient();
        locationApi = client.target(baseUrl);
    }

    public String[] fetchCodesPost(String lat, String lon) {
        WebTarget target = locationApi.path("communes");
        target = target.queryParam("lat",lat);
        target = target.queryParam("lon", lon);
        target = target.queryParam("fields", "nom,code,codesPostaux,codeDepartement,codeRegion,population");
        target = target.queryParam("format", "json");
        target = target.queryParam("geometry", "centre");
        System.out.println(target);
        LocationModel r = target.request(MediaType.APPLICATION_JSON).get(LocationModel.class);
        return r.getCodesPostaux();
    }
}
