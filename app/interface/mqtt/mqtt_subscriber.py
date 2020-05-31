from app.interface.mqtt.mqtt_client import MQTTInterface


class Subscriber(MQTTInterface):
    def __init__(self):
        pass

    def receive(self, client, data, msg):
        pass
