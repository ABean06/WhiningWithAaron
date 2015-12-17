from flask import Flask, render_template, redirect, url_for

# found this online https://exploreflask.com/forms.html
# from .import app
from .forms import WineForm, ScotchForm


# set variable name app to shorten flask name
app = Flask(__name__)


# Home Page of App. Describe what app about and links to tasting forms
@app.route('/')
def home_page():
    return render_template('home.html')


# HTML page containing Wine Form
@app.route('/wine')
def wine_page():
    form = WineForm()
    return render_template('wine.html', form=form)


# HTML page containing Scotch Form
@app.route('/scotch')
def scotch_page():
    form = ScotchForm()
    return render_template('scotch.html', form=form)


# HTML page containing Cigar Form
@app.route('/cigar')
def cigar_page():
    return render_template('cigar.html')

# says if running this file, treat it as 'main' for the application
if __name__ == '__main__':
    app.run()
