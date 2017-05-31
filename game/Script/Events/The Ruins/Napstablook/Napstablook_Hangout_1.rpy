label napstablook_hangout_1:
    #Event Name: "Snail Hunting is an Art"
    #Event Trigger:  Having at least +10 FP with Napstablook
    #                Having played the snail minigame at least 3 times
    #                Finding Napstablook in Toriel's garden
    #Synopsis: Napstablook notices you've been catching a lot of snails recently, and offers to help.

    scene background ruins_snailhunting_room
    show napstablook normal at napstabob with dissolve

    $ ruinsnails_asked = False
    $ net_asked = False
    $ extrasnails_asked = False
    
    $ torielsnails_asked = True
    $ napstablookfavsnail_asked = True
    $ boughtsnails_asked = True

    napstablook "hi.... i see you've been catching a lot of snails lately and, um...."
    napstablook "i was wondering if... maybe... you wanted some advice? n-not that you're not doing well on your own........."
    
    menu:
        "Sure!":
            $world.get_monster('Napstablook').update_FP(3)
            napstablook "okay... i'm glad...."
            napstablook "so, um..... what do you want to know?"
            jump snail_advice
        "Sorry, not now.":
            $world.get_monster('Napstablook').update_FP(-1)
            napstablook "oh..... okay......."
            napstablook "well, see you later, then. or not. whatever you want...."
            jump end_blook_hangout2
        "I don't need advice, I'm a snail hunting expert!":
            $world.get_monster('Napstablook').update_FP(-3)
            napstablook "oh, well.... if you're sure......."
            napstablook "i guess i'll just leave, then. sorry to bother you....."
            jump end_blook_hangout2

    label snail_advice:
    #Napstablook is giving you snail-hunting advice.

        menu:
            "What types of snails are there in the Ruins?" if ruinsnails_asked is False:
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "oh, there's not much difference between the snails here...."
                napstablook "the snails in waterfall are a little more diverse and interesting......"
                napstablook "...um, not that the snails here aren't interesting, just......."
                napstablook "well, nevermind...."
                $ ruinsnails_asked = True
                $ torielsnails_asked = False
                $ napstablookfavsnail_asked = False                
            "My net is too slow and big… is there anywhere I can get a better one?" if net_asked is False:
                $world.get_monster('Napstablook').update_FP(2)
                napstablook "um.... Toriel probably has better nets.... but they can get kind of expensive, so she might not trust you with them right away...."
                napstablook "but, uh.... i just prefer the slower nets, anyway. i like to take my time."
                napstablook "i actually have a net that i'm not using... do you want it?"
                $ net_asked = True
                call snailnet_q
            "How can I get rid of my extra snails?" if extrasnails_asked is False:
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "oh, i'll take them.... if you don't want them...."
                napstablook "or you could sell them to Toriel.... i think she'll give you 1G per snail."
                napstablook "but, um.... if you happened to find me in the ruins.... i'll give you a better deal...."
                
                $ extrasnails_asked = True
                $ boughtsnails_asked = False
            "Why are there so many snails in this room?" if torielsnails_asked is False:
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "i don't actually know.... i think Toriel does something to the grass here...."
                napstablook "i thought i saw her spreading something on the ground once..... but i didn't ask her what it was.... i didn't want to bother her...."
                
                $ torielsnails_asked = True
            "What's your favorite kind of snail?" if napstablookfavsnail_asked is False:
                $world.get_monster('Napstablook').update_FP(2)
                napstablook "oh...... that's a difficult question......."
                napstablook "i don't think i have a favorite kind. i like all snails.... especially the ones that live on my farm."
                $ napstablookfavsnail_asked = True
            "What do you do with the snails you buy?" if boughtsnails_asked is False:
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "i just bring them back to my farm.... it's in waterfall..."
                napstablook "people will pay more for snails there than they will in the ruins. that's how we stay in business."
                $ boughtsnails_asked = True
            "That's all I wanted to know.": #(+0 FP)
                napstablook "oh, okay... i hope that was helpful......"
                napstablook "did you, um.... want to try catching snails again? i could watch and tell you how you did after..."
                
                menu: 
                    "Sure!":
                        $world.get_monster('Napstablook').update_FP(1)
                        napstablook "i'll wait here.... good luck....."
                        
                        call demo_undersnail
                        scene background ruins_snailhunting_room
                        $ snail_score = 0
                        
                        show napstablook normal at napstabob with dissolve
                        
                        if ((snail_score < 5) and (snail_score > 0)): #Adjust as needed
                            napstablook "oh.... um... you did......... fine........"
                            napstablook "i'm sure you'll do better next time, now that you've practiced."
                        
                        if snail_score > 5: #Adjust as needed
                            show napstablook smallsmile with dissolve
                            napstablook "i guess my advice really helped..... i'm glad...."
                        
                        if snail_score <= 0:
                            napstablook "um...... i'm not a snail......... i'm sorry....."
                    
                    "I'll pass.":
                        $world.get_monster('Napstablook').update_FP(-1)
                        napstablook "oh, okay.... i understand. i wouldn't want anyone to watch me, either..."
                        napstablook "um, well... in that case... i'll see you around...... i guess......"
                        jump end_blook_hangout2
                        
        jump snail_advice

    label snailnet_q:
        menu:
            "Yes, please!":
                $world.get_monster('Napstablook').update_FP(2)
                napstablook "okay, here you go.... i hope that's helpful..."
                
                ###### NYI - GET INTERMEDIATE NET ITEM ######
                
            "No, thanks!": #(+0 FP)
                napstablook "oh, okay.... just thought i'd offer...."
        return

    label end_blook_hangout2:
        #neutral
        napstablook "well, that's all i have to say...."
        napstablook "if you have any more questions about snails, you can always find me..... i'll be around...."
        return