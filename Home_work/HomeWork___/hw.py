from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    text = ""
    for i in range(1, 1000):
        text += f"<p>{i}</p>"
    return text
# покапался на Хероку, еще не разобрался