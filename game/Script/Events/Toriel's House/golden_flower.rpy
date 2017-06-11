label golden_flower_event:

    if (world.day - player.variables['toriel_plant_watered_day'] > 2):
        $ player.variables['toriel_plant_watered_count'] = 0
        
    if (player.variables['toriel_plant_watered_count'] < 3):
        if (world.day - player.variables['toriel_plant_watered_day'] == 0):
            "This flower pot is home to a yellow flower. It looks refreshed for now."
        else:
            if (world.day - player.variables['toriel_plant_watered_day'] == 1) :
                "This flower pot is home to a yellow flower. The earth is still a little damp."
            else:   
                "This flower pot is home to a yellow flower, but the earth inside it is dry."
            menu:
                "Water it":
                    $ player.variables['toriel_plant_watered_count'] +=1
                    $ player.variables['toriel_plant_watered_day'] = world.day
                    "It perks up immediately"
                "Don't water it":
                    "You must be thirstier, huh?"
    elif (player.variables['toriel_plant_watered_count'] < 5):
        "The flower is nice and healthy"
        if (world.day - player.variables['toriel_plant_watered_day'] == 0):
            "The flower already looks happier from your earlier watering."
        else:
            menu:
                "Water it":
                    $ player.variables['toriel_plant_watered_count'] +=1
                    $ player.variables['toriel_plant_watered_day'] = world.day
                    "Daily waterings seem to be doing this flower good."
                "Don't water it":
                    if (world.day - player.variables['toriel_plant_watered_day'] == 1):
                        "It looks like it could go another day without."
                    else:
                        "The flower seems to droop slightly as you decide not to water it."
    else:
        "The flower is well cared for, "
        if (world.day - player.variables['toriel_plant_watered_day'] == 0):        
            "The soil is already nice and moist from your diligent watering."
        else:
            menu:
                "water it":
                    $ player.variables['toriel_plant_watered_count'] +=1
                    $ player.variables['toriel_plant_watered_day'] = world.day
                    "The flower quite enjoys your care"
                    "You must have a green thumb"
                "Don't water it":
                    "It seems healthy enough as is, you suppose"
    return

label toriel_friendship_event_2(owner=get_toriel()):

    show toriel smile with Dissolve(.25)
    toriel "Oh! I have great news. I do not know if you have noticed, but the stunted golden flower in our corridor has finally bloomed. I had been fretting over that poor thing so long, too. Ah well, no worries now I suppose. Maybe it was just shy."
    toriel "Still, it is quite strange is it not? It flowered only a little after you came. Perhaps you are some sort of good omen?"
    menu:
        "Or perhaps I’ve actually been watering it.":
            $world.get_monster ('Toriel').update_FP(-5)
            show toriel blushing with Dissolve(.25)
            toriel "Err, yes. I suppose that is also a possibility."
            toriel "Although, even if only through common sense – it appears you have a way with plants."
        "It’s the power of friendship.":
            $world.get_monster('Toriel').update_FP(8)
            show toriel smile with Dissolve(.25)
            toriel "Oh, that is a nice way to put it!"
            toriel "Although, friendship or no - it appears you have a way with plants."
        "It’s the power of love.":
            $world.get_monster('Toriel').DP +=8
            $world.get_monster('Toriel').update_FP(8)
            show toriel surprised with Dissolve(.25)
            toriel "Ah yes. I suppose love is said to be the most powerful source... Still – you must have had a lot of love for that flower for it to bloom so fast..."
            toriel "Although, love or no – it appears you have a way with plants."
    show toriel normal with Dissolve(.25)
    toriel "That is already miles more than I can say for myself. It is not that I haven't tried. I have, and many times... but it seems I have a 'black thumb' of sorts."
    toriel "I am not terribly good at keeping anything alive for very long. Truthfully, it is impressive the flower survived as long as it did."
    toriel "If you have some spare time, perhaps sometime you would like to help me out with the tree in front of our home? Any leaves that grow on it just drop off, regardless of weather or season."
    toriel "It really is quite a shame. However, I am sure that with your help, we could bring it back around."
    menu:
        "I’d love to.":
            $world.get_monster('Toriel').update_FP(5)
            toriel "Fantastic! Please approach me about it when you would like to start."
        "That dead black thing? It’ll be tough.":
            $world.get_monster('Toriel').update_FP(-5)
            toriel "Oh yes, I fully realize. You do not have to of course – just if you have a boring day and nothing to do."
            toriel "Either way, there is no need to worry about it for now. Just approach me if you would like to start."
    $ player.variables['Toriel_Friendship_2_Complete'] = True
    # dateSaveTheTreeOpen = True
    return