label testing_area:
    call initialize
    stop music

    menu:
        "Testing Area"

        "Phone Calls":
            jump testing_phone_calls

        "Characters":
            jump testing_characters

        "Item Reactions":
            jump testing_item_reactions

    jump testing_area


label testing_phone_calls:
    while True:
        menu:
            "Toriel":
                call test_call("Toriel")
            "Frisk":
                call test_call("Frisk")
            "Napstablook":
                call test_call("Napstablook")

            "Exit":
                return


label test_call(monster = 'Toriel'):
    while True:
        menu:
            "[monster]"

            "Unknown":
                call expression "call_"+monster+"_Unknown"
            "Cave_Room":
                call expression "call_"+monster+"_Cave_Room"
            "Grass_Room":
                call expression "call_"+monster+"_Grass_Room"
            "Ruins_Entrance":
                call expression "call_"+monster+"_Ruins_Entrance"
            "Tunnels":
                call expression "call_"+monster+"_Tunnels"
            "Dummy_Room":
                call expression "call_"+monster+"_Dummy_Room"
            "Froggit_Room":
                call expression "call_"+monster+"_Froggit_Room"
            "Sassy_Rock_Room":
                call expression "call_"+monster+"_Sassy_Rock_Room"
            "Blooky_Room":
                call expression "call_"+monster+"_Blooky_Room"
            "Spider_Bakery":
                call expression "call_"+monster+"_Spider_Bakery"
            "Snail_Hunter":
                call expression "call_"+monster+"_Snail_Hunter"
            "Tunnel_Divide":
                call expression "call_"+monster+"_Tunnel_Divide"
            "Overlook":
                call expression "call_"+monster+"_Overlook"
            "Black_Tree_Room":
                call expression "call_"+monster+"_Black_Tree_Room"
            "Exit":
                return
    return

label test_character(monster = "Toriel"):
    
    $ world.currentArea.current_room.monsters = []
    $ world.get_monster(monster).move_to_room("Dead Room")
    $ world.move_to_room("Dead Room")

    return


label testing_characters:
    

    menu:
        "Toriel":
            call test_character("toriel")

        "Napstablook":
            call test_character("napstablook")

        "Flowey":
            jump testing_flowey

        "Frisk":
            jump testing_frisk

        "Whimsum":
            jump testing_whimsum

        "Vegetoid":
            jump testing_vegetoid

        "Dummy":
            jump testing_dummy
        
    jump testing_area


label testing_item_reactions:
    
    "Items go here."

    jump testing_area