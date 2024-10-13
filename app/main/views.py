from . import main_bp
from flask import render_template

@main_bp.route('/')
def show_index():
    card1 = {
        'imgsrc': '...',
        'title': 'Intuitive Dashboard',
        'text': 'Manage your projects effortlessly with our user-friendly interface.'
    }
    card2 = {
        'imgsrc': '...',
        'title': 'Client Portal',
        'text': 'Allow your clients to view project progress, approve designs, and provide feedback.'
    }
    card3 = {
        'imgsrc': '...',
        'title': 'Marketing Tools',
        'text': 'Promote your services effectively with customizable marketing templates.'
    }
    card4 = {
        'imgsrc': '...',
        'title': 'Learning Center',
        'text': 'Access tutorials and expert advice to improve your landscaping techniques.'
    }
    features = [card1, card2, card3, card4]
    quote1 = {
        'quote': '"OpenSprouts has streamlined my workflow and made client communication a breeze!"',
        'author': 'Jane D., Landscape Designer'
    }
    quote2 = {
        'quote': '"I can\'t wait to see how this platform helps my business grow!"',
        'author': 'John S., Landscaper'
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