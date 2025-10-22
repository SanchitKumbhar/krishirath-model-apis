import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
from datetime import datetime, timedelta, UTC

def get_historical_weather(lat, lon, months=3):
    # Setup cache + retry
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=3, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Define date range (past `months`)
    end_date = datetime.now(UTC).date()
    start_date = end_date - timedelta(days=30 * months)

    # Use the archive endpoint
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "relative_humidity_2m_max",
            "relative_humidity_2m_min",
            "precipitation_sum"
        ],
        "timezone": "auto",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat()
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()

    # Extract data arrays
    tmax = daily.Variables(0).ValuesAsNumpy()
    tmin = daily.Variables(1).ValuesAsNumpy()
    hmax = daily.Variables(2).ValuesAsNumpy()
    hmin = daily.Variables(3).ValuesAsNumpy()
    rain = daily.Variables(4).ValuesAsNumpy()

    # Compute averages over the period
    avg_temp = ((tmax + tmin) / 2).mean()
    avg_humidity = ((hmax + hmin) / 2).mean()
    avg_rainfall = rain.mean()

    return {
        "average_temperature": round(float(avg_temp), 2),
        "average_humidity": round(float(avg_humidity), 2),
        "average_rainfall": round(float(avg_rainfall), 2)
    }


