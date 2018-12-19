[Please note text below taken from Tutorial videos (Code Institute)].

[Below are tutorials taken from Code Institute on Flask Framework]

# What is Jinja?

Commenting out in Jinja2 (Template Designer Documentation):-

http://jinja.pocoo.org/docs/2.10/templates/#comments

(Stack Overflow):-
https://stackoverflow.com/questions/16275877/comments-not-working-in-jinja2

Explanation of Jinja taken from Quora:-

https://www.quora.com/What-are-the-main-differences-between-Jinja2-and-Django-and-why-would-you-use-one-over-the-other

Jinja2 is a templating library that can be used to simplify the process of generating HTML for Python web apps. Django, on the other hand, is a full-fledged MVC framework, which means that it contains libraries for things like database interactions, routing, and caching. Django also includes its own templating library, which works a bit differently than Jinja2. So, the functionality provided by Jinja2 is simply a piece of the functionality that's provided to you by Django. You can actually use Jinja2 to write templates for a Django web application, but it's probably more common to use Jinja2 with more minimalist Python frameworks like Flask (A Python Microframework).

Other explanation of Jinja:-

Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:

<title>{% block title %}{% endblock %}</title>
<ul>
{% for user in users %}
  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
</ul>
Features:

sandboxed execution
powerful automatic HTML escaping system for XSS prevention
template inheritance
compiles down to the optimal python code just in time
optional ahead-of-time template compilation
easy to debug. Line numbers of exceptions directly point to the correct line in the template.
configurable syntax
Jinja2 Documentation
Introduction
Prerequisites
Installation
Basic API Usage
Experimental Python 3 Support
API
Basics
Unicode
High Level API
Autoescaping
Notes on Identifiers
Undefined Types
The Context
Loaders
Bytecode Cache
Async Support
Policies
Utilities
Exceptions
Custom Filters
Evaluation Context
Custom Tests
The Global Namespace
Low Level API
The Meta API
Sandbox
API
Operator Intercepting
Native Python Types
Examples
API
Template Designer Documentation
Synopsis
Variables
Filters
Tests
Comments
Whitespace Control
Escaping
Line Statements
Template Inheritance
HTML Escaping
List of Control Structures
Import Context Behavior
Expressions
List of Builtin Filters
List of Builtin Tests
List of Global Functions
Extensions
Autoescape Overrides
Extensions
Adding Extensions
i18n Extension
Expression Statement
Loop Controls
With Statement
Autoescape Extension
Writing Extensions
Integration
Babel Integration
Pylons
TextMate
Vim
Switching from other Template Engines
Jinja1
Django
Mako
Tips and Tricks
Null-Master Fallback
Alternating Rows
Highlighting Active Menu Items
Accessing the parent Loop
Additional Information
Frequently Asked Questions
Why is it called Jinja?
How fast is it?
How Compatible is Jinja2 with Django?
Isn’t it a terrible idea to put Logic into Templates?
Why is Autoescaping not the Default?
Why is the Context immutable?
My tracebacks look weird. What’s happening?
Why is there no Python 2.3/2.4/2.5/3.1/3.2 support?
My Macros are overridden by something
Jinja Changelog
Version 2.10
Version 2.9.6
Version 2.9.5
Version 2.9.4
Version 2.9.3
Version 2.9.2
Version 2.9.1
Version 2.9
Version 2.8.1
Version 2.8
Version 2.7.3
Version 2.7.2
Version 2.7.1
Version 2.7
Version 2.6
Version 2.5.5
Version 2.5.4
Version 2.5.3
Version 2.5.2
Version 2.5.1
Version 2.5
Version 2.4.1
Version 2.4
Version 2.3.1
Version 2.3
Version 2.2.1
Version 2.2
Version 2.1.1
Version 2.1
Version 2.0
Version 2.0rc1

# The Flask framework 

is a web-based framework using Python language that began it's life as an April Fool's joke was has since risen to become one of the biggest Python frameworks become the most popular and widely supported Python frameworks within the Python community. 

The flask framework is what is known as a micro framework it allows us to get up and running building websites with as minimal Python code as possible It doesn't come with, micro frameworks don't come with batteries included which means that we don't get a lot of features that we would get with Django but the appeal of flask is its simplicity. 

We'll use flask throughout this lesson.  To run a Python server side project we use to serve HTML files from a server we'll use it to write logic inside of our Python templates, which will allow us to use 'for' loops and 'if' statements and also inheritance, which will look out, and we'll also learn how to submit forms which will allow us to take data from the client posted to the server.  In the instance that a user fills with that information. So we're going to learn how to create and run a flask application, we're gonna learn how to serve HTML, CSS and JavaScript from the backend. I'm gonna make you learn how to make our code reusable. By using template logic, we learn how to post data from HTML forms on back-end, and we'll also learn how to deploy our project using a platform called Heroku so we can serve our project. Also we can host our project externally for all the world to see.

# Hello Flask

## What is it?

Flask is a small framework

## What does it do?

Allows us to build web apps

## How do you use it?

First we need to install it!
LESSON:

    Start of transcript. Skip to the end.
    In order to get up and running with the flask framework what I'm going to do is I'm
    going to create a new brand new workspace in cloud 9 I will give it a name of
    flask and this is going to be using a blank template and then we're
    going to click on create workspace so what we're going to do throughout this
    this lesson is we're going to just create a simple website that outputs
    some pages and we'll take a look at how you tie those pages together and how we
    can inject content from the server side and pass information back from the
    client side to the server side. What we're going to do is
    we're just gonna create a simple little hobbit website for the the company of
    dwarves later on but what we're going to do now is firstly I'm just going to
    delete this readme file and I'm going to create a brand new file but first let's
    do sudo pip3 install Flask and that will install the Flask framework for us
    and once that's done then we can go ahead and we should be able to we can go
    ahead and create a new file now. This would be the default file that we
    will use this would be the main file that will run the application and in flask
    the convention is to either called this run.py or app.py. I'm going to call it
    run.py so what I want to do now is I want to open up that run.py file
    and I'm going to say from flask import flask through the import flask object
    from the flask module and then we want to say app = flask
    then underscore underscore name what we want to do that is we want to say we
    want to use our decorator to say we have @ symbol app.route and then in
    their brackets we have just forward slash as a string then we say def hello()
    and then we're going to return hello world and this will just output hello
    world out to the browser and what we want to do then is we won't say if
    dunder name is equal to dunder main and inside of that we're a few things we
    need to do here so we need to app.run() which will run the
    server but there are a couple of things we need to pass in and we can retrieve
    those from the cloud nine but this here these kind of ten lines here are the
    usual ten lines of code that you would use to run a flask application we need a
    couple of things here we need from retrieved from the cloud nine work space
    and we do that by importing OS and then inside of our app.run we pass in the
    series of arguments so the first argument passing is the host name
    OS.environ.get will allow us to get the IP address now this is so we can
    tell flask which what the IP address we want to run this on is the port that we
    want to open for this so next one we do is the port and we need to cast that to a
    string or an int sorry so int OS out and fire not get past your port and we want
    to say that the debug mode is true because we're going to be developing and
    we want to be able to to do some debugging so what I need to do now is
    there a couple ways I could run this I can either bring this directly from the
    command line now by doing Python3 run.py and that will allow us to run
    brill in our application here or what we can do is we once we have this
    information we can just use click on the Run button up the very top on there on
    cloud nine will give us the URL that's running on so we can see now we're a
    flask - username
    .c9users.IO now if I go in and change something some piece of
    code we can see that changes so hello flask now if I remove our debug
    statement and stop running code and run the code again now head over to that in
    the browser so I'm gonna click open now if I go change something while debug
    mode is not on it won't allow us to change so I can refresh here and it
    doesn't update to hello hello it sticks with hello Flask so this is why
    it's important to have debug equal to true when we're developing our applications

