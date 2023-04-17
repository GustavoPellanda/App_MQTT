import paho.mqtt.client as mqtt

broker_address = "localhost" 
broker_port = 1883 
name = "sensor_pressao"
topic = "pressao"

client = mqtt.Client(name)
client.connect(broker_address, broker_port)

while True:
    data = input("Sensor de Pressão: ")
    client.publish(topic, data)
    