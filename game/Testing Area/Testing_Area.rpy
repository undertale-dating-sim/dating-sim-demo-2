label testing_area:
    call initialize
    stop music
    scene background deadroom

    while True:
        menu:
            "Testing Area"

            "Phone Calls":
                call testing_phone_calls

            "Events":
                call testing_events

            "Characters":
                #call testing_characters
                pass
            "Item Reactions":
                call testing_item_reactions

            "Test Images":
                call testing_images

            "Test Minigames":
                call testing_minigames

            "Test Credits":
                call scrolling_credits

            "Test Death":
                call death_event


label testing_phone_calls:
    while True:
        menu:
            "Toriel":
                call test_call("Toriel")
            "Frisk":
                call test_call("Frisk")
            "Flowey":
                call test_call("Flowey")
            "Napstablook":
                call test_call("Napstablook")

            "Exit":
                return


label test_call(monster = 'Toriel'):
    while True:
        menu:
            "[monster]"

            "Unknown":
                call expression "call_"+monster+"_Unknown" pass(world.get_monster(monster))
            "Same Room":
                call expression "call_"+monster+"_Same_Room" pass(world.get_monster(monster))
            "Cave_Room":
                call expression "call_"+monster+"_Cave_Room" pass(world.get_monster(monster))
            "Grass_Room":
                call expression "call_"+monster+"_Grass_Room" pass(world.get_monster(monster))
            "Ruins_Entrance":
                call expression "call_"+monster+"_Ruins_Entrance" pass(world.get_monster(monster))
            "Tunnels":
                call expression "call_"+monster+"_Tunnels" pass(world.get_monster(monster))
            "Dummy_Room":
                call expression "call_"+monster+"_Dummy_Room" pass(world.get_monster(monster))
            "Froggit_Room":
                call expression "call_"+monster+"_Froggit_Room" pass(world.get_monster(monster))
            "Sassy_Rock_Room":
                call expression "call_"+monster+"_Sassy_Rock_Room" pass(world.get_monster(monster))
            "Blooky_Room":
                call expression "call_"+monster+"_Blooky_Room" pass(world.get_monster(monster))
            "Spider_Bakery":
                call expression "call_"+monster+"_Spider_Bakery" pass(world.get_monster(monster))
            "Snail_Hunter":
                call expression "call_"+monster+"_Snail_Hunter" pass(world.get_monster(monster))
            "Tunnel_Divide":
                call expression "call_"+monster+"_Tunnel_Divide" pass(world.get_monster(monster))
            "Overlook":
                call expression "call_"+monster+"_Overlook" pass(world.get_monster(monster))
            "Black_Tree_Room":
                call expression "call_"+monster+"_Black_Tree_Room" pass(world.get_monster(monster))
            "Exit":
                return
    return

label test_character(monster = "Toriel"):

    $ world.current_area.current_room.monsters = []
    $ world.get_monster(monster).move_to_room("Dead Room")
    $ world.move_to_room("Dead Room")


    return
   

# label testing_characters:


#     menu:
#         "Toriel":
#             call test_character("toriel")

#         "Napstablook":
#             call test_character("napstablook")

#         "Flowey":
#             jump testing_flowey

#         "Frisk":
#             call test_character("frisk")

#         "Whimsun":
#             jump testing_whimsun

#         "Vegetoid":
#             jump testing_vegetoid

#         "Dummy":
#             jump testing_dummy

#         "Back":
#             return

#     return


label testing_item_reactions:

    menu:
        "Toriel":
            call test_items(world.get_monster("Toriel"))
        "Frisk":
            call test_items(world.get_monster("Frisk"))
        "Napstablook":
            call test_items(world.get_monster("Napstablook"))

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
            "Flowey":
                call test_flowey_events
            "Frisk":
                call test_frisk_events
            "Napstablook":
                call test_napstablook_events
            "Toriel":
                call test_toriel_events

            "Meals in the ruins":
                call ruins_meals_events

            "Back":
                return
    return

label test_flowey_events:
    while True:
        menu:
            "Flowey Hangout 1.5":
                call Flowey_Hangout_1_5_menu
label test_frisk_events:
    while True:
        menu:
            "Meeting Frisk":
                pass
            "Friendship Hangout 1":
                call frisk_friendship_hangout1_main
            "Friendship Event 1":
                call frisk_friendhsip_event_1
            "Friendship Event 2":
                call frisk_friendship_hangout2_menu
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

label test_toriel_events:
    while True:
        menu:
            "True Love Date 1":
                call toriel_tl_date01_opening
            "Friendship Event 1":
                call toriel_friendship_event01
            "Friendship Event 2":
                call toriel_friendship_event_2
            "Friendship Hangout":
                call toriel_friendship_hangout
            "Heartbreak Date 1":
                pass
            "Back":
                return
    return


label death_event:
    jump player_dies

label ruins_meals_events:
    while True:
        menu:
            "First meal":
                call ruins_first_breakfast
            "Dinners":
                menu:
                    "Frisk stays":
                        $World.days = "Monday"
                    "Frisk leaves":
                        $World.days = "Tuesday"
                    "Frisk is tired":
                        $World.days = "Wednesday"
                call ruins_dinner
            "Leftovers":
                call ruins_dinner_leftovers
            "Breakfast":
                call ruins_breakfast
            "Leave the Ruins":
                "Okay, so it's not a meal, but that's where this is for now. >_<"
                call ruins_basement_door_first_visit
            "Back":
                return
    return
