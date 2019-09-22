from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user_action', methods=['GET', 'POST'])
def user_action():
    return render_template('index.html')


@main.route('/recommend_videos', methods=['GET', 'POST'])
def recommend_videos():
    return render_template('index.html')


@main.route('/personal_videos', methods=['GET', 'POST'])
def personal_videos():
    return render_template('index.html')
