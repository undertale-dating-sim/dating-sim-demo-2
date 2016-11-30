#Please ignore this file.  It shouldnt exist.  Why did I spend time making this.  Its a bad joke.


init python:
    credit_text = ["Voice Actor\n","Writers\n","Artists\n"]
    credit_speed = 25
    credit_gap = 10
    movecenter = Move((.5,1.5),(0.5,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    moveleft = Move((.33,1.5),(0.33,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    moveright = Move((.66,1.5),(0.66,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")

init:
    image sans_cred = Text(["{size=30}Sans\n"] + credit_text, text_align=0.5)
    image toriel_cred = Text(["{size=30}Toriel\n"] + credit_text, text_align=0.5)
    image frisk_cred = Text(["{size=30}Frisk\n"] + credit_text, text_align=0.5)
    image flowey_cred = Text(["{size=30}Flowey\n"] + credit_text, text_align=0.5)
    image undyne_cred = Text(["{size=30}Undyne\n"] + credit_text, text_align=0.5)
    image alphys_cred = Text(["{size=30}Alphys\n"] + credit_text, text_align=0.5)
    image mettaton_cred = Text(["{size=30}Mettaton\n"] + credit_text, text_align=0.5)
    image papyrus_cred = Text(["{size=30}Papyrus\n"] + credit_text, text_align=0.5)
    image grillby_cred = Text(["{size=30}Grillby\n"] + credit_text, text_align=0.5)
    image begin = Text("{size=80}UDS", text_align =0.5)
    image sans_credit = im.Scale("sans.png",200,200)
    image toriel_credit = im.Scale("characters/Toriel/toriel_ph.png",200,200)
    image frisk_credit = im.Scale("frisk.png",200,200) 
    image flowey_credit = im.Scale("flowey.png",200,200) 
    image undyne_credit = im.Scale("undyne.png",200,200) 
    image alphys_credit = im.Scale("alphys.png",200,200) 
    image mettaton_credit = im.Scale("mettaton.png",200,200) 
    image papyrus_credit = im.Scale("papyrus.png",200,200) 
    image grillby_credit = im.Scale("grillby.png",200,200) 
    image end = Text("Thanks for Playing!",text_align = .5)



label scrolling_credits:
    
    play music "audio/music/megalovania.mp3"
    scene black
    

    show begin at movecenter
    with Pause(credit_gap)

    show sans_cred at moveleft
    show sans_credit at moveright
    with Pause(credit_gap)
    
    show toriel_cred at moveright
    show toriel_credit at moveleft
    with Pause(credit_gap)

    show frisk_cred at moveleft
    show frisk_credit at moveright
    with Pause(credit_gap)

    show grillby_cred at moveright
    show grillby_credit at moveleft
    with Pause(credit_gap)

    show flowey_cred at moveleft
    show flowey_credit at moveright
    with Pause(credit_gap)

    show undyne_cred at moveright
    show undyne_credit at moveleft
    with Pause(credit_gap)

    show alphys_cred at moveleft
    show alphys_credit at moveright
    with Pause(credit_gap)

    show mettaton_cred at moveright
    show mettaton_credit at moveleft
    with Pause(credit_gap)

    show papyrus_cred at moveleft
    show papyrus_credit at moveright
    with Pause(credit_gap)


    show end at Move((.5,1),(0.5,0.5), credit_speed*.7, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credit_speed)

    return