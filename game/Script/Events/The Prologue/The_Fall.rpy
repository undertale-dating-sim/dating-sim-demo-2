label the_beginning:
    $ player.current_health = 1
    $ player.gold = 0
    $ player.current_snails = 0

    #play thud
    call hide_buttons
    stop music
    #play sound "audio/sfx/Hitting_the_ground.wav"
    scene

    with vpunch
    "* Thud"

    $ renpy.show(world.get_room("Cave Room").bg)
    with fade

    "* Ow."
    #this looks dirty, but I need to make the variables unique to this screen
    $ tf_loop = True
    $ player.variables['tf_scream_count'] = 1
    $ tf_look_around_count = 1
    $ tf_lie_down_count = 1
    $ tf_show_exit = 0
    $ tf_scream_enabled = True
    $ scream_button_text = "Scream for help"

    while tf_loop:
        menu:
            "[scream_button_text]" if tf_scream_enabled:
                call tf_scream
            "Lie down and hope for the best":
                call tf_lie_down
            "Look around" if not tf_show_exit:
                call tf_look_around


label tf_scream:

    if player.variables['tf_scream_count'] == 1:
        "* You scream."
        "* ..."
        "* But nobody came."
        $ scream_button_text = "Scream again"
    elif player.variables['tf_scream_count'] == 2:
        "* You scream with all your might."
        "* Your ears start ringing."
        "* ..."
        "* But nobody came."
        $ scream_button_text = "Scream as loud as you can"
    elif player.variables['tf_scream_count'] == 3:
        "* You scream until your throat hurts."
        "* ..."
        "* Great, now you are deaf {i}and{/i} mute."
        "* ...But still, nobody came."
        $ scream_button_text = "Scream..."
    else:
        "* You try to scream but all that comes out is a croak."
        "* ..."
        "* It may be better to keep your voice down for a while."
        $ tf_scream_enabled = False
    $ player.variables['tf_scream_count'] += 1
    return

label tf_lie_down:

    if tf_lie_down_count == 1:
        "* You lie down on the flower patch."
        "* It's sticky but otherwise quite soft."
        "* ..."
        "* ..."
        "* What now?"
    elif tf_lie_down_count == 2:
        "* This doesn't seem to be solving much."
    elif tf_lie_down_count == 3:
        "* Maybe you should get up and try to do something."
        "* ...Something besides lying down and giving up."
    elif tf_lie_down_count == 4 or tf_lie_down_count == 5:
        "* ..."
    elif tf_lie_down_count == 6:
        "* You're not going to take a nap, are you?"
    else:
        "* ..."
    $ tf_lie_down_count += 1

    return

label tf_look_around:
    

    if tf_look_around_count == 1:
        "* You see dark shadows moving along the cave walls."
        "* Your eyes must not have gotten used to the darkness yet."
        "* ...The concussion you probably have can't be helping any, either."

    elif tf_look_around_count == 2:
        "* You move your hand over the walls. They're surprisingly clean and dust free."
        "* Your nail gets stuck in a crevice. When you try to pull it out, it breaks."
        "* Ow!"
    elif tf_look_around_count == 3:
        "* One side of the cave looks slightly brighter than the others..."
        "* Is there a door here?"
        call unlock_movement_engine
    else:
        "* Nothing else to see here."
    $ tf_look_around_count += 1
    return

#NOTE : There are quite a few TL and HB descriptions I'm going to comment out until those routes are implemented.
label tf_item_room:
    #Adding flowey introduction to the cave room
    $ get_room("Cave Room").add_event('flowey_introduction',False)
    #lock the ruins entrance so they can't get out
    $ set_lock_room("Ruins Entrance",True)
    "* Mounds of trash litter the edges of the small cave. The sparse light which floods through a crack in the ceiling reveals a small mound of grass in the center of the cavern."
    "* There is one exit... but it seems to be covered by a curtain of vines." 
    "* A few pieces of trash sparkle in the scattered sunshine, catching your eye."

label .item_menu:
    menu:
        "Pick up the heart locket":
            "* It looks brand new, but it has an antique style to it. Someone must have cherished this locket."
            call .pick_up(Heart_Locket())
        "Pick up the mirror":
            "* It's cracked down the middle, but you can still see your reflection in it."
            call .pick_up(Mirror())
        "Pick up the stick":
            "* It's a stick."
            call .pick_up(Stick())
        "Pick up the rose":
            "* A pristine, red rose. What's it doing among all of this trash?"
            call .pick_up(Rose())

    return


        #Description of the locket if the player examines it after starting a TL run:
        #*It shines brightly. Looking at it makes you think of that special someone.
        #Description of the locket if the player examines it after starting an HB run:
        #*It looks dingy and dull. A small crack runs down its center.
        #Description of the mirror if the player examines it after starting a TL run:
        #*You look at your reflection and smile, thinking of that special someone.
        #Description of the mirror if the player examines it after starting an HB run:
        #*You look at your reflection and smile. You don't even recognize yourself.
        #Description of the stick if the player examines it after starting a TL run:
        #*It seems a little sturdier than before... it even has a small leaf sprouting from it.
        #Description of the stick if the player examines it after starting an HB run:
        #*The stick is becoming more dry and brittle. It could break at any moment.
        #Description of the rose if the player examines it after starting a TL run:
        #*Despite not actively taking care of it, it seems to be full of life and beauty
        #Description of the rose if the player examines it after starting an HB run:
        #*It's wilting... but you expected that, didn't you?
