
from flask import Flask, render_template, request, redirect, jsonify
import json
import requests
app = Flask(__name__, template_folder="templates")



@app.route("/")
def hello():
    return redirect("/home")


@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/experiences")
def experiencesPage():
    return render_template("experiences.html")


@app.route("/about")
def aboutPage():
    return render_template("about.html")


@app.route("/places", methods=['GET'])
def placePage():
    placeName = request.args["query"]
    print(placeName)
    placeName = placeName.replace(' ', '+')
    print(placeName)

    response = requests.get(
        f'https://e4hw20a837.execute-api.us-east-1.amazonaws.com/v1/places?name={placeName}')

    response = response.json()
    placeName = placeName.replace('+', ' ')

    print(response)
    htmlContent = f'''
    ~~~ &emsp;  ~~~ &emsp;  ~~~ &emsp; ~~~
    <h1>  {placeName}</h1>
    ~~~ &emsp;  ~~~ &emsp;  ~~~ &emsp; ~~~
    <h2>🗺️{response['City']}, {response['State']}</h2>
    <p></p>
    <h3>{response['Description']}</h3>
    <p></p>
    
    <div class="container">
      <div class="row g-2">
        <div class="col-6">
          <div class="p-3 border bg-light">
            <h4>⭐Rating - {response['Rating']}</h4>
          </div>
        </div>
        <div class="col-6">
          <div class="p-3 border bg-light">
            <h4>⏱️Duration : {response['Duration']}</h4>
          </div>
        </div>
        <div class="col-6">
          <div class="p-3 border bg-light">
            <h4>👨‍👩‍👧‍👦Visitors per year : {response['No of visitors per year']}</h4>
          </div>
        </div>
        <div class="col-6">
          <div class="p-3 border bg-light">
            <h4>🏄‍♂️Best Time To Visit : {response['Best time to visit']}</h4>
          </div>
        </div>
      </div>
    </div>
    <p></p>
    <h4>💸Ticket fare : {response['Price']}</h4>
    
    '''
    return render_template('home.html', cust_cont=htmlContent)
    # return jsonify(data[placeName])



if __name__ == "__main__":
    app.run(debug=True, port=5000)
