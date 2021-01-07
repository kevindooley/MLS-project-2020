# Machine Learning & Statistics Tasks 2020
Tasks 2020 Assessment by Kevin Dooley

### Background
This repository contains the completed Machine Learning and Statistics Project 2020. The project is worth 50% of the total marks for this module. All aspects of this project are contained in a git repository and submitted up to Moodle prior to the project deadline on the 08th January 2021.

Git must be used document your work and marks will be awarded under the following headings: Research, Development, Consistency and Documentation.

The project description is detailed in full on the GMIT Moodle page under the 'Project 2020 Assessment' PDF.

### Overview of Project
To create a web service that uses machine learning to make predictions based on the data set `powerproduction` which is saved in this repository.  The goal is to produce a model that accurately predicts wind turbin epoweroutput from windspeed values, as in the data set.  You must then develop a web service that will respond wit hpredicted power values based on speed values sent as HTTP requests.

The project mus contain the below as a minimum:
1. Jupyter  notebook  that  trains  a  model  using  the  data  set.
2. Python script that runs a web service based on the model, as above.
3. Dockerfile to build and run the web service in a container.
4. Standard items in a git repository such as a README.


### Getting Started
1. If not already installed, download and install Python 3.
2. Recommend downloading Python via the Anaconda download to get useful additional software including Jupyter and iPython. By downloading Anacoda you will also get essential packages such as; NumPy, Pandas, SciPy already built into Python. All of are used within this project.
3. Download and install a command prompt - recommend Cmder (Windows) or Terminal (Mac).
4. To run this Jupyter notebook on your computer you will need to download the `Project 2020.ipynb` file to your desktop. To do this copy the url https://github.com/kevindooley/MLS-project-2020 which will bring you to the repository. Click the green `Code` button on the screen and then copy the link under the `HTTPS` tab. On the command line, enter `git clone`, paste the url and hit enter. This will then clone the Github repository onto your desktop in your current working directory. 
5. Once cloned/downloaded to your desktop, open your command line
6. Using the 'cd' command on your command line, go to the directory you cloned the .ipynb file to.
7. Type `jupyter notebook` or `jupyter lab` into the command line to open up Jupyter. The Jupyter notebook will then open up in your browser and click on the `Tasks 2020.ipynb` file to view the Jupyter notebook. Note: If your browser does not open with the notebook, go to the command line and it will say `To access the notebook, open this file in a browser:/Or copy and paste one of these URLs:`. Copy one of the provided URLs and paste into a browser of your choosing. The Jupyter homepage containing `Project 2020.ipynb` should be shown on your screen. 
8. All cells should be completed and already executed but if you wish to re-run the cells, click the `Kernel` button and then the `Restart & Clear Output` button if you wish to clear all executions and run each cell one by one manually or click `Restart & Run All` if you want to clear all executions and re-run all cells again automatically.
9. To end viewing of the Jupyter notebook, close your browser showing the notebook. Go to the command line and press `CTRL + C` which will terminate the notebook viewing. 
9. You can also view the Jupyter notebook directly on Github by clicking on the link to my repository https://github.com/kevindooley/MLS-project-2020. All commits to this repository can be viewed on Github.
10. Sometimes, the Jupyter notebook does not always load on Githib, you can also view on nbviewer using the link https://github.com/kevindooley/MLS-project-2020

### Running Virtual Environment
To run this repository you will need certain modules or packages. These are all contained in the requirements.txt file in this repository. To load them onto your virtual machine, follow the below:
1. Open the virtual environment `python -m venv venv`
2. Load the requirements.txt to the virtual environment `pip install -r requirements.txt`
3. Use `pip freeze` to see the packages now installed on your virtual environment.

### Run the server
1. Enter the below onto your command line. This will run the flask server.
```
set FLASK_APP=rando.py
python -m flask run
```
2. To check that connection has been made with the server, run `curl -i http://localhost:5000/` on a new command console. Do not run the above curl on the same console as the flask server. 
3. To access the server, go to your browser of choice and copy in the following url `http://localhost:5000/`. This will bring you directly to the web page that will predict generated power from the wind speed model.
![](flask.png)