label .pick_up(item):

    "* Take it?"
    menu:
        "* Take it?"
        "Yes":
            "* You got the [item.name]"
            $ pickup_item(item)
        "No":
            "* Then why did you even pick it up?"
            jump .item_menu

label tf_grass_room_options:
    $ take_another = True
    $ tf_look_around_count = 1
    $ alt_way = True
    $ show_vines = True
    while True:
        if not alt_way and not show_vines:
            call show_buttons
            $ renpy.pause()
        else:
            menu:
                "Take another item" if take_another:
                    "* You don't have enough hands to carry all of this stuff."
                    $ take_another = False

                #change button twice then go away
                "Look around" if tf_look_around_count == 1:
                    call .look_around(tf_look_around_count)
                "Look again" if tf_look_around_count == 2:
                    call .look_around(tf_look_around_count)

                "Search for an alternate way" if alt_way:
                    "* You walk along the stone walls for a while, looking into corners and shifting through the piles of trash, but you find nothing that can help you."
                    #patience + 1
                    $ alt_way = False

                "Try to remove the vines covering the exit" if show_vines:
                    "* You try to wrestle the vines free from their purchase on the walls, but they cling stubbornly, resisting your attempts."
                    $ show_vines = False
                    #BRAVERY + 1

    label .look_around(count):
        if count == 1:
            "* Besides the trash and the mound of grass, there is little else to see."
        else:
            "* You sift through some of the garbage but find nothing else of interest. "
            "* However, you do notice that something recently disturbed the mound of grass. "
            "* ...Are there other people down here?"
        return

label summon_flowey:

    $ give_monster_event("Flowey","flowey_introduction")
    $ summon("Flowey")
    return

label flowey_introduction():

    "* The small cave suddenly smells strongly like flowers." 
    show flowey backside with Dissolve(.25)
    "* A large, golden flower has sprouted right where you first fell, appearing to bask in the light coming from the ceiling."
    "* It definitely hadn't been there earlier."
    unknown "Psst... down here!"

    menu:
        "Look around":
            "* Nothing else is different, aside from the flower."
            show flowey annoyed with Dissolve(.25)
            unknown "Hey, buddy, I'm over here!"
        "Approach the flower":
            #ADD BRAVERY +1
            show flowey normal with Dissolve(.25)
            unknown "Howdy!"
            unknown "Hehe, did I startle you?"
        "Run away":
            #BRAVERY - 1
            "* You've seen enough horror movies to know better than to poke around eerie stuff that wasn't there before."
            "* Especially if said eerie stuff talks to you."
            $ get_room("Grass Room").events = {}
            $ get_room("Grass Room").add_event("grass_room_revisited",False)
            $ get_room("Cave Room").add_event("flowey_intro_annoyed",False)
            $ move_to_room("Grass Room")
    jump ruins_intro_flowey
    return
label flowey_intro_annoyed():
    show flowey annoyed with Dissolve(.25)
    "* You return to the small cavern. The odd flower is still there."
    unknown "Were you really just gonna ignore me? Gee, you're a rude one."
    unknown "Since you obviously have no manners, allow me to introduce myself first."
    call ruins_intro_flowey
    return

label grass_room_revisited:
    call show_buttons
    $ search_room = True
    $ vines = True

    while True:
        if search_room or vines:
            menu:
                "Search the room" if search_room:
                    "* You walk around some more. "
                    "* Maybe you missed a crevice or a handhold you could use to climb out of here... "
                    "* Unfortunately, you don't find anything new."
                    $ search_room = False
                "Try to remove the vines covering the exit" if vines:
                    "* The vines hold tighter the more you pull at them."
                    "* There's no way you can break them."
                    $ vines = False
        else:
            return


