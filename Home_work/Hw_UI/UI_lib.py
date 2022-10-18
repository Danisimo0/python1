# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello world</p>"
# if __name__ == "__main__":
#     app.run()


# Task 2
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    text = ""
    for i in range(1, 667):
        text += f"<p>{i}</p>"
    return text


if __name__ == "__main__":
    app.run()
