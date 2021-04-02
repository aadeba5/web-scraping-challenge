from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars



app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db


@app.route('/')
def index():
    mars = list(db.mars.find())
    print(mars)

    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    scrape = db.mars
    scrape_data = scrape_mars.scrape()
    scrape.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)