import pickle
import pandas as pd

pipe = None

with open('model.pkl','rb') as pikle_file:
    pipe = pickle.load(pikle_file)


#test the model
X_test = {'yearpublished': [2010],
          'minplayers': [2],
          'maxplayers': [4],
          'minplaytime': [30],
          'maxplaytime': [60],
          'minage': [8],
          'averageweight' : [4.0],
          'category' : ["Card Game"]
          }
X_test = pd.DataFrame(X_test)
y_pred = pipe.predict(X_test)
print("오늘의 보드게임은",list(y_pred)[0])