# Rendering HTML Code
 
## What is it?

Returning HTML code from a Flask function


## What does it do?

Allows us to render HTML code from the server


## How do you use it?

By returning a string that contains HTML tags

LESSON:

Now that we have our Flask application running what we can do is inside the
return statement of our hello function we can actually put in pure HTML so if I
were to say h1 hello and then close that h1 and then say create a h2 after
that and say flask I can go ahead I'm gonna save this and then I can just let
me make sure my application is running so if i refresh now we can see hello and
flask are now being displayed in a h1 and h2 respectively so this shows us
that we can actually return pure HTML code from from inside of our methods and
then the browser sees that and goes oh this is HTML code so I'm gonna render
this as HTML code a better way to do this is to use the render template
function so the render template function we can import from flask and then we
return render function and we can say index.html now when we say when we put
the name of a file flask always assumes the top file as any directory called
templates which would be in the same the same directory level as the
run.py file. So in order to do that was a create templates folder inside of the
Flask directory we'll create a new file called index.html. Iinside of there we're
just gonna pop it in some HTML code so I'm gonna have my HTML tags inside of
that and I'll have a head tag we give that title and we just say give it a
title of hello flask and then give our code body
an inside of the body then we will just create simple nav bar for example we'll
have a ul and we'll have an li inside of that and inside of the li then we'll
have an href is equal to put in a content that just says low or
homepage and we just put in hash as the href there for the time being so if I go
ahead and refresh now you can see that this little index.html page is
in fact running so we have our navigation bar we have our lists
displaying inside of the inside of the browser so the render template is
retrieving the text from the HTML index.html file and then sending it to
the browser and the browser is picking up on it and displaying displaying it as
markup so if I put in a h1 and just say homepage and inside of our nav I'll
just create a second page it says about and I get rid of the word page there I get rid
of both page in both of those and then what I can do is I can actually copy all
of this code and I'll create in an HTML page and inside that about the HTML page
I'll paste the content from the index.html page I'll just update the
h1 to say that this is the about page and then what we'll look at next is how
we can actually link to these different pages using by different methods of
using the href to determine the path.

# Routing
 
## What is it?

Routing


## What does it do?

Allows us to swich between views using URLs


## How do you use it?

By creating routes

LESSON: 

Okay so in order to hook up our views in our templates now what we need to do is
we need to use what's called routing and routing will allow us to basically route
to a specific function or a view and I suppose this was called here this
function here is typically referred to as a view and then this
decorator on top at the very top here on line six this is the route so our
application knows that if we go to our domain forward slash then it will use the
function that has that route so what we can do is we can create additional
routes so what I'm going to do now is I'm going to create a new view function
so we're gonna say you have decorator of app.route and then we say forward
slash about supplies a def about and then I can just return render template
about.html I'm just going to rename my hello function there to index just to make it a bit more but
more readable and a bit more correct so instead of them having our hash symbol
inside of the href's I'm going to update them to forward slash for the home index page and then
forward slash about for the about page so what I need to do is I need to add those
changes to both of those pages so inside of the index.html I need to do it on the
inside of the about.html so once I've done that both those files I can
just go ahead and refresh and you can see them once we click on the about link
then we're brought to the about page we can click between the two for a while
and okay get a feel for how it works there is another way of doing this we
can what we can do is we can say we can use what's called a template logic and
the template logic allows us to inside of these curly braces we can say URL
underscore for and that's a function where it will take a string argument we
will say index in the first one and these two curly braces here allow, we'll
say to flasks look I need you to inject some piece of text here the piece of I
wants is the output of this URL for index so go ahead and we do that again
for the about page so if you remember earlier we have view functions are named
index and about and so we pass in the name of the views that we want to call
and flask will give us tell us what the route for that is and inject it in place
there I mean do the same then on the about page so you can see if you keep an eye
on the URL bar there when you're switching between the two the URLs are
actually updating to the number forward slash index and for slash about for the about page
and that's just those name function names there so we say URL for the
specific view if I change mine to say hello now then it will give me an error
to say they couldn't find a name an endpoint for the index did you mean
hello instead and then evens go so far as to suggest the name that we should
have inside the URL there so let's go ahead add another one so add in a
contact page say app.route and then this is forward slash content and then the
name of the function would be contact and we just returned another template called render template. And the template that will return will be contact on HTML so I'm gonna copy the code from the index.html file actually I won't just yet I will update the index.html file to include the URL for the contact page so we'll just update that there in the href and then we'll update the content I then I can go ahead once that's done then I'll copy the whole a copy that cross into the about HTML page first and then I'll copy the whole HTML file and I will copy it in to create a new template in templates directory called contact HTML and I will paste all of that code in there and I'll just update the h1 on the page to say contact us okay I still have my error in there because I didn't update save this file and I need to change this back to index,and if I change contact to hello, Flask is actually smart enough to actually know the difference and get an idea of the actual page that it is supposed to render of the details. Suppose app will actually suggest that to you to us when we're trying to get it to work so I'm gonna say it everything back to normal then refresh and we can see now that everything is working.

# Template Inheritance
 
## What is it?

Template Inheritance


## What does it do?

Allows us to inherit code from other templates


## How do you use it?

By creating a base template and using {% extends 'base.html' %} in a child template

LESSON:

