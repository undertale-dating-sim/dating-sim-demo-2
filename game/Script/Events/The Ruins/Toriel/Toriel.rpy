init:
    #placeholder variables so code compiles:
    #talking variables
    $ snailPlayed = True
    $ normalSnails = 2
    $ dailySnails = 2
    $ snailType = "snaily Snails"
    $ goldEarned = 0
    $ playerGold = 0
    
    #item variables
    $ itemsGivenToday = 0
    $ buttsPie = 0
    $ snailPie = 0
    $ monCandy = 0
    $ spiDonut = 0
    $ spiCider = 0
    $ milkChoc = 0
    $ whiteChoc = 0
    

label toriel_general_dialogue:
    
    toriel "Hello, dear. Can I help you?"
    while True:
        show toriel normal
        menu:
            "I brought you the snails!" if inventory.get_count(Snail):
                call toriel_gd_give_snails
            "Chat":
                call toriel_gd_talk
            "Ask":
                call toriel_gd_ask
            "Flirt":
                call toriel_gd_flirt
            "Give":
                call toriel_gd_give
            "Leave":
                toriel "Take care, dear"
                return

        
label toriel_gd_talk:
    menu:
        "How are you doing?":
            show toriel smile
            jump toriel_gd_howryou
            toriel "I am doing well! Thank you for asking. How are you doing, dear?"
        "What’s crackin’?":
            show toriel awkward
            toriel "… I don’t believe anything is cracking... Did you hear something breaking? Oh dear, is it that rock again?"
        "'Sup?":
            jump toriel_gd_sup
        "What have you been doing lately?":
            show toriel small_smile
            toriel "Not much, just the usual. Watching over Frisk, baking, the occasional snail hunting. Although I have also been having a wonderful time with you."
    return
    
label toriel_gd_howryou:
    toriel "I am doing well! Thank you for asking. How are you doing, dear?"
    menu:
        "I'm good, thanks.":
            show toriel small_smile
            toriel "That is good to hear."
        "Better now that I'm talking to you.":
            #Adds 2 FP
            show toriel blushing
            toriel "Oh! Well, I am glad I could brighten your day!"
    return

label toriel_gd_sup:
    toriel "... ‘Sup’? Is… Is that a surface word? I am sorry, but I am not familiar with it."
    menu:       #Once you've explained it, should she give a different dialogue for repeated clicks?
        "Oh! Sorry. It stands for ‘What is up’, which is a commonly used greeting on the surface.":
            #Adds 2 FP
            show toriel smile
            toriel "Ah, I see! Thank you for explaining so well."
            show toriel small_smile
            toriel "Well, I suppose I shall also ask you, ‘sup’?"
        "It means ‘what’s up’.":
            show toriel awkward
            toriel "Oh… Ah… The ceiling, I suppose... Although I think I might see a spider up there."
        "You seriously don’t know what ‘sup’ means?!":
            #Subtracts 2 FP
            show toriel awkward
            toriel "Oh… Should I know? I am… I am sorry dear, but I do not…"
    return

label toriel_gd_give_snails:
    $ goldEarned = normalSnails + dailySnails*3
    toriel "Thank you so much dear."
    show toriel smile
    if dailySnails > 0:
        toriel "Oh!"
        toriel "I see you brought [dailySnails] [snailType]"
    toriel "Here, please take this as a thank you."
    "Toriel hands you [goldEarned] gold"
    $ playerGold += goldEarned
    $ normalSnails = 0
    $ dailySnails = 0
    return

label toriel_gd_flirt:
    menu:
        "Do you have a compass? Because I keep getting lost in your eyes.":
            show toriel surprised
            toriel "Oh!"
            show toriel laughing
            toriel "Ahahahaha!"
            show toriel blushing
            toriel "My, you caught me off guard with that! I honestly do not know what to say… Perhaps… I could {i}map{/i} out a way for you?"
            show toriel laughing
            toriel "Hehehehe!"
        "I love the way your fur looks in the ruins light.":
            show toriel blushing
            toriel "Oh! Ah… Thank you! Thank you very much, dear. That was very... Very kind of you to say! ...You are looking nice yourself! Hehehe!"
        "Butterscotch Pie has got nothing on you in sweetness":
            show toriel blushing
            toriel "Oh my… I am… I am at quite a loss for words… Th-thank you dear. That was very… Well… Sweet of you!"
        "Are you using fire magic right now? Because you’re warming my heart.":
            show toriel blushing
            toriel "Oh dear… You’re making me so flustered… Thank… Thank you dear! I am… So glad I could make you feel happy!"
    return
    

label toriel_gd_ask:
    menu:
        "What do you do for fun?":
            show toriel smile
            toriel "Usually, I like to read, bake, and hunt for bugs. I know it does not sound like much, but it’s just perfect for me."

        "Do you have a job?":
            show toriel small_smile
            toriel "Not at the moment... Unless you count taking care of Frisk."
            show toriel surprised
            toriel "Not in a bad way, I hope you understand!"
            show toriel smallsmile
            toriel "Frisk is wonderful, but they are still a teenager. Hehehe!"

        "How long have you lived in the Ruins?":
            jump toriel_gd_askLivedRuins

        "What's your favorite thing to bake?":
            show toriel smile
            toriel "Well, I do very much enjoy making Butterscotch Pie. However, if I manage to find enough snails, Snail Pie is something I love to make as well." 
            toriel "Frisk seems to like Butterscotch more than Snail, however. So I try not to make Snail Pie too often."
            toriel "I have also been known to make the occasional cake."

        "How’s Frisk treating you?":
            show toriel smile
            toriel "Ah, Frisk's arrival has been a true blessing. They are a very conscientious child."
            toriel "They help me with cooking, do chores without complaining, and they are kind to the other residents of the ruins."
            toriel "Really, I have nothing to complain about. They are the most wonderful child I could ever ask for."

        "What do you think of Napstablook?":
            show toriel normal
            toriel "I think that they are… Well, I can not have a real opinion of them because they never talk to me."
            toriel "They are particularly shy, so I try not to bother them. But I hope one day I can join them in a real conversation. Maybe even invite them over!"

    return
    
label toriel_gd_askLivedRuins:
    show toriel awkward
    toriel "... A while."
    menu:
        "Oh, okay.":
            show toriel awkward
            toriel "..."
            show toriel normal
            toriel "I do hope you’re enjoying your stay here!"
        "What’s wrong?":
            #Adds 1 FP
            show toriel normal
            toriel "… It is nothing, dear. But thank you for your concern."
        "How long is ‘a while’?":
            show toriel awkward
            toriel "... I do not remember. It is not important, anyway."
    jump end


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
    

