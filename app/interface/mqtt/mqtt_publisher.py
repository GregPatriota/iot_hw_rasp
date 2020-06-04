from app.interface.mqtt.mqtt_client import MQTTInterface


class Publisher(MQTTInterface):

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        pass

    def subscribe(self, client, userdata, flags, rc):
        pass

    def listen(self):
        pass
