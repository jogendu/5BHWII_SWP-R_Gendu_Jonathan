import requests

url = 'http://127.0.0.1:5000/'

data = {
    'user_name': 'example_user',
    'score': 100
}

response = requests.post(url+"set_score", json=data)

print(response.text)

user_name = 'example_user'

response = requests.get(url+"get_score", params={'user_name': user_name})

print(response.text)

response = requests.post(url+"update_score", json={'user_name': user_name})
print(response.text)

response = requests.post(url+"delete_score", json={'user_name': user_name})
print(response.text)

response = requests.post(url+"set_symboles", json={'user_name': user_name, 'schere_count': 10, 'stein_count': 20, 'papier_count': 30, 'echse_count': 40, 'spock_count': 50})
print(response.text)

response = requests.get(url+"get_symboles", params={'user_name': user_name})

print(response.text)

response = requests.post(url+"update_symboles", json={'user_name': user_name, 'field_name': 'schere_count'})
print(response.text)


response = requests.post(url+"delete_symboles", json={'user_name': user_name})
print(response.text)
