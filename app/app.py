import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def student_information():
    if request.method == "POST":
        rollno = request.form.get("rollno.")
        print(f"Roll No.: {rollno}")
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
                "U101113FCS106": {
                    "student_name": "Albus Dumbeldore",
                    "age": 35,
                    "gender": "Male",
                    "house": "Griffendor"

                }
        }

        if rollno in studinfo:
            data = jsonify(studinfo[rollno])
        else:
            data = jsonify({})
            print("No data")
        return data
    elif request.method == "GET":
        return render_template("student_information.html")
