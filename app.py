from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import index.html


app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.post

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db_app"
mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_app")
# mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    scrape = mongo.db.scrape.find_many()
    return render_template("index.html", scrape=scrape)


@app.route("/scrape")
def scraper():
    scrape = mongo.db.scrape
    scrape_data = scrape_mars.scrape()
    scrape.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)