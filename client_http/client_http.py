from flask import Flask
from threading import Thread
from tasks import get_status_code

app = Flask("app")


@app.route("/")
def index():
  
  thr = Thread(target=get_status_code)
  thr.daemon = True
  thr.start()
  return "Welcome to client http!"

if __name__ == '__main__':
  app.run(port="6001", host="0.0.0.0")

