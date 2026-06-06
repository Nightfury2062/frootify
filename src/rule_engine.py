def generate_recommendation(

        bad_probability,

        humidity,

        temp

):

    actions=[]


    if bad_probability >= 0.7:

        shelf="Consume within 1-3 days"


    elif bad_probability >= 0.3:

        shelf="Consume within 4-7 days"


    else:

        shelf="Suitable for long storage"



    if humidity > 90:

        actions.append(

            "Reduce humidity"

        )



    if temp > 28:

        actions.append(

            "Lower storage temperature"

        )



    if len(actions)==0:

        actions.append(

            "Storage conditions acceptable"

        )



    return {

        "shelf": shelf,

        "actions": actions

    }