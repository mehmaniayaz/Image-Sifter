from flask import Flask, render_template,redirect
import pandas as pd

app = Flask(__name__,template_folder='../templates')
df = pd.read_csv('imgsifter/src/static/data/df_classes.csv')
df.set_index('image_name',inplace=True)
df['class'] = df['class'].astype('string')

@app.route('/')
def home():
    ## read images from each category and display them 20 at a time. See example below.
    return render_template('sample_page.html',
    img_name='/data/simplifed-data-only-oranges/1/IMG_6047.png',
     df=df,ip=0)
@app.route('/add/<string:i>',methods=['GET'])
def change_df(i=None):
    df.loc['IMG_6047.png','class']=i
    return redirect('/')