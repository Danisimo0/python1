import os
import requests
from bs4 import BeautifulSoup
from flask import Flask

#
app = Flask(__name__)
url = "https://tengrinews.kz/weather/almaty/day/"


#
@app.route("/")
def pars():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    temp = soup.find_all('div', {'class': "temp"})
    objs2 = [x.text.strip() for x in temp]
    return f"<h1>Today in Almaty : {objs2[-1]}</h1>"


if __name__ == '__main__':
    app.run()
