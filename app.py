from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app=flask(__name__)
client=MongoClient("localhost", 27015)

@app.route("/")
@app.route("/index")
def index:
    return render_template("index.html")

if __name__ == "__main__":
    print(:27015)
    app.run(debug=True)