One of the biggest benefits of using a framework like Flask or Django is that it
allows us to reuse as much code as possible so in the example here we have
three pages that all contain pretty much the exact same code which is fine but it
means that if we add a new link then we have to add it to all of the pages etc
so what we can do is instead of a template directory I'll just create a
page called base.html so what I'm gonna do is I'm gonna copy pretty much all of
my content from my about page and I'm gonna paste that into the base.html
file I'm going to remove that h1 that we had there earlier and instead I'm going
to put in a curly brace on a percent symbol and I say block content and then
go percent symbol and a curly brace and then I'm going to copy that opening
curly brace percent symbol I'm gonna say end block and then go say a percent sign
and then a closing curly brace and this defines an area or a block and Flask will
go all right okay I'm going to need to inject something
into here so I'm gonna open up my about HTML page and I'm going to remove
everything except for the h1 this is about
that's top I'm going to use my templating logic here that says extends and
then in quotes base.html after that we're going to do the same block content
that we did inside our base.html file so what will happen now is when flask
tries to read the about our HTML file I go oh this needs to inherit from this
needs to inherit from the base.html file and then I need to find a block
called content and I need to put this h1 inside of that content block so
we'll do that across all of our pages so for the bit about
index and contact and once I've done it for all of those pages and they will
actually all be the exact same as they were put each file has much less content
much less HTML content because it's all written inside of the basic HTML page
and then the individual pages themselves get injected into the content into the
content block so if I create a new route here for careers we can say we call this
careers I know instead of having to we just returned a simple career template
and instead of having to update this on several different HTML pages it will I
just have to add it to the one based on HTML file and then because all of the
additional pages all of the individual pages are loaded into the basic HTML
file that change will be available on each page so I was gonna copy this code
from the index.html I'm gonna paste it into the careers.html file and then
going to copy in my base.html file I'm gonna copy the URL here I'm just
creating new one that says careers I'm gonna update the URL for we have one for
careers then we refresh and we can see that our careers I need to update the h1
so we'll update that say come work with us
okay if I refresh now you can see now that all of these pages have a nav bar.

# Using A Bootstrap Theme

## What is it?

A bootstrap theme


## What does it do?

Allows us to quickly style our website


## How do you use it?

We'll download it from Start Bootstrap


LESSON:

So now that we have some HTML content in the place what we need to do is we also
need to actually be able to style our content using CSS so I'm just going to
go ahead and I going to do Google search for some bootstrap teams so some themes
that somebody people have already built and startbootstrap.com is usually
a really good place to go they have a lot load of different pre-built themes
here we can go in to the team different themes and have a look we can preview
them before we choose to download them so for example if I click on preview
here I can preview this new age kind of landing page theme get preview I can go
into it I can have a scroll through page and get a feel for what it looks like
but let's go find one that might be more applicable to the to our purposes we're
not just we don't just have a landing page we have multiple pages on ours so
this clean blog should work pretty well let's see a preview that friend some
different pages and yeah that looks like it should be good so what I can do then
is we'll go in with download that we won't download it actually what we need to
do is we need to right click on the download button
so I right click on the download button here and we need to download it to Cloud9 so we
need the when we right on it we need to click on copy link address this
way we'll be able to do wget commands to download it to our workspace
so see us to mkdir called static. And static is a file is the name is usually
given to the folder that contains CSS JavaScript images and stuff like that so
let's see okay this command doesn't work it doesn't want to copy it into the static
directory for us. So what we'll do is just I'll do a, I will cd into my static
directory so
let's just clear this up. I'm going to cd into the static directory here and then I'm
going to run my wget command so I'm going to paste in the URL that I
copied from the download button and this gives me a file called gh-pages.zip
and I can just run the command unzip followed by gh-pages.zip on this will
unzip the gh-pages.zip directory for us so there's only there's not actually
that many pages in here that we need to use our directories we mostly just need
the CSS JavaScript we need to vendor files and the images so what I'm going
to do is I'm just gonna move those out of the start bootstrap-clean-blog-gh-pages
directory things firstly get the CSS
and then after that I'm going to get the JavaScript or sorry the images times a
js after that and then we'll get the vendor files and the vendor files or we
get the scss and then the vendor files as well so the vendor files are just the
kind of jQuery bootstrap and all that stuff and we just want to do with dot
at the end copy that into this directory is one that we're currently
working in and we can go ahead and once we've done that then we can actually
remove rm -rf the entire start boot trap directory because our files
will be moved in from because the necessary directories have been moved
into the static directory we can we've no need for it anymore and we can also
get rid of the gh-pages.zip file. As well as we going to do an LS
something see that the CSS images the JavaScript and all that have been
loaded into the static directory so inside the head of our base.html file
then we can just go ahead and we can reference those and we'll use the URL
for here as well will be slightly different this time around because we're
targeting a specific file as opposed to a specific view function so the first
argument that we pass in is just word static and then we pass in the second
argument this is file name. We were looking for a specific file name here so
the file name that we're looking for is clean-blog.min.css
so go ahead and run this now
see nothing happens I mean inspect element here see what
happened console not found in blog ah yes so instead of just referencing the
file name because were referencing the static directory we also need to specify
css/green-blog so I'm gonna update that now once I refresh my page
then we can see that this CSS file is now being loaded and these CSS styles are
being applied.

#  Styling Our Templates
 
## What is it?

Taking the styles of the theme and adding them to our own site


## What does it do?

Styles the content on our site


## How do you use it?

By using the theme that we got from Start Bootstrap

LESSON:

Now that we have bootstrap theme downloaded we can head over to their
their repository on github we can actually just start to retrieve a lot of
the code that we need from here and we can build up our own boilerplate from
this code so what I'm gonna do is inside of the head element over based on HTML
and gonna reference the style sheets so there are more style sheets for this
so we have to reference the bootstrap style sheets we have to
reference a jQuery and the bootstrap JavaScript files as well so both the
team blog preference what I'm going to use and it's going to create a reference
for bootstrap so the path for that is vendor/bootstrap/css/bootstrap.min.css
so once we have that loaded in then we can, close that off there. The next thing
that we want to do is we want to we can grab all of this pretty much all of this
code from the outside of the footer actually we can grab everything inside
the body really including the nav so we'll get rid of our own nav here for
the time being but also remove our content blocks there so the first thing
main thing that we need to do here is okay we can see we have all of that
there and we need to actually we can move the majority of this into into our
index.html file and that will allow us to remove kind of a lot of code from
from the base.html pages we won't be needing all this code on every page but
for now let's go ahead and I'm going to try referencing these scripts so down at
the bottom of, just before our closing body tag we're
just going to copy the source and then I'm gonna pop it inside of the
static URL for our method so we have our URL there for our jQuery now and I what
I'm gonna do is I'm gonna copy that entire URL and I'm gonna paste it into
the next script tag and I just gonna paste in the JavaScript are they
bootstrap JavaScript reference it was already there and then the clean block
has its own JavaScript file so I'm going to reference that also okay we want to
do now last thing now there's an image we wants
you the images in the static directory so we're just going to use the the
static URL for instead of the standard image forward slash so go ahead refresh the
page now and we can see that our code is all loading up and working fine you see
we have posts there we have it's just some boilerplate content what we can do
is see this main content here what we can do is we can actually take all of
this content and we'll move it into the index.html file just so we can use their
content blocks so everything inside we leave the container div here and then
we'll take everything inside of that so inside of the container div will just
create our content block so I'll create my block content and then I'll pop in my end block inside the container and save that then and then inside of the block content, content block in the index.html file I'll paste in all of this code so what we want to do the next thing that we need to do now is we need to just need to update our URLs in our nav bar so our href's are going to become our URL forwards instead of specific HTML files. Just coming to pop that code in there is my closing braces create one for the about page and sorry but we'll have contact and careers that just hangs up from sample post as well to say contact us and then for the last one and it's already said contact but we'll change this to careers now so my URL is wrong here so they should be name's not slashes so as I saved this file and check it in browser will see those errors there if I
do a refresh and see yep no URL for that so instead of those slashes that should be index and about contact and careers. So I'm going to go ahead and save that now and now if I do a refresh again we'll see that these all work so I click on these links and it'll bring me to the various pages and as because we still have our content block in place it still will inject all the content into our pages into our base.html page.

