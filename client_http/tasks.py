import requests
import time

def get_status_code():
  api_url = "http://app:5001/renda-fixa"
  status = 200
  while status == 200:
    response = requests.get(api_url) 
    print(response.status_code)
    status = response.status_code
    time.sleep(10)
    return status