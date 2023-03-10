from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    with open(os.path.join(os.getcwd(), 'data.txt')) as f:
        content = f.read()
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
