import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
   
    
@app.route('/about')
def about():
    data = []
    #need to pass in json_data
    with open ("data/company.json", "r") as json_data:
        #json.data will be passed into json.load function and create a list of dictionaries.
        data = json.load(json_data)
        #have also created an empty list to store data in before opening the file, and have passed it through as company_data (which is equal to data).    
    return render_template("about.html", page_title="About", company_data=data)


@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
