from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:123@localhost/recipe'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://lmlvkvpmnrigwx:470b839cbb4d2a62af7b989a43bef8310cce50b8e804df9890cadfb9c405f262@ec2-54-208-11-146.compute-1.amazonaws.com:5432/d830gasejdt0fd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)



class recipeinfo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    recipe_title=db.Column(db.String(100))
    recipe_detail=db.Column(db.String(2000))

    def __init__(self, recipe_title, recipe_detail):
        self.recipe_title=recipe_title
        self.recipe_detail=recipe_detail

# with app.app_context():
#     db.create_all()



@app.route('/')
def index():
    result=recipeinfo.query.all()
    # return '<h1>Secret Receipes!</h1>'
    # menu=["cheecake","fires","beansoup"]
    return render_template('index.html', result=result)
   # val1='cheesecake recipe', menu=menu, 
  

@app.route('/recipeform')
def recipeform():
    return render_template('recipeform.html')


@app.route('/confirmation', methods=['POST'])
def confirmation():
    if request.method=='POST':
     recipename=request.form['recipename']
     recipedetail=request.form['recipedetails']
     recipedata=recipeinfo(recipename,recipedetail)
     db.session.add(recipedata)
     db.session.commit()  
    return redirect(url_for('index'))




# @app.route('/about')
# def about():
#     return '<h1>About this secret Recipes...</h1>'


# @app.route('/detail')
# def detail():
#     return '<h1>DETAILS about Secret Receipes !</h1>'