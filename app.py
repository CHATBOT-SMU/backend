from flask import Flask, request
from chatbot import academiaChat, buildingChat

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# building
@app.route('/api/building', methods=["POST", "GET"])
def chatBuildingBot():
    option = request.json["choice"]
    print(option)
    print(buildingChat(option))
    return {"answer": buildingChat(option)}

# academies
@app.route('/api/academia', methods=["POST", "GET"])
def chatAcademiaBot():
    option = request.json["choice"]
    print(option)
    response= academiaChat(option)
    print(response)
    return {"answer": response}


if __name__ == '__main__':
    app.run()
