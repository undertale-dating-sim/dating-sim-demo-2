label testing_area:
    call initialize
    stop music
    play music "audio/music/scary.ogg"
    scene background deadroom

    while True:
        menu:
            "Testing Area"

            "Phone Calls":
                call testing_phone_calls

            "Events":
                call testing_events

            "Characters":
                call testing_characters

            "Item Reactions":
                call testing_item_reactions

            "Test Images":
                call testing_images

            "Test Minigames":
                call testing_minigames

            "Test Credits":
                call scrolling_credits


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

        "Back":
            return
        
    return


label testing_item_reactions:
    
    menu:
        "Toriel":
            call test_items(world.get_monster("Toriel"))
        "Frisk":
            call test_items(world.get_monster("Frisk"))

        "Back":
            return

    jump testing_area

label test_items(monster):
    $  renpy.show(monster.default_sprite)
    while True:
        menu:
            "Current item total [monster.given_today_count].  Current FP [monster.FP]."
            "Spider_Donut":
                $ monster.give_item(Spider_Donut())
            "Butts_Pie":
                $ monster.give_item(Butts_Pie())
            "Snail_Pie":
                $ monster.give_item(Snail_Pie())
            "White_Chocolate":
                $ monster.give_item(White_Chocolate())
            "Milk_Chocolate":
                $ monster.give_item(Milk_Chocolate())
            "Monster_Candy":
                $ monster.give_item(Monster_Candy())
            "Spider_Cider":
                $ monster.give_item(Spider_Cider())
            "Unknown / Ungiftable":
                $ monster.give_item(Stick())
            "Reset Items for day":
                $ monster.given_today_count = 0
            "Back":
                return
    return



label testing_minigames:
    menu:
        "Choose your poison."
        "Undersnail":
            call demo_undersnail

    return

label testing_events:
    while True:
        menu:
            "Poor Whimsun":
                call whimsun_re_start
            "Vegetoid Event":
                call vegetoid_ruins_re_start
            "Dummy Event NYI":
                call dummy_ruins_event_start
                
            "Frisk":
                call test_frisk_events
            "Napstablook":
                call test_napstablook_events
            "Back":
                return
    return


label test_frisk_events:
    while True:
        menu:
            "Meeting Frisk":
                pass
            "Friendship Hangout 1":
                pass
            "Friendship Event 1":
                pass
            "Friendship Event 2":
                pass
            "Back":
                return
    return
    
label test_napstablook_events:
    while True:
        menu:
            "True Love Date 1":
                pass
            "Friendship Hangout 1":
                pass
            "Friendship Hangout 2":
                pass
            "Heartbreak Date 1":
                pass
            "Back":
                return
    return


    