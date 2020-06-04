"""
Thread Module for Subscriber MQTT
"""
import threading
from time import sleep
from app.interface.mqtt.mqtt_subscriber import Subscriber


class ChannelPool:
    """
    The class to handle all threads for subscriber MQTT
    """
    def __init__(self, user: str, password: str, channel: str):
        self.subs = Subscriber(user=user, password=password, channel=channel)
        self.subs.connect(host='mqtt.prod.konkerlabs.net', port=1883)

    def run(self):
        """
        Runnable method
        """
        channel = threading.Thread(target=self.subs.listen())
        channel.run()
        while True:
            if channel.is_alive():
                sleep(60)
            else:
                break

