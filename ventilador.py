import paho.mqtt.client as mqtt

broker_address = "localhost" 
broker_port = 1883 
name = "ventilador"
topic = "pressao"

print("Ventilador")

# Recebe e printa o tópico e a mensagem
def message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# Cria o cliente e atribui a função message à sua propriedade
client = mqtt.Client(name)
client.on_message = message

client.connect(broker_address, broker_port, 300) # Último argumento é o tempo máximo de espera
client.subscribe(topic)
client.loop_forever()