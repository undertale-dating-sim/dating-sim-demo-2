init -9 python:

    class Toriel(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Toriel_manager_default",True,self)
            self.default_room = "Toriel's Room"
            self.name = "Toriel"
            self.FP = 40
            self.seed_default_schedule()
            self.default_sprite = "toriel normal"

        def give_item(self,item = False):

            # give_Gift_name_itemclassname
            # builds the label and calls it with current count + 1
            label_name = "give_Gift_%s_%s" % (self.name,item.get_class_name())

            if renpy.has_label(label_name):

                if self.given_today_count >= 5:
                    renpy.call_in_new_context("give_Gift_%s_Rejection" % self.name,self)
                else:
                    response = renpy.call_in_new_context(label_name,self.get_total_specific_item(item) + 1,self)
                    self.given_items[item.get_class_name()] = self.get_total_specific_item(item) + 1
                    if response:
                        self.given_today_count += 1
                        renpy.call_in_new_context("%s_Gift_Count_Reaction" % self.name,self)

            else:
                renpy.call_in_new_context("give_Gift_%s_Unknown" % self.name)
            return
            
        def seed_default_schedule(self):
            self.reset_schedule() 
            #night
            self.update_schedule("Sunday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Monday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Tuesday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Wednesday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Friday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Night","Toriel's Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Kitchen",self.default_event)
            #self.update_schedule("Monday","Morning","Kitchen",self.default_event)
            self.update_schedule("Monday","Morning","Basement Door",self.default_event)
            self.update_schedule("Tuesday","Morning","Kitchen",self.default_event)
            self.update_schedule("Wednesday","Morning","Kitchen",self.default_event)
            self.update_schedule("Thursday","Morning","Kitchen",self.default_event)
            self.update_schedule("Friday","Morning","Kitchen",self.default_event)
            self.update_schedule("Saturday","Morning","Kitchen",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Cave Room",self.default_event)
            #self.update_schedule("Monday","Day","",self.default_event)
            self.update_schedule("Tuesday","Day","Cave Room",self.default_event)
            #self.update_schedule("Wednesday","Day","",self.default_event)
            self.update_schedule("Thursday","Day","Cave Room",self.default_event)
            #self.update_schedule("Friday","Day","",self.default_event)
            self.update_schedule("Saturday","Day","Cave Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Spider Bakery",self.default_event)
            self.update_schedule("Monday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Sassy Rock Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Sassy Rock Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Sassy Rock Room",self.default_event)
            #evening
            self.update_schedule("Sunday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Monday","Evening","Living Room",self.default_event)
            self.update_schedule("Tuesday","Evening","Living Room",self.default_event)
            self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Evening","Living Room",self.default_event)
            self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Evening","Living Room",self.default_event)
            


label initialize_toriel:
        
    image toriel placeholder = "characters/Toriel/toriel_ph.png"
    image toriel angry = "characters/Toriel/Toriel_Angry.png"
    image toriel annoyed = "characters/Toriel/Toriel_Annoyed.png"
    image toriel awkward = "characters/Toriel/Toriel_Awkward.png"
    image toriel blushing = "characters/Toriel/Toriel_Blushing.png"
    image toriel laughing = "characters/Toriel/Toriel_Laughing.png"
    image toriel normal = "characters/Toriel/Toriel_Neutral.png"
    image toriel reallysad = "characters/Toriel/Toriel_ReallySad.png"
    image toriel sad = "characters/Toriel/Toriel_Sad.png"
    image toriel smallsmile = "characters/Toriel/Toriel_Small_Smile.png"
    image toriel smile = "characters/Toriel/Toriel_Smile.png"
    image toriel surprised = "characters/Toriel/Toriel_Surprised.png"


    define toriel = ('Toriel')
    define torielChar = Character('Toriel', color="#FFFFFF")
    python:
        def toriel(text, *args, **kwargs):
               torielChar(text, *args, **kwargs)
    return

#this is Toriels default scene
label Toriel_manager_default(owner = False,pause = True):
    
    call show_buttons from _call_show_buttons

    if owner.FP < 20:
        show toriel reallysad
    elif owner.FP < 40:
        show toriel awkward
    elif owner.FP < 60:
        show toriel normal
    elif owner.FP < 80:
        show toriel laughing
    else:
        show toriel blushing

    if pause:
        $renpy.pause()
    

    "Hello, dear. Can I help you?"
    
    menu:
        
        "Hello, dear. Can I help you?"
        '"I brought you some snails!"' if player.current_snails > 0:
            call Toriel_Manager_Give_Snails
        "Chat":
            call Toriel_Manager_Chat
        "Ask":
            call Toriel_Manager_Ask
        "Flirt":
            call Toriel_Manager_Flirt
        "Gift" if len(inventory.items) > 0:
            show screen gift_item_menu(owner)
            "What should you give them?"
        "Leave":
            toriel "Take care, dear."

    
    return



label Toriel_Manager_Chat(owner=False):
    #These were implemented over in the Toriel.rpy file under Script\Events\The Ruins\Toriel
    menu:
        "How are you doing?":
            show toriel smile
            toriel "I am doing well! Thank you for asking. How are you doing, dear?"
        "What’s crackin’?":
            show toriel awkward
            toriel "... I don’t believe anything is cracking... Did you hear something breaking? Oh dear, is it that rock again?"
        "'Sup?":
            jump toriel_gd_sup
        "What have you been doing lately?":
            show toriel smallsmile
            toriel "Not much, just the usual. Watching over Frisk, baking, the occasional snail hunting. Although I have also been having a wonderful time with you."
    return

label toriel_gd_sup:
    toriel "... ‘Sup’? Is... Is that a surface word? I am sorry, but I am not familiar with it."
    menu:       #Once you've explained it, should she give a different dialogue?
        "Oh! Sorry. It stands for ‘What is up’, which is a commonly used greeting on the surface.":
            show toriel smile
            toriel "Ah, I see! Thank you for explaining so well."
            show toriel smallsmile
            toriel "Well, I suppose I shall also ask you, ‘sup’?"
        "It means ‘what’s up’.":
            show toriel awkward
            toriel "Oh... Ah... The ceiling, I suppose... Although I think I might see a spider up there."
        "You seriously don’t know what ‘sup’ means?!":
            show toriel awkward
            toriel "Oh... Should I know? I am... I am sorry dear, but I do not..."
    return

label Toriel_Manager_Give_Snails:
    toriel "Thank you so much dear."
    "* Toriel takes the [player.current_snails] snails from your inventory."
    show toriel smile
    # if dailySnails > 0:
    #     toriel "Oh!"
    #     toriel "I see you brought [dailySnails] [snailType]"
    toriel "Here, please take this as a thank you."
    "* Toriel hands you [player.current_snails] gold."
    $ player.gold += player.current_snails
    $ player.current_snails = 0
    return

label Toriel_Manager_Flirt:
    menu:
        "Do you have a compass? Because I keep getting lost in your eyes.":
            show toriel surprised
            toriel "Oh!"
            show toriel laughing
            toriel "Ahahahaha!"
            show toriel blushing
            toriel "My, you caught me off guard with that! I honestly do not know what to say... Perhaps... I could {i}map{/i} out a way for you?"
            #laugh
            toriel "Hehehehe!"
        "I love the way your fur looks in the ruins light.":
            #blush
            toriel "Oh! Ah... Thank you! Thank you very much, dear. That was very... Very kind of you to say! ...You are looking nice yourself! Hehehe!"
        "Butterscotch Pie has got nothing on you in sweetness":
            #blush
            toriel "Oh my... I am... I am at quite a loss for words... Th-thank you dear. That was very... Well... Sweet of you!"
        "Are you using fire magic right now? Because you’re warming my heart.":
            #blush
            toriel "Oh dear... You’re making me so flustered... Thank... Thank you dear! I am... So glad I could make you feel happy!"
    return
    

label Toriel_Manager_Ask:
    #Friendship level neutral options:
    menu:
        "What do you do for fun?":
            show toriel smile
            toriel "Usually, I like to read, bake, and hunt for bugs. I know it does not sound like much, but it’s just perfect for me."

        "Do you have a job?":
            show toriel smallsmile
            toriel "Not at the moment... Unless you count taking care of Frisk."
            show toriel surprised
            toriel "Not in a bad way, I hope you understand!"
            show toriel smallsmile
            toriel "Frisk is wonderful, but they are still a teenager. Hehehe!"

        "How long have you lived in the Ruins?":
            jump toriel_gd_askLivedRuins

        "What's your favorite thing to bake?":
            #smile
            toriel "Well, I do very much enjoy making Butterscotch Pie. However, if I manage to find enough snails, Snail Pie is something I love to make as well." 
            toriel "Frisk seems to like Butterscotch more than Snail, however. So I try not to make Snail Pie too often."
            toriel "I have also been known to make the occasional cake."

        #For some reason, these 2 options were seperated in the writing?
        "How’s Frisk treating you?":
            toriel "Ah, Frisk's arrival has been a true blessing. They are a very conscientious child."
            toriel "They help me with cooking, do chores without complaining, and they are kind to the other residents of the ruins."
            toriel "Really, I have nothing to complain about. They are the most wonderful child I could ever ask for."

        "What do you think of Napstablook?":
            #neutral
            toriel "I think that they are... Well, I can not have a real opinion of them because they never talk to me."
            toriel "They are particularly shy, so I try not to bother them. But I hope one day I can join them in a real conversation. Maybe even invite them over!"

    return
    
label toriel_gd_askLivedRuins:
    #awkward
    toriel "... A while."
    menu:
        "Oh, okay.":
            #awkward
            toriel "..."
            #neutral
            toriel "I do hope you’re enjoying your stay here!"
        "What’s wrong?":
            #awkward
            toriel "... It is nothing, dear. But thank you for your concern."
        "How long is ‘a while’?":
            #awkward
            toriel "... I do not remember. It is not important, anyway."
    return


#i need to look at my code to see how to do this exactly
label toriel_gd_give:
    toriel "Oh! Have you brought me something?"
    menu:
        "Give gift":
            #???
            jump torielItems
        "Cancel":
            toriel "That is alright, dear."
    return
