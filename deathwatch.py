import docker
import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()
webhook_url = os.getenv("DISCORD_WEBHOOK")

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]
    date_time = datetime.datetime.fromtimestamp(epoch_time)

    payload = {"content": "O container %s (%s) foi finalizado as %s" % (container_name,container_id,date_time)}
    requests.post(webhook_url, data=payload)
