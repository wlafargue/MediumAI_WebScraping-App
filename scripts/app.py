#!/usr/bin/env python
from flask import Flask, render_template, redirect
from scripts import Database, scrape

# Initialize Flask
app = Flask(__name__)

# MongoDB server
db = Database("localhost", 27017, "my_db")
col = db.init_collection("my_col")

def close_app():
    """Close connections to Mongo database."""
    db.close()

# Default route
@app.route("/")
def index():
    # Find Mongo data
    data = db.find_one(col)
    return render_template("templates/index.html", 
                           data=data)

# Scrape route
@app.route("/scrape")
def scraper():
    # Run the scrape function
    data = scrape()
    # Update the Mongo database
    db.update_many(col, {}, data, upsert=True)
    return redirect("/", code=302)