label ruins_intro_flowey:
        
    show flowey normal with Dissolve(.25)
    unknown "Howdy! I'm Flowey, Flowey the flower! You're new here, aren'tcha?"
    flowey "You look a little nervous... are you scared of little ol' me?"

    menu:
        flowey "You look a little nervous... are you scared of little ol' me?"
        "Take a step back":
            show flowey sideglance with Dissolve(.25)
            flowey "Hey. What's that for?" 
            show flowey smug with Dissolve(.25)
            flowey "Haven't you ever seen a talking flower before?"
            menu:
                flowey "Haven't you ever seen a talking flower before?"
                "Of course I have!":
                    show flowey sideglance with Dissolve(.25)
                    flowey "Hehe, are you sure about that?"
                "Why would I have?":
                    flowey "Oh, a wise guy, huh?"
                    show flowey sideglance with Dissolve(.25)
                    flowey "No reason, really..."
        '"No!"':
            flowey "Oh really?"
            show flowey smug with Dissolve(.25)
            flowey "Don't you know that talking to strangers is dangerous?"
        "Stare":
            flowey "..."
            show flowey sideglance with Dissolve(.25)
            flowey "..."
            show flowey smug with Dissolve(.25)
            flowey "Wow, do you need some water?"
            flowey "...Because you look mighty thirsty."

    show flowey sideglance with Dissolve(.25)
    flowey "Well, at any rate..."

    show flowey normal with Dissolve(.25)
    flowey "Things have changed around here..."
    flowey "The normal rules don't apply anymore, if you know what I mean."
    flowey "So don't worry..."

    show flowey horror with Dissolve(.25)
    flowey "I'm not going to kill you."

    show flowey surprised with Dissolve(.25)
    flowey "...I can't."

    show flowey normal with Dissolve(.25)
    flowey "Instead, I have a new game I'd like to play."
    flowey "It's a game about true love..."

    show flowey horror with Dissolve(.25)
    flowey "...or tragic h e a r t b r e a k..."

    show flowey wink with Dissolve(.25)
    flowey "It'll be fun, don'tcha think?"

    show flowey sideglance with Dissolve(.25)
    flowey "Although, I hope you can come up with a better story than the last human who fell down here. They didn't make it too far..."

    show flowey normal with Dissolve(.25)
    flowey "Guess that means it's up to you to mix things up a bit!"
    
    show flowey annoyed with Dissolve(.25)
    flowey "Try not to disappoint me..."
    
    show flowey wink with Dissolve(.25)
    flowey "Good luck!"
    
    hide flowey with moveoutbottom
    $ banish("Flowey")
    $ get_room("Grass Room").set_event("intro_vines_gone",False)
    $ get_room("Ruins Entrance").set_event("ruins_entrance_intro",False)
    $ set_lock_room("Ruins Entrance",False)
    $ get_room("Tunnels").set_event("tunnels_intro",False)
    $ get_room("Dummy Room").set_event("dummy_intro",False)
    $ get_room("Froggit Room").set_event("ruins_intro_leaves",False)
    $ get_room("Sassy Rock Room").set_event("ruins_intro_rock_toriel",False)
    $ get_room("Blooky Room").set_event("ruins_intro_blooky",False)
    $ get_room("Staircase").set_event("ruins_intro_toriel_house",False)

    call show_buttons
    while True:
        menu:
            "Look Around":
                "* The patch of flowers looks practically untouched, as if flowey had never been here."
                "* You're all alone."
    
label intro_vines_gone:
    "* The vines covering the exit have disappeared."
    "* The trash littered around the room glints in the scattered sunlight."

label dont_be_greedy:
    "* The items are no longer here. Instead, there's a note..."
    "* Don't be greedy~"
    return


label ruins_entrance_intro:

    "* A gentle breeze brushes against your face."
    "* The floor of the stone hallway is covered in red leaves that gather in drifts in the corners and scatter across the path, leading to a set of curving staircases. "
    "* The stairs climb up to a landing that supports a large, ivy-covered building. Its entrance yawns darkly and is flanked by two high windows."
    $ count = 1
    $ loop = True
    $ blook_scream = False
    while loop:

        menu:
            "Look around" if count == 1:
                "* There are piles of the leaves gathered in the corners of the room and between the two staircases, but you see no tree or plant they could have come from. They look crunchy."
                $ count += 1
            "Look again" if count == 2:
                "While looking around, you step on a leaf.  They are crunchy."
                $ count += 1
            "Continue onward":
                "* You cross the hall, stepping on a few leaves when they intersect your path, and climb the gently curving staircase on the left."
                "* You approach the open doorway cautiously, expecting another surprise, but nothing moves or blocks your way."
                "* ...This time."
                $ loop = False
    return

label tunnels_intro:
    "* The tunnels criss-crossing in and out of the various rooms that you pass through are riddled with what appear to be disabled traps and puzzles."
    return

