from . import main_bp
from app import db
from app.models import Waitlist
from flask import render_template, request, redirect, url_for, current_app, jsonify, flash
import requests
import json


@main_bp.route('/')
def show_index():
    card1 = {
        'imgsrc': "img/dashboard.png",
        'title': 'Intuitive Dashboard',
        'text': 'Manage your projects effortlessly with our user-friendly interface.'
    }
    card2 = {
        'imgsrc': 'img/clientportal.png',
        'title': 'Client Portal',
        'text': 'Allow your clients to view project progress, approve designs, and provide feedback.'
    }
    card3 = {
        'imgsrc': 'img/marketing.png',
        'title': 'Marketing Tools',
        'text': 'Promote your services effectively with customizable marketing templates.'
    }
    card4 = {
        'imgsrc': 'img/education.png',
        'title': 'Learning Center',
        'text': 'Access tutorials and expert advice to improve your landscaping techniques.'
    }
    features = [card1, card2, card3, card4]
    quote1 = {
        'quote': '"All factors go into doing your best to give a quote to the customer, really like, as soon as possible. You know your closing rates are gonna increase most definitely. If you\'re able to give a quote on the spot."',
        'author': 'Rob Fajardo, Trenton Falls, Idaho'
    }
    quote2 = {
        'quote': '"I can\'t wait to see how this platform helps my business grow!"',
        'author': 'John D., Landscaper'
    }
    quotes = [quote1, quote2]
    question1 = {
        'headingId': 'question1',
        'collapseId': 'question1Collapse',
        'question': 'What is OpenSprouts?',
        'answer': 'OpenSprouts is an all-in-one platform designed to help landscapers manage their businesses effectively.'
    }
    question2 = {
        'headingId': 'question2',
        'collapseId': 'question2Collapse',
        'question': 'How does the waitlist work?',
        'answer': 'Sign up now, and you’ll be notified as soon as we launch, gaining early access to our features.'
    }
    question3 = {
        'headingId': 'question3',
        'collapseId': 'question3Collapse',
        'question': 'Is there a cost to join the waitlist?',
        'answer': 'No, signing up for the waitlist is completely free!'
    }
    questions = [question1, question2, question3]
    return render_template('main/index.html', features=features, quotes=quotes, questions=questions, title="Welcome")

@main_bp.route('/waitlist', methods=['POST'])
def add_to_waitlist():
    captcha_response = request.get_json
    if request.method == "POST":
        email = request.form.getlist('email')

        if is_human(captcha_response):
            waitlist_item = Waitlist(email=email)
            db.session.add(waitlist_item)
            db.session.commit()
            status = "Email Saved!"
        else:
            status = "Sorry! Bots are not allowed."
        
        flash(status)
    return redirect(url_for("main.thank_you"))

def is_human(captcha_response):
    secret = current_app.config['CAPTCHA_SECRET_KEY']
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

@main_bp.route('/thank_you')
def thank_you():
    return render_template('main/thank_you.html', title="Thank You")