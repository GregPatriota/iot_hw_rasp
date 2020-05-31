import paho.mqtt.client as mqtt


class MQTTInterface:

    def __init__(self):
        self.mqtt_c.on_message = self.receive
        self.mqtt_c.on_connect = self.subscribe
        self.mqtt_c.on_publish = self.on_publish
        self.mqtt_c.on_subscribe = self.on_subscribe
        self.mqtt_c.on_log = self.on_log

    def on_publish(self, mqttc, obj, mid):
        # print("mid: " + str(mid))
        pass

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        # LOGGER.format_log(content={"info": "Subscribed: " + str(mid) + " " + str(granted_qos)})
        pass

    def on_log(self, mqttc, obj, level, string):
        # LOGGER.format_log(content={"info": "Log of subscribe"})
        # LOGGER.format_log(content={"info": string})
        pass

    def receive(self, client, data, msg):
        # body = loads(msg.payload)
        pass

    def connect(self, host: str, port: int, user: str, password: str):
        self.mqtt_c = mqtt.Client()
        self.mqtt_c.username_pw_set(username=user, password=password)
        self.mqtt_c.connect(host=host, port=port)

    def publisher(self, message: str):
        self.mqtt_c.publish(payload=message)

    def subscribe(self, client, userdata, flags, rc):
        topic_channel = self.channel.replace(' ', '') + "_rec"
        topic = f"data/{self.user}/sub/{topic_channel}"
        # LOGGER.format_log(content={"info": "Subscribing: " + topic})
        self.mqtt_c.subscribe(topic)

    def listen(self):
        self.mqtt_c.loop_forever()

    def unsubscribe(self, topic: str):
        self.mqtt_c.unsubscribe(topic=topic)

    def disconnect(self):
        self.mqtt_c.disconnect()
