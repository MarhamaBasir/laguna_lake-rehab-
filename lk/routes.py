from flask import Flask, render_template, url_for
import os
import secrets
from PIL import Image
from lk import app

@app.route("/")
@app.route("/laguna/lake")
def index():
	return render_template("index.html", title='Laguna Lake')