label dummy_intro:
    
    #handle the global
    if 'tf_scream_count' not in player.variables:
        $ player.variables['tf_scream_count'] = 0
    show dummy normal at left
    show napstablook normal at napstabob
    "* The small, curved room houses a training dummy, set up beside the arched doorway leading on to further rooms. A ghost seems to be speaking to the dummy."
    "* The dummy looks friendly, with a smile sewn into its burlap face, but the ghost looks almost... scared."

    menu:
        "Wave":
            unknown "uh...."
            hide napstablook 
            with dissolve
        "Scream":
            #scream sound
            $ blook_scream = True
            if player.variables['tf_scream_count'] > 1:
                "* Wow, you sure do have a thing for screaming, don't you?"
            unknown "....oh no... i didn't mean to scare you..."
            unknown "let me... just....."
            hide napstablook
            with dissolve
        "Stand very still":
            "* Maybe if you stand still, they won't notice you."
            "* ..."
            hide napstablook with Dissolve(2.0)

    show dummy normal at center with Dissolve(.25)

    $ player.variables['satchel_found'] = False
    $ player.variables['satchel_refused'] = False
    $ closer_look = True
    $ kungfu_count = 1
    $ flirt_count = 1
label .dummy_options:
    menu:
        "Look around":
            if not player.variables['satchel_found']:
                "* Oh!"
                "* There's a small leather satchel here. It looks large enough to fit several items inside."
                jump .intro_find_satchel
            elif player.variables['satchel_refused']:
                "* There's that satchel you didn't want."
                "* It looks lonely... Too bad you can't pick it up now."
                "* The satchel doesn't want you. You couldn't see its value before, so you don't deserve it now."
                "* All it wanted to do was hold your things."
            else:
                "* Nothing here anymore."
            jump .dummy_options

        "Examine the dummy":
            "* Looks like a well-used training dummy. You spot some stuffing coming out at the seams."
            "* Who could've put it here?"

            $ loop = True
            while loop:
                menu:
                    "Take a closer look" if closer_look:
                        "* There are some loose stitches near the eyes."
                        "* ...The black, soulless, button eyes that stare right into your soul."
                        "* A shiver runs down your spine."
                        $ closer_look = False

                    #KUNG FU
                    "Practice your kung fu moves" if kungfu_count == 1:
                        "* You miss the dummy entirely."
                        "* Man, you suck at that."
                        $ kungfu_count = 2
                    "Practice your kung fu again" if kungfu_count == 2:
                        "* You prepare a more careful move this time."
                        "* Annnnd you still miss, although not as badly as the previous try." 
                        "* How can you miss, anyway? It's just standing there."
                        $ kungfu_count = 3
                    "Kung fu!" if kungfu_count == 3:
                        "* Three tries. "
                        "* Three misses."
                        "* Either you're really bad at this, or something is going on."
                        $ kungfu_count = 4
                    "Kung......fu......" if kungfu_count >= 4:
                        "* No matter how hard you try, you can't hit the dummy."
                        "* It's as if some higher power were forcing you to miss."


                    #FLIRT
                    "Flirt" if flirt_count == 1:
                        menu:
                            "Did I see you at a toy store? Because you're simply a doll.":
                                $ flirt_count = 2
                            "Hey there, hot stuff. How's it going?":
                                $ flirt_count = 2
                        "* ..."
                        "* ..."
                        "* And now you've started talking to a dummy. This place must really be getting to you."

                    "Flirt..." if flirt_count == 2:
                        menu:
                            "If I could rearrange the alphabet, I'd put U and I together.":
                                pass
                            "Are you a parking ticket? Because you've got fine written all over you.":
                                pass
                        $ flirt_count = 3
                        show dummy blush with Dissolve(.25)
                        "* Is it just you, or are the dummy's cheeks redder than before?"
                        "* ...That concussion you probably have must be worse than you thought."

                    "Flirt!" if flirt_count == 3:
                        menu:
                            "Is your father a farmer? Because you must've fallen from the hay-vens.":
                                pass
                            "Are you from Tennessee? Because you're the only ten I see.":
                                pass
                        $ flirt_count = 4
                        show dummy blush with Dissolve(.25)
                        "* The dummy seems to be winking at you. "
                        "* ...Oh." 

                    "Flirt." if flirt_count == 4:
                        "* You wink at the dummy. It winks back. "

                    "Leave the dummy alone":
                        "* Probably best to leave it be."
                        jump .dummy_options

        "Continue onward":
            if not player.variables['satchel_found']:
                # #keening sound plays
                "* Hmm...?"
                # #keening sound plays again, but louder and more desperate
                "* Oh! It seems to be coming from near the wall."
                "* ...Is that a satchel?"
                "* How did you almost miss this?"
                "* You should really look around more."
                jump .intro_find_satchel
            else:
                call show_buttons
    return

label .intro_find_satchel:
    $ loop = True
    $ count = 1
    $ button1_text = "Take it"
    $ button2_text = "Leave it be"
    $ player.variables['satchel_found'] = True
    while True:
        menu:
            "[button1_text]":
                if count == 4:
                    "* Finally."
                    "* The satchel practically clings to you..."
                    "* ...Was it afraid you wouldn't take it?"
                elif count == 5:
                    "* Was that really so hard now?"
                    "* The satchel practically clings to you..."
                    "* ...Was it afraid you wouldn't take it?"
                else:
                    "* The satchel... wiggles in glee?"
                jump .dummy_options
                $ loop = false
            "[button2_text]":
                if count == 1:
                    "* You decide not to pick it up, despite it being a great tool to hold all of your items."
                elif count == 2:
                    "* You continue to leave the satchel where it is."
                    "* Are you afraid it belongs to someone?"
                    "* It doesn't."
                    "* ..."
                    "* Just take it."
                    $ button1_text = "Take it"
                    $ button2_text = "Do Not"
                elif count == 3:
                    "* You're going to need this..."
                    "* You won't get it anywhere else..."
                    $ button1_text = "TAKE IT"
                    $ button2_text = "Don't click this"
                elif count == 4:
                    "* Quit trolling."
                    $ button1_text = "Last chance"
                    $ button2_text = "This is not the correct option"
                else:
                    "* Fine! "
                    "* Just leave it there!"
                    "* Have fun carrying around everything in your arms."
                    $ loop = False
                    $ player.variables['satchel_refused'] = True
                    jump .dummy_options

        $ count += 1
    
    return

label ruins_intro_leaves:

    "* The bricked hall zig-zags its way around several large piles of red leaves, passing walls hung with flourishing ivy plants and leading to the exit at the far end of the room."
    "* There’s someone here..."
    show toriel normal with Dissolve(.25)
    "* She doesn’t seem to notice you."

    menu:
        "Sneak around":
        #-1 Bravery
            "* There’s nowhere to hide, and not enough room to maneuver around..."
        "Hold your ground":
            #+1 Bravery
            "* Eventually, the monster notices you."
    show toriel surprised with Dissolve(.25)        
    unknown "Oh, goodness! I am sorry, dear... I did not notice you there. Are you alright?"

    menu:
        "Yeah, I’m okay. Thank you.":
            show toriel smile with Dissolve(.25)
            unknown "That is good to hear."
            show toriel surprised with Dissolve(.25)
            unknown "Oh, where are my manners?"
            show toriel smile with Dissolve(.25)
            unknown "My name is Toriel, and I am the caretaker of the Ruins. I come down to the cavern every day to see if anyone has fallen down. And here you are!"
        "Stay back!":
            show toriel sad with Dissolve(.25)
            unknown "Do not worry... I mean you no harm."
            unknown "It must have been quite the shock to find yourself here, no longer among your own people. You have nothing to fear from me, though."
            unknown "I am Toriel, the caretaker of the Ruins, and I can assure you that you are safe here."
        "What is this place?":
            unknown "These are the Ruins, and I am Toriel, their caretaker. I pass through here every day to see if anyone has fallen down. And here you are!"
        "You’re a goat.":
            show toriel laughing with Dissolve(.25)
            unknown "Indeed I am, although I prefer to go by the name of Toriel."
    
    
    show toriel normal with Dissolve(.25)
    toriel "Your fall was not kind to you; you are injured. Please, take this... If you eat it, you are sure to gain some strength back."
    "* You receive a Spider Donut!"
    $ inventory.add(Spider_Donut())
    toriel "And, if you would like, you can accompany me to my house at the far end of the Ruins, to rest and heal the remainder of your injuries."
    toriel "Only my child and I live there, so it will be a peaceful place for you to stay."

    menu:
        "Sure, I’ll come with you.":
            show toriel smallsmile with Dissolve(.25)
            toriel "I am glad... Our home is humble, but I hope you will stay for a while."
            toriel "And I am sure you and Frisk will get along just fine."
            toriel "Follow me then, dear... It is not far."
            $ player.variables['accepted_toriel'] = True
            $ move_to_room("Sassy Rock Room")
            #need some logic here
        "Thanks for the offer, but I’d rather continue on my own.":
            show toriel sad with Dissolve(.5)
            $ player.variables['accepted_toriel'] = False
            toriel "I understand... it can be hard to trust new people when you meet them, but you do not need to be afraid of us."
            toriel "If you change your mind, our door will be open. Be safe."
            hide toriel with Dissolve(.25)
            menu:
                "Look around":
                    "* Now that Toriel’s gone, the room feels pretty empty."
                "Continue onward":
                    call show_buttons
    return


