from flask import render_template, request, flash, url_for, Blueprint, redirect

main= Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', title='Main')

@main.route('/first_rule')
def first_rule():
    return render_template('first_rule.html')

@main.route('/second_rule')
def second_rule():
    return render_template('second_rule.html')

@main.route('/third_rule')
def third_rule():
    return render_template('thir_rule.html')

@main.route('/fourth_rule')
def fourth_rule():
    return render_template('fourth_rule.html')

@main.route('/fifth_rule')
def fifth_rule():
    return render_template('fifth_rule.html')

@main.route('/sixth_rule')
def sixth_rule():
    return render_template('sixth_rule.html')