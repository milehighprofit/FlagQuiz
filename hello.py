from flask import Flask, render_template, request
import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
import cv2

app = Flask(__name__)

@app.route("/")
def index():
    path = "flags/"
    files=os.listdir(path)
    d=random.choice(files)
    img = cv2.imread("flags/"+d)
    cv2.imshow(d, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return render_template("index.html", flag=d)

@app.route("/check", methods=["POST"])
def check():
    data = get_data()
    vej = request.form["flag"]
    for d in data:
        if d['filnavn'] == vej:
            country_name = d['land']
            break
        else:
            country_name = "Not found yet"

    if request.form["guess"] == country_name:
        return "That's correct!"
    else:
        return f"That's wrong, it's {country_name}."

def get_data():
    """Reads csv file and returns list of dictionaries the represents each row in csv file"""
    data = []
    with open('Products.csv', newline='') as csvfile:
        prison_reader = csv.DictReader(csvfile)
        for row in prison_reader:
            data.append(row)
        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')