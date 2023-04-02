#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

uint8_t redPin = D0;
uint8_t greenPin = D1;
uint8_t bluePin = D2;

byte i;
bool startup = 0;

char ssid[] = "-your-network-name-";
char pass[] = "-your-wifi-password-";

WiFiUDP UDP;
unsigned int localUdpPort = 53;  // local port to listen on
char packet[255];  // buffer for incoming packets

IPAddress local_IP(192, 168, 1, 127);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress dns1(192, 168, 1, 1);

IPAddress PC_IP(192, 168, 1, 128);  // set your computer's IP as this manually (static)


void setup()
{
  Serial.begin(115200);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);

  if (!WiFi.config(local_IP, gateway, subnet, dns1)) {
   Serial.println("STA Failed to configure");
  }

  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  UDP.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}


void loop()
{
  byte packetSize = UDP.parsePacket();
  if (packetSize)
  {

      Serial.print("Received packet! Size: ");
      Serial.println(packetSize);
      String color = incoming();
      Serial.println(color);

      analogWrite(redPin, color.substring(0,3).toInt());
      analogWrite(greenPin, color.substring(3,6).toInt());
      analogWrite(bluePin, color.substring(6,9).toInt());

  }
}


String incoming()
{
  int len = UDP.read(packet, 255);
  if (len > 0)
  {
    packet[len] = '\0';
  }
  return packet;
}
