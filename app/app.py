import os
import logging

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)

metrics = PrometheusMetrics(app)

APP_NAME = os.getenv("APP_NAME", "devsecops-demo")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
INSTANCE_NAME = os.getenv("INSTANCE_NAME", "app-01")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def index():
    logger.info("Request received on root endpoint")

    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "instance": INSTANCE_NAME,
        "message": "Final Exam application is running for DevOps Course"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION,
        "instance": INSTANCE_NAME
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "instance": INSTANCE_NAME
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )