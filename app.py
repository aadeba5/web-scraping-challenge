from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
# import scrape_mars
# import index.html


app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db

db.mars.drop()

db.mars.insert_many([
        {   'title': 'news_title_text',
            'news_p': 'news_p.text'},   
            
        {   'feature_image': 'feature_image'},
            
        {   'html_table': 'html_table'},   
            
        {   'hemisphere_image_urls': 'hemisphere_image_urls'
        }])   


@app.route('/')
def index():
    mars = list(db.mars.find())
    print(mars)

    return render_template('index.html', mars=mars)

    # scrape = mongo.db.scrape
    # scrape_data = mars_mission.scrape()
    # scrape.update({}, scrape_data, upsert=True)
    # return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)