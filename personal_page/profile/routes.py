from flask import render_template, redirect, url_for, request, Blueprint, current_app as app
from . import models
import git

profile_bp = Blueprint('profile', __name__, static_url_path="",
                       static_folder="static",
                       template_folder="templates"
                       )


@profile_bp.route("/")
def profile():
    return 'Exentric update'


@profile_bp.route("/update_server", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/Oscaran02/personal-page')
        origin = repo.remotes.origin
        origin.pull()
        return 'Update successful', 200
    if request.method == 'GET':
        return 'it is working', 200

