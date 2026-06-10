from predict import predict_spoilage
from rule_engine import generate_recommendation


def get_sensor_value(message, min_value, max_value):

    try:

        value = float(input(message))

    except:

        print("Invalid input")

        exit()


    if value < min_value or value > max_value:

        print(

            f"Value must be between {min_value} and {max_value}"

        )

        exit()


    return value


temp = get_sensor_value(

    "Temperature: ",

    0,

    50

)


humidity = get_sensor_value(

    "Humidity: ",

    0,

    100

)


prediction, bad_probability = predict_spoilage(

    temp,

    humidity

)


result = generate_recommendation(

    bad_probability,

    humidity,

    temp

)


print()

print(

    "Prediction:",

    prediction

)

print(

    "Bad Probability:",

    round(

        bad_probability * 100,

        2

    ),

    "%"

)

print(

    "Shelf Recommendation:",

    result["shelf"]

)

print()

print("Actions:")

for action in result["actions"]:

    print("-", action)