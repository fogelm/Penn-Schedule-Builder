import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from penn.registrar import Registrar

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
	return render_template("index.html")

@app.route("/scheduler", methods=['POST'])
def scheduler():
	# courses = open("class_list.txt", 'r')
	# depts = open("department_list.txt", 'r')
	# classes = list()
	# departments = list()
	# r = Registrar('UPENN_OD_emFc_1001364', '6kl4eonkquheuti65e32qick6l')
	# for course in courses:
	# 	classes.append(course)
	# for dep in depts:
	# 	departments.append(dep)
	# courses.close()
	# depts.close()
	# departments.sort()
	if request.method == 'POST':
		return "Hello World"
	else:
		return render_template("scheduler.html")

@app.route("/restrictions")
def restrictions():
	return render_template("restrictions.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)