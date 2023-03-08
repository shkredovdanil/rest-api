from requests import get, delete, post

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/2').json())
print(post('http://localhost:5000/api/v2/users', json={'name': 'Алексей', 'surname': 'Лазарев', 'age': 16,
                                                       'speciality': 'радиотехник', 'address': 'module_8',
                                                       'position': 'Пайка микросхем', 'email': 'l@gmail.com', 'hashed_password': '123'}).json())
print(delete('http://localhost:5000/api/v2/users/7').json())
print(post('http://localhost:5000/api/v2/users', json={'name': 'Алексей', 'surname': 'Лазарев', 'age': 'абракадабра',
                                                       'speciality': 'радиотехник', 'address': 'module_8',
                                                       'position': 'Пайка микросхем', 'email': 'l@gmail.com', 'hashed_password': '123'}).json())

print(post('http://localhost:5000/api/v2/users', json={'name': 'Алексей', 'surname': 'Лазарев', 'age': 16,
                                                       'speciality': 'радиотехник', 'address': 'module_8',
                                                       'position': 'Пайка микросхем', 'email': 'l@gmail.com'}).json())
print(delete('http://localhost:5000/api/v2/users/1234').json())