from app.interface.mqtt.mqtt_client import MQTTInterface, LOGGER
from app.utils.enumerators import LogTypes
from json import loads, JSONDecodeError


class Subscriber(MQTTInterface):

    def publisher(self, message: str):
        pass

    def on_publish(self, mqttc, obj, mid):
        pass

    def receive(self, client, data, msg):
        try:
            body = loads(msg.payload)
            LOGGER.format_log(content={"level": LogTypes.INFO.name, "tag": "[mqtt_client][receive]",
                                       "message": body})
        except JSONDecodeError as err:
            LOGGER.format_log(content={"level": LogTypes.ERROR.name, "tag": "[mqtt_client][receive]",
                                       "message": str(err)})
