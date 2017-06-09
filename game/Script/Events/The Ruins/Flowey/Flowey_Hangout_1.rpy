label flowey_hangout1:
    #Hangout 1 
    #{After tutorial}
    #This initial "Hangout" dialogue will occur regardless if player has or has not yet met the prerequisites for a friendship with flowey
    show flowey surprised with Dissolve(.25)
    flowey "Wha-?! You snuck up on me."

    label flowey_hangout1_Q1:
        show flowey suspicious with Dissolve(.25)
        flowey "What do you want? I'm not here to talk, and I'm not gonna give you any tips, either. Buzz off."
        
        menu:
            "Exit":
                return
            "...I'd just like to chat.":
                $world.get_monster('Flowey').update_FP(2)
            "I'd like to talk to you, flower.": 
                $world.get_monster('Flowey').update_HB(2)
                
        show flowey horror with Dissolve(.25)
        flowey "I d i o t . You're in the wrong place. Get out before you piss me off. I'm busy."
        
        menu:
            "Alright, bye.":
                return
            "Busy? Busy doing what?":
                show flowey annoyed with Dissolve(.25)
                flowey "That's none of your business." 
            "What does a flower have to do?":
                $world.get_monster('Flowey').update_HB(2)
                show flowey angry with Dissolve(.25)
                flowey "Seriously? More than you do {i}clearly{/i}."
                flowey "I'm not the one wasting my time annoying someone who has no interest in talking to them."
                flowey "I have a lot more to do than you, apparently."

                show flowey annoyed with Dissolve(.25)
            
                menu:
                    "I'm just interested in what life is like down here.":
                        if (owner.HB >= 2):
                            show flowey sideglance
                            flowey "That's... a matter of perspective."
                            flowey "For obvious reasons."
                            show flowey normal
                            "........"
                            show flowey annoyed
                            flowey "Don't you have anything {i}better{/i} to do?"
                            show flowey smug
                            flowey "Silly me, of course you don't."
                            call flowey_hangout1_path1
                        if (owner.HB < 2):
                            flowey "Then go ask someone else. I have better things to do than talk to some human, and you're not going to find your {i}happy ending{/i} here."
                            flowey "Don't you have anything {i}better{/i} to do?"
                            show flowey smug
                            flowey "Silly me, of course you don't."
                            call flowey_hangout1_path1
                    "We're going to play a game.":
                        if (owner.HB >= 5):
                            show flowey angry
                            flowey "I don't think so."
                            flowey "In fact, I think we're done here."
                            #NYI- HB route is now triggered, player moves onto Flowey HB 1 instead of the usual friendship route
                        if (owner.HB < 5):
                            show flowey surprised
                            flowey "........"
                            show flowey angry
                            flowey "I'm not interested in playing games with you right now."
                            flowey "Or ever, actually."
                            call flowey_hangout1_path1
                    "Sorry, my bad.":
                        call flowey_hangout1_path2
        return
                                
    label flowey_hangout1_path1:
        show flowey annoyed
        flowey "Stop trolling and wasting both of our time."
        menu:
            "You got me. I'm a big troll.":
                $world.get_monster('Flowey').update_FP(-3)
                show flowey horror
                flowey "That's pretty funny, idiot."
                flowey "Now go, before I kill you."
            "Maybe I could help you.":
                $world.get_monster('Flowey').update_FP(2)
                show flowey surprised
                flowey "Help me?"
                show flowey sideglance
                flowey "Idiot. You can't help me."
                flowey "...Not that I need help, anyway."
                flowey "..."
                show flowey normal
                flowey "I'm gonna go. Stay here by your lonesome as long as you'd like."
                flowey "Or go bother someone else."
        return

    label flowey_hangout1_path2:
        show flowey horror
        flowey "That's right, {i}you're{/i} bad--"
        show flowey surprised
        flowey "...wait"
        show flowey suspicious
        flowey "Your bad? That's it?"
        show flowey angry
        flowey "You wasted not just your time, but mine, for the sake of showing up to \"chat\" and now you have nothing better to say than \"my bad\"?!"
        flowey "This is pathetic."
        
        menu:
            "Did... you want me to stay, FLowey?":
                if (owner.FP >= 5):
                    show flowey surprised
                    flowey "..."
                    show flowey blush
                    flowey "I..."
                    show flowey sideglance
                    flowey "Don't be stupid."
                    show flowey normal
                    flowey "I mean, this encounter was actually kind of entertaining."
                    flowey "..."
                    flowey "But I couldn't care less if you chose to leave."
                    show flowey smug
                    flowey "So go. And I'll see you around~ Heehee~!"
                if (owner.FP < 5):
                    show flowey horror
                    flowey "..."
                    flowey "Are you kidding?"
                    show flowey laugh
                    flowey "Pff hahahaHAHAHA!!"
                    show flowey normal
                    flowey "..."
                    show flowey angry
                    flowey "Get out of my face, idiot."
            "It sure is. So I'm leaving.":
                show flowey normal
                flowey "Of course you are."
                show flowey wink
                flowey "Get out of my face, idiot."
            "What did you expect from me?":
                if (owner.FP >= 5):
                    show flowey sideglance
                    flowey "..."
                    show flowey normal
                    flowey "Nothing, apparently."
                    show flowey surprised
                    flowey "Nothing at all."
                    show flowey normal
                    flowey "Well, get going, then. Stop wasting my time."
                if (owner.FP < 5):
                    show flowey laugh
                    flowey "Heh, my expectations for you are very low."
                    show flowey normal
                    flowey "But you already failed them."
                    show flowey smug
                    flowey "Can't say I'm disappointed, however."
                    flowey "It's expected by now."
                    show flowey normal
                    flowey "..."
                    flowey "Get out of my face, idiot."
        return
        