from flask import Flask, current_app, make_response, jsonify, request, g
from models.user import User 
from models.post import Post, db
from flask_cors import CORS 
import os

def create_app():
    # define routes , request hooks , define is helper methods associated to the routes 
    # create the flask app 
    app = Flask(__name__)
    # allow CORS FOR ALL ROUTES 
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    # @app.before_request
    # def app_path():
    #     g.path = os.path.abspath(os.getcwd())

    # define routes 
    @app.route('/', methods=['GET'])
    def index():
        # usage of make response 
        responsebody = f'''Hello World'''
        statusCode = 200

        return make_response(responsebody, statusCode)



   # route to get my users in JSON format 
    @app.route('/users', methods=['GET'])
    def get_users():
       users = User.query.all()
       users_data = [{'id' : user.id , 'username': user.username} for user in users]
       return jsonify(users_data)


    
    # returning JSON responses 
    @app.route('/users', methods=['POST'])
    def create_user():
        # multipart data (FORMDATA): uploads / JSON raw , text 
        # json data :   { "username" : "Joseph" }
        data = request.get_json()
        username = data.get('username')
        # utilize my models for ORM Mapping 
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        # return my JSON data 
        return jsonify({'message': "User created successfully", "username" : username})
    
    return app