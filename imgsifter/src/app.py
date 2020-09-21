from flask import Flask, render_template,redirect, request
import pandas as pd
import shutil
from pathlib import Path

app = Flask(__name__,template_folder='../templates')
df_main = pd.read_csv('imgsifter/src/static/data/df_classes.csv')
df_main.set_index('image_name',inplace=True)
df_main['class'] = df_main['class'].astype('string')

@app.route('/')
@app.route('/topClass/1')
def home():
    df = df_main[df_main['class']=='1']
    return render_template('index.html',df=df,main_class=1,view_status='all')

@app.route('/add/<view_status>/<class_name>/<img_name>',methods=['GET'])
def change_df(view_status,class_name,img_name):
    orig_class = df_main.loc[img_name,'class']
    shutil.move(str(Path('imgsifter/src/static/data/simplifed-data-only-oranges'
    )/Path(df_main.loc[img_name,'class'])/Path(img_name)),str(Path(
        'imgsifter/src/static/data/simplifed-data-only-oranges')/Path(class_name)))
    df_main.loc[img_name,'class']=class_name
    df_main.to_csv('imgsifter/src/static/data/df_classes.csv')

    if 'random' in view_status:
        return redirect('/select_randomly/'+orig_class)
    else: 
        return redirect('/select_all/'+orig_class)


@app.route('/select_all/<string:main_class>',methods=['GET'])
def select_all(main_class):
    df = df_main[df_main['class']==main_class]
    return render_template('index.html',df=df,main_class=main_class,view_status='all')

@app.route('/select_randomly/<string:main_class>',methods=['GET'])
def select_randomly(main_class):
    df = df_main[df_main['class']==main_class].sample(10)
    return render_template('index.html',df=df,main_class=main_class,view_status='random')
