from flask_restful import abort, Resource
from data import db_session
from data.jobs import Jobs
from flask import jsonify
from resources.pars_jobs import parser
from datetime import datetime


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                                                  'end_date', 'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify({'job': [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                                                   'end_date', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = Jobs(job=args['job'],
                   team_leader=args['team_leader'],
                   collaborators=args['collaborators'],
                   work_size=args['work_size'],
                   start_date=args['start_date'],
                   end_date=args['end_date'],
                   is_finished=args['is_finished'])
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})
