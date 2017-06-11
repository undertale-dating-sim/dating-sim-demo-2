label flowey_hangout1(owner = get_flowey()):
    #Hangout 1 
    #{After tutorial}
    #This initial "Hangout" dialogue will occur regardless if player has or has not yet met the prerequisites for a friendship with flowey
    show flowey surprised with Dissolve(.25)
    flowey "Wha-?! You snuck up on me."

    label flowey_hangout1_Q1:
        show flowey suspicious with Dissolve(.25)
        flowey "What do you want? I'm not here to talk, and I'm not gonna give you any tips, either. Buzz off."
        
        menu:
            "...I'd just like to chat.":
                $world.get_monster('Flowey').update_FP(2)
            "I'd like to talk to you, flower.": 
                $world.get_monster('Flowey').update_HB(2)
            "Exit":
                $ player.variables['Flowey_Hangout_1_Complete'] = True
                return
                
        show flowey horror with Dissolve(.25)
        flowey "I d i o t . You're in the wrong place. Get out before you piss me off. I'm busy."
        
        menu:

            "Busy? Busy doing what?":
                show flowey sideglance with Dissolve(.25)
                flowey "That's none of your business."
                flowey "Why don't you go and find someone else to annoy?"
            "What does a flower have to do?":
                $world.get_monster('Flowey').update_HB(2)
                show flowey angry with Dissolve(.25)
                flowey "Seriously? More than you do {i}clearly{/i}."
                flowey "I'm not the one wasting my time annoying someone who has no interest in talking to them."
                flowey "I have a lot more to do than you, apparently."

            "Alright, bye.":
                $ player.variables['Flowey_Hangout_1_Complete'] = True
                return

        show flowey annoyed with Dissolve(.25)
            
        menu:
            "I'm just interested in what life is like down here.":
                if (world.get_monster('Flowey').HB >= 2):
                    show flowey sideglance with Dissolve(.25)
                    flowey "That's... a matter of perspective."
                    flowey "For obvious reasons."
                    show flowey normal with Dissolve(.25)
                    "........"
                    show flowey annoyed with Dissolve(.25)
                    flowey "Don't you have anything {i}better{/i} to do?"
                    show flowey smug with Dissolve(.25)
                    flowey "Silly me, of course you don't."

                if (world.get_monster('Flowey').HB < 2):
                    flowey "Then go ask someone else. I have better things to do than talk to some human, and you're not going to find your {i}happy ending{/i} here."
                    flowey "Don't you have anything {i}better{/i} to do?"
                    show flowey smug with Dissolve(.25)
                    flowey "Silly me, of course you don't."

            "We're going to play a game.":
                if (world.get_monster('Flowey').HB >= 5):
                    show flowey angry with Dissolve(.25)
                    flowey "I don't think so."
                    flowey "In fact, I think we're done here."
                    #NYI- HB route is now triggered, player moves onto Flowey HB 1 instead of the usual friendship route
                    $ player.variables['flowey_heartbreak_activated'] = True

                if (world.get_monster('Flowey').HB < 5):
                    show flowey surprised with Dissolve(.25)
                    flowey "........"
                    show flowey angry with Dissolve(.25)
                    flowey "I'm not interested in playing games with you right now."
                    flowey "Or ever, actually."

            "Sorry, my bad.":
                jump flowey_hangout1_path2
                                
    label flowey_hangout1_path1:
        show flowey annoyed with Dissolve(.25)
        flowey "Stop trolling and wasting both of our time."
        menu:
            "You got me. I'm a big troll.":
                $world.get_monster('Flowey').update_FP(-3)
                show flowey horror with Dissolve(.25)
                flowey "That's pretty funny, idiot."
                flowey "Now go, before I kill you."
                #exit
            "Maybe I could help you.":
                $world.get_monster('Flowey').update_FP(2)
                show flowey surprised with Dissolve(.25)
                flowey "Help me?"
                show flowey sideglance with Dissolve(.25)
                flowey "Idiot. You can't help me."
                flowey "...Not that I need help, anyway."
                flowey "..."
                show flowey normal with Dissolve(.25)
                flowey "I'm gonna go. Stay here by your lonesome as long as you'd like."
                flowey "Or go bother someone else."
                #exit
        $ player.variables['Flowey_Hangout_1_Complete'] = True
        return

    label flowey_hangout1_path2:
        show flowey horror with Dissolve(.25)
        flowey "That's right, {i}you're{/i} bad--"
        show flowey surprised with Dissolve(.25)
        flowey "...wait"
        show flowey suspicious with Dissolve(.25)
        flowey "Your bad? That's it?"
        show flowey angry with Dissolve(.25)
        flowey "You wasted not just your time, but mine, for the sake of showing up to \"chat\" and now you have nothing better to say than \"my bad\"?!"
        flowey "This is pathetic."
        
        menu:
            "Did... you want me to stay, FLowey?":
                if (world.get_monster('Flowey').FP >= 5):
                    show flowey surprised with Dissolve(.25)
                    flowey "..."
                    show flowey blush with Dissolve(.25)
                    flowey "I..."
                    show flowey sideglance with Dissolve(.25)
                    flowey "Don't be stupid."
                    show flowey normal with Dissolve(.25)
                    flowey "I mean, this encounter was actually kind of entertaining."
                    flowey "..."
                    flowey "But I couldn't care less if you chose to leave."
                    show flowey smug with Dissolve(.25)
                    flowey "So go. And I'll see you around~ Heehee~!"
                    #exit

                if (world.get_monster('Flowey').FP < 5):
                    show flowey horror with Dissolve(.25)
                    flowey "..."
                    flowey "Are you kidding?"
                    show flowey laugh with Dissolve(.25)
                    flowey "Pff hahahaHAHAHA!!"
                    show flowey normal with Dissolve(.25)
                    flowey "..."
                    show flowey angry with Dissolve(.25)
                    flowey "Get out of my face, idiot."
                    #exit

            "It sure is. So I'm leaving.":
                show flowey normal with Dissolve(.25)
                flowey "Of course you are."
                show flowey wink with Dissolve(.25)
                flowey "Get out of my face, idiot."
                #exit

            "What did you expect from me?":
                if (world.get_monster('Flowey').FP >= 5):
                    show flowey sideglance with Dissolve(.25)
                    flowey "..."
                    show flowey normal with Dissolve(.25)
                    flowey "Nothing, apparently."
                    show flowey surprised with Dissolve(.25)
                    flowey "Nothing at all."
                    show flowey normal with Dissolve(.25)
                    flowey "Well, get going, then. Stop wasting my time."
                    #exit

                if (world.get_monster('Flowey').FP < 5):
                    show flowey laugh with Dissolve(.25)
                    flowey "Heh, my expectations for you are very low."
                    show flowey normal with Dissolve(.25)
                    flowey "But you already failed them."
                    show flowey smug with Dissolve(.25)
                    flowey "Can't say I'm disappointed, however."
                    flowey "It's expected by now."
                    show flowey normal with Dissolve(.25)
                    flowey "..."
                    flowey "Get out of my face, idiot."
                    #exit
        $ player.variables['Flowey_Hangout_1_Complete'] = True
        return
        