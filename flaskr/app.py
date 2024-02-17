import json
import os
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")    

    print(client_id, client_secret)


    app.run(debug=True, host='0.0.0.0')