# Making The Design Our Own
 
## What is it?

Styling our site


## What does it do?

Customising the theme

## How do you use it?

By modifying the theme to suit our needs

LESSON:

Now that our styles and our CSS files are in place ours styles and our JavaScript files are in place what we can do is we can start to make this design our own and what I'm gonna do is I'm going to open up Google and go and search for a Thorin and company and head to images and I'm gonna find some company pictures of Thorin and the company of dwarfs from The Hobbit this looks like a pretty good image here so I'm gonna click on the view image link and then I'm going to grab the URL from the URL bar there and inside of my notes you add this
then to the page-header so this will this image will be displayed on all of
the pages and the website so in the base.html file if I go to my page
header and them inside there's a style set here for a background image and I'm
going to update that from the local image to the URL that I just retrieved
also in the navigation bar here on line 13 there's a href that points to
index.html so I'm just gonna update this and say URL for index instead and
instead of saying to start bootstrap I'm going to say Thorin and company I'm
basically just gonna change the branding of this in several different places here right now to reflect my own usage of the site and once that's done then back in page header here we have our we have kind of a heading and a subheading so we have our h1 this is clean blog and then we have a subheading just a blog theme by start bootstrap so I'm gonna turn this into something that's more
applicable here so I'm gonna say Thorin on company again and then inside of our
soap heading spine I'm gonna say Thorin on his company of dwarves
just to, just to found that a bit so once we're done it's going to escape
this so once it's redundant we can refresh and see now that we have our own image in place our own h1 our own title and it's all looking good one thing I will do now though is because I'm using a h1 in my page heading what I'm going to do is I'm going to go back over to try out 9 and what I'll do is I will use a switch all of our headings and each of our files to h2 so in the back page for example we have a h1 that just has about something we're gonna change that to a h2 just for consistency and just make it a little bit more semantic so inside the contact contact us contact our HTML them as well I'm gonna do the same I'm gonna change it from an h2 to h1 and lastly I'll do the same thing in careers ok so I can save that now and if I head back to the browser and check this out just do a refresh and click on some different pages and we can see though that we have our h2 on each of our different pages.

# Adding In Some Company Data

## What is it?

Data about the company


## What does it do?

Gives the user some information on the company


## How do you use it?

LESSON:

Okay so now let's start adding some data to our about page so we want to do is
we're going to create a P element here and basically what I'm going to do on
this page is I'm gonna give kind of an overview of Thorn and Company and then
we list each member so what I'm going to do is I'm just going to Google
Thorin and Company and I found a background here we will be able to pop into
that P element. I copied that all wrong go back and I'll grab try grab that again okay so I'll copy that background that piece of text on the background and pop that into our P element I'm just going to carriage
return here it's quite a big chunk of text so we're just for the sake of being able to read all, scroll horizontally so once that's done then I can run this and I'm in the wrong file here in my about.html I think should be good to go now close down this and open it up again there we go
okay so once we got that running so now I'm gonna head over to the about page as
we can see that piece of content that we just created so if I click on about
and we can see now that we have that piece of text under the about h2 so what
we want to do now is we want to start adding in some content about each kind
of specific each specific member of the company so we have Thorne we have
Killy and Philly, Oin, Gloine, Ballin and so on so what I'm going to do is use some bootstrap classes here so I go to great new div I'm gonna give this div a two classes we're going to give it a class of row and we're going to give it a
class of featurette then inside of that we're going to create a narrative it's
just gonna be col it's md-7. Inside of there we're just gonna create a h3 and
we call put a piece of text in there Thorin Oakenshield and after that then
we can pop in some text into a p element so this iotr and wiki
page here we can grab some text about each of the members so I'm going to text
grab this piece of text here from Thorin's biography and I'll just paste
that into the P element there once again I will do some carriage returns just to
just to bring it round so it's not running off the screen
okay so once I've done that then I can go ahead and save this file and we can
go ahead now and we can check the yeah the about page we have that text
there so next thing we want to do is we want to pop in an image so outside of
so after the after we close off the medium column of file on seven we'll
create a new one with a five so the 7 will fill up the left hand side and then
after that we'll have the addition of five row column then to fill up the
rest of 12 so I'm just going to Google some images of Thorin Oakenshield here and I'll just grab one from the Internet's and I grabbed the source and I'll pop it into my image tag okay so how about there it's going to paste that in if I
head over to the browser now and do refresh we should see that image in
there. Doesn't seem to be running it seems to be having an issue okay let's just try that again okay it seems work now and there we go we have our heading we h or h3 our piece of text and our image for Thorin Oakenshield so let's do another
one of these featurette at rows we'll create some text for someone else I
think Philly and Killy you're up next so we create our div with classes with class of row and feature it and then this time around we're going to show the image on the left hand side so we'll put our image our col-md5 first and put our image in there and then once we've done that and then we will put inner piece of text or a piece of text for this time we'll display on the right so we have kind of an offset kind of grid going on so okay we have our piece of text on Killy and Philly there let's go grab an image of the two and we'll pop that into our
source element in our image tag okay we should be able to use this image here
it's going to paste that in and then outside of that I col-md5 we're going to
create our col-md7 and this will contain our h3 for Killy Philly will also contain the kind of biography biographical piece for Killy and Philly as well just like above where we have our h3 and our P for Thorin Oakenshield so he's going to head over here and grab a piece of the text and paste that in and then I'm just going to once again just pop some carriages returns in there and go ahead and save that now and if I do refresh them we can see we have Killian and Philly some with the image on the left hand side and the text on the right hand side so one issue with these images is that they're not now taking up the full width space of what I'm going to do is inside of CSS directory what I'm going to do is I'm going to create a new file I'm just gonna call this style.css and then I'm going to open up that file and I'm going to target that image and I'll make it width 100 so what I need to do is to avoid targeting all of the images what I'm gonna do is I'm gonna to save the images inside of the col-md5 element and that will just target those images on the about page and I'm just going to delete this I have an extra gh-pages.zip file I'm just going to delete I'll get rid of it later but for now I'll just pop in this URL here okay so instead of the clean-blog.css then what we want is style.css do refresh them we can see that those images are increasing in size and there we go.

