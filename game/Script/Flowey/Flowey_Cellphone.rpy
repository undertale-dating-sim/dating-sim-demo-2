label call_Flowey_Unknown(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        flowey "Jeez, where are you even calling from? Your signal sucks! You suck!"
    else:
        pass
    return

label call_Flowey_Cave_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
        
    if owner.variables['SpecCall'] == False:
        if "ruins_cave_phonecall" not in owner.variables:
            $ owner.variables['ruins_cave_phonecall'] = 1
        else:
            $ owner.variables['ruins_cave_phonecall'] += 1
        
        ## Dialogue
        if owner.variables['ruins_cave_phonecall'] == 1:
            flowey "..."
        elif owner.variables['ruins_cave_phonecall'] == 2:
            flowey "..."
        elif owner.variables['ruins_cave_phonecall'] == 3:
            flowey "Why do you keep calling me here?"
            flowey "...What do you know?"
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Grass_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_grass_phonecall" not in owner.variables:
            $ owner.variables['ruins_grass_phonecall'] = 1
        else:
            $ owner.variables['ruins_grass_phonecall'] += 1
            
        ##Dialogue
        if owner.variables['ruins_grass_phonecall'] == 1:
            flowey "Hey, look! It’s where we first met."
            flowey "Boy, did I startle ya. It was like you’d never been threatened by a flower before."
            flowey "Well, there’s plenty more time for that..."
        elif owner.variables['ruins_grass_phonecall'] == 2:
            flowey "You had some sticky fingers in this room."
            flowey "Just waltzed in here and starting taking things as if you owned the place."
            flowey "You’d better learn to not stick your nose where it doesn’t belong."
            flowey "Before someone has to teach you the hard way..."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Ruins_Entrance(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_entrance_phonecall" not in owner.variables:
            $ owner.variables['ruins_entrance_phonecall'] = 1
        else:
            $ owner.variables['ruins_entrance_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_entrance_phonecall'] == 1:
            flowey "I hate stairs."
            flowey "Why? How about you try climbing them when you’re rooted to the ground."
        elif owner.variables['ruins_entrance_phonecall'] == 2:
            flowey "..."
            flowey "The vines are nice, though."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Tunnels(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_tunnels_phonecall" not in owner.variables:
            $ owner.variables['ruins_tunnels_phonecall'] = 1
        else:
            $ owner.variables['ruins_tunnels_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_tunnels_phonecall'] == 1:
            flowey "I don’t see why that goat had to disable all the traps."
            flowey "A couple of spikes never hurt anyone."
        elif owner.variables['ruins_tunnels_phonecall'] == 2:
            flowey "These puzzles were made for babies. Anyone could solve them."
            flowey "Which means you would have been lost in these tunnels until you starved to death."
        elif owner.variables['ruins_tunnels_phonecall'] == 3:
            flowey "Frisk once fell down a ten-foot pit in these tunnels. Wasn’t even scratched."
            flowey "I thought humans were more fragile than that."
            flowey "Kid must be a freak."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Dummy_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_dummy_phonecall" not in owner.variables:
            $ owner.variables['ruins_dummy_phonecall'] = 1
        else:
            $ owner.variables['ruins_dummy_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_dummy_phonecall'] == 1:
            flowey "Great. {i}This guy.{/i}"
            flowey "I’ve tried talking to it a few times. Won’t even acknowledge me."
            flowey "Jerk."
        elif owner.variables['ruins_dummy_phonecall'] == 2:
            flowey "...What?"
            flowey "It’s not like there are a lot of monsters to chat with down here."
            flowey "Especially not ones who’d listen to a talking flower."
            flowey "This guy, however, is a captive audience."
        elif owner.variables['ruins_dummy_phonecall'] == 3:
            flowey "...Lonely? Who said I was lonely?"
            flowey "Don’t make me laugh."
            flowey "I don’t need anyone."
            flowey "..."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Froggit_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_froggit_phonecall" not in owner.variables:
            $ owner.variables['ruins_froggit_phonecall'] = 1
        else:
            $ owner.variables['ruins_froggit_phonecall'] += 1
            
        ##Dialogue
        if owner.variables['ruins_froggit_phonecall'] == 1:
            flowey "Froggits are the worst."
            flowey "All they do is croak when you’re trying to sleep."
        elif owner.variables['ruins_froggit_phonecall'] == 2:
            flowey "Froggits are also as weak as a blind Loox."
            flowey "A dormant Vulkin."
            flowey "A wingless Whimsun."
        elif owner.variables['ruins_froggit_phonecall'] == 3:
            flowey "An immobile Moldsmal."
            flowey "A waterless Woshua."
            flowey "A...magic-less...Madjick..."
            flowey "..."
            flowey "Wait, are you still on?"
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Monster_Candy_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_candy_phonecall" not in owner.variables:
            $ owner.variables['ruins_candy_phonecall'] = 1
        else:
            $ owner.variables['ruins_candy_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_candy_phonecall'] == 1:
            flowey "I say you should take the whole bowl of candy."
            flowey "I mean, who’s gonna stop you? They’re all pushovers."
        elif owner.variables['ruins_candy_phonecall'] == 2:
            flowey "Just take the whole bowl."
            flowey "We both know how greedy you are."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Sassy_Rock_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_rock_phonecall" not in owner.variables:
            $ owner.variables['ruins_rock_phonecall'] = 1
        else:
            $ owner.variables['ruins_rock_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_rock_phonecall'] == 1:
            flowey "You know how they say you can lay on a bed of nails and not feel pain?"
            flowey "Bet you can try that with those spikes over there."
            flowey "Why don’t you give it a shot?"
        elif owner.variables['ruins_rock_phonecall'] == 2:
            flowey "What, are you scared?"
            flowey "Don’t worry, I’ll make sure you don’t get hurt..."
            flowey "...not mortally, at least."
        elif owner.variables['ruins_rock_phonecall'] == 3:
            flowey "I’d say there’s about a fifty percent chance you’ll survive."
            flowey "..."
            flowey "..."
            flowey "Okay, fine. Twenty percent."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Blooky_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_blooky_phonecall" not in owner.variables:
            $ owner.variables['ruins_blooky_phonecall'] = 1
        else:
            $ owner.variables['ruins_blooky_phonecall'] += 1
           
        ##Dialogue
        if owner.variables['ruins_blooky_phonecall'] == 1:
            flowey "Oh. This is where that crybaby ghost likes to hang out."
            flowey "They’re scared of just about everything. I managed to startle them once just by rustling some leaves."
            flowey "It’s about the only entertainment I get down here."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Spider_Bakery(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_bakery_phonecall" not in owner.variables:
            $ owner.variables['ruins_bakery_phonecall'] = 1
        else:
            $ owner.variables['ruins_bakery_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_blooky_phonecall'] == 1:
            flowey "This place is a ripoff."
            flowey "Besides, who wants to eat baked goods made out of spiders?"
            flowey "I’d rather take a bite out of a Vegetoid."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Snail_Hunter(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_snail_phonecall" not in owner.variables:
            $ owner.variables['ruins_snail_phonecall'] = 1
        else:
            $ owner.variables['ruins_snail_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_snail_phonecall'] == 1:
            flowey "Ugh. Snails are so worthless. How can you go through life moving that slow?"
        elif owner.variables['ruins_snail_phonecall'] == 2:
            flowey "...Snail Pie is alright, though."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Tunnel_Divide(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_crossroad_phonecall" not in owner.variables:
            $ owner.variables['ruins_crossroad_phonecall'] = 1
        else:
            $ owner.variables['ruins_crossroad_phonecall'] += 1
            
        ##Dialogue
        if owner.variables['ruins_crossroad_phonecall'] == 1:
            flowey "What, you don’t know which way to go?"
            flowey "How about back from where you came from?"
            flowey "Maybe you’ll stop bothering me, then."
        elif owner.variables['ruins_crossroad_phonecall'] == 2:
            flowey "Can’t you make any decisions for yourself?"
            flowey "You really are a moron."
        elif owner.variables['ruins_crossroad_phonecall'] == 3:
            flowey "You’re just gonna keep calling me until I give you an answer, aren’t ya?"
            flowey "{i}Fine.{/i} If you’re looking for the last human who fell down here, head east. If you’re trying to find that aggravating goat, go north."
            flowey "Now leave me alone."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Overlook(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_overlook_phonecall" not in owner.variables:
            $ owner.variables['ruins_overlook_phonecall'] = 1
        else:
            $ owner.variables['ruins_overlook_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_overlook_phonecall'] == 1:
            flowey "The view?"
            flowey "Yeah, it’s okay, I guess."
            flowey "..."
        elif owner.variables['ruins_overlook_phonecall'] == 2:
            flowey "I used to come here a lot, before..."
            flowey "...before..."
            flowey "..."
            flowey "Don’t call me again."
        elif owner.variables['ruins_overlook_phonecall'] == 3:
            flowey "Are you deaf? I told you not to call me."
            flowey "Idiot."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Black_Tree_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_blacktree_phonecall" not in owner.variables:
            $ owner.variables['ruins_blacktree_phonecall'] = 1
        else:
            $ owner.variables['ruins_blacktree_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_blacktree_phonecall'] == 1:
            flowey "How can a dead tree drop so many leaves?"
            flowey "Doesn’t make any sense."
        elif owner.variables['ruins_blacktree_phonecall'] == 2:
            flowey "I’m sick of nothing making sense."
        else:
            "*No one's answering.*"
    else:
        pass
    return
    
label call_Flowey_Same_Room(owner = False):
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 0
    $ owner.variables['SpecCall'] = False
    $ owner.variables['SameRoom'] = True
    call FloweyCall_FreqCheck
    
    if owner.variables['SpecCall'] == False:
        if "ruins_floweyroom_phonecall" not in owner.variables:
            $ owner.variables['ruins_floweyroom_phonecall'] = 1
        else:
            $ owner.variables['ruins_floweyroom_phonecall'] += 1
        
        ##Dialogue
        if owner.variables['ruins_floweyroom_phonecall'] == 1:
            show flowey normal with fade
            
            flowey "What do you want?"
            flowey "...Wait."
            
            show flowey suspicious with dissolve
            
            flowey "Stop wasting my time."
        elif owner.variables['ruins_floweyroom_phonecall'] == 2:
            show flowey horror with fade
            
            flowey "You really are an idiot."
        else:
            show flowey annoyed with fade
            
            "*No one's answering.*"
            
        hide flowey
    else:
        pass
    return
    
    
label FloweyCall_FreqCheck:
    
    if "CallCounter" not in owner.variables:
        $ owner.variables['CallCounter'] = 1
    else:
        $ owner.variables['CallCounter'] += 1
        $ CallCount = owner.variables['CallCounter']
        $ SameRoom = owner.variables['SameRoom']
    
    if CallCount == 1:
        $ owner.variables['SpecCall'] = True
        
        if SameRoom == True:
            show flowey normal with fade
            
        flowey "Hello?"
        
        if SameRoom == True:
            show flowey suspicious with dissolve
        
        flowey "...Wait. I have a phone?"
        flowey "And you have my number?"
        
        if SameRoom == True:
            show flowey annoyed with dissolve
        
        flowey "How the hell am I even using this thing?!"
        flowey "This game gets dumber by the minute."
        
        if SameRoom == True:
            hide flowey with fade
        return
    elif CallCount == 10:
        $ owner.variables['SpecCall'] = True
        
        if SameRoom == True:
            show flowey angry with fade
        
        flowey "Why are you so needy?!"
        flowey "HOW IS THERE EVEN RECEPTION DOWN HERE?!"
        
        if SameRoom == True:
            hide flowey with fade
        return
    elif CallCount == 16:
        $ owner.variables['SpecCall'] = True
        
        if SameRoom == True:
            show flowey annoyed with fade
            
        flowey "Are you just bored? Is that why you keep calling me?"
        
        if SameRoom == True:
            show flowey normal with dissolve
            
        flowey "To be honest, I don’t even know where this phone came from."
        flowey "It definitely isn’t mine."
        
        if SameRoom == True:
            show flowey excited with dissolve
        
        flowey "Do you feel better? Knowing you’re wasting someone elses ‘anytime minutes’?"
        flowey "They could be charged for ROAMING!"
        
        if SameRoom == True:
            hide flowey with fade
        return
    elif CallCount == 20:
        $ owner.variables['SpecCall'] = True
        
        if SameRoom == True:
            show flowey suspicious with fade
        
        flowey "Ugh."
        flowey "You’re so annoying."
        flowey "Locate the trashcan closest to you and toss your phone in."
        flowey "Oh, and feel free to toss yourself in there, too."
        
        if SameRoom == True:
            hide flowey with fade
        return
    elif CallCount == 25:
        $ owner.variables['SpecCall'] = True
        
        if SameRoom == True:
            show flowey excited with fade
        
        flowey "There’s texting!"
        
        if SameRoom == True:
            show flowey surprised with dissolve
        
        flowey "Oh, I picked up the call, whoops."
        
        if SameRoom == True:
            show flowey wink with dissolve
            
        flowey "Well here, check this out."
        
        if SameRoom == True:
            hide flowey with fade
        return
    elif CallCount == 26:
        $ owner.variables['SpecCall'] = True
        if SameRoom == True:
            show flowey smug with fade
            
        "*Right before you call Flowey again, you feel your phone vibrate."
        "*It’s a text message."
        "*It reads…"
        "* :-) I hope the goat makes you into a pie."
        
        if SameRoom == True:
            show flowey laugh with dissolve
            
        "*..."
        
        if SameRoom == True:
            hide flowey with fade
        return
    elif CallCount == 30:
        $ owner.variables['SpecCall'] = True
        
        if SameRoom == True:
            show flowey normal with fade
            
        flowey "You know what? I won’t indulge you anymore."
        
        if SameRoom == True:
            show flowey smug with dissolve
            
        flowey "You do realize after a certain amount of calls I won’t have anything else to say, right?"
        flowey "You’re just wasting time to see how much I can talk, huh?"
        flowey "Well..."
        
        if SameRoom == True:
            show flowey wink with dissolve
        
        flowey "Sucks to suck."
        
        if SameRoom == True:
            hide flowey with fade
        return
    else:
        return
        