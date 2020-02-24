from flask import Flask
from threading import Thread
from flask import render_template
is_down = False
app = Flask('')

@app.route('/')
def home():
  if is_down == False:
    return render_template('online.html')
  else:
    return render_template('offline.html')

def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
