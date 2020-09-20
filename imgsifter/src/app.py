from flask import Flask, render_template,redirect
import pandas as pd
import shutil
from pathlib import Path

app = Flask(__name__,template_folder='../templates')
df = pd.read_csv('imgsifter/src/static/data/df_classes.csv')
df.set_index('image_name',inplace=True)
df['class'] = df['class'].astype('string')

@app.route('/')
def home():
    ## read images from each category and display them 20 at a time. See example below.
    return render_template('sample_page.html',df=df)
@app.route('/add/<string:class_name>/<string:img_name>',methods=['GET'])
def change_df(class_name=None,img_name=None):
    shutil.move(str(Path('imgsifter/src/static/data/simplifed-data-only-oranges')/Path(df.loc[img_name,'class'])/Path(img_name)),str(Path('imgsifter/src/static/data/simplifed-data-only-oranges')/Path(class_name)))
    df.loc[img_name,'class']=class_name
    df.to_csv('imgsifter/src/static/data/df_classes.csv')

    return redirect('/')