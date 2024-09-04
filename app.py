from flask import Flask

app = Flask(__name__)


@app.route("/")
def healthz():
    return "Healthy", 403


app.run(host="0.0.0.0", port=8080)