# Challenge - Challenge Hint: 

## Ensure the content is present for all of the following: 

Thorin Oakenshield, Kili & Fili, Óin, Gloin, Balin, Dwalin, Ori, Dori, Nori, Bifur, Bofur, Bombur, Gandalf.

# Passing Data From A View To A Template
 
## What is it?

Information that we can provide to a template from the backend


## What does it do?

Allows us to generate information inside our view and inject it into a template


## How do you use it?

LESSON:

One of the biggest benefits of using frameworks on over a site you generated
content such as HTML is that we we can actually get the server-side code to
provide the front-end with certain pieces of data. Inside of the return
template function here I can actually add in as many additional arguments as I
want so I'm going to create for each of these pages I'm gonna add in a new
argument called page title and I can call this whatever I want and each page
then is going to have a string representing its name so in the about view that going to page title is going to say about contact it's gonna say contact and so forth so once I've done that then I can open up my about.html page and inside my h1 I can get rid of the about and I can actually just pop in two opening curly
braces followed by two closing curly braces and pop the word page underscore
title in there instead like I said this could be anything instead of saying page title you could say page heading heading could be any any variable name that you give it so once I pasted it out into the h2's of each of those pages now I can refresh my application and click on that all of the different pages and we'll see that the the, for the most part the headings are just still the same except for careers which used to say come work for us.

# Using For Loops Inside HTML
 
## What is it?

A template tag

## What does it do?

It allows us to perform logic inside of our HTML templates. In this case, it allows us to use a for loop inside of our HTML

## How do you use it?


LESSON:

So as I said as I mentioned earlier one of the benefits of using frameworks like
Flask and Django is that they allow us to reduce the amount repetition
that we would normally have to do one of the ways it allows us reduce this
repetition is by using for loops so just sending data to our our templates
we can also send we can also send lists and we can actually use for loops in our
templates to iterate over those lists so for example if I head into my run.py
file now and I in addition to returning the page title I can also
return a variable called list underscore of underscore numbers you just got me a
list of numbers so just gonna contained numbers 1 2 & 3
okay so what I need to do then is I need to open up the about.html page and just
before the page style I'm just going to use my double curly braces to show the list of
numbers being rendered on the page so I can go ahead and save that now and I'll
do a refresh over here and we'll be able to see now that we have our list of
numbers 1,2 & 3 being rendered on the page inside of their square brackets to note that this is a list what I can do is I can use the same templating tags that we use for the block and the extend
so we have our opening curly brace followed by a percent sign and this kind of this is
usually kind of referred to as kind of a template logic tag so this is logical
performing in the template and we're using specific tags here to
denote the logic so I'm gonna say for number in list of numbers and then I
need an end for template tag as well just so that Flask will know where to stop so inside of top for loop I'm just gonna create a number and I'm gonna show the I'm gonna put create paragraph and inject the number into that paragraph as we can see now we have three new paragraphs all containing the number one and then another one containing number two and then the third one containing the number 3 and that's how we can use template logic to iterate over data inside of our HTML code. 

# Reading From A JSON File
 
## What is it?

A JSON file that will contain our data
 
## What does it do?

Allows us to store data in a JSON file

## How do you use it?

By creating a .json file and adding our data to the file

LESSON:

Instead of hard-coding all of our information into the HTML
template what we can do is we can actually store information in a file so
I'm going to create a new directory inside my fast directory called data and
inside of that data directory I'm gonna create a new file called company.JSON
this is the file that I'm going to use to store all the information about the company so what I'm gonna do is I'm gonna open up that file first thing I do is create an array and then inside of that array when I'm gonna create an array of objects here and the properties that these objects are gonna have we're gonna be
the name the description and the image stores so the first one first name is
gonna be Thorin Oakenshield then we're gonna pop in a description
after that and in order to get that description I'm just going to go into
the about.html file and copy the description that we already have in
there and I'm gonna paste this code in and one thing we need to make sure is
that all of our text is actually on one line otherwise it's not actually
valid JSON so I'm just going to remove my carriage returns and make sure it's
all on one line and after that then what we want to do is we want to come at the
end of this line and then we have our image source I'm missing quotation there
we go so comment the end line and then we want the image underscore source is the next property and once again I'm just gonna
grab the image source from the about.html page so I can copy that and I will
paste that into this file now okay so I can go ahead and I can save my adjacent
file now and what I can do is I can that run.py file and on line two
I've imported JSON so import JSON and then on line
14 I'm going to open up and say with open I'm gonna open data/company.json
I'm going to import it as read hang on and data is equal to JSON
data and I'm going to oh sorry that is equal to json.load and I
need to pass in json_data which I'm going to say open the file as
json_data and then let that json_data is going to be passed
into the josn.load function which will take the JSON data and
create a list of dictionaries I've also just created an empty list just to
store our data in before opening the file and I've also passed it through as
company data so company data is equal to data in our render template function
once I've done that then I can go ahead and open up an about page and inside
of our double quote double curly braces I will put the company_data
variable name and then we can see this being rendered inner page and we can see
that we have the standard square bracket and curly bracket notation here for our
lists and dictionaries so let's go ahead we can use the standard Python
notation then so we can say company underscore data and then in square
brackets use the integer to specify the index and we can also then say the name
so after we actually index for left with a dictionary so we can specify a key
then and then we can say with them it will output Thorin Oakenshield that's
that's the key that's associated with company data at the 0th index and that's the name associate with that dictionary okay so I'm just gonna get rid of this now I'm going to add some more data to the company.json file so I'm gonna create a new object and this is going to be our Killy and Philly object
so the name is going to be Killy and Philly and then the description and the
image source then as well I will retrieve from the HTML file but we
already have one thing to be careful of here is that this subscription has
some double quotes in so I'm gonna need to get rid of those double quotes and
replace them with single quotes and I have another set of them here just get rid of those we should be good to go just double-check make sure there's no more. And now I just need to get the image source okay so I'll grab the source attribute there the value for the source attribute from the image element I'll pop that in to the company.json file okay so now inside the about HTML file we'll just do a similar thing here we did with the last time around so we'll just open up our curly our template tag I would say company and then we'll company underscore data and then we'll use a index to retrieve an item from the list we'll use index one this time I'm used index zero last time and index zero is going to be Thorin Oakenshield so the next one this time then should be Killy and Philly and that's how we can read information from a kind of makeshift data store using a JSON file.

