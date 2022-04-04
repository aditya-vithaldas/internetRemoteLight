How often have we wanted to control something over the internet (a smartphone app, or a simple web page). Sure Google Home and Alexa and control practically any commercial off the shelf project, but where is the fun in that. 

As a maker, would you want to create something that allows you to control something as simple as a light (lets start with an LED light, and progress from there). 

For most users getting into electronics, one of the first projects that they do, is controlling an LED with a battery, to get a basic undertanding of the circular circuit). Sommething like this

![alt text](images/101.png)

What we are attempting to do, is just a minor variation of #2. We would control the switch off the internet, with a simple webpage, with basic controls. From a framework standpoint, the objective would be to make the same as flexible as possible, with the ability to add as many controls (E.g. up, down), for any number of applications (robotics, fans etc). 

But for now, all we care about, is a "start" and a "stop" options. 

So here goes. 

Client code (Raspberry Pi sniffer)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"
```
	
What did that code do?

First we `import` the `Flask` class. An instance of this class will be our WSGI application.

Next we create an instance of this class. The first argument is the name of the application’s module or package. `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

We then use the `route()` decorator to tell Flask what URL should trigger our function. In this case we use `/` routh, which is the default route of any website.

The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

To learn more, checkout the [official guide](https://flask.palletsprojects.com/en/2.0.x/quickstart/).
