from predict import predict_spoilage

from rule_engine import generate_recommendation


VALID_FRUITS={

1:'Banana',

2:'Orange',

3:'Pineapple',

4:'Tomato'

}


def get_fruit():

    print()

    print("Choose Fruit:")

    print("1 Banana")

    print("2 Orange")

    print("3 Pineapple")

    print("4 Tomato")

    try:

        choice=int(
            input(
                "Enter choice: "
            )
        )

    except:

        print(
            "Invalid input."
        )

        exit()


    if choice not in VALID_FRUITS:

        print(
            "Invalid fruit choice."
        )

        exit()


    return VALID_FRUITS[
        choice
    ]


def get_sensor_value(
        message,
        min_value,
        max_value
):

    try:

        value=float(
            input(
                message
            )
        )

    except:

        print(
            "Invalid numeric input."
        )

        exit()


    if value<min_value or value>max_value:

        print(

f"Value must be between {min_value} and {max_value}"

        )

        exit()

    return value



fruit=get_fruit()


temp=get_sensor_value(

"Temperature: ",

0,

50

)

humidity=get_sensor_value(

"Humidity: ",

0,

100

)

light=get_sensor_value(

"Light: ",

0,

1000

)

co2=get_sensor_value(

"CO2: ",

0,

5000

)



prediction,bad_probability = predict_spoilage(fruit,temp,humidity,light,co2)


result=generate_recommendation(

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
"Shelf Recommendation:",
result["shelf"]
)

print()

print(
"Actions:"
)

for action in result[
"actions"
]:

    print(
        "-",
        action
    )