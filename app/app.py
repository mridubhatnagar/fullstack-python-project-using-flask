import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def student_information():
    studinfo = {
            "U101113FCS103": {
                "student_name": "Harry Potter",
                "age": 25,
                "gender": "Male",
                "house": "Griffendor",
            },
            "U101113FCS104": {
                "student_name": "Hermione Granger",
                "age": 27,
                "gender": "Female",
                "house": "Griffendor"
            },
            "U101113FCS105": {
                "student_name": "Ron Weasley",
                "age": 26,
                "gender": "Male",
                "house": "Griffendor"
            },
            "U101113FCS105": {
                "student_name": "Albus Dumbeldore",
                "age": 35,
                "gender": "Male",
                "house": "Griffendor"

            }
    }
    return render_template("student_information.html", data=jsonify(studinfo))