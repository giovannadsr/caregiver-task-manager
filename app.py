from flask import Flask
from src.weather import obter_clima
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Caregiver Task Manager Online"


@app.route("/clima")
def clima():
    return obter_clima()


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)

