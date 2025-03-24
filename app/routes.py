from flask import Blueprint, render_template, request, redirect, url_for
# from .models import Aluno

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('base.html')

@main_routes.route('/teste')
def teste():
    return render_template('teste.html')