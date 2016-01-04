import subprocess
from time import strftime

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hit the /reload route to force a reload.'

@app.route('/reload')
def reload():
    print("Forcing a reload.")
    subprocess.call("xdotool keydown ctrl key r; xdotool keyup ctrl".split(" "))

def get_time():
    return strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    app.run()
