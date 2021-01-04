# import flask for application
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root(home) route.
# show static page index.html at root
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}