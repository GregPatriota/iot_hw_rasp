"""
Main module
"""
import threading
import time
from env_config import CONNECTION_STRING, DEVICE_ID
import random
import sys
from json import dumps
import paho.mqtt.client as mqtt


if __name__ == "__main__":
    mqttc = mqtt.Client()
    mqttc.username_pw_set('i1nuk5re363k', 'muPvapM6lQ0X')
    mqttc.connect("mqtt.prod.konkerlabs.net", 1883)
    otaro_list = list()
    otaro_list.append({'msg': 'Hello World'})
    otaro_list.append({'msg': 'Otaru'})
    otaro_list.append({'msg': 'Nood!'})
    mqttc.publish('data/i1nuk5re363k/pub/test', dumps({'lista': otaro_list}))
    print("OK!")

