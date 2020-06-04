import paho.mqtt.client as mqtt
from app.utils.logger import FormatLog
from app.utils.enumerators import LogTypes

LOGGER = FormatLog()


class MQTTInterface:

    def __init__(self, user: str, password: str, channel: str):
        self.mqtt_c = mqtt.Client()
        self.mqtt_c.on_message = self.receive
        self.mqtt_c.on_connect = self.subscribe
        self.mqtt_c.on_publish = self.on_publish
        self.mqtt_c.on_subscribe = self.on_subscribe
        self.mqtt_c.on_log = self.on_log
        self.user = user
        self.password = password
        self.channel = channel

    def on_publish(self, mqttc, obj, mid):
        LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][on_publish]",
                                   "message": "mid: " + str(mid)})

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][on_subscribe]",
                                   "message": "Subscribed: " + str(mid) + " " + str(granted_qos)})

    def on_log(self, mqttc, obj, level, string):
        LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][on_log]",
                                   "message": "level=" + level + "text=" + string})

    def receive(self, client, data, msg):
        LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][receive]",
                                   "message": str(msg.payload)})

    def connect(self, host: str, port: int):
        try:
            self.mqtt_c.username_pw_set(username=self.user, password=self.password)
            self.mqtt_c.connect(host=host, port=port)
        except Exception as err:
            LOGGER.format_log(content={"level": LogTypes.ERROR.name, "tag": "[mqtt_client][connect]",
                                       "message": err})

    def publisher(self, message: str):
        try:
            self.mqtt_c.publish(payload=message)
            LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][publisher]",
                                       "message": "The package was sent..."})
        except Exception as err:
            LOGGER.format_log(content={"level": LogTypes.ERROR.name, "tag": "[mqtt_client][publisher]",
                                       "message": err})

    def subscribe(self, client, userdata, flags, rc):
        try:
            topic_channel = self.channel.replace(' ', '') + "_rec"
            topic = f"data/{self.user}/sub/{topic_channel}"
            self.mqtt_c.subscribe(topic)
            LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][subscribe]",
                                       "message": "Connection successfully established..."})
        except Exception as err:
            LOGGER.format_log(content={"level": LogTypes.ERROR.name, "tag": "[mqtt_client][subscribe]",
                                       "message": err})

    def listen(self):
        self.mqtt_c.loop_forever()

    def unsubscribe(self, topic: str):
        self.mqtt_c.unsubscribe(topic=topic)

    def disconnect(self):
        self.mqtt_c.disconnect()
