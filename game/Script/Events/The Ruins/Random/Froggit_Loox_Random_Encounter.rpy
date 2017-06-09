#Froggit_Loox sidestory

# Definition of Froggit, figure out later what it's stuff is/where it is/etc.
#Setting some variables, may not need these
#$player.variables['1_find_it_for_froggit'] = False
#$player.variables['4_took_it_back'] = False
#$player.variables[6_no_for_som1_else] = False 
#$player.variables[7_whats_init_for_me] = False


label froggit_loox_ss_start:
    
    show froggit normal with Dissolve(.25)
    
    $sure_here_you_go_loox = False
    $yeah_sure_loox = False
    
    "*A Froggit hops close!"
    froggit "Ribbit, ribbit."
    "*This poor soul says they've lost a very important item of theirs."
    menu:
        "Don't worry, buddy. I'll find it for you.":
            froggit "Ribbit, ribbit."
            "The Froggit describes, in great detail, the item that they need, and then thanks you for your help."
            
            hide froggit with Fade(0.5,1.0,0.5)
            
            # froggit leaves, player eventually goes to next room
            
            "*Oh! There is something on the ground. It looks exactly like what the Froggit was searching for."
            menu:
                "Take it back to the Froggit":
                    "*You pick up the item and turn around to take it back to the Froggit."
                    show loox normal with Dissolve(.25)
                    "*A Loox intercepts your path." #enter Loox
                    loox "... Hey... That thing you're carrying... Can I have it?"
                    menu:
                        "No, it's for someone else.":
                            #+1 kindness
                            #+1 justice
                            jump You_Win
                            
                        "What's in it for me?":
                            loox "I have 30G. Would that work?"
                            menu:
                                "No, I changed my mind.":
                                    jump You_Win
                                "Yeah, sure.":
                                    #-1 kindness
                                    $yeah_sure_loox = True
                                    show loox happy
                                    loox "Great, here's the money."
                                    hide loox with Dissolve(.25)
                                    "*You count the money."
                                    "*They only gave you 5G..." #are we keeping count of gold somewhere?
                                    $ player.gold += 5
                                    jump What_A_Loser
                                "I don't know... I mean, if it was {i}40{/i} gold...": #make 40 italics
                                    #-1 Justice
                                    loox "Oh... I don't have that much. It's okay. I guess it's not that important."
                                    hide loox with Dissolve(.25)
                                    "*Loox has left. Somehow, you managed to lose the item during your conversation..."
                                    jump What_A_Loser
                        "Sure, here you go.":
                            #-1 Kindness
                            $sure_here_you_go_loox = True
                            show loox happy 
                            loox "Thanks, I appreciate it!"
                            hide loox with fade
                            jump What_A_Loser
                "Leave it there":
                    #-1 perseverance
                    "*You leave the item lying all along on the ground with no Froggit to hold it."
                    return
  
        "Ha, loser.":
            # -1 kindness
     
            froggit "Ribbit, ribbit."
            "*They tell you that all they wanted was to find their child's birthday present..."
            hide froggit with Dissolve(.25)
            #probably queue the Froggit leaving, maybe a bit faster than usual
            "*They leave in tears."
 
            #Froggit leaves, player eventually goes to the next room
            "*Huh? There's something on the ground... You wonder if it belongs to that Froggit you bullied."
            "*No use finding out now. They probably wouldn't want to speak to you, anyway."
            "*You leave the item on the ground."
            return
        "You are a frog, all you say is 'ribbit.' How did I understand any of that?":
            # -1 Patience
            froggit "Creak."
            "*They tell you that's your problem, and that you should think before you talk to frogs that way."
            hide froggit with Dissolve(.25)
            "*The Froggit indignantly hops away."
            #probably queue the Froggit leaving the screen
            "*You have no answers."
            return

    return



label You_Win:
    loox "Oh, alright. Good day, then."
    hide loox with fade
    show froggit normal with Dissolve(.25)
    "*You reach the Froggit and give back the item."
    show froggit happy
    "*They seem happy."
    hide froggit with Dissolve(.25)
    return
    
label What_A_Loser: #in the next room, or two rooms or whatever
    show froggit normal with Dissolve(.25)
    froggit "Ribbit, ribbit."
    "*They greet you and ask if you ever found that thing they were looking for."
    menu:
        "Nope, sorry.":
            #-1 integrity
            froggit "Ribbit, ribbit."
            "*They say that's too bad, but thank you for the help either way..."
            hide froggit with Dissolve(.25)
            return
        "Well I {i}did{/i} find it, but then I lost it again.": #add italics on 'did'
            #-1 integrity
            froggit "Ribbit, ribbit."
            "*They tell you that's fine, it's not your fault. Their child might not get a birthday present this year, but it's not that big of a deal..."
            "*They thank you for your help, either way."
            hide froggit with Dissolve(.25)
            return
        "Yes, I have it right here.":
            froggit "Ribbit, ribbit."
            "*They are plesantly surprised. They say that, if you would give it to them, that would be swell."
            menu:
                "I lied. I actually don't have it.":
                    #-1 integrity
                    froggit "... Meow."
                    "*...... Oh."
                    hide froggit with Dissolve(.25)
                    "*Froggit leaves in tears."
                    return
                "Yes, here you go.":
                    froggit "... Woof?"
                    "*They point out that there is nothing in your hand."
                    menu:
                        "I accidentally turned it invisible. And intangible.":
                            #-2 integrity
                            froggit "... Ribbit......"
                            "*They think that you're a liar."
                            "*This Froggit doesn't associate with liars, so they decide that they don't want your help and leave."
                            hide froggit with Dissolve(.25)
                            return
                            #queue leaving?
                        "You're just not looking hard enough.":
                            #-2 integrity
                            froggit "Ribbit, ribbit."
                            "*The Froggit disagrees. They see all that they need to see."
                            "*You disgust them."
                            hide froggit with Dissolve(.25)
                            "*Froggit leaves."
                            #queue leaving?
                            return
                        "I lied. I actually don't have it.":
                            #-2 integrity
                            froggit "... Meow."
                            "*......Oh."
                            hide froggit with Dissolve(.25)
                            "*Froggit leaves in tears."
                            #queue leaving
                            return
                        "*Run away":
                            #-1 bravery
                            hide froggit with fade
                            "*You decide to run away from your shame."
                            return #end of event, put player in next room
                "*Run away":
                    #-1 bravery
                    hide froggit with fade
                    "*You decide to run away from your shame."
                    
                    return #end of event, put player in next room
       # if((player.variables['sure_here_you_go_loox'] == True) || (player.variables[yeah_sure_loox'] == True)):
        "I don't have it, but only because I selfishly sold it for my own gain." if sure_here_you_go_loox or yeah_sure_loox: # code in, only available if picked option 8 or 10
            #-2 justice
            froggit "Croak..."
            "*They say that they thought they could trust you..."
            hide Froggit with Dissolve(.25)
            "*Froggit leaves in tears."
            return #queue leaving 
        
