init:
    transform napstabob:
        xalign 0.5
        yalign 0.4
        linear 2.0 yalign 0.6
        linear 2.0 yalign 0.4
        repeat

init -9 python:

    class Napstablook(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Napstablook_manager_default",True,self)
            self.name = "Napstablook"
            self.default_sprite = "napstablook normal"
            self.FP = 20

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

        def handle_schedule(self):
            #night
            # self.update_schedule("Sunday","Night","Toriel"s Room",self.default_event)
            # self.update_schedule("Monday","Night","Toriel"s Room",self.default_event)
            # self.update_schedule("Tuesday","Night","Toriel"s Room",self.default_event)
            # self.update_schedule("Wednesday","Night","Toriel"s Room",self.default_event)
            # self.update_schedule("Thursday","Night","Toriel"s Room",self.default_event)
            # self.update_schedule("Friday","Night","Toriel"s Room",self.default_event)
            # self.update_schedule("Saturday","Night","Toriel"s Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Morning","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Morning","Snail Hunting Room",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Day","Snail Hunting Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Snail Hunting Room",self.default_event)
            #evening
            # self.update_schedule("Sunday","Evening","Toriel"s Room",self.default_event)
            # self.update_schedule("Monday","Evening","Living Room",self.default_event)
            # self.update_schedule("Tuesday","Evening","Living Room",self.default_event)
            # self.update_schedule("Wednesday","Evening","Toriel"s Room",self.default_event)
            # self.update_schedule("Thursday","Evening","Living Room",self.default_event)
            # self.update_schedule("Friday","Evening","Toriel"s Room",self.default_event)
            # self.update_schedule("Saturday","Evening","Living Room",self.default_event)

            


label initialize_napstablook:
    
    #Blooky Sprites
    image napstablook normal = "characters/Napstablook/Napstablook_Normal.png"
    image napstablook sad = "characters/Napstablook/Napstablook_Sad.png"
    image napstablook shyblush = "characters/Napstablook/Napstablook_ShyBlush.png"
    image napstablook smallsmile = "characters/Napstablook/Napstablook_Smallsmile.png"
    image napstablook smile = "characters/Napstablook/Napstablook_Smile.png"
    image napstablook surprised = "characters/Napstablook/Napstablook_Surprised.png"


    #Blooky Text Font and Scripted Name
    define napstablook = ("Napstablook")
    define napstablookChar = Character("Napstablook", color="#FFFFFF")
    python:
        def napstablook(text, *args, **kwargs):
               napstablookChar(text, *args, **kwargs)
    return

label Napstablook_manager_default(owner = False, pause = True):

    #Show the GUI while you talk to him
    call show_buttons from _call_show_buttons_7

    #Bobbing Animation
    show napstablook normal at napstabob with Dissolve(.25):

    #allows the game to wait so you have to click for the options to pop up
    if pause:
        $ renpy.pause()
    
    #Default Menu
    menu:
        "Napstablook"
        "Flirt" if owner.flirt_count < 3 :
            if owner.flirt_count == 0:
                "You're a very lovely shade of pale today."
                napstablook "oh...... thanks, i guess? i didn't realize i could be different shades of anything........."
            elif owner.flirt_count == 1:
                "Did it hurt when you fell from heaven?"
                napstablook "well...... uh... i don't remember falling from anywhere, actually......... sorry........."
            elif owner.flirt_count == 2:
                "Do you have a bandaid? I scraped my knee falling for you."
                napstablook "sorry, i didn't mean to hurt you...... that was an accident...... and i'm sorry i don't carry around bandaids either"
            elif owner.flirt_count == 3:
                "You look like trash, may I take you out?"
                napstablook "i already know i'm trash. you don't have to do anything about that........."
            elif owner.flirt_count == 4:
                "Are you a magician? Because whenever I look at you everyone else disappears."
                napstablook "um...... i have no idea why that would happen? i think you should see a doctor"
            elif owner.flirt_count == 5:
                "Sorry, I can't hold on… I've already fallen for you."
                napstablook "huh? hold on to what? oh, and, uh… sorry for hurting you, i guess?"
            
            $owner.flirt_count +=1
        "Chat":
            menu:
                "\"What's shakin' bacon?\"":
                    napstablook "um... oh...... nothing's shaking..... and i don't have any bacon.... awkward......."
                "\"How're you doing?\"":
                    napstablook "i'm fine..........."
                "\"You look a little down. Are you okay?\"":
                    napstablook "oh, i guess.... this is just how i always look. but thanks for asking...... that's nice of you to notice....."
                "Go back":
                    pass
        "Ask":
            menu:
                "\"What do you do for fun?\"":
                    napstablook "i like to listen to music, and.... sometimes.... i make my own, too"
                    menu:
                        "\"What kind of music do you make?\"":
                            "oh...... all kinds...... i'm not a very good singer, though, so nothing with vocals........"
                            #wait, doesn"t he say in Undertale that one of the songs makes him want to sing along?
                        "\"I like music, too!\"":
                            napstablook "that's nice...... i'm glad.... we have the same interests......."
                        "\"Oh, I don't really listen to much music.\"":
                            napstablook "oh...... oh no........ maybe you'd like it if you gave it another chance............"
                "\"Do you have a job?\"":
                    napstablook "um... yeah....... i'm a snail farmer...... it's pretty quiet, now that i'm the only one working there........"
                    menu:
                        "\"Snail farmer? What does that entail?\"":
                            napstablook "um...... i just...... sell snails... on my farm........ it's all in the title......."
                        "\"What happened to your coworkers?\"":
                            napstablook "oh, nothing, they just....... all wanted to become corporeal........ but i stayed behind......."
                            napstablook "someone needs to stay and look after the snails..."
                "\"Do you have any pets?\"":
                    napstablook "oh... well... i have snails. do those count?"
                    menu:
                        "\"Yes, of course they do.\"":
                            $world.get_monster("Napstablook").update_FP(2)
                            show napstablook smallsmile with Dissolve(.25)
                            napstablook "oh, that's good..."
                        "\"Why would you have snails?\"":
                            napstablook "well... i sell them. people usually want them for food..."
                        "\"Snails aren't pets. They're gross.\"":
                            $world.get_monster("Napstablook").update_FP(-2)
                            show napstablook sad with Dissolve(.25)
                            napstablook "oh..............."
                "\"Have you ever met Toriel?\"":
                    napstablook "oh, uh, yeah. i've met toriel. but she's kind of intimidating..."
                    menu:
                        "\"What about Frisk? Do you know them?\"": #[only if you met frisk]
                            napstablook "yeah, i know them too. they're very nice, and they don't intimidate me like toriel does"
                        "\"Why is she intimidating?\"":
                            napstablook "she's just, like...... really tall. and sometimes, when she smiles, i feel like she secretly wants to kill me.........."
                        "\"She's not that bad.\"":
                            napstablook "uh... okay. i guess i'll take your word for it"
                        "\"Yeah I'm pretty sure she secretly eats children.\"":
                            napstablook "um, okay? i don't know why you would think that, but sure"
        "Give Gift" if len(inventory.items) > 0:
            napstablook "oh, a gift?"
            "What should you give them?"
            $ result = renpy.call_screen("gift_item_menu",owner)
            if result == 'cancel':
                napstablook "oh...... thanks anyway."
            show napstablook normal at napstabob with dissolve
            
        "Testing":
            menu:
                "Raise FP 10":
                    $ owner.FP += 10
                "Lower FP 10":
                    $ owner.FP -= 10
                "Raise DP 10":
                    $ owner.DP += 10
                "Lower DP 10":
                    $ owner.DP -= 10
                "Raise HB 10":
                    $ owner.HB += 10
                "Lower HB 10":
                    $ owner.HB -= 10
            return
        "Events":
            $ issinger = False
            $ isdancer = False
            $ likedmusic = False
            $ dislikedmusic = False
            $ listened_music = False
            $ hobbies_asked = False
            $ napstablook_friendship_hangout1_complete = False
            $ apathy = False
            
            menu:
                "Like Karaoke, but Without the Lyrics on the Screen": # If all rooms explored, in blooky room.
                    call napstablook_event_1
                "Snail Hunting is an Art" if (owner.FP >= 10): # Good end to friendship event 1, caught snails 3+ times, in snail room.
                    call napstablook_hangout_1
                "One Man's Trash...":
                    call napstablook_hangout_3
                "Blooky's HB Date":
                    if (owner.HB > 12):
                        call napstablook_hb_date
                    else:
                        napstablook "oh... that's a nice idea..."
                        napstablook "but... i don't know... i don't think i can today..."
                        napstablook "...sorry..."
                "Blooky's TL Date":
                    call napstablook_tl_date
                "Exit":
                    return
            show napstablook normal
            scene background ruins_hallway
        "Exit":
            "okay."

    #return to the world manager event
    return
