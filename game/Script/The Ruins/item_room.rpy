label tf_item_room:
    
    "The smell of freshly turned earth is carried on the wind."

    pause

    "The much smaller cave holds many interesting things."
    "It seems like a lot of trash has fallen down here through the hole in the ceiling." 
    "Most of it is either broken or so old it has fallen apart, but some may still be useful." 
    "The grass in the middle looks upturned, but behind it you can see a door."

    pause

    "What should you do?"

    menu:
        "What should you do?"
        "Check the garbage":
            "There are a few items here..."
            menu:
                "Pick up the.."
                "Heart Locket":
                    $ inventory.pick
                "Mirror":
                    "mirror"
                "Stick":
                    "stick"
                "Flower":
                    "flower"

    
    return