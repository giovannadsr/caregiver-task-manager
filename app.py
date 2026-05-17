from flask import Flask
from src.weather import obter_clima

app = Flask(__name__)


@app.route("/")
def home():
    return "Caregiver Task Manager Online"


@app.route("/clima")
def clima():
    return obter_clima()


if __name__ == "__main__":
    app.run(debug=True)
