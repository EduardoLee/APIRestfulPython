from flask import Flask, jsonify
from client import Client
app = Flask(__name__)
app.config["MONGO_URI"] = \
    "mongodv://192.168.106.44:27017/DBwaltercoan"
mongo = PyMongo(app)
listClients = [Client (name='Jao', email="sda@univille.br", phone="55464654"),
               Client (name='papum', email="hou@univille.br", phone="454575732"),
               Client (name='zuao', email="asds@univille.br", phone="554744654")
               ]

@app.route('/api/V1.0/client', methods=['GET'])
def get_tasks():
    return jsonify({'clients': [umcli.__dict__ for umcli in listClients]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
