package com.example.demo;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaMessageListener {

    @KafkaListener(topics = "crypto-topic", groupId = "crypto-group")
    public void listen(String message) {
        System.out.println("Received message: " + message);
    }
}
