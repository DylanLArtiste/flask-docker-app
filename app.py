from flask import Flask # type: ignore
from datetime import datetime
import socket

app = Flask(__name__)

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
