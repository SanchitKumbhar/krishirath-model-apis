import json
from flask import Flask, request, jsonify
from historicalPreprocessing import get_historical_weather
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/api/v1/crop-predict', methods=["POST"])
def predict_crop():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        corr = request.get_json()
        lat = corr.get("lat")
        long = corr.get("long")
        soiltype = corr.get("soil")
        data = get_historical_weather(lat=lat,lon=long)
        print("here")

        temperature = data.get("average_temperature")
        humidity = data.get("average_humidity")
        rainfall = data.get("average_rainfall")

        with open("soil_type.json", "r") as file:
            jsondata = json.load(file)

        for soil in jsondata["indian_soils"]:
            if soil["type"].lower() == soiltype.lower():
                ph=soil["average_pH"]
                break
        else:
            print("Soil not found!")


        if None in [temperature, humidity, rainfall, ph]:
            return jsonify({"error": "Missing one or more required fields: temperature, humidity, rainfall, ph"}), 400

        features = np.array([[temperature, humidity, rainfall, ph]])
        prediction = model.predict(features)[0]

        return jsonify({
            "input": data,
            "predicted_crop": str(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
