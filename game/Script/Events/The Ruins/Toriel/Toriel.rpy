define t = Character('Toriel')

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
    

label toriel_start:
    
    t "Hello, dear. Can I help you?"
    menu:
        "talk":
            jump talk
        "flirt":
            jump flirt
        "ask":
            jump ask
        "give":
            jump give
    
label talk:
    $ canGiveSnails = snailPlayed and (normalSnails > 0 or dailySnails > 0)
    menu:
        "How are you doing?":
            #smile
            t "I am doing well! Thank you for asking. How are you doing, dear?"
        "What’s crackin’?":
            #awkward
            t "… I don’t believe anything is cracking... Did you hear something breaking? Oh dear, is it that rock again?"
        "'Sup?":
            jump talkSup
        "What have you been doing lately?":
            #small smile
            t "Not much, just the usual. Watching over Frisk, baking, the occasional snail hunting. Although I have also been having a wonderful time with you."
        "I brought you the snails!" if canGiveSnails:
            jump talkBroughtSnails
    jump end

label talkSup:
    t "... ‘Sup’? Is… Is that a surface word? I am sorry, but I am not familiar with it."
    menu:       #Once you've explained it, should she give a different dialogue?
        "Oh! Sorry. It stands for ‘What is up’, which is a commonly used greeting on the surface.":
            #smile
            t "Ah, I see! Thank you for explaining so well."
            #cute smile
            t "Well, I suppose I shall also ask you, ‘sup’?"
        "It means ‘what’s up’.":
            #awkward
            t "Oh… Ah… The ceiling, I suppose... Although I think I might see a spider up there."
        "You seriously don’t know what ‘sup’ means?!":
            #awkward
            t "Oh… Should I know? I am… I am sorry dear, but I do not…"
    jump end
label talkBroughtSnails:
    $ goldEarned = normalSnails + dailySnails*3
    t "Thank you so much dear."
    #smile
    if dailySnails > 0:
        t "Oh!"
        t "I see you brought [dailySnails] [snailType]"
    t "Here, please take this as a thank you."
    "Toriel hands you [goldEarned] gold"
    $ playerGold += goldEarned
    $ normalSnails = 0
    $ dailySnails = 0
    jump end




label flirt:
    menu:
        "Do you have a compass? Because I keep getting lost in your eyes.":
            #suprised
            t "Oh!"
            #laugh
            t "Ahahahaha!"
            #blush
            t "My, you caught me off guard with that! I honestly do not know what to say… Perhaps… I could {i}map{/i} out a way for you?"
            #laugh
            t "Hehehehe!"
        "I love the way your fur looks in the ruins light.":
            #blush
            t "Oh! Ah… Thank you! Thank you very much, dear. That was very... Very kind of you to say! ...You are looking nice yourself! Hehehe!"
        "Butterscotch Pie has got nothing on you in sweetness":
            #blush
            t "Oh my… I am… I am at quite a loss for words… Th-thank you dear. That was very… Well… Sweet of you!"
        "Are you using fire magic right now? Because you’re warming my heart.":
            #blush
            t "Oh dear… You’re making me so flustered… Thank… Thank you dear! I am… So glad I could make you feel happy!"
    jump end
    

label ask:
    #Friendship level neutral options:
    menu:
        "What do you do for fun?":
            jump askFun
        "Do you have a job?":
            jump askJob
        "How long have you lived in the Ruins?":
            jump askLivedRuins
        "What's your favorite thing to bake?":
            jump askFavBake
        #For some reason, these 2 options were seperated in the writing?
        "How’s Frisk treating you?":
            jump askFriskTreat
        "What do you think of Napstablook?":
            jump askThinkNapsta
    
label askFun:
    #smile
    t "Usually, I like to read, bake, and hunt for bugs. I know it does not sound like much, but it’s just perfect for me."
    jump end
label askJob:
    #small smile
    t "Not at the moment... Unless you count taking care of Frisk."
    #surprised
    t "Not in a bad way, I hope you understand!"
    #small smile
    t "Frisk is wonderful, but they are still a teenager. Hehehe!"
    jump end
label askLivedRuins:
    #awkward
    t "... A while."
    menu:
        "Oh, okay.":
            #awkward
            t "..."
            #neutral
            t "I do hope you’re enjoying your stay here!"
        "What’s wrong?":
            #awkward
            t "… It is nothing, dear. But thank you for your concern."
        "How long is ‘a while’?":
            #awkward
            t "... I do not remember. It is not important, anyway."
    jump end
label askFavBake:
    #smile
    t "Well, I do very much enjoy making Butterscotch Pie. However, if I manage to find enough snails, Snail Pie is something I love to make as well." 
    t "Frisk seems to like Butterscotch more than Snail, however. So I try not to make Snail Pie too often."
    t "I have also been known to make the occasional cake."
    jump end
label askFriskTreat:
    t "Ah, Frisk's arrival has been a true blessing. They are a very conscientious child."
    t "They help me with cooking, do chores without complaining, and they are kind to the other residents of the ruins."
    t "Really, I have nothing to complain about. They are the most wonderful child I could ever ask for."
    jump end
label askThinkNapsta:
    #neutral
    t "I think that they are… Well, I can not have a real opinion of them because they never talk to me."
    t "They are particularly shy, so I try not to bother them. But I hope one day I can join them in a real conversation. Maybe even invite them over!"
    jump end
    

    
label give:
    t "Oh! Have you brought me something?"
    menu:
        "Give gift":
            #???
            jump torielItems
        "Cancel":
            t "That is alright, dear."
    jump end
    
    
label end:
    menu:
        "continue talking":
            jump start
        "leave":
            t "Take care, dear"
    return

#talk
    #talkSup
    #talkBroughtSnails
#flirt
#ask
    #askFun
    #askJob
    #askLivedRuins
    #askFavBake
    #askFriskTreat
    #askThinkNapsta
#give
    #giveItem
        #torielItems.rpy
    #giveCancel

