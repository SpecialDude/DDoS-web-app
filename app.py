from flask import Flask
from flask import render_template
from flask import request
from prediction import getPrediction

import pandas as pd

app = Flask(__name__)

SAMPLE_DATA_FILENAME = "sample data.csv"
SAMPLE_DATA = pd.read_csv(SAMPLE_DATA_FILENAME)

def arrange_data(data):
    arranged_data = dict(data.lists())
    return pd.DataFrame(arranged_data)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input-feature/", methods=["GET", "POST"])
def input_feature():
    if request.method == "POST":
        return "Predicted Target: " + str(getPrediction(request.form))

    feature_names = SAMPLE_DATA.columns[:-1]
    return render_template("input_feature.html", context={"features":feature_names})


@app.route("/select-feature/", methods=["GET", "POST"])
def select_random_feature():
    context = {
        "display": False
    }

    if request.method == "POST":
        n_of_features = int(request.form["number_of_features"])

        if n_of_features > len(SAMPLE_DATA):
            context["errmsg"] =  "Cannot fetch samples, number is too large"
        else:

            feature_values = SAMPLE_DATA.sample(n_of_features)

            variables = feature_values.iloc[:, :-1]
            target = feature_values["target"]
            predicted_target = [getPrediction(values.to_dict()) for _, values in variables.iterrows()]

            feature_values["predicted_target"] = predicted_target

            context["feature_values"] = feature_values
            context["number_of_features"] = n_of_features
            context["display"] = True

    return render_template("select_feature.html", context=context)


@app.route("/update-feature/")
def update_feature():
    return "Update Feature"


@app.route("/get-ddos-prediction/")
def get_ddos_prediction():
    return "Get  DDos Prediction"


@app.route("/bulk-prediction/", methods=["GET", "POST"])
def perform_bulk_prediction():

    feature_names = SAMPLE_DATA.columns[:-1]
    context = {
        "display_form": True,
        "feature_names": feature_names,
        "bulk_data": [],
    }

    if request.method == "POST":
        print(request.form)
        bulk_data = arrange_data(request.form)
        print(bulk_data)

        predicted_target = [getPrediction(values.to_dict()) for _, values in bulk_data.iterrows()]
        bulk_data["predicted_target"] = predicted_target

        context["display_form"] = False
        context["bulk_data"] = bulk_data

    return render_template("bulk_prediction.html", context=context)


@app.route("/metrics/")
def get_metrics():
    return "Get Metrics"
