
from flask import Flask, render_template, request, redirect, jsonify
import json
import requests
app = Flask(__name__, template_folder="templates")



@app.route("/")
def rootRoute():
    return redirect("/home")


@app.route("/home")
def homePage():
    return render_template("home.html", response="")


@app.route("/experiences")
def experiencesPage():
    return render_template("experiences.html")


@app.route("/about")
def aboutPage():
    return render_template("about.html")


@app.route("/places", methods=['GET'])
def placePage():
    placeName = request.args["query"]

    response = requests.get(
        f'https://e4hw20a837.execute-api.us-east-1.amazonaws.com/v1/places?name={placeName}').json()


    return render_template('places.html', response=response)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
