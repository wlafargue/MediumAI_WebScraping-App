from flask import Flask, render_template, redirect

from .db import Database
from .scraper import scrape

# Initialize Flask
app = Flask(__name__)

# MongoDB server
db = Database("localhost", 27017, "my_db")
col_name = "my_col"

# Webpage
url = "https://medium.com/tag/artificial-intelligence/recommended"

# Default route
@app.route("/")
def index():

    # Find documents
    data = db.find(col_name)
    return render_template("index.html", data=data)

# Scrape route
@app.route("/scrape")
def scraped():

    # Web scraping
    scrap_data = scrape(url)

    # Fill the Mongo database
    col = db.init_collection(col_name)
    col.drop()
    col.insert_many(scrap_data)

    return redirect("/", code=302)
