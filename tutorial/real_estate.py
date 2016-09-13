from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(sqft=None, condition=None):
    valuation = None
    if request.method == 'POST':
        if request.form['sqft'] and request.form['condition']:
            sqft = request.form['sqft']
            condition = request.form['condition']
            valuation = ballpark_estimator(int(sqft), float(condition))

    return render_template('index.html',
                           sqft=sqft,
                           condition=condition,
                           valuation=valuation)

# put ballpark_estimator here


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)