label ruins_intro_rock_toriel:

    show toriel normal with Dissolve(.25)
    #phone ringing sound
    toriel "Excuse me, I must answer this."
    #ringing stops
    toriel "Hello, m-"
    show toriel sad with Dissolve(.25)
    toriel "Oh... oh, dear."
    toriel "Just hold on. Stay right there, okay?"
    toriel "Everything will be alright. Just remain calm. I will be right there."
    #click of phone hanging up
    show toriel awkward with Dissolve(.25)
    toriel "I am afraid something has come up… I am very sorry, but I will have to leave you."
    toriel "You should be fine... Just make your way over to my house. It is straight down this path; you cannot miss it. I will meet you there shortly."
    #toriel sprite fades away
    hide toriel with moveoutright
    jump ruins_intro_rock_alone


label ruins_intro_rock_alone:

    "* The room before you is long and filled with odd items. There is a sign hanging on the wall closest to you."
    "* Three grey rocks sit on top of strange square pads on the ground, and a moat crosses the opposite side of the hall."
    "* A short bridge extends across the still water. There is an exit across the bridge."

    menu:
        "Look around":
            "* A gust of wind trails from the wide doorway ahead, shifting a few leaves across the floor."
            "* There are suspicious-looking holes in the bridge, but it seems safe enough."
        "Continue onward":
            call show_buttons
    return

label ruins_intro_blooky:

    "* The room is average sized and is divided by a wall halfway through that separates the side of the room you are on from two exits on the other side. "
    "* There is a narrow opening in the wall, its floor covered with a scattering of red leaves."
    "* There’s that ghost from earlier..."
    show napstablook normal at napstabob with Dissolve(.25)

    if not blook_scream:
        unknown "....sorry about just disappearing earlier... i didn’t mean to ignore you... or be awkward... i just made this awkward... didn’t i...?"
        unknown "..."
        unknown "...i wasn’t really expecting to meet anyone there..."
        unknown "i wasn’t expecting to run into you here, either... but... i guess i’m not completely surprised..."
        unknown "........ ...... ......."
        unknown "so... uh... you’re new here, right? i’m napstablook..."
    else:
        unknown "oh...... ..."
        unknown "uh, sorry.... i didn’t mean to scare you earlier..."
        unknown "you kind of scared me, too..."
        unknown "um... that’s okay, though... it can’t be helped..."
        unknown "...... .... ............"
        unknown "...well... um... i’m napstablook..."

    menu:
        "It’s nice to meet you.":                          #(+3)
            napstablook "oh... you too..."
            napstablook "....."
            napstablook "it's been..... .. a while since someone new showed up..."
            napstablook "but the last time a human fell down.... .. it wasn’t so bad..."
            show napstablook smallsmile with Dissolve(.25)
            napstablook "they were pretty nice, actually..."
            menu:
                "There are others?":                    #(+0)
                    show napstablook normal with Dissolve(.25)
                    napstablook "oh... yeah... just one, though..."
                    napstablook "i’m sure you’ll meet them soon enough... the ruins aren’t that big..."

                "What happened to them?":                    #(+1)
                    show napstablook normal with Dissolve(.25)
                    napstablook "they’re fine... they’re still here... in the ruins..."
                    napstablook ".... ......."
                    napstablook "i see them every now and again..."
                    napstablook "they’re really nice..."
                    napstablook "......"
                    napstablook "i’m sure you two will get along..."

        "Wow, so you’re really a ghost? That’s creepy...":       #(-3)
            napstablook "oh... well... i’m sorry... there’s not much i can do about that..."
            menu:
                "People are probably scared of you, right?":        #(+2)
                    napstablook "um... i guess... i never thought about it like that..."
                    napstablook "......"
                    show napstablook sad with Dissolve(.25)
                    napstablook "...you’re probably right..."
                "That’s okay, I’ll get used to it.":             #(+1)
                    napstablook "oh... that’s good... sorry..."
                "Sorry, that came out the wrong way.":           #(+0)
                    napstablook "oh... okay..."
                "Sorry about scaring you before...":                   #(+1)
                    napstablook "oh no... you’re fine... i probably did something..."
    
                    menu:
                        "No, not at all!":                           #(+3)
                            napstablook "...really?"
                            show napstablook smallsmile with Dissolve(.25)
                            napstablook "okay... that’s good... thank you..."
                        "I forgive you.":                           #(+2)
                            napstablook "oh, i’m glad..."
                            show napstablook sad with Dissolve(.25)
                            napstablook "i... uh... mess up a lot... it’s one of the few things i’m good at..."
                            show napstablook smallsmile with Dissolve(.25)
                            nastablook "so... thanks for giving me another chance..."


    napstablook "um... i better get back to work now..."
    napstablook "oh... but... before i go..."
    napstablook "i’ve noticed you... uh... haven’t been using the navigation options..."
    napstablook "you’ve just been going in a straight line..."
    napstablook "but... there’s a branching path here... so you might want to press 'E'..."
    napstablook "anyway..."
    napstablook "see you later.....?"
    hide napstablook with Dissolve(2.0)
    return
