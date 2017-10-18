#Please ignore this file.  It shouldnt exist.  Why did I spend time making this.  Its a bad joke.


init python:
    credit_text = ["Voice Actor\n","Writers\n","Artists\n"]
    coders_text = ["AnnAisu\n","Chloekat1things (Cece)\n","lzuehsow\n","PayneGray\n"]
    leadership_text = ["Al\n","Blue\n","Becca\n","Louie\n","Nekomayata\n","Sky\n","Wilson\n"]
    audio_text = ["Mitsuko\n","Anna Mangette\n","X2H\n"]
    writers_text = ["CelestialSushi\n","Felix\n","Jeffrey\n","Kate\n","Nevran\n","Quinn\n","Riza\n","Ronnie\n","Rose\n","Sage\n","Sam\n","Vunde\n"]
    credit_speed = 25
    credit_gap = 10
    movecenter = Move((.5,2),(0.5,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    moveleft = Move((.33,1),(0.33,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    moveright = Move((.66,1),(0.66,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")

init:
    image sans_cred = Text(["{size=30}Sans\n"] + credit_text, text_align=0.5)
    image coder_cred = Text(["{size=50}Coders\n{/size}{size=30}"] + coders_text, text_align=0.5)
    image writer_cred = Text(["{size=50}Writers\n{/size}{size=30}"] + writers_text, text_align=0.5)
    image audio_cred = Text(["{size=50}Audio\n{/size}{size=30}"] + audio_text, text_align=0.5)
    image leader_cred = Text(["{size=50}Leadership\n{/size}{size=30}"] + leadership_text, text_align=0.5)
    image begin = Text("{size=80}Project UDS \n {size=40} inLove : An Undertale Dating Simulator\n", text_align =0.5)
    image end = Text("Thanks for Playing!",text_align = .5)



label scrolling_credits:
    
    #play music "audio/music/megalovania.mp3"
    scene black
    

    show begin at movecenter
    with Pause(credit_gap)

    show coder_cred at movecenter
    with Pause(credit_gap*1.1)
    show writer_cred at movecenter
    with Pause(credit_gap)
    show audio_cred at movecenter
    with Pause(credit_gap)
    show leader_cred at movecenter
    with Pause(credit_gap)
    #show sans_credit at moveright
    
    
    # show toriel_cred at moveright
    # show toriel_credit at moveleft
    # with Pause(credit_gap)

    


    show end at Move((.5,1),(0.5,0.5), credit_speed*.7, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credit_gap)

    return