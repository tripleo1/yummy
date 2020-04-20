#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from datetime import datetime
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name': 'Toronto'}, {'name': 'Montreal'}, {'name': 'Calgary'},
              {'name': 'Ottawa'}, {'name': 'Edmonton'}, {'name': 'Mississauga'},
              {'name': 'Winnipeg'}, {'name': 'Vancouver'}, {'name': 'Brampton'},
              {'name': 'Quebec'}])


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)


@app.route("/hello", methods=['GET', 'POST'])
def hello_there2():
    return hello_there(request.form.get("name"))

@app.route("/hello/<name>")
def hello_there(name):

    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


if __name__ == '__main__':
    app.run(debug=True)
