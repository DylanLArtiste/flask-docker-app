from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Flask App without Database</h1>
    <h1>Hello, welcome to my website!</h1>
    <p><strong>Your Name:</strong> Quentin Nempont </p>
    <p><strong>Project Name:</strong> challenge1 NET4255</p>
    <p><strong>Version:</strong> V3.1</p>
    <p><strong>Server Hostname:</strong> {socket.gethostbyname(socket.gethostname())}</p>
    <p><strong>Current Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
