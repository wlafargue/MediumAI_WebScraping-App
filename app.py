#!/usr/bin/env python
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from utils import scrape

# Initialize Flask
app = Flask(__name__)

# MongoDB server
client = MongoClient("localhost", 27017)
db = client.flask_db
collection = db.collection

# Default route
@app.route("/")
def index():
    # Find Mongo data
    listings = collection.find_one()
    return render_template("index.html", 
                           collections=listings)

# Scrape route
@app.route("/scrape")
def scraper():
    # Run the scrape function
    listings_data = scrape()
    # Update the Mongo database
    collection.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

# Run application
if __name__ == "__main__":
    app.run(debug=True)