#!/usr/bin/python3

from flask import Flask, render_template 
import random
app = Flask(__name__)

colors = ["red","blue","green","pink","orange","black"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

@app.route("/")
def home():
    return render_template("index.html", 
                        heading="What's lucky for you?")

@app.route("/color")
def color_page():
    lucky_color = random.choice(colors)
    return render_template("page.html", 
                        category="color",
                        lucky_item=lucky_color,
                        icon="paint.png")

@app.route("/week")
def week_page():
    random_weekday = random.choice(weekdays)
    return render_template("page.html", 
                        category="weekday",
                        lucky_item=random_weekday,
                        icon="calendar.png")

@app.route("/month")
def month_page():
    random_month = random.choice(months)
    return render_template("page.html", 
                        category="month",
                        lucky_item=random_month,
                        icon="calendar.png")
