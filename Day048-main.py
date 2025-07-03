# To Do:
# Add users
# delete users
# Post & put
# look at limit for arguments

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

list_of_usernames = {}

class HelloWorld(Resource):
    def get(self, name, test):
        return {"passed string": name, "passed integer": test}
#         my_string = "Hello "+name+"...   "
#         my_string = my_string * test
#         return {"passed string": name, "passed integer": test, "greeting": my_string}

    
    def post(self, user_name):
        # return {"Hello world": "posted"}
        list_of_usernames.append(user_name)
        return {
            "username": list_of_usernames
        }



# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
api.add_resource(HelloWorld, "/helloworld/")

if __name__ == "__main__":
    app.run(debug=True)
    
    
