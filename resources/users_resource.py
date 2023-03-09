from flask_restful import abort, Resource
from data import db_session
from data.users import User
from flask import jsonify
from resources.pars_users import parser
from datetime import datetime


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    user = session.query(User).get(users_id)
    if not user:
        abort(404, message=f"User {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        user = session.query(User).get(users_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'surname', 'email', 'age', 'position', 'speciality', 'address', 'modified_date'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        news = session.query(User).get(users_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('name', 'surname', 'email', 'age', 'position', 'speciality', 'address', 'modified_date')) for item in
            users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            email=args['email'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            hashed_password=args['hashed_password'],
            modified_date=datetime.now()
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
