package eu.esgi.meteo;

import eu.esgi.meteo.types.SerdeFactory;
import eu.esgi.meteo.model.MeteoEvent;
import eu.esgi.meteo.rest.LocationApiService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.Consumed;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;

import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class MeteoProcessor {
    public static void main(final String[] args) {

        System.out.println("######## METEO STREAM PROCESSOR ########");
        System.out.println("Initialize app...");
        final String bootstrapServers = args.length > 0 ? args[0] : "localhost:29092";
        String applicationId = "transform-meteo-stream";
        String clientId = "transform-meteo-stream-client";
        String sourceTopic = "raw_station_data";
        System.out.println("Broker address: " + bootstrapServers);
        final Properties streamsConfiguration = new Properties();
        streamsConfiguration.put(StreamsConfig.APPLICATION_ID_CONFIG, "transform-meteo-stream");
        streamsConfiguration.put(StreamsConfig.CLIENT_ID_CONFIG, "transform-meteo-stream-client");
        streamsConfiguration.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        streamsConfiguration.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.ByteArray().getClass().getName());
        streamsConfiguration.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass().getName());
        System.out.println("Application id: " + applicationId);
        System.out.println("Application id: " + clientId);
        System.out.println("Source topic: " + sourceTopic);

        final Serde<String> stringSerde = Serdes.String();
        final Map<String, Object> serdeProps = new HashMap<>();
        final Serde<MeteoEvent> MeteoEventSerde = SerdeFactory.createSerde(MeteoEvent.class, serdeProps);
        ObjectMapper mapper = new ObjectMapper();

        LocationApiService locationApi = new LocationApiService("https://geo.api.gouv.fr/");

        final StreamsBuilder builder = new StreamsBuilder();

        final KStream<String, MeteoEvent> meteoStream = builder
                .stream(sourceTopic, Consumed.with(stringSerde, MeteoEventSerde))
                .mapValues(ev -> {
                    try{
                        System.out.println(mapper.writeValueAsString(ev));
                        ev.setCodesPostaux(locationApi.fetchCodesPost(ev.getLat(),ev.getLon()));
                    } catch (JsonProcessingException ex) {
                        System.out.println("Error writing ev");
                        return ev;
                    }
                    return ev;
                });

        final KafkaStreams streams = new KafkaStreams(builder.build(), streamsConfiguration);
        streams.cleanUp();
        streams.start();
        Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
    }
}
