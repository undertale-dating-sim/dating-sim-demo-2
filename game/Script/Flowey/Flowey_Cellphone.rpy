label call_Flowey_Unknown(attempted_room):
    
    call FloweyCall_FreqCheck
    return


label call_Flowey_Cave_Room(owner,call_count):

    call Flowey_Cell_Count_Check(owner)
    if _return:
        return  
  
        
    ## Dialogue
    if call_count == 1:
        flowey "..."
    elif call_count == 2:
        flowey "..."
    elif call_count == 3:
        flowey "Why do you keep calling me here?"
        flowey "...What do you know?"
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Grass_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return

    if call_count == 1:
        flowey "Hey, look! It’s where we first met."
        flowey "Boy, did I startle ya. It was like you’d never been threatened by a flower before."
        flowey "Well, there’s plenty more time for that..."
    elif call_count == 2:
        flowey "You had some sticky fingers in this room."
        flowey "Just waltzed in here and starting taking things as if you owned the place."
        flowey "You’d better learn to not stick your nose where it doesn’t belong."
        flowey "Before someone has to teach you the hard way..."
    else:
        "*No one's answering.*"

    return
    
label call_Flowey_Ruins_Entrance(owner,call_count):

    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 


    ##Dialogue
    if call_count == 1:
        flowey "I hate stairs."
        flowey "Why? How about you try climbing them when you’re rooted to the ground."
    elif call_count == 2:
        flowey "..."
        flowey "The vines are nice, though."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Tunnels(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "I don’t see why that goat had to disable all the traps."
        flowey "A couple of spikes never hurt anyone."
    elif call_count == 2:
        flowey "These puzzles were made for babies. Anyone could solve them."
        flowey "Which means you would have been lost in these tunnels until you starved to death."
    elif call_count == 3:
        flowey "Frisk once fell down a ten-foot pit in these tunnels. Wasn’t even scratched."
        flowey "I thought humans were more fragile than that."
        flowey "Kid must be a freak."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Dummy_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "Great. {i}This guy.{/i}"
        flowey "I’ve tried talking to it a few times. Won’t even acknowledge me."
        flowey "Jerk."
    elif call_count == 2:
        flowey "...What?"
        flowey "It’s not like there are a lot of monsters to chat with down here."
        flowey "Especially not ones who’d listen to a talking flower."
        flowey "This guy, however, is a captive audience."
    elif call_count == 3:
        flowey "...Lonely? Who said I was lonely?"
        flowey "Don’t make me laugh."
        flowey "I don’t need anyone."
        flowey "..."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Froggit_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "Froggits are the worst."
        flowey "All they do is croak when you’re trying to sleep."
    elif call_count == 2:
        flowey "Froggits are also as weak as a blind Loox."
        flowey "A dormant Vulkin."
        flowey "A wingless Whimsun."
    elif call_count == 3:
        flowey "An immobile Moldsmal."
        flowey "A waterless Woshua."
        flowey "A...magic-less...Madjick..."
        flowey "..."
        flowey "Wait, are you still on?"
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Monster_Candy_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "I say you should take the whole bowl of candy."
        flowey "I mean, who’s gonna stop you? They’re all pushovers."
    elif call_count == 2:
        flowey "Just take the whole bowl."
        flowey "We both know how greedy you are."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Sassy_Rock_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "You know how they say you can lay on a bed of nails and not feel pain?"
        flowey "Bet you can try that with those spikes over there."
        flowey "Why don’t you give it a shot?"
    elif call_count == 2:
        flowey "What, are you scared?"
        flowey "Don’t worry, I’ll make sure you don’t get hurt..."
        flowey "...not mortally, at least."
    elif call_count == 3:
        flowey "I’d say there’s about a fifty percent chance you’ll survive."
        flowey "..."
        flowey "..."
        flowey "Okay, fine. Twenty percent."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Blooky_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 


    ##Dialogue
    if call_count == 1:
        flowey "Oh. This is where that crybaby ghost likes to hang out."
        flowey "They’re scared of just about everything. I managed to startle them once just by rustling some leaves."
        flowey "It’s about the only entertainment I get down here."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Spider_Bakery(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "This place is a ripoff."
        flowey "Besides, who wants to eat baked goods made out of spiders?"
        flowey "I’d rather take a bite out of a Vegetoid."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Snail_Hunter(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 


    ##Dialogue
    if call_count == 1:
        flowey "Ugh. Snails are so worthless. How can you go through life moving that slow?"
    elif call_count == 2:
        flowey "...Snail Pie is alright, though."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Tunnel_Divide(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "What, you don’t know which way to go?"
        flowey "How about back from where you came from?"
        flowey "Maybe you’ll stop bothering me, then."
    elif call_count == 2:
        flowey "Can’t you make any decisions for yourself?"
        flowey "You really are a moron."
    elif call_count == 3:
        flowey "You’re just gonna keep calling me until I give you an answer, aren’t ya?"
        flowey "{i}Fine.{/i} If you’re looking for the last human who fell down here, head east. If you’re trying to find that aggravating goat, go north."
        flowey "Now leave me alone."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Overlook(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

        ##Dialogue
    if call_count == 1:
        flowey "The view?"
        flowey "Yeah, it’s okay, I guess."
        flowey "..."
    elif call_count == 2:
        flowey "I used to come here a lot, before..."
        flowey "...before..."
        flowey "..."
        flowey "Don’t call me again."
    elif call_count == 3:
        flowey "Are you deaf? I told you not to call me."
        flowey "Idiot."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Black_Tree_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    

    ##Dialogue
    if call_count == 1:
        flowey "How can a dead tree drop so many leaves?"
        flowey "Doesn’t make any sense."
    elif call_count == 2:
        flowey "I’m sick of nothing making sense."
    else:
        "*No one's answering.*"
    return
    
label call_Flowey_Same_Room(owner,call_count):
    call Flowey_Cell_Count_Check(owner)
    if _return:
        return 
    
    if call_count == 1:
        show flowey normal
        flowey "What do you want?"
        flowey "...Wait."
        show flowey suspicious with dissolve
        flowey "Stop wasting my time."

    elif call_count == 2:
        show flowey horror
        flowey "You really are an idiot."
    else:
        show flowey annoyed
        "*No one's answering.*"
    return
    
    
label Flowey_Cell_Count_Check(owner):

    python:
        CallCount = 0
        SameRoom = get_monster("Flowey").current_room == current_room()
        for key,var in owner.variables.iteritems():
            if "_call_count" in key:
                CallCount += var
    
    if CallCount == 1:
        
        if SameRoom == True:
            show flowey normal
            
        flowey "Hello?"
        
        if SameRoom == True:
            show flowey suspicious with dissolve
        
        flowey "...Wait. I have a phone?"
        flowey "And you have my number?"
        
        if SameRoom == True:
            show flowey annoyed with dissolve
        
        flowey "How the hell am I even using this thing?!"
        flowey "This game gets dumber by the minute."
        
        return
    elif CallCount == 10:
        
        if SameRoom == True:
            show flowey angry
        
        flowey "Why are you so needy?!"
        flowey "HOW IS THERE EVEN RECEPTION DOWN HERE?!"
        
        return
    elif CallCount == 16:
        
        if SameRoom == True:
            show flowey annoyed 
            
        flowey "Are you just bored? Is that why you keep calling me?"
        
        if SameRoom == True:
            show flowey normal with dissolve
            
        flowey "To be honest, I don’t even know where this phone came from."
        flowey "It definitely isn’t mine."
        
        if SameRoom == True:
            show flowey excited with dissolve
        
        flowey "Do you feel better? Knowing you’re wasting someone elses ‘anytime minutes’?"
        flowey "They could be charged for ROAMING!"
        
        return
    elif CallCount == 20:
        
        if SameRoom == True:
            show flowey suspicious 
        
        flowey "Ugh."
        flowey "You’re so annoying."
        flowey "Locate the trashcan closest to you and toss your phone in."
        flowey "Oh, and feel free to toss yourself in there, too."
        
        return
    elif CallCount == 25:
        
        if SameRoom == True:
            show flowey excited 
        
        flowey "There’s texting!"
        
        if SameRoom == True:
            show flowey surprised with dissolve
        
        flowey "Oh, I picked up the call, whoops."
        
        if SameRoom == True:
            show flowey wink with dissolve
            
        flowey "Well here, check this out."
        
        return
    elif CallCount == 26:
        if SameRoom == True:
            show flowey smug 
            
        "*Right before you call Flowey again, you feel your phone vibrate."
        "*It’s a text message."
        "*It reads…"
        "* :-) I hope the goat makes you into a pie."
        
        if SameRoom == True:
            show flowey laugh with dissolve
            
        "*..."
        
        return
    elif CallCount == 30:
        
        if SameRoom == True:
            show flowey normal 
            
        flowey "You know what? I won’t indulge you anymore."
        
        if SameRoom == True:
            show flowey smug with dissolve
            
        flowey "You do realize after a certain amount of calls I won’t have anything else to say, right?"
        flowey "You’re just wasting time to see how much I can talk, huh?"
        flowey "Well..."
        
        if SameRoom == True:
            show flowey wink with dissolve
        
        flowey "Sucks to suck."
        
        return True
    else:
        return False
        