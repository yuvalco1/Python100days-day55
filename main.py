import random

from flask import Flask

app = Flask(__name__)

randon_number = random.randint(0, 9)

colors = ["red", "blue", "yellow", "orange", "purple", "pink", "black", "brown", "gray", "cyan"]

# random.choice(colors)

print(randon_number)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")


@app.route("/<int:number>")
def check(number):
    if number == randon_number:
        return right()
    elif number < randon_number:
        return too_low()
    else:
        return too_high()

def right():
    return ("<h1 style='color:green' >You Found me !</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")


def too_low():
    color_style_str = f"style='color:{random.choice(colors)}'"
    return (f"<h1 {color_style_str} >Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")

def too_high():
    color_style_str = f"style='color:{random.choice(colors)}'"
    return (f"<h1 {color_style_str} >Too high, try again!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")


if __name__ == '__main__':
    app.run(debug=True)