# Iterating Over Our JSON Data
 
## What is it?

A for loop to iterate over our JSON data

## What does it do?

It allows us to re-render the same HTML code for each item in a list (or iterable)

## How do you use it?

By passing the data to the template and using the {% for member in company_data %} tag

LESSON:

Now that we've managed to output some of our json data to our HTML template what
we want to do is we actually just want to iterate over all of that information
and display all of it I'll render all of it inside the HTML file instead of all of the hard-coded data that we have what I'm going to do is I'm going to create a for loop setting for member in company_data and then basically what I'm going
to do is I'm going to come to grab theev erything except for the first row and delete it and then I'm just going to write up my end for tag once I've done that I'm going to start removing the information that's in there and start replacing it with template tags so the h3 here we're going to remove this and we're going to use member.name instead in the next, I'm in the next paragraph then what we'll do is we'll do member that description so we can delete all of this in from our within our P elements. There we go and then we can just do member dot description and similarly then we'll do the exact same for the source in our image here so we will say source is member.image_source and then for the alt what we'll do is we'll say instead of a generic placeholder we will say
image for and then we can pass in member.name okay so we can get rid of our style attribute there we'll come back to that later on when we start dealing we have a style already set for that so we can get rid of it so for the alt will just say picture of member.image_source our member.image_name sorry member.name and now if I do a refresh we can see that we have all of our members of the company still displaying however one has changed is they're all displaying with the name and description on the left and the image on the right so we'll take a look at how to revert that back to our old offset type look in the next video.

#  Using If Statements Inside Our HTML
 
## What is it?

The if template tag


## What does it do?

Allows us to use if statements inside our templates


## How do you use it?

By using the {% if some_condition %} tag and the closing {% endif %} tag

LESSON:

Now that we've seen how we would iterate over data inside of our templates let's
how we can use some kind of if statements inside our templates so at
the moment we have all of our, we almost have a design back in place again only
all of our texts are now lying down the left and all of our images are right
whereas previously we had kind of an all set deal with the text on the left and
then on the right an image on the right hand side and then for the second the
image is on the left and text was on the right so what we can do inside of our
template is when were using for loops inside of a Flask template it actually gives us a variable the loop is an object and that object comes with a property of dot index which will tell us which iteration of the loop we're on and as we've seen there we can actually put this inside of our header or inside our h1 and it will number all of the members of the company forest so Thorin being one and Fíli number 2 and 3 then and so on and so forth so what we can do is we can
actually do some checking on this value to see what we would want to do is we
want we want to check to see if this value is divisible evenly by zero and so
what we can do then is we can say if looped.index modulo 2 so this will check to see if we have a remainder or not and then we can close it outside of our call 5 but what we want to do is we want to make sure that there's not a remainder of zero for the first one. So if the loop index is not divisible by two evenly then we will show the text on the left and the image on the right. If I run this now after putting in my end if we will only see 1, 3, 5, 7 so on and so forth what we need to do is we need to pop in and else now to show the image on the left and then the text on the right so what I'm going to do is I'm going to pop in an
else and you notice that this syntax is very similar to Python actual Python
code the only real difference here is that we have to specify tabs. We
can't, we don't have the visual indicator of tabs or in an indentation
in language we need to specify the end if and end for so once we've
done that now I'll refresh the page and see that they're all kind of aligned in
this kind of offset way that we had previously thanks to our if statements
and the last thing we want to do is the hr the horizontal rule that we have at
the end we don't want to display at after the very last one so we're going
to do, we know we have 13 items in our list so what we do is we say if
loops.index is not equal to 13 then we'll show the hr class this way once we reach the next of 13 we won't be displayed we already have a horizontal rule going the width of the whole page now we've got rid of, we only have them separating each company member now.

In our previous video, we got our data displaying to screen and iterating through from our JSON file.
As we said though, it would be nice if we could reverse the order of the images and the text columns for each subsequent line, just as we did in our initial example.
And we can do this because when we create a for loop using the Jinja templating language, it also creates an object for us called loop.
And that object loop has a property which is .index.
And that shows us exactly which iteration of the loop we're on.
If I just put it in there as an expression and refresh the page, you can see that the first iteration, so number 1, is Thorin, number 2 is Kili and Fili, so on and so forth.
What we can actually do is take our loop index there and put it into our member.name <h3> tags.
I'll do that and then put a space just to separate them.
And so now it gives us a nice numbered list of all of the members of Thorin's company.
But we can do more than this. We can actually check this value to see where we are in the for loop.
And what we're going to do is put in an if statement.
So just like for loops, if statements in our templates go with the curly bracket and % notation because they are logic.
So inside the row here, I'm going to put {% if loop.index % 2 != 0 %}
And then beneath this, before the closing <div> tag for my row, I'm just going to put {% end if $} in there.
So just before the closing div tag for my row because, again, just like a for loop, the templating language needs to know where our if statement ends.
So what this will do is check the loop index, divide it by 2, and see if it divides cleanly.
If it doesn't, then it will display the HTML here.
So let's save that and just see the effect that that has on our page at the moment.
So when I refresh now, I have 1, 3, 5, 7, 9
So I have all of the odd numbers now.
So we want all of the odd rows to display with the text on the left and the photograph on the right.
Now what I can do is put in an else statement, and this will take care of the even rows.
And I'm just going to copy the code from above.
So {% else %} we display the image first.
And then, followed by our col-md-7 here, which contains our loop.index, our member.name, and our member.description.
So if it's an odd number, then we display the text first and then the image.
If it's an even number, we display the image first and then the text.
Let's refresh that.
And that's what we see coming up here for each alternate row.
The photograph is either on the left or the right, and that gives us a much nicer layout.
One thing, though, that we do have is this horizontal rule at the end, which looks a little bit messy.
So again, we can use an if statement to take care of that.
We'll do that by going back to our code.
And right down at the end here, we're going to enclose our <hr> in an if clause.
We know that we have 13 elements, so what we're going to do is say: {% if loop.index != 13 $}, then display the horizontal rule.
And again, we'll put the {% end if %} here so that the templating language knows where our if statement ends.
Okay, so when you refresh it now, as we can see, the horizontal rule has disappeared, and this looks a lot neater.
So in this series of videos, we've looked at how to get data from the backend displayed through on the frontend.
And we've also seen how using features of the templating language can help us to write less HTML by using variables and logic, such as for loops and if statements.
Next, we're going to have a look at how to create forms and some advanced routing.

