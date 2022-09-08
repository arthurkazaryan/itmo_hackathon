import requests
import datetime

# GET REQUEST TO CUSTOMERS DATABASE
requests_get_data = requests.get('http://127.0.0.1:8000/api/v1/get/customers')
requests_get_data.json()

# POST REQUEST TO CUSTOMERS DATABASE
datetime_from = datetime.datetime.now() - datetime.timedelta(hours=1)
datetime_to = datetime.datetime.now()

post_data = {
    'count': 30,
    'warnings': 3,
    'mean_time': 88,
    'user': 1,
    'camera': 1,
    'date_from': datetime_from,
    'date_to': datetime_to
}

requests_post_data = requests.post(
    'http://127.0.0.1:8000/api/v1/post/customers',
    data=post_data
)
print(requests_post_data.json())
