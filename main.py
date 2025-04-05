import pandas as pd
import numpy as np
from flask import Flask, render_template
import os

data = pd.read_csv("data.csv")

def index():
    name = data[data["category"] =="name"]["text"].values[0]
    position = data[data["category"] =="position"]["text"].values[0]
    contacts = data[data["category"] =="contacts"]["text","link"].replace({np.nan: None}).values
    skills = data[data["category"] =="name"]["skills"].values
    projects = data[data["category"] =="name"]["projects","link"].replace({np.nan: None}).values
    education = data[data["category"] =="education"]["text"].values
    achievments = data[data["category"] =="name"]["achievments"].values
    facts = data[data["category"] =="facts"]["text"].values

    return render_template("index.html", name=name, photo=photo, position=position, contacts=contacts,skills=skills,projects=projects,education=education,achievments=achievments,facts=facts)

folder = os.getwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)
app.add_url_rule("/", "index", index)
app.run()