#the option to navigate is now available to the player. They can now go back to any previous room or choose to go forward. 
#if the player goes east, they encounter the spider bakery
#if the player goes north, they reach the tunnel divide. The tunnel divide should have its own room description, but no story elements take place here. The player can finally go east to encounter Frisk, in which case jump frisk_meeting_start. Or, the player could go north past the black tree room to encounter Toriel, in which case jump ruins_intro_toriel_house
label ruins_intro_toriel_house:
    if 'accepted_toriel' not in player.variables:
        $ player.variables['accepted_toriel'] = True
    if 'met_frisk' not in player.variables:
        $ player.variables['met_frisk'] = False
    if 'accepted_frisk' not in player.variables:
        $ player.variables['accepted_frisk'] = True
    if player.variables['accepted_toriel'] == True and player.variables['met_frisk'] == False:
        show toriel smallsmile with Dissolve(.25)
        toriel "Oh, hello, dear! I am glad to see you made it. You did not have any trouble finding the house, did you?"

        menu:# 29
            "Yes.":                              #(+0
                show toriel awkward with Dissolve(.25)
                toriel "I am sorry about that. I would not have left you behind, but there was an emergency that I had to see to personally."
            "No.":                              #(+0
                toriel "That is wonderful to hear... I knew you would be capable on your own. However, I must apologize for leaving you so suddenly. There was a dire situation that I could not ignore."

        menu:# 30
            "Are you okay?":                        #(+3
                show toriel smile with Dissolve(.25)
                toriel "Oh, I am fine! Your concern is sweet."
                toriel "It was my child, Frisk."
                toriel "But it is nothing for you to worry about. All is well now."
        
            "What happened?":                            #(+0
                show toriel normal with Dissolve(.25)
                toriel "My child, Frisk, called and needed my assistance with... something."
                toriel "However, all is well now. There is no need for you to worry."
                
            "You still abandoned me…":                       #(+2
                show toriel sad with Dissolve(.25)
                toriel "I really cannot apologize enough, dear... I honestly did not want to leave you."
                toriel "But, you see, my child, Frisk, needed my assistance, and I had to reach them right away."
                toriel "It turned out fine, in the end."
        jump ruins_intro_find_Frisk
                
    
    if player.variables['accepted_toriel'] == False and player.variables['met_frisk'] == False:           
        show toriel smallsmile with Dissolve(.25)
        toriel "Oh, hello, dear! I see you have made it to my home…"
        toriel "Have you changed your mind? You are always welcome to stay here and rest awhile."

        menu:# 31
            "Yes, I would like to stay here.":               #(+2
                show toriel smile with Dissolve(.25)
                toriel "Great! I am glad to hear that."
                toriel "You will not regret it… my child and I will be happy to have you here, I assure you."
                $ player.variables['accepted_toriel'] = True
                jump ruins_intro_find_Frisk
            "No, I don’t want to stay with you.":               #(+0
                show toriel normal with Dissolve(.25)
                toriel "Alright… I do wish you would reconsider, but if you insist on striking out on your own…"
                toriel "Well, just know that you will always have a place here, should you ever need it."
                toriel "Feel free to come back anytime!"
                $ move_to_room("Black Tree Room")
            #player can go find Frisk, who also offers to let them stay at their house. If the player refuses all offers, maybe toriel finds them after they’ve passed out from low stamina and brings them to her house.

    #If the player did not accept toriel’s offer (option 57 of selection 22) AND finds Frisk, AND declines Frisk’s offer (option 62 of selection 11 in the Meeting Frisk script) AND returns to toriel’s house:
    if player.variables['accepted_toriel'] == True and player.variables['met_frisk'] == True and player.variables['accepted_frisk'] == False: 
        show toriel smallsmile with Dissolve(.25)
        toriel "Oh, hello again!"
        toriel "My child told me that you helped them collect snails… we are very grateful for your assistance."
        toriel "Are you sure that you would not like to stay for dinner?"

        menu:# 32
            "Sure, I’ll stay.":                          #(+2
                show toriel smile with Dissolve(.25)
                toriel "Excellent! I am glad you have come around."
                toriel "Frisk! We have a guest."
                show toriel smile at right with Dissolve(.25)
                show frisk tinysmile at left with Dissolve(.25)
                frisk "Oh, hey! You changed your mind?"
                frisk "That’s great! I was worried that you wouldn’t find a place to stay before nightfall."
                $ player.variables['reject_toriel'] = False
                jump frisk_meeting_eat
            "For the last time, no. I’m not staying with you.":      #(-3
                #+2 Determination
                show toriel annoyed with Dissolve(.25)
                toriel "Well, fine. If you will not accept our hospitality, then there is little I can do."
                toriel "You are always welcome here, once you have learned to accept help when it is offered."
                $ move_to_room("Black Tree Room")
    return

