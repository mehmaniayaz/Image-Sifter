from flask import Flask, render_template,redirect
import pandas as pd
import shutil
from pathlib import Path

app = Flask(__name__,template_folder='../templates')
df_main = pd.read_csv('imgsifter/src/static/data/df_classes.csv')
df_main.set_index('image_name',inplace=True)
df_main['class'] = df_main['class'].astype('string')

@app.route('/')
def home():
    df = df_main[df_main['class']=='1']
    return render_template('sample_page.html',df=df,main_class=1)
@app.route('/add/<string:class_name>/<string:img_name>',methods=['GET'])
def change_df(class_name=None,img_name=None):
    shutil.move(str(Path('imgsifter/src/static/data/simplifed-data-only-oranges'
    )/Path(df.loc[img_name,'class'])/Path(img_name)),str(Path(
        'imgsifter/src/static/data/simplifed-data-only-oranges')/Path(class_name)))
    df.loc[img_name,'class']=class_name
    df.to_csv('imgsifter/src/static/data/df_classes.csv')

    return redirect('/')

# @app.route('/select_all',methods=['GET'])

# @app.route('/select_randomly',methods=['GET'])

@app.route('/add/topClass/<string:main_class>',methods=['GET'])
def change_main_class(main_class):
    df = df_main[df_main['class']==main_class]
    return render_template('sample_page.html',df=df,main_class=main_class)