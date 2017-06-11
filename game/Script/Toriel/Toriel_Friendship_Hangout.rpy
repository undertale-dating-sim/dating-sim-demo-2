#if world.get_monster ('Toriel').FP >=20
#if friendship1 complete
init:
    $loop_count =0
    $toriel_hangout_pun = False
    $toriel_hangout_pun_count = 0
    $toriel_hangout_pun_hater = False

label toriel_friendship_hangout_1(owner=get_toriel()):
    show toriel smallsmile with Dissolve(.25)
    toriel "Hello, my friend. I am preparing a new pie recipe for dinner. Would you like to help?"
    menu:
        "Sure!":
            $world.get_monster('Toriel').update_FP(2)
            toriel "Wonderful! I think this pie will be very delicious."
            toriel "Well, actually, it is not quite a pie. It is actually a quiche - a snail quiche, in fact."
            toriel "It is not a recipe that I recognize, but a friend gave it to me, so I just had to try it."
        "I can try, but it might be a disaster.":
            $world.get_monster('Toriel').update_FP(2)
            toriel "Do not worry, I am sure you will do just..."
            show toriel laughing with Dissolve(.25)
            toriel "{i}Pie{/i}-ne!"
            call .pie_ne                    
        "No, thank you.":
            toriel "Well then, I will need you to leave the kitchen if you will not be helping. Dinner will be ready shortly." 
            return
        "What sort of pie is it?":
            $world.get_monster('Toriel').update_FP(1)
            toriel "Oh! It is actually not exactly a pie. It is a quiche! A snail quiche, in fact. I am very excited to try it." 
            toriel "So, would you like to help make it with me?"
            menu:
                "Sure, sounds delicious":
                    $world.get_monster('Toriel').update_FP(2)
                    toriel "Wonderful! I think it will be delicious indeed. A friend of mine gave me the recipe, and I just had to try it!"
                "I can try, but it might be a disaster.":
                    $world.get_monster('Toriel').update_FP(1)
                    toriel "Do not worry, I am sure you will do just..."
                    show toriel laughing with Dissolve(.25)
                    toriel "{i}Pie{/i}-ne!"
                    call .pie_ne
                "Ew, no thanks.":
                    $world.get_monster('Toriel').update_FP(-1)
                    show toriel annoyed  with Dissolve(.25)
                    toriel "Well, you do not need to be so rude about it."
                    toriel "I will need you to leave the kitchen, then, so you will not be in the way."
                "No, thank you.":
                    toriel "Well, then, I will need you to leave the kitchen if you will not be helping. Dinner will be ready shortly." 

    show toriel smile with Dissolve(.25)
    toriel "The first step is to make the crust. Would you please get the butter from the fridge?"
    $loop_count = 0
    call .get_butter
    if loop_count == 7:
        return
    
    show toriel smile with Dissolve(.25)
    toriel "If you need help understanding this recipe, my friend, you need only ask for a..."
    show toriel laughing with Dissolve(.25)
    toriel "...Tu-Toriel!"
    menu:
        "*Force a chuckle":
            show toriel awkward with Dissolve(.25)
            toriel "Anyway, next we will need to roll the crust and put it into the pie tin."
            toriel "The pie tin is under the oven. Would you please go get it?"
        "*Laugh":
            $world.get_monster('Toriel').update_FP(2)
            show toriel blushing with Dissolve(.25)
            toriel "I am glad you are enjoying my jokes, but we do need to put this crust in the pan, now."
            toriel "Would you please get the pie tin from under the oven?" 
        "If I need help, I will {i}crust{/i} you to assist me.":
            $world.get_monster('Toriel').update_FP(4)
            toriel "Oh my, that is a good one!" 
            toriel "But now, we should roll out this crust and put it in the tin."
            toriel "Would you please get the pie tin from under the oven for me?"
    call .get_tin
    if loop_count == 7:
        return

    $toriel_hangout_pun = False
    call .roll_crust
    if loop_count == 7:
        return
        
    show toriel smile  with Dissolve(.25)
    toriel "That crust looks great!"
    toriel "Now, would you mind chopping these vegetables while I prepare the snails?"
    menu:
        "Sure.":
            toriel "Thank you. After we mix all this up, I can bake the quiche." 
        "I'm allergic to vegetables. And knives.":
            $world.get_monster('Toriel').update_FP(-3)
            show toriel annoyed with Dissolve(.25)
            toriel "..."
            toriel "I highly doubt that."
            toriel "If you did not wish to help, you only needed to tell me so."
            menu:
                "It was just a joke, I'll help!":
                    if toriel_hangout_pun_hater == False:
                        show toriel awkward with Dissolve(.25)
                        toriel "..."
                        toriel "I did not realize, I am sorry."
                    else:
                        toriel "..."
                        toriel "Well... it wasn’t very funny." 
                "Sorry.":
                    toriel "..."
                    show toriel normal with Dissolve(.25)
                    toriel "...Apology accepted." 
                "Fine, I don't want to help.":
                    $world.get_monster('Toriel').update_FP(-3)
                    show toriel angry with Dissolve(.25)
                    toriel "What has gotten into you all of a sudden?"
                    toriel "If you do not intend to help, I will need you to leave the kitchen."
                    return
        "I don’t know if I’m {i}cut{/i} out for that kind of work, but I’ll try.":
            $world.get_monster('Toriel').update_FP(2)
            show toriel surprised  with Dissolve(.25)
            toriel "Oh! That is another joke!"
            show toriel laughing with Dissolve(.25)
            toriel "You are very good at these!"
    
    show toriel smile with Dissolve(.25)
    "*Toriel shells the snails while you chop the vegetables."
    toriel "That should be good." 
    toriel "Would you please bring me the vegetables? We must simply mix everything together, and then I can bake the quiche." 
    $toriel_hangout_pun = False
    call .get_veggies
    if loop_count == 7:
        return

    show toriel smile with Dissolve(.25)
    "*Toriel mixes the ingredients and pours them into the crust in the pan."
    toriel "Now to bake!"
    "*Toriel conjures a glowing flame in her hands and bakes the quiche in a few moments."
    menu:
        "*Scream in alarm":
            $world.get_monster('Toriel').update_FP(-1)
            show toriel surprised with Dissolve(.25)
            toriel "Oh no!" 
            toriel "I did not intend to surprise you like that."
            toriel "I am very sorry, I should have warned you."
            show toriel awkward with Dissolve(.25)
            toriel "..."
            toriel "Perhaps you should go get Frisk for dinner?"
            toriel "I shall finish preparing the meal." 
            return
        "Woah! That's so cool!":
            $world.get_monster('Toriel').update_FP(2)
            show toriel surprised with Dissolve(.25) 
            toriel "Oh, thank you."
            show toriel blushing with Dissolve(.25)
            toriel "It is just simple fire magic..."
            toriel "But I am glad you liked it!" 
        "Wow, your backing skills are on {i}fire{/i}!":
            $world.get_monster('Toriel').update_FP(3)
            show toriel blushing with Dissolve(.25) 
            toriel "Oh, thank you." 
            toriel "It is just simple fire magic, but I am glad you liked it."
            toriel "Down here, magic like that is very commonplace. Certainly not a..."
            show toriel laughing with Dissolve(.25)
            toriel "{i}Hot{/i} commodity!"
            
    if toriel_hangout_pun_count > 0:
        #I think you should get an extra friendship point for getting here...
        $world.get_monster('Toriel').update_FP(1)
        show toriel smile with Dissolve(.25) 
        toriel "I did enjoy baking with you."
        show toriel laughing with Dissolve(.25)
        toriel "And your jokes!" 
        show toriel smile with Dissolve(.25)
        toriel "We should cook together again sometime."
        toriel "For now, though, would you please go get Frisk for dinner?" 
    elif loop_count > 0:
        show toriel neutral with Dissolve(.25) 
        toriel "Well, now that the quiche is done, would you please get Frisk for dinner?"
    else:
        show toriel smallsmile with Dissolve(.25) 
    toriel "Thank you for your help."
    toriel "Now that dinner is ready, would you please go get Frisk so we can eat together?"
    
    $loop_count =0
    return
    
    
    
    
    
    
