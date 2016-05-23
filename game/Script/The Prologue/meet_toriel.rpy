#I swiped this from the demo
screen click_test:
    imagemap:
        ground "backgrounds/background-ruins-blacktree.png"
        hotspot (8, 200, 78, 78) action Return("swimming") alt "Swimming"
        hotspot (204, 50, 78, 78) action Return("science") alt "Science"
        hotspot (452, 79, 78, 78) action Return("art") alt "Art"
        hotspot (602, 316, 78, 78) action Return("go home") alt "Go Home"

#the script for when you first meet toriel
label meet_toriel:
    
    #this is all stupid and is just a placeholder
    show toriel placeholder
    with moveinright

    flowey "IS THAT A GOA.."
    
    hide flowey placeholder
    with moveoutleft
    with hpunch
    
    
    toriel "What a miserable creature."
    toriel "You are a human!  We don't get very many of them down here."
    toriel "One day you might meet monsters down here."
    toriel "When that day comes, I'll teach you how to make friends with them."
    toriel "Oh no! I have a snail, snail, butterscotch, and snail pie cooking!"
    toriel "Quick, come with me to my house."

    hide toriel placeholder
    with moveoutright


    "That was definitely a goat..."
    jump Toriels_House



#a test for clicking on the screen
label toriel_tutorial:
    
    scene background ruins_outsidehouse
    with slideleft

    show toriel placeholder
    with moveinbottom

    toriel "Welcome my child."
    toriel "Because this is a demo, I need you to test something for me."

    toriel "Click on stuff on the screen"
    hide toriel placeholder
    with moveoutbottom

    $ click_score = 0;
    while click_score < 3:
        call screen click_test 
        if _return:
            $ click_score = click_score + 1
            toriel "[click_score] out of 3 found."
    
    show toriel placeholder
    with moveintop
    toriel "Good job! I'm going to go make more pie."

    hide toriel placeholder
    with moveouttop

    "Okay...."
    menu:
        "I found out how to do dialogue and menu"
        "Follow her again":
            jump TheRuins
    return

