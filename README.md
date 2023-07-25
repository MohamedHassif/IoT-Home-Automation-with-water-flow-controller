# IoT-Home-Automation-with-water-flow-controller
Using this project we can control our appliances and water flow in order to save water and time with the help of ESP8266.
Hello Everyone 
This website made using Python Flask Module
so do follow the steps
1. Put all the image,css,video file in folder called as "static" if not create and put
2. then put all the html file in the folder called as "templates" if not create and put
3. and now the above two folders where the main.py is located.
4. then also change IP address  according to the ESP8266.
5. also i have uploaded ESP8266 code which you can run using VS Code or Arduino IDE.
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

ESP8266WebServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  server.on("/process_string", handleString);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}

void handleString() {
  if (server.method() == HTTP_POST) {
    String string_value = server.arg("string_value");
    Serial.print("Received string value: ");
    Serial.println(string_value);
    // Do something with the string value
    server.send(200, "text/plain", "String value received successfully");
  }
}

//string_value is variable which will have value like "a","b",etc
with that value you can turn on or off according to your need.
