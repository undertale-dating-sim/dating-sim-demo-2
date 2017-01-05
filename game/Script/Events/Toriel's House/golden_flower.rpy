
label golden_flower_event:
    #"Today is day [world.day]"
    #$ world.currentArea.current_room.plant_watered_times = 0
    if (world.day - world.currentArea.current_room.day_watered > 2):
        $ world.currentArea.current_room.plant_watered_times = 0
        
    if (world.currentArea.current_room.plant_watered_times < 3):
        if (world.day - world.currentArea.current_room.day_watered == 0):
            "This flower pot is home to a yellow flower. It looks refreshed for now."
        else:
            if (world.day - world.currentArea.current_room.day_watered == 1) :
                "This flower pot is home to a yellow flower. The earth is still a little damp."
            else:   
                "This flower pot is home to a yellow flower, but the earth inside it is dry."
            menu:
                "Water it":
                    $ world.currentArea.current_room.plant_watered_times +=1
                    $ world.currentArea.current_room.day_watered = world.day
                    "It perks up immediately"
                "Don't water it":
                    "You must be thirstier, huh?"
    elif (world.currentArea.current_room.plant_watered_times < 5):
        "The flower is nice and healthy"
        if (world.day - world.currentArea.current_room.day_watered == 0):
            "The flower already looks happier from your earlier watering."
        else:
            menu:
                "Water it":
                    $ world.currentArea.current_room.plant_watered_times +=1
                    $ world.currentArea.current_room.day_watered = world.day
                    "Daily waterings seem to be doing this flower good."
                "Don't water it":
                    if (world.day - world.currentArea.current_room.day_watered == 1):
                        "It looks like it could go another day without."
                    else:
                        "The flower seems to droop slightly as you decide not to water it."
    else:
        "The flower is well cared for, "
        if (world.day - world.currentArea.current_room.day_watered == 0):        
            "The soil is already nice and moist from your diligent watering."
        else:
            menu:
                "water it":
                    $ world.currentArea.current_room.plant_watered_times +=1
                    $ world.currentArea.current_room.day_watered = world.day
                    "The flower quite enjoys your care"
                    "You must have a green thumb"
                "Don't water it":
                    "It seems healthy enough as is, I guess"
    return