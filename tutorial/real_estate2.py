from flask import Flask, render_template, request
from sklearn.externals import joblib
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(sqft=None, condition=None):
    location = None
    valuation = None
    if request.method == 'POST':
        if request.form['sqft']:
            sqft = request.form['sqft']
            condition = request.form['condition']
            waterfront_flag = 1 if request.form.get("waterfront") == 'on' else 0
            address = request.form['address']
            below_grade = request.form['below_grade']
            if len(address) > 10:
                valuation, location = better_estimator(int(sqft), waterfront_flag, int(below_grade), address)
            else:
                valuation = ballpark_estimator(int(sqft), float(condition))

    return render_template('index2.html',
                           sqft=sqft,
                           condition=condition,
                           location=location,
                           valuation=valuation)


def ballpark_estimator(sqft=2080, condition=3.4):
    return -214216.30529291916 + 292.81216765 * sqft + 43037.62951553 * condition


#  put better_estimator code here



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
