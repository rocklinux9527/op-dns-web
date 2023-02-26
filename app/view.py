from flask import Blueprint
from flask import request, render_template
import subprocess

mainUrl = Blueprint('/login', __name__)
@mainUrl.route('/', methods=['GET', 'POST'])
def loginMain():
    if request.method == "GET":
        return render_template('login.html')





