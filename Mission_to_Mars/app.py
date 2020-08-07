# Import dependencies
# Flask is a web framework that creates web applications like web pages
from flask import Flask, render_template, redirect
# Flask-PyMongo bridges Flask and PyMongo
from flask_pymongo import PyMongo
# Scrape function used to add data to Mongo database
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection and create database named mars_app
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database which contains
    # collection named mars
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_info = scrape_mars.mars_scraper()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)
