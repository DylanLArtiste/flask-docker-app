from flask import Flask, request # type: ignore
from datetime import datetime
import socket
import os
import pymongo # type: ignore
from pymongo import MongoClient # type: ignore

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client['example_db']
collection = db['example_collection']

@app.route('/')
def home():
    # Récupérer l'adresse IP du client et la date actuelle
    client_ip = request.remote_addr
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insérer les informations dans la base de données
    collection.insert_one({"ip": client_ip, "date": current_date})

    # Récupérer les 10 derniers enregistrements
    last_records = list(collection.find().sort("_id", -1).limit(10))

    # Construire une réponse HTML
    records_html = "".join([f"<p>{record['ip']} - {record['date']}</p>" for record in last_records])

    return f"""
    <h1>Flask App with Database</h1>
    <h1>Hello, welcome to my website!</h1>
    <p><strong>Your Name:</strong> Quentin Nempont </p>
    <p><strong>Project Name:</strong> challenge1 NET4255</p>
    <p><strong>Version:</strong> V3.1</p>
    <p><strong>Server Hostname:</strong> {socket.gethostbyname(socket.gethostname())}</p>
    <p><strong>Current Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <h2>Last 10 Records:</h2>
    {records_html}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
