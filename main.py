from flask import Flask, request, jsonify
from flask_cors import CORS

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route("/api_server", methods=["GET", "POST"])
def api_server():
    if request.method == "GET":
        return jsonify({
            "status_code": 200,
            "method": "GET",
            "status": "ok"
        })

    if request.method == "POST":
        return jsonify({
            "status_code": 200,
            "method": "POST",
            "status": "ok"
        })


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
