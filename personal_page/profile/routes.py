from flask import render_template, redirect, url_for, request, Blueprint, current_app as app
from . import models
import git

profile_bp = Blueprint('profile', __name__, static_url_path="",
                       static_folder="static",
                       template_folder="templates"
                       )


@profile_bp.route("/")
def profile():
    return 'Esta es la base de algo grande, y no la pineapple'


# Update the repo in GitHub and pull the changes to the server
@profile_bp.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/Oscaran02/personal-page')
        x_hub_signature = request.headers.get("X-Hub-Signature")
        print(app.config['SECRET_KEY'])
        if not models.is_valid_signature(x_hub_signature, request.data, app.config['SECRET_KEY']):
            return 'Invalid signature', 401
        origin = repo.remotes.origin
        origin.pull()
        return 'Update successful', 200
