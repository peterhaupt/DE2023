# importing Flask and other modules
import json
import os

import requests
from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkdiabetes', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        prediction_input = [
            {
                "ntp": int(request.form.get("ntp")),  # getting input with name = ntp in HTML form
                "pgc": int(request.form.get("pgc")),  # getting input with name = pgc in HTML form
                "dbp": int(request.form.get("dbp")),
                "tsft": int(request.form.get("tsft")),
                "si": int(request.form.get("si")),
                "bmi": float(request.form.get("bmi")),
                "dpf": float(request.form.get("dpf")),
                "age": int(request.form.get("age"))
            }
        ]

        print(prediction_input)

        # use requests library to execute the prediction service API by sending an HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        predictor_api_url = os.environ['PREDICTOR_API']
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))

        print(res.status_code)
        print(res.json())

        prediction_value = res.json()['result']

        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