#This one is called twice. 
label .pie_ne:
    menu:
        "*Chuckle awkwardly":
            show toriel smile
            toriel "Well, anyway. Shall we begin?" 
        "*Laugh":
            $world.get_monster ('Toriel').FP +=2
            show toriel blushing
            toriel "Oh, I am glad you liked my little joke." 
            toriel "I have many more, if you would like to hear them!"
            show toriel smile 
            toriel "Though, for now, we should probably begin baking if we want to have it ready for dinner!"
        "Uh...":
            $world.get_monster('Toriel').update_FP(-2)
            show toriel awkward
            toriel "..."
            toriel "Shall we begin, then?"
        "That's... not very funny.":
            $world.get_monster('Toriel').update_FP(-3)
            $toriel_hangout_pun_hater = True
            show toriel awkward
            toriel "..."
            toriel "I am sorry. Shall we begin baking, then?"
    return
    
#Loops!
label .get_butter:
    menu:
        "*Get the butter":
            "*Toriel mixes the butter in a bowl with some flour."
            toriel "You know, there is very little that I like..."
            show toriel laughing
            toriel "...{i}butter{/i} than baking!"
        "*Do not.":
            $loop_count +=1
            if loop_count == 1:
                show toriel annoyed
                toriel "..."
                toriel "...What are you doing?"
                jump .get_butter
            elif loop_count <7:
                show toriel annoyed
                toriel "..."
                jump .get_butter
            else:
                show toriel annoyed 
                toriel "..."
                toriel "If you will not be helpful, I must ask you to please leave the kitchen."
    return
    
