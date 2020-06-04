"""
Main module
"""
from app.interface.mqtt.mqtt_channel_subscriber import ChannelPool
from env_config import KONKER_USR, KONKER_PWD


def configure_device():
    pass


def start_device():
    task = ChannelPool(user=KONKER_USR, password=KONKER_PWD, channel='test')
    task.run()


if __name__ == "__main__":
    configure_device()
    start_device()

