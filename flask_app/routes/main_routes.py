import pandas as pd
from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/', methods=['POST','GET'])
def index():
    if request.method== "POST":
        
        category = request.form["category"]
        minplaytime = int(request.form["minplaytime"])
        maxplaytime = int(request.form["maxplaytime"])
        minplayers = int(request.form["minplayers"])
        maxplayers = int(request.form["maxplayers"])
        averageweight = int(request.form["averageweight"])
        yearpublished = int(request.form["yearpublished"])
        minage = int(request.form["minage"])
        
        # print(category,minplaytime,maxplaytime,minplayers,maxplayers,averageweight,yearpublished,minage)

        X_test = {'yearpublished': yearpublished,
            'minplayers': minplayers,
            'maxplayers': maxplayers,
            'minplaytime': minplaytime,
            'maxplaytime': maxplaytime,
            'minage': minage,
            'averageweight' : averageweight,
            'category' : category
            }
      
        return render_template('result.html')
    return render_template('main.html')
