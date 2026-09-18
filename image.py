from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route("/image")
def image():
    url = "2rhrh.jpg"
    r = requests.get(url)

    return Response(
        r.content,
        status=r.status_code,
        content_type=r.headers.get("Content-Type", "image/jpg")
    )

if __name__ == "__main__":
    app.run()
