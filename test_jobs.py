from requests import delete, post, get
import datetime

print(datetime.datetime(year=2023, month=1, day=1).)
"""print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/3').json())"""
print(post('http://localhost:5000/api/v2/jobs', json={'job': 'Покоритель марсианских гор',
                                                      'team_leader': 1,
                                                      'collaborators': '1, 2',
                                                      'work_size': 15,
                                                      'start_date': datetime.datetime(year=2023, month=1, day=1).date(),
                                                      'end_date': datetime.datetime(year=2023, month=1, day=30).date(),
                                                      'is_finished': False}).json())