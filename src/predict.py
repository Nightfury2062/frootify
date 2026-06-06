import joblib
import pandas as pd
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"


model = joblib.load(
    MODEL_DIR / "fruit_spoilage_rf.pkl"
)

feature_order = joblib.load(
    MODEL_DIR / "feature_order.pkl"
)


def create_features(
        fruit,
        temp,
        humidity,
        light,
        co2
):

    light = np.log1p(light)

    data = {

        'Temp': temp,

        'Humid (%)': humidity,

        'Light (Fux)': light,

        'CO2 (ppm)': co2,

        'Temp_Humidity':
            temp * humidity,

        'CO2_Temp_Ratio':
            co2 / (temp + 1e-6),

        'High_Humidity':
            int(humidity > 90),

        'Fruit_Banana':
            int(fruit == "Banana"),

        'Fruit_Orange':
            int(fruit == "Orange"),

        'Fruit_Pineapple':
            int(fruit == "Pineapple"),

        'Fruit_Tomato':
            int(fruit == "Tomato")

    }

    return data


def predict_spoilage(
        fruit,
        temp,
        humidity,
        light,
        co2
):

    data = create_features(

        fruit,

        temp,

        humidity,

        light,

        co2

    )

    df = pd.DataFrame(
        [data]
    )

    df = df[
        feature_order
    ]

    prediction = model.predict(
        df
    )[0]

    probabilities = model.predict_proba(
        df
    )[0]

    bad_index = list(
        model.classes_
    ).index(
        "Bad"
    )

    bad_probability = probabilities[
        bad_index
    ]

    return (
        prediction,
        bad_probability
    )