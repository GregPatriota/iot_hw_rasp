from app.interface.mqtt.mqtt_client import MQTTInterface


class Subscriber(MQTTInterface):

    def publisher(self, message: str):
        pass

    def on_publish(self, mqttc, obj, mid):
        pass

    def receive(self, client, data, msg):
        print(str(msg))