label .get_tin:
    menu:
        "*get the pie tin":
            toriel "Thank you."
            "*Toriel takes the pie tin and hands you a rolling pin."
            toriel "Now, I will prepare the filling while you roll the dough. Make sure it is even! We wouldn’t want the ingredients to..."
            show toriel laughing
            toriel "...{i}roll{/i} out."
        "*do not":
            $world.get_monster('Toriel').FP-=1
            $loop_count +=1
            if loop_count ==1:
                show toriel annoyed
                toriel "..."
                toriel "...What are you doing?"
                jump .get_tin
            elif loop_count <7:
                show toriel annoyed
                toriel "..."
                jump .get_tin
            else:
                show toriel annoyed 
                toriel "..."
                toriel "If you will not be helpful, I must ask you to please leave the kitchen."
        "*Tell another pun instead" if toriel_hangout_pun == False:
            $world.get_monster('Toriel').update_FP(2)
            $toriel_hangout_pun = True
            $toriel_hangout_pun_count +=1
            if loop_count < 6:
                show toriel laughing
                toriel "As much as I enjoy your puns, I do need you get the pie tin."
                jump .get_tin
            else:
                show toriel annoyed 
                toriel "..."
                toriel "...Though I have been enjoying your jokes, there is work to be done." 
                toriel "If you will not be helpful, I must ask you to leave the kitchen."
                $loop_count =7
    return

label .roll_crust:
    menu:
        "*Roll out the pie crust":
            "*You begin to roll out the crust."
            toriel "I think this recipe will turn out..."
            show toriel laughing
            toriel "{i}Egg{/i}-cellent!"
            menu:
                "*laugh":
                    $world.get_monster('Toriel').update_FP(1)
                    show toriel smile
                "*Just keep rolling":
                    $world.get_monster('Toriel').update_FP(-1)
                    if toriel_hangout_pun_hater == False:
                        show toriel awkward
                        toriel "..."
                        toriel "I shall begin preparing the filling." 
                    else:
                        show toriel awkward
                        toriel "..." 
                        toriel "Perhaps it would be better for me to take care of dinner myself."
                        $loop_count = 7
                "I'm sure it {i}shell{/i}." if toriel_hangout_pun == False:
                    $world.get_monster('Toriel').update_FP(2)
                    $toriel_hangout_pun = True
                    $toriel_hangout_pun_count +=1
                    show toriel blushing
                    toriel "Oh!"
                    show toriel laughing
                    toriel "That is a good {i}yoke{/i}!"
        "*Do not":
            $world.get_monster('Toriel').update_FP(-1)
            $loop_count +=1
            if loop_count ==1:
                show toriel annoyed
                toriel "..."
                toriel "...What are you doing?"
                jump .roll_crust
            elif loop_count <7:
                show toriel annoyed
                toriel "..."
                jump .roll_crust
            else:
                show toriel annoyed 
                toriel "..."
                toriel "If you will not be helpful, I must ask you to please leave the kitchen."
        "*Tell another pun" if toriel_hangout_pun == False:
            $world.get_monster('Toriel').update_FP(2)
            $toriel_hangout_pun = True
            $toriel_hangout_pun_count +=1
            if loop_count < 6:
                "I think this quiche will be {i}egg{/i}-celent."
                show toriel laughing 
                toriel "Oh, my, that is a good {i}yoke{/i}!"
                jump .roll_crust
            else:
                show toriel annoyed 
                toriel "..."
                toriel "...Though I have been enjoying your jokes, there is work to be done." 
                toriel "If you will not be helpful, I must ask you to leave the kitchen."
                $loop_count = 7
    return

label .get_veggies:
    menu:
        "*Bring Toriel the vegetables":
            "*You begin to roll out the crust."
            show toriel smile 
            toriel "Thank you." 
        "*Do not":
            $world.get_monster('Toriel').update_FP(-1)
            $loop_count +=1
            if loop_count ==1:
                show toriel annoyed
                toriel "..."
                toriel "...What are you doing?"
                jump .get_veggies
            elif loop_count <7:
                show toriel annoyed
                toriel "..."
                jump .get_veggies
            else:
                show toriel annoyed 
                toriel "..."
                toriel "If you will not be helpful, I must ask you to please leave the kitchen."
        "Well, we've made it this far, things just {i}plant{/i} go wrong." if toriel_hangout_pun == False:
            $world.get_monster('Toriel').update_FP(2)
            $toriel_hangout_pun = True
            $toriel_hangout_pun_count +=1
            if loop_count < 6:
                show toriel laughing 
                toriel "Well, if something does, we will just have to look for the {i}root{/i} of the problem." 
                show toriel smile
                toriel "I do need those vegetables, however. Root and otherwise." 
                jump .get_veggies
            else:
                #show toriel annoyed 
                toriel "..."
                toriel "...Though I have been enjoying your jokes, there is work to be done." 
                toriel "If you will not be helpful, I must ask you to leave the kitchen."
                $loop_count = 7
    return

