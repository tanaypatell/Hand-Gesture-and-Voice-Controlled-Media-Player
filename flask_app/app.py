# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:15:21 2021

@author: Tanay
"""
from flask import Flask, request, render_template, redirect
import os
import time

from flask.helpers import url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index.html", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/mediaList.html", methods=["GET", "POST"])
def mediaList(): 
    return render_template("mediaList.html")


@app.route("/video.html", methods=["GET", "POST"])
def video():
    return render_template("video.html")
    

@app.route("/hand_gesture", methods=["GET"])
def hand_gesture():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("\\")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "\\".join(path_list)
        print(final_path)
        os.chdir(final_path+"\\Hand_gesture")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python Hand_Gesture.py")
        
    return redirect(url_for('home'))
     

if __name__ == "__main__":
    app.debug = False
    app.run()