import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        material = request.form["material"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(material),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(material):
    return """Suggest three names for a product for this material type.

material: Aluminum
Names: Aluminum Foil, Aluminum Spacers, Aluminum Cans
material: Brass
Names: Brass Bolts, Brass Bar, Brass Sheet
material: {}
Names:""".format(
        material.capitalize()
    )
