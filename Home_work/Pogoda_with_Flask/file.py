from bs4 import BeautifulSoup
from flask import Flask
import time

import requests
from bs4 import BeautifulSoup
import random
import threading

app = Flask(__name__)

def get_weather_now(text):
    url = f'https://www.gismeteo.kz/weather-almaty-5205/now/-{text.lower()}'
    html = get_html(url)
    soup = b