from flask import Flask, render_template
import pandas as pd

app = Flask(__name__,template_folder='../templates')
df = pd.read_csv('imgsifter/src/static/data/df_classes.csv')

@app.route('/')
def home():
    ## read images from each category and display them 20 at a time. See example below.
    return render_template('sample_page.html',img_name='/data/simplifed-data-only-oranges/1/IMG_6047.png',
        df=df)
@app.route('/add/1',methods=['GET'])
def add_1():
    return 