from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
# from flask_pymongo import PyMongo
# mongo = PyMongo(app)
# app.config['MONG_URI'] = 'mongodb://127.0.0.1:27017/Microblog'

def create_app():
    # main
    app = Flask(__name__)
    # client = MongoClient("mongodb://127.0.0.1:27017/")
    # app.db = client.Microblog

    entries = []

    @app.route("/", methods = ["GET", "POST"])
    def home():
        # print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            entries.append((entry_content, formatted_date))

        return render_template("index.html", entries = entries)

    return app    
   