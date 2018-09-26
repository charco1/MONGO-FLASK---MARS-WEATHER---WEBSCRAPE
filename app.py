from flask import Flask, render_template, jsonify
import pymongo
import scrape_mars

app = Flask(__name__)

mongo = pymongo(app)

print(app)
# Use flask_pymongo to set up mongo connection

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)
    
@app.route("/scrape")
def scrape():
    mars.mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
       {},
       mars_data,
       upsert = True
    )
    return  "Successful scrape"

if __name__ == "__main__":
    app.run(debug=False)

