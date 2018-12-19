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
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)



#We've previously added url in company.json, and when we run it, we can see that it picks up the url link but we need to get it working. We need to employ some advanced features in Flask to get it working, creating new about decorator and route.


@app.route('/about/<member_name>')
#Creating new view, taking member_name as argument}, so whenever we go to url with something after it, that will be passed into this view
def about_member(member_name):
    
    #Will create empty object, which we will use to store out data later
    member = {}
   
    with open("data/company.json", "r") as json_data:
         #We then create another variable inside where we pass the data that we've passed through and convert it into json
        data = json.load(json_data)
        for obj in data:
            
         #And now what we're going to do is iterate through that data array that we've created, so what we will say is that if obj["url"] == member_name, as that's the variable that we've passed in, then member = object.  So we can see that those two link, our URL and our member_name have to match,And if they do, then we're going to return this member object so that we can do something with it.
            if obj["url"] == member_name:
                member = obj
        #And just to demonstrate that, we're going to just return some HTML, the same as we did in one of our earlier videos. So the name key out of our object.
        
        #So now that our HTML file is created to provide basic information about the member when we click on them, all we need to do is go back into our run.py and instead of returning this HTML, then we're going to return render_template. The first argument is going to be the member.html template. And then we're going to say member = member. So that's how we refer to it inside our template.

    #return "<h1>" + member["name"] + "</ h1>"
    return render_template("member.html", member=member)


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

#So we've created a makeshift database using JSON files, and we've also seen some very advanced routing features in Flask. We can take a variable, pass that in to our URL, and then do something based on that variable. That's the last we're going to look at our About page for now. We're going to move on now to our Contact page and have a look at how to process forms using Flask.
