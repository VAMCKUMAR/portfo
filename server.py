#here at first we need to activate the virtual environment that we have created. by using <venv>\Scripts\activate.bat

from flask import Flask, render_template, request, redirect
import csv
#import requests
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page>')
def redirection(page):
    return render_template(page)

@app.route('/form', methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		data = request.form.to_dict()
		print(data)
		database2(data)
		return redirect('/acknowledge.html')
	else:
		'something went wrong'

def database(data):
	with open('database.txt', mode='a') as store:
		store.write(f'{data}')
		#or
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		user_data = store.write(f'\n{email}, {subject}, {message}')

def database2(data):
	with open('database.csv', newline='', mode='a') as csv_data:
		csv_writer = csv.writer(csv_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer.writerow([email,subject,message])


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/hello_world')
# def hello_world():
#     return "Wow it's working!!!"

# @app.route('/<user_name>')
# def user_name(user_name = None):
#     return render_template('dynamic.html', name=user_name)

# @app.route('/<user_name>/<int:page_number>')
# def user_with_page(user_name = None, page_number = None):
#     return render_template('dynamicpages.html', name=user_name, page = page_number)


# @app.route('/index.html')
# def index():
# 	return render_template('index.html')

# # def my_world():
# # 	return "My world is here" #it wont work it only concerns about the first function in this given path

# @app.route('/path1')
# def path1():
#     return "I cannot believe it"