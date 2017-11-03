init -9 python:

    class Frisk(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Frisk_manager_default",True,0,self)
            self.name = "Frisk"
            self.default_sprite = "frisk normal"
            self.default_room = "Frisk's Room"
            self.FP = 0
            self.consumables_given = 0
            self.cell_phone_pic = "UI/frisk.png"
            self.d_1 = {"Is Afternoon" : False}
            self.d_2 = {"Not Night": False,"Not Same Day": False}
            self.dating_requirements = {"Friendship 1" : self.d_1, "Friendship 2" : self.d_2}
            self.handle_schedule()

        def give_item(self,item = False):

            # give_Gift_name_itemclassname
            # builds the label and calls it with current count + 1
            label_name = "give_Gift_%s_%s" % (self.name,item.get_class_name())

            if renpy.has_label(label_name):

                if self.given_today_count >= 5:
                    if not item.equip:
                        renpy.call_in_new_context("Frisk_Consumable_Reject",self)
                    else:
                        renpy.call_in_new_context("Frisk_Equip_Reject",self)

                else:
                    
                    response = renpy.call_in_new_context(label_name,self.get_total_specific_item(item) + 1,self)
                    
                    if response:
                        self.given_items[item.get_class_name()] = self.get_total_specific_item(item) + 1
                        inventory.drop(item)
                        #dirty check, but its easier than hiding it somewhere
                        if self.given_today_count == 0:
                            self.consumables_given = 0

                        self.given_today_count += 1

                        if not item.equip:
                            self.consumables_given += 1

                        if self.consumables_given == 3:
                            renpy.call_in_new_context("Frisk_Consumable_Warning")
                        elif self.given_today_count == 4:
                            renpy.call_in_new_context("Frisk_Equip_Warning")

                        

            else:
                renpy.call_in_new_context("give_Gift_%s_Unknown" % self.name)
            return

        def handle_relationship_requirements(self):

            self.d_1 = {}
            self.d_2 = {}
            self.d_3 = {}

            self.dating_requirements = {}

            yellow = "#ffff00"
            red = "#f00"
            green = "#00ff00"

            if 'frisk_friendship_1_Complete' in player.variables:
                text = "Complete!"
                status = True
            elif world.get_current_timezone() == 'Afternoon':
                text = "Go to Frisk's Room!"
                status = False
            else:
                text = "Wait til Afternoon"
                status = False

            self.d_1[text] = status


            if 'frisk_friendship_2_Complete' in player.variables:
                self.d_2["Complete!"] = True
            elif world.get_current_timezone() != 'Night' and world.get_current_timezone() != 'Evening' and 'frisk_friendship_1_Complete' in player.variables:
                self.d_2["Go to the Kitchen \n    before Dinner"] = False
            else:
                self.d_2["Go to Kitchen\n    before Dinner"] = world.get_current_timezone() != 'Night' and world.get_current_timezone() != 'Evening' and player.current_room == "Kitchen"
                self.d_2['Friendship 1 Complete'] = 'frisk_friendship_1_Complete' in player.variables

            if 'Hunted_Snails_With_Frisk' in player.variables:
                self.d_3["Complete!"] = True
            elif 'frisk_f1_phase3' in player.variables:
                self.d_3["Go to Black Tree Room!"] = False
            elif 'frisk_f1_phase2' in player.variables:
                self.d_3["Go to Tunnel Divide!"] = False
            else:
                self.d_3["Ask Frisk to Hunt Snails"] = False

            if 'frisk_friendship_1_Complete' not in player.variables:
                self.dating_requirements["{color=%s}Arts and Crafts{/color}" % red] = self.d_1
            else:
                self.dating_requirements["{color=%s}Arts and Crafts{/color}" % green] = self.d_1

            if 'frisk_friendship_2_Complete' not in player.variables:
                self.dating_requirements["{color=%s}Having a Knife Time?{/color}" % red] = self.d_2
            else:
                self.dating_requirements["{color=%s}Having a Knife Time?{/color}" % green] = self.d_2

            if 'Hunted_Snails_With_Frisk' not in player.variables:
                self.dating_requirements["{color=%s}Is Everything Okay?{/color}" % red] = self.d_3
            else:
                self.dating_requirements["{color=%s}Is Everything Okay?{/color}" % green] = self.d_3

            return

        def handle_special_events(self):
                
            if 'Hunted_Snails_With_Frisk' not in player.variables and 'frisk_f1_phase2' in player.variables and 'frisk_f1_phase3' not in player.variables:
                get_frisk().move_to_room("Tunnel Divide")
                get_frisk().set_special_event('frisk_friendship_event_1_tunnels')
            elif 'Hunted_Snails_With_Frisk' not in player.variables and 'frisk_f1_phase2' in player.variables and 'frisk_f1_phase3' in player.variables:
                get_frisk().move_to_room("Black Tree Room")
                get_frisk().set_special_event('frisk_friendship_event_1_blacktree')
            #painting
            elif world.get_current_timezone() == 'Afternoon' and 'Hunted_Snails_With_Frisk' in player.variables and 'frisk_friendship_1_Complete' not in player.variables:
                get_frisk().move_to_room("Frisk's Room")
                self.set_special_event('frisk_friendship_hangout1_main')

            #knife in kitchen
            elif world.get_current_timezone() == 'Morning' or world.get_current_timezone() == 'Day' or world.get_current_timezone() == 'Afternoon':
                if 'frisk_friendship_1_Complete' in player.variables and 'frisk_friendship_2_Complete' not in player.variables:
                    if 'frisk_friend_hangout2_day' not in player.variables or ('frisk_friend_hangout2_day' in player.variables and player.variables['frisk_friend_hangout2_day'] != world.day):
                        self.set_special_event('frisk_friendship_hangout2')
                        get_frisk().move_to_room("Kitchen")
            else:
                self.remove_event()

            return
        def handle_schedule(self):
            #night
            self.update_schedule("Sunday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Monday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Tuesday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Wednesday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Thursday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Friday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Saturday","Night","Frisk's Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Overlook",self.default_event)
            self.update_schedule("Monday","Morning","Grass Room",self.default_event)
            self.update_schedule("Tuesday","Morning","Grass Room",self.default_event)
            self.update_schedule("Wednesday","Morning","Frisk's Room",self.default_event)
            self.update_schedule("Thursday","Morning","Dummy Room",self.default_event)
            self.update_schedule("Friday","Morning","Frisk's Room",self.default_event)
            self.update_schedule("Saturday","Morning","Dummy Room",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Day","Snail Hunting Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Monday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Frisk's Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Frisk's Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Frisk's Room",self.default_event)
            #evening
            self.update_schedule("Sunday","Evening","Living Room",self.default_event)
            #self.update_schedule("Monday","Evening","Living Room",self.default_event)
            self.update_schedule("Tuesday","Evening","Frisk's Room",self.default_event)
            #self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Evening","Frisk's Room",self.default_event)
            #self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Evening","Frisk's Room",self.default_event)

            


label initialize_frisk:
    #here is where the sprites go

    image frisk angry  = "characters/Frisk/Frisk_Angry.png"
    image frisk annoyed = "characters/Frisk/Frisk_Annoyed.png"
    image frisk bigsmile = "characters/Frisk/Frisk_Big_Smile.png"
    image frisk blushing = "characters/Frisk/Frisk_Blush.png"
    image frisk coveredface = "characters/Frisk/Frisk_CoveredFace.png"
    image frisk coveredfacewitheyes = "characters/Frisk/Frisk_CoveredFaceandeyered.png"
    image frisk disappointed = "characters/Frisk/Frisk_Disappointed.png"
    image frisk disgusted = "characters/Frisk/Frisk_Disgusted.png"
    image frisk distant = "characters/Frisk/Frisk_Distant.png"
    image frisk giggly = "characters/Frisk/Frisk_Giggly.png"
    image frisk hurtsurprised = "characters/Frisk/Frisk_Hurtful_Surprised.png"
    image frisk normal = "characters/Frisk/Frisk_Normal.png"
    image frisk panickinghands = "characters/Frisk/Frisk_Panic_Hands.png"
    image frisk panicking = "characters/Frisk/Frisk_Panicking.png"
    image frisk sad = "characters/Frisk/Frisk_Sad.png"
    image frisk somehappy = "characters/Frisk/Frisk_Somewhat_Happy.png"
    image frisk smallsmile = "characters/Frisk/Frisk_Tiny_Smile.png"
    image frisk soulless = "characters/Frisk/Frisk_Soulless.png"
    image frisk surprised = "characters/Frisk/Frisk_Surprised.png"
    image frisk tearyeyes = "characters/Frisk/Frisk_Teary_Eyes.png" 
    image frisk upset = "characters/Frisk/Frisk_Upset.png"

    
    define frisk = ('Frisk')
    define friskChar = Character('Frisk', color="#FFFFFF")
    python:
        def frisk(text, *args, **kwargs):
               friskChar(text, *args, **kwargs)
    return

######    Frisk's default scene     ######

label Frisk_manager_default(owner = False,pause = True):


    call show_buttons from _call_show_buttons_6
    if renpy.music.get_playing() != "audio/ruins/frisk.mp3":
        play music "audio/ruins/frisk.mp3" fadein 5
    
    show frisk normal:
        xalign 0.5
        yalign 1.0
        
    python:
        renpy.pause()
        
        ## Chat options
        frisk_howare = False
        frisk_doingwell = False
        frisk_didtoday = False
        frisk_chataway = False

        ## Ask options
        frisk_forfun = False
        frisk_livetoriel = False
        frisk_blookyopinion = False
        frisk_howfell = False
        frisk_askaway = False

        ## Flirt options
        frisk_iscute = False
        frisk_fellfor = False
        frisk_smilelit = False
        frisk_flirtaway = False

    
    label Frisk_interact:
        call Frisk_dialogue  
    return

######     Frisk's dialogue options     ######

label Frisk_dialogue:
    show frisk normal with Dissolve(.25)
    
    if 'Hunted_Snails_With_Frisk' in player.variables and 'Hunted_Snails_With_Frisk_Response' not in player.variables:
        frisk "Hey, about last time we talked..."
        frisk "Sorry I was acting so weird!"
        frisk "It’s just a really complicated situation, and I’d rather not think about it."
        frisk "So, let’s just pretend that never happened!"
        frisk "Anyway, did you need something?"
        $ player.variables['Hunted_Snails_With_Frisk_Response'] = True


    menu:
        "Do you want to go snail hunting with me?" if 'Hunted_Snails_With_Frisk' not in player.variables and world.day > 0:
            call frisk_friendship_event_1
        "Chat" if frisk_chataway is False:
            jump Frisk_chat
            $ world.add_to_ac(2)
        "Ask" if frisk_askaway is False:
            jump Frisk_ask
            $ world.add_to_ac(2)
        "Flirt" if frisk_flirtaway is False:
            jump Frisk_flirt
            $ world.add_to_ac(2)

        "Give Gift" if len(inventory.items) > 0:
            show frisk smallsmile
            frisk "Oh, do you have something?"
            
            "What should you give them?"
            
            $ result = renpy.call_screen("gift_item_menu",owner)
            
            if result == 'cancel':
                frisk "No? That’s alright."
            else:
                $ world.add_to_ac(5)


        "Never mind.":
            "You decide not to say anything after all."

    return


label Frisk_chat:
    show frisk normal with Dissolve(.25)
    
    if frisk_howare and frisk_doingwell and frisk_didtoday:
        $frisk_chataway = True 
        "You tried to say something, but couldn't think of anything to say."
        jump Frisk_dialogue
        
    menu:
        "How are you?" if frisk_howare is False:
            $ frisk_howare = True
            
            frisk "I’m good! How about you?"
            
            menu:
                "I’m good, too.":
                    show frisk smallsmile with Dissolve(.25)
                    frisk "Well, that’s good."
                "Never better!":
                    show frisk bigsmile with Dissolve(.25)
                    frisk "Great!"
                "Eh.":
                    show frisk somehappy with Dissolve(.25)
                    frisk "Oh... Well, maybe tomorrow will be better for you."
                    show frisk smallsmile with Dissolve(.25)
                    frisk "You gotta keep your chin up!"
                    
            jump Frisk_chat
                    
        "Is everything going well for you?" if frisk_doingwell is False:
            $ frisk_doingwell = True
            show frisk somehappy with Dissolve(.25)
            
            frisk "Oh, yeah..."
            
            show frisk bigsmile with Dissolve(.25)
            
            frisk "No complaints here!"
            
            jump Frisk_chat
            
        "What have you done today?" if frisk_didtoday is False:
            $ frisk_didtoday = True
            
            frisk "Same old, same old... Took a walk, did some drawing, said ‘hi’ to some Froggits..."
            frisk "There’s not much else to do around here, but you probably know that by now."
            
            jump Frisk_chat
            
        "Never mind.":
            "You decide not to say anything after all."
            jump Frisk_interact
            
    label Frisk_ask:
        show frisk normal with Dissolve(.25)
        
        if frisk_forfun and frisk_livetoriel and frisk_blookyopinion and frisk_howfell:
            $frisk_askaway = True 
            show frisk distant with Dissolve(.25)
            "Frisk looks a little uncomfortable."
            "Maybe it's better if you don't say anything..."
            jump Frisk_dialogue
        
        menu:
            "What do you like to do for fun?" if frisk_forfun is False:
                $ frisk_forfun = True
                show frisk smallsmile with Dissolve(.25)
                
                frisk "I love to paint things that I see down here!"
                
                menu:
                    "You paint? Me too!":
                        # $ get_frisk().update_FP(3)
                        
                        if "frisk_friendship_1_Complete" in player.variables:
                            show frisk giggly with Dissolve(.25)
                            frisk "I already knew that, silly!"
                            frisk "And you already knew that I liked to paint, so why’d you ask?"
                            
                            menu:
                                "I was just wondering if you had any other hobbies.":
                                    # $ get_frisk().update_FP(3)
                                    show frisk smallsmile with Dissolve(.25)
                                    
                                    frisk "Well, not really. Maybe I should get some."
                                    
                                "No reason.":
                                    
                                    frisk "Alright, then!"
                                        
                        else:
                            show frisk bigsmile with Dissolve(.25)
                            frisk "That’s great! We should paint together sometime!"
                            
                        jump Frisk_ask
                        
                    "You should show me your paintings sometime.":
                        show frisk smallsmile with Dissolve(.25)
                        
                        frisk "Yeah?"
                        
                        if "frisk_friendship_1_Complete" in player.variables:
                            frisk "Well, I already showed you one..."
                            
                        frisk "Maybe some other time."
                        
                        jump Frisk_ask
                        
                    "Painting? That’s boring.":
                        # $ get_frisk().update_FP(-3)
                        
                        show frisk disappointed with Dissolve(.25)
                        
                        frisk "It’s really not, if you give it a chance..."
                        
                        jump Frisk_ask
                        
            "What’s living with Toriel like?" if frisk_livetoriel is False:
                $ frisk_livetoriel = True
                show frisk bigsmile with Dissolve(.25)
                
                frisk "She’s the best mom! I couldn’t have asked for anyone better to have taken me in..."
                
                show frisk normal with Dissolve(.25)
                
                frisk "When I fell down here, I was pretty... lost. But Mom found me, and everything’s been great ever since."
                
                show frisk somehappy with Dissolve(.25)
                
                frisk "Well, if not great, then at least okay. And ‘okay’ is just fine by me."
                
                jump Frisk_ask
                
            "What do you think of Napstablook?" if frisk_blookyopinion is False:
                $ frisk_blookyopinion = True
                show frisk smallsmile with Dissolve(.25)
                
                frisk "They’re nice! They can be pretty shy... Well, make that very shy. But they’re fun to hang out with, in their own way."
                
                jump Frisk_ask
                
            "How did you fall?" if frisk_howfell is False:
                $ frisk_howfell = True
                show frisk distant with Dissolve(.25)
                
                frisk "...I don’t remember."
                
                menu:
                    "Did I upset you? I’m sorry. I won’t ask again.":
                        # $ get_frisk().update_FP(3)
                        
                        show frisk somehappy with Dissolve(.25)
                        
                        frisk "It’s okay. You were only curious."
                        
                        jump Frisk_ask
                        
                    "Do you miss the surface?":
                        show frisk disappointed with Dissolve(.25)
                        
                        frisk "I can’t really say, since I don’t remember much of my surface life, either. Do I wanna go back, though?"
                        frisk "Hard to answer. On one hand, I really want to go back to the surface with all of the monsters. They haven’t seen the sun in so long... Some monsters have never seen it at all. I know they’d all be much happier on the surface."
                        
                        show frisk sad with Dissolve(.25)
                        
                        frisk "...On the other hand, I know how humans can be. I’m not sure if I really want to go back in that case, with or without the monsters."
                        
                        jump Frisk_ask
                        
                    "I’m sure you remember; you’ve gotta think harder.":
                        # $ get_frisk().update_FP(3)
                        
                        show frisk annoyed with Dissolve(.25)
                        
                        frisk "I already told you, I can’t remember."
                        
                        jump Frisk_ask
                        
            "Never mind.":
                jump Frisk_dialogue
                
    label Frisk_flirt:
        show frisk normal with Dissolve(.25)
        
        if frisk_iscute and frisk_fellfor and frisk_smilelit:
            $ frisk_flirtaway = True
            "It seems that your flirting is not having the effect you were looking for."
            jump Frisk_dialogue
            
        menu:
            "Aside from being cute, what do you do for a living?" if frisk_iscute is False:
                $ frisk_iscute = True
                show frisk surprised with Dissolve(.25)
                    
                frisk "Oh! Haha, thanks!"
                
                show frisk smallsmile with Dissolve(.25)
                
                frisk "I mostly just hunt snails, if you’re actually wondering."
                
                jump Frisk_flirt
                
            "Do you have a band-aid? Because I scraped my knees falling for you." if frisk_fellfor is False:
                $ frisk_fellfor = True
                show frisk giggly with Dissolve(.25)
                
                frisk "Must’ve been a long fall, if you ended up all the way down here!"
                
                jump Frisk_flirt
                
            "Your smile lit up the room, so I just had to come over." if frisk_smilelit is False:
                $ frisk_smilelit = True
                show frisk giggly with Dissolve(.25)
                
                frisk "That’s a good one! Gotta remember that for some other time."
                
                jump Frisk_flirt
                
            "Never mind.":
                jump Frisk_dialogue
