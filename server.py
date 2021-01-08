# import flask for application
from flask import Flask,url_for, request,redirect, abort,jsonify
# numpy for numerical work.
import numpy as np

#import keras - https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
import tensorflow.keras as kr
from numpy import loadtxt
from keras.models import load_model

# Create a new web app.
app = Flask(__name__,static_url_path='', static_folder='static')

# load neural network model
model = load_model("neural_model.h5")


# Add root(home) route.
# show static page index.html at root
@app.route("/")
def home():
  return app.send_static_file('index.html')

# prediction deployment -https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
#https://levelup.gitconnected.com/deploy-a-predictive-model-with-flask-33c1976293cc
@app.route("/api/predict/<int:wind>", methods=["GET"]) #if int entered
@app.route("/api/predict/<float:wind>", methods=["GET"]) # if float entered
def prediction(wind):
  neural = model.predict([wind]) # creating variable neural which contains model prediction 
  return str(neural[0][0]) # return result

#practice to connact to server
# Add uniform route.
# @app.route('/api/uniform')
# def uniform():
#   return {"value": np.random.uniform()}

# # Add normal route.
# @app.route('/api/normal')
# def normal():
#   return {"value": np.random.normal()}

if __name__ == "__main__":
  app.run(debug= True) 