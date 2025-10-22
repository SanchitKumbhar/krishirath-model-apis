Absolutely brooo 😎 — here’s your complete **Markdown (`.md`) documentation** version, ready to save as `API_DOCUMENTATION.md` or paste into your project’s `README.md`.

---

````markdown
# 🌾 Crop Prediction API Documentation

## 📘 Overview
This API predicts the **most suitable crop** for a given location based on:
- **Latitude** and **Longitude** (used to fetch historical weather data)
- **Soil type** (used to determine average pH)
- A **pre-trained ML model** (`model.pkl`)

---

## 🚀 Endpoint

### **POST** `/api/v1/crop-predict`

---

## 📤 Request Format

### **Headers**
```http
Content-Type: application/json
````

### **Body (JSON)**

```json
{
  "lat": 19.0760,
  "long": 72.8777,
  "soil": "Alluvial Soil"
}
```

| Field  | Type   | Required | Description                                      |
| ------ | ------ | -------- | ------------------------------------------------ |
| `lat`  | float  | ✅        | Latitude of the location                         |
| `long` | float  | ✅        | Longitude of the location                        |
| `soil` | string | ✅        | Soil type (must match one from `soil_type.json`) |

---

## 🧪 Example Request

```bash
curl -X POST http://127.0.0.1:5000/api/v1/crop-predict \
     -H "Content-Type: application/json" \
     -d '{"lat": 19.0760, "long": 72.8777, "soil": "Black Soil (Regur Soil)"}'
```

---

## 📦 Example Response

```json
{
  "input": {
    "average_temperature": 28.5,
    "average_humidity": 70.3,
    "average_rainfall": 210.6
  },
  "predicted_crop": "Cotton"
}
```

---

## 📋 Response Fields

| Field                       | Type   | Description                                                 |
| --------------------------- | ------ | ----------------------------------------------------------- |
| `input.average_temperature` | float  | Average temperature fetched from `get_historical_weather()` |
| `input.average_humidity`    | float  | Average humidity fetched from weather data                  |
| `input.average_rainfall`    | float  | Average rainfall fetched from weather data                  |
| `predicted_crop`            | string | Predicted best crop for given soil and weather              |

---

## ❌ Error Responses

| HTTP Code | Cause                           | Example                                                                                 |
| --------- | ------------------------------- | --------------------------------------------------------------------------------------- |
| `400`     | Missing or invalid request body | `{"error": "Request must be JSON"}`                                                     |
| `400`     | Missing required field          | `{"error": "Missing one or more required fields: temperature, humidity, rainfall, ph"}` |
| `500`     | Internal server error           | `{"error": "KeyError: 'average_temperature'"}`                                          |

---

## ⚙️ Internal Logic Summary

1. Receive input — latitude, longitude, and soil type
2. Fetch **historical weather data** using `get_historical_weather(lat, lon)`
3. Fetch **soil pH** value from `soil_type.json`
4. Prepare features: `[temperature, humidity, rainfall, pH]`
5. Use **ML Model (`model.pkl`)** to predict the crop
6. Return prediction as a JSON response

---

## 🧩 Dependencies

| Library                   | Purpose                                 |
| ------------------------- | --------------------------------------- |
| `flask`                   | Web API framework                       |
| `numpy`                   | For creating feature arrays             |
| `joblib`                  | Loading the trained ML model            |
| `json`                    | Reading soil type data                  |
| `historicalPreprocessing` | Custom module for weather data fetching |

---

## ▶️ Run the API

```bash
python app.py
```

Server will start on:

```
http://127.0.0.1:5000/
```

---

## 🗂 File Structure Example

```
project/
│
├── app.py
├── model.pkl
├── soil_type.json
├── historicalPreprocessing.py
└── API_DOCUMENTATION.md
```

---

## 💡 Tips

* Make sure `soil_type.json` contains valid soil types for India.
* You can test the endpoint easily using **Postman** or **curl**.
* If you host this on a server (like Render, Railway, or AWS), ensure that your model and JSON files are deployed with it.

---

**Author:** *Sanchit Kumbhar*
**Version:** 1.0.0
**Framework:** Flask
**Language:** Python 🐍

```

---

Would you like me to make it **GitHub README-ready** (with badges, logo, and emoji styling for sections)? It’ll look 🔥 when viewed on your repo page.
```
