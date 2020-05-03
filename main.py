#!/usr/bin/env python
#~ from flask import Flask, flash, redirect, render_template, request, url_for

#~ app = Flask(__name__)

from app import app

if __name__ == '__main__':
    app.run(debug=True)
