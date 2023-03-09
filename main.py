from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from resources import users_resource
from resources import jobs_resource
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run()
