from flask import Flask, render_template

app = Flask(__name__,template_folder='../templates')


@app.route('/')
def home():
    ## read images from each category and display them 20 at a time. See example below.
    return render_template('sample_page.html',img_name='/data/simplifed-data-only-oranges/1/IMG_6047.png')
