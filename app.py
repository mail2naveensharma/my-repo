import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'I am here - Naveen'

if __name__ == "__main__":
	app.run()

