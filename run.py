
import os
import json
#On debugger, we can see that 200 status means success and all is ok. So now we import request library from flask. Request is going to handle things like finding out what method we used, and also it will contain our form object when we've posted it.
from flask import Flask, render_template, request

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

# POST lesson
# And now we get Error: Method Not Allowed. And if I just pull down the top, so you can see the top of the tab here, we can see that it's a 405 method not allowed error, so this is an error from our server. The reason is that by default, all of Flask's views will handle a GET request, but when we need to start handling anything outside of that, such as a POST, or the other methods DELETE or PUT, then we need to explicitly state that our route can accept that. So we'll go down to our contact route here, and we're going to put in another argument.


@app.route('/contact', methods=["GET", "POST"])
def contact():
    # then we put in an If statement using the method of request object.
    # We can see in debugger that msg typed below arreas. Blanked this out, as a further request method (request.form) is used below after this. 
    # if request.method =="POST":
    #   print("Is there anybody out there")
    
    # the request object has a lot more things attached to it as well. When we submit a form, it actually has the form object attached. So remember that we gave each of our fields names. Let's see what happens if we print out request.form. So again, we'll save that, go back to our contact form, and autofill information yet again. And this time, my message will be "Here is my message to you..." Click on send. And now in our immediate window, you can see we have this thing called an ImmutableMultiDict([('email', u'deirdreweldon2016@gmail.com'), ('message', u'this is my message to you.'), ('number', u'1234'), ('name', u'Deirdre Weldon')]).
   
   # blanked out, as repeated using (print.request["name"])
   # if request.method =="POST":
     #   print (request.form)
    # return render_template("contact.html", page_title="Contact")
    
   # Now because this is a dictionary, we can actually use a standard Python method of accessing the keys for that dictionary. So if I do print(request.form["name"], let's see what happens. We'll go back to the form again, and for one last time, we'll do the autofill information and another message. Send. And when we check our immediate window again, now we can see that my name, Matt Rudge, has printed out because we've accessed that key, and it's printed out the value.

    if request.method =="POST":
        print (request.form["name"])
    return render_template("contact.html", page_title="Contact")
    

@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
            
# So we've created a makeshift database using JSON files, and we've also seen some very advanced routing features in Flask. We can take a variable, pass that in to our URL, and then do something based on that variable. That's the last we're going to look at our About page for now. We're going to move on now to our Contact page and have a look at how to process forms using Flask. 


