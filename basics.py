from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)  # inits the fact we are using a RESTful API

class HelloWorld(Resource):

    def get(self, name, test):
        return {"date": f"Hello {name} and {test}!"}
    
    def post(self):
        return {"date": "Posted!"}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")


if __name__ == "__main__":
    app.run(debug=True)
