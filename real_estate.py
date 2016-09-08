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


def ballpark_estimator(sqft=2080, condition=3.4):
    return -214216.30529291916 + 292.81216765 * sqft + 43037.62951553 * condition

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