# Advanced Routing

## What is it?

Additional routing parameters

## What does it do?

Allows us to create more specific routes

## How do you use it?

By passing part of a route to a function as an argument

LESSON:

Our project is nicely taking shape.
But what we would like to be able to do is to click on the title or the name of one of the characters and have it bring us to a page that displays more information about them.
Doing this also allows us to demonstrate some of the advanced routing features of Flask.
So let's go to our about.html file and add in a link into our <h3> tags where it shows the loop.index and the member.name.
So we'll create an <a> tag.
Give it the href="/about/{{ member.url }}"
We're going to create that member.url value.
Take out that closing <a> tag, and I just want to put a full-stop after the loop.index number because I think it looks nicer.
And then I'll put a closing tag here inside my <h3>.
Okay, I'm going to copy that and go down to the other <h3> for the even numbers and paste it in there.
As we said, we could have used member.name, but we're going to create a new key and value called member.url.
Some of the names have spaces in.
Some of them also have ampersands (&) in.
And all of them have uppercase characters.
So we're going to create a new key and value in our company.json file.
So put a comma after "image_source".
And then we'll create a new key, "url".
And I'm just going to give this "thorin".
So again, we put a comma in after "image_source", put "url": "kili-and-fili"
Using the magic of technology, we'll go down to the end, where I'm putting "bombur".
And then finally, a comma after "image_source", and the "url": "Gandalf".
So each character now just has a URL associated with them that's their name in lowercase.
I can see now when I go and refresh my page and scroll down, I can click on Thorin's name now because that's a link.
And it says that the requested URL wasn't found on the server as expected.
But when I have a look at the address bar, you can see that where we were trained to go to was about/Thorin.
So it was picking up the URL that we created in our company.json file.
To get this working then, we need to use some of the advanced routing features in Flask, which means we have to go back to our run.py file and create a new route and view.
We can't just modify our existing /about route here.
So I'm going to create a new route decorator: @app.route.("/about/<member_name>")
And then I'm going to create a new view, which is going to be: about_member
And that's going to take member_name as an argument.
So whenever we look at our about URL with something after it, that's going to be passed in to this view.
So we'll create an empty object, which we're going to use to store our data in later.
Just as we did in our about view, we're going to open our company.json file for reading and refer to that as json_data.
We'll then create another variable inside where we pass the data that we've passed through and converted into JSON.
So data = json.load(json_data)
And now what we're going to do is iterate through that data array that we've created.
And we're going to say if obj["url"] == member_name, so that's the variable that we've passed in, then member = object.
So we can see that those two link, our URL and our member_name have to match.
And if they do, then we're going to return out this member object so that we can do something with it.
And just to demonstrate that, we're going to just return some HTML, the same as we did in one of our earlier videos.
I'm going to return "<h1>" + member["name"] + "</ h1>"
Okay, so we'll save that, go back, and now when I click on Thorin, it should bring up his name, which it does.
Go back again, click on Kili and Fili, see what we get, and it brings up their names.
And so on for Oin and so forth.
So that's helpful, but it would be better if we had a template that was displaying this information.
So let's go ahead and create one of those now.
In my templates directory, I'm going to create a new file, and I'm going to call that member.html and then open it up for editing.
Member.html is going to be very similar to all of the other template files that we have.
For instance, it's going to extend our base.hmtl template.
So let's pass in that directive at the top here: {% extends "base.html" %}
So we're going to get all that styling that we have in our other templates.
Then we're going to provide our block content.
So again, {% block content %}
And I'll put the {% end block %} here as well before I start adding my HTML.
Okay, now that my block is created, I can create a Bootstrap row and then a Bootstrap col-md-5.
And in there, we're going to display the image.
So <img src= "{{ member.image_source }}"
And this time, I'm going to also supply an alt attribute.
I should really supply these with all my images.
And the alt attribute is going to say "Profile image for {{ member.name }}"
There's my <img> tag.
Underneath that then, we'll put a heading, which will be a <h2>.
We're going to give that the class of col-md-7 so that it doesn't go the full way across the screen.
And in there, we'll put {{ member.name }}
And then finally, outside of our col-md-5 and our row, I'm gonna create a col-md-12 that goes the full width of the screen.
And in there, we'll put our {{ member.description }}
So now that our HTML file is created to provide basic information about the member when we click on them, all we need to do is go back into our run.py and instead of returning this HTML, then we're going to return render_template.
The first argument is going to be the member.html template.
And then we're going to say member = member.
So that's how we refer to it inside our template.
Okay, we can save that.
And now when I refresh my page and click on Thorin, as we can see, it's extended the base.html template, and I have this basic information about Thorin.
If I do the same for Kili and Fili, you can see that the same thing happens.
So we've created a makeshift database using JSON files, and we've also seen some very advanced routing features in Flask.
We can take a variable, pass that in to our URL, and then do something based on that variable.
That's the last we're going to look at our About page for now.
We're going to move on now to our Contact page and have a look at how to process forms using Flask.

# Creating A Form In A Template
 
## What is it?

A HTML form

## What does it do?

Allows us to submit data to the server

## How do you use it?

LESSON:

Our previous videos have focused on getting our About page up and running.
Now, though, we want to give some attention to our Contact page, which is still looking a little bit light on content.
What we'd like to have here is a contact form.
And we can get that by going back to the Clean Blog Github repository and clicking on the contact.hmtl file.
And as you can see, as I scroll down here, when we get to main content, we have a form.
And that form is expecting input of name, email address, phone number, and then a message of our choice.
So we're going to take this code and copy and paste it into our own project.
We can start copying just below the container.
We don't need to copy the container definition because we already have that in our base.hmtl template.
Then we can go to contacts.html, and, after the page title, I'm just going to put in a couple of blank lines and paste that in.
And now you can see here from the comment at the top, that it's expecting to be running on a server with PHP.
We're not going to use PHP to process our contact form.
We're going to use Python, but it works in a very similar way.
And then if you're using a PC, you can press ctrl + shift + B, or, if you're using a Mac, command + shift + B just to format our code nicely.
So now that that's done, we can save our file, go back, and refresh our contact page.
And here we see our Contact form in all its glory.
So let's try filling it in.
So I'm going to fill in my name, Matt Rudge, my email address, not my real phone number, and a message.
And what click on send, then nothing happens.
The form just resets itself.
If you've completed our interactive frontend development course, you'll remember that we linked up a contact form with an SDK so that we could send emails when somebody had completed the form.
We're not going to do that in this lesson.
What we want to do in this lesson is just make sure that we can handle the data that's been passed to the backend from our template.
And we're going to see how to do that in our next video.

# POST
 
## What is it?

The POST request method

## What does it do?

Allows us to post infomation to our server

## How do you use it?

By specifying the POST method on the form element and handling it on the backend.

LESSON:

In our last video, we got our very nice-looking form attached to our site, but it doesn't actually do anything.
In this video, we're going to wire that up to the backend.
To get our form working, though, actually requires some changes first to the HTML of the form itself.
By default, the Clean Blog template expects us to be using their JavaScript file to do the form handling for us.
We're not going to do that. We're going to use a HTTP method, and we're going to do it with Python.
So to our form we're going to supply method = "POST".
Remember that we've looked at HTTP methods before.
The GET method is used for retrieving data from the server, and the POST method is used for sending data to the server.
What we also need to do is give each of our inputs a name.
We're just going to wrap the lines here to make it a bit easier to see.
So first of all, I have my "Name" input.
And I'm going to give that name= "name".
Then in our "Email Address" input, I'm going to give that name= "email".
The reason we're doing this is that this is how Python will refer to the different fields in our form.
So we need to give them all names.
Name= "phone" for our "Phone Number", and name= "message" in our message text area.
Now that all that's done, we can refresh our form, try to fill it out again, and see what happens.
So I'm just going to use the auto prompts here to fill this information in.
And I'm going to put in just "Test message" here and click on send.
And now we get Error: Method Not Allowed.
And if I just pull down the top, so you can see the top of the tab here, we can see that it's a 405 method not allowed error, so this is an error from our server.
The reason is that by default, all of Flask's views will handle a GET request, but when we need to start handling anything outside of that, such as a POST, or the other methods DELETE or PUT, then we need to explicitly state that our route can accept that.
So we'll go down to our contact route here, and we're going to put in another argument.
We'll put a comma after /contact.
And then methods=[GET and POST]. I'm going to say that the methods that are allowed are GET and POST.
Okay, so now that's done, let's go back again to our contact form, try filling it out again, send, and see what happens.
Well, now we don't get the error.
But again, we also don't get anything back.
So how do we know that this actually worked?
Well, one of the ways is by having a look at the debugger here.
So if I pull that up, we can see there, my previous request of posting our contact form resulted in a 405 error, which was that the method was not allowed.
This time when we did it, though, we got a 200 response code.
And as we remember before, the 200 response code means "that's okay, everything worked".
So now, then, we can actually do something with that.
The first thing we need to do is import the request library from Flask.
And request is going to handle things like finding out what method we used, and also it will contain our form object when we've posted it.
So now we'll just put in an if statement here, and we're going to use the method of the request object.
So if requests.method == "POST":
Then we're just going to print in the debugger window "Hello! Is there anybody there?"
So now that's done, let's save that and try submitting our form again.
So we'll go back to our contact form.
Again, I'm going to use the autofill for name, email address, phone number, put the word "Message", and send.
Again, our form is empty now, but when we go back, we can actually see that the message "Hello! Is there anybody there?" has been printed out in the debugger because we were using the request method of POST.
The request object has a lot more things attached to it as well.
When we submit a form, it actually has the form object attached.
So remember that we gave each of our fields names.
Let's see what happens if we print out request.form.
So again, we'll save that, go back to our contact form, and autofill information yet again.
And this time, my message will be "Here is my message to you..."
Click on send.
And now in our immediate window, you can see we have this thing called an ImmutableMultiDictionary.
But there it is.
We have the data that came through from our form: our phone number, message, name, and email address, and a status code of 200, so it worked.
Now because this is a dictionary, we can actually use a standard Python method of accessing the keys for that dictionary.
So if I do print(request.form["name"], let's see what happens.
We'll go back to the form again, and for one last time, we'll do the autofill information and another message.
Send.
And when we check our immediate window again, now we can see that my name, Matt Rudge, has printed out because we've accessed that key, and it's printed out the value.
For now, I'm just going to leave it at request.form.
So that's how we can access a form's data from the backend of our site.
As we said, we're not going to be sending emails in this video.
But in our next video, we'll have a look at how to provide feedback to the user.

# Providing Feedback To The User
 
## What is it?

The flash function

What does it do?

## Allows us to provide users with feedback

How do you use it?

## By using the flash function!

LESSON:

In our previous video, we got our form up and working.
So now that we have information coming in from our form, and we can do stuff with it on the backend, now what we want to do is display some feedback to the user.
And to do that, we're going to import a function from Flask called Flash.
Often, we want to display a non-permanent message to the user, something that only stays until we refresh the page or go to a different one.
These are called flashed messages in Flask.
And we want to display a flashed message when our visitor submits the contact form.
To use flashed messages, we need to create a secret key because Flask cryptographically signs all of the messages for security.
This might sound complicated, but really all we need to do is provide a secret key that Flask can use to sign the messages.
Generally, in production, we'd keep the secret key private.
And we'll look at how to do that in a future unit.
To use it after we instantiate our app, we need to say app.secret_key =
And then provide a random string that Flask can use for signing.
I'm just going to use 'some_secret'.
Secret keys are generally used for security, but we're going to go into more detail about these in future units as we said.
Now here, instead of a print statement, I'm going to call the Flash() function.
Let's say: ("Thanks {}, we have received your message!")
And then use the .format() method to pass in the request.form["name"] field.
Now that that's done, all we need to do is update our template so that it can retrieve the flashed messages.
To do that, we're going to create a with block.
So I'm going to use {% with messages = get_flashed_messages() %}
So get_flashed_messages() will return any of the messages that we've created using the Flash() function on the backend and store that in a variable called messages.
Now we're going to say that if there are messages, I'm just going to close off my if statement here, and my with statement with an {% endif %} and an {% endwith %}.
So if we have successfully returned messages from our get_flashed_messages() function, then we're going to create some HTML.
We'll give that a class so that we can style it later.
And then what we're going to do inside our <ul> is iterate through each of the messages because it's possible for us to create more than one.
So we'll create a for block that says {% for message in messages %}.
And I'll close that off with an {% end for %}.
And then in my for block, I'm going to say <li>{{ message }}</li>.
So this will display each individual message that we leave.
Now if we refresh our form, again I'll fill in Aaron's name, email address, and a random string as a phone number and a message.
Click on send, and we can see here now that as a list item, our flashed message is displayed: Thanks Aaron Sinnott, we have received your message!
Now of course, we probably would want to provide more styling for that and make it look a lot nicer.
But that's the basics of how to get flashed messages working with Flask.
In this section then, we've seen how to do advanced routing in Flask, how to create a form, and how to retrieve that information and do something with it on the backend.
Now our project is almost complete.
The only thing left to do is to deploy it so that it can be seen on the internet at large.
We'll do that in our next series of videos.

Next, we're going to have a look at how to create forms and some advanced routing.
  
  
  
