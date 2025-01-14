from flask import Flask, app # type: ignore
from datetime import datetime
import socket
import os
from pymongo import MongoClient # type: ignore


mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["my_database"]  # Nom de la base de données
mongo_status = "Connected"

@app.route('/')
def home():
    return f"""
    <h1>Hello, welcome to my website!</h1>
    <p><strong>Your Name:</strong> Quentin Nempont </p>
    <p><strong>Project Name:</strong> challenge1 NET4255</p>
    <p><strong>Version:</strong> V1</p>
    <p><strong>Server Hostname:</strong> {socket.gethostname()}</p>
    <p><strong>Current Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