label ruins_intro_find_Frisk:
    
    if 'clicked_toriel' not in player.variables:
        $ player.variables['clicked_toriel'] = 0

    if player.variables['clicked_toriel'] == 0:
        show toriel smallsmile with Dissolve(.25)
        toriel "In any case, I was just about to prepare dinner. Please, follow me…"
        show toriel awkward with Dissolve(.25)
        toriel "Oh... of course..."
        toriel "It seems that I have run out of snails..."
        show toriel normal with Dissolve(.25)
        toriel "Would you mind finding Frisk, and helping them catch some? They will take you to the best hunting patches."
        toriel "Simply go back through the tunnels, take the path to the east, and they should be there."
        show toriel normal with Dissolve(.25)
        call show_buttons
    else:
        $ renpy.pause()
    #if the player keeps trying to click on toriel
    if player.variables['clicked_toriel'] == 1:
        toriel "Hello, dear. Do you need to hear the directions again? Just go back to the tunnels and take the path to the east. Frisk should still be there."
    elif player.variables['clicked_toriel'] == 2:
        toriel "I really need that final ingredient..."
    elif player.variables['clicked_toriel'] == 3:
        toriel "I am sorry, dear. I am busy making dinner right now. Could you please go find Frisk for me?"
    elif player.variables['clicked_toriel'] == 4:
        toriel "Just go back to the tunnels and take the path to the east. Frisk should still be there."
    if player.variables['clicked_toriel'] > 4:
        show toriel annoyed with Dissolve(.25)


    $ player.variables['clicked_toriel'] += 1
    jump ruins_intro_find_Frisk

label movement_unlocked:
    "Movement unlocked!"
    "Press E or Click the Nav Menu to navigate the Ruins!"
    return

label unlock_movement_engine:
    #activates the movement engine, adds the item room event to the grass room, shows the unlock text, and locks ruins entrance
    $ get_room("Grass Room").add_event("tf_item_room",False)
    $ set_lock_room("Ruins Entrance",True)
    $ move_to_room("Cave Room",False)
    call show_buttons
    "Movement unlocked!"
    "Press E or Click the Nav Menu to navigate the Ruins!"
    return



#if the player refuses all offers by Toriel and Frisk to stay at their house, they will eventually run out of stamina. In this case, the following scene will play:
label ruins_intro_pass_out:
    #can we have some kind of transition showing the MC's eyes slowly opening?
    $ world.move_to_room('Your Room')
    show toriel normal with Dissolve(.25)
    toriel "Oh, thank goodness you are awake..."
    toriel "I apologize, this must be very disorienting for you."
    show toriel awkward with Dissolve(.25)
    toriel "I found you lying on the ground outside, and thought it would be best to bring you into my home. You would not wake up, I was afraid that..."
    show toriel normal with Dissolve(.25)
    toriel "Well, you should be more careful. You mustn't keep running yourself into the ground... You need to allow yourself time to rest."
    show toriel smallsmile with Dissolve(.25)
    toriel "You are more than welcome to return here whenever you are tired. I promise, my child and I do not bite!"

    menu:
        toriel "You are more than welcome to return here whenever you are tired. I promise, my child and I do not bite!"
        "Alright, I'll stay here with you.":
            $ world.get_monster('Toriel').FP += 1
            show toriel smile with Dissolve(.25)
            toriel "I am glad to hear it."

            if player.variables['met_frisk'] == True:
                toriel "While you were gone, I made a meal with the snails you and Frisk caught. I am sure there is enough to go around, if you would like to join us for dinner."
                frisk "Mom? Are they awake yet?"
                show frisk bigsmile at left with moveinleft
                show toriel normal at right
                frisk "Oh, hey! I'm glad you're okay... Mom and I were really worried about you!"
                frisk "If you're staying for dinner, you should hurry up! The food's getting cold!"
                show frisk normal with Dissolve(.25)
                frisk "C'mon, I'll show you to the living room..."
                jump frisk_meeting_eat
            else:
                jump ruins_intro_find_Frisk

        "No way, I'm leaving!":
            $ world.get_monster('Toriel').FP -= 2
            show toriel annoyed with Dissolve(.25)
            toriel "Well, if that is how you feel..."
            toriel "Just do not expect me to find you the next time you pass out."
            show toriel sad with Dissolve(.25)
            toriel "I cannot keep chasing after someone who does not want my help."
            toriel "You are always welcome to return if you change your mind. Just remember that."
            $ move_to_room("Black Tree Room")
            $ player.safe_room = 'Black Tree Room'


    #player is now free to wander the Ruins. If they pass out again, they'll just wake up in the same spot with the following narration:
    

    #*You wake up, sore from laying on the ground. You must've passed out again.
    #the game cannot progress until the player returns to toriel's house and accepts her offer





    



