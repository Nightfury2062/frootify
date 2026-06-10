import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"


model = joblib.load(

    MODEL_DIR / "fruit_spoilage_rf_tomato.pkl"

)


feature_order = joblib.load(

    MODEL_DIR / "feature_order_tomato.pkl"

)


def create_features(

        temp,

        humidity

):

    data = {

        'Temp': temp,

        'Humid (%)': humidity,

        'Temp_Humidity': temp * humidity,

        'High_Humidity': int(

            humidity > 90

        )

    }

    return data



def predict_spoilage(

        temp,

        humidity

):

    data = create_features(

        temp,

        humidity

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