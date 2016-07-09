

#character-settings
define toriel = Character('Toriel')

#default-font
init python:
    style.default.font = "font/DTM-Mono.otf"
    
label toriel_ruins:
    menu:
        "So how are you settling in?":
            jump toriel_event1
        "The Stunted Golden Flower":
            jump toriel_event4
        "FLOWER DATE":
            jump toriel_flower_date
        "Exit":
            jump start
    
label toriel_event1:

    #Event Name: So how are you settling in?
    #Event Trigger: 1. Spending (3) consecutive nights at the ruins.
    #Toriel inquires about the player's well-being. This is the first event wherein Toriel really opens up to the player, as she has become attached now- and begins to believe that the player is here to stay.
    #The first subject Toriel truly opens up on is Frisk – because Frisk is so important to her it's the first personal thing that she's willing to talk about.

    menu:
        "FP with Frisk is >-5 (Event starter)":
            jump toriel_event1_Q1
        "FP WITH FRISK >=15":
            jump toriel_event1_Q2
        "FP WITH FRISK -5<FP<15":
            jump toriel_event1_Q3
        "FP WITH FRISK Below -5FP and relationship is negative":
            jump toriel_event1_Q4
        "Other events":
            jump toriel_ruins

    label toriel_event1_Q1:
        # Happens when FP with Frisk is >-5

        #*worried smile* 
        toriel "Actually, I have been meaning to talk to you. It is nothing serious, do not be concerned! I just wanted to know how you were getting along. Have you had time to adjust to the ruins yet?"
        menu:
            toriel "Actually, I have been meaning to talk to you. It is nothing serious, do not be concerned! I just wanted to know how you were getting along. Have you had time to adjust to the ruins yet?{fast}"

            "Yes, I love it here.": #(+5)
                #happy
                toriel "That is wonderful. I was worried that the ruins would get boring quickly for someone like you. Of course, it is a charming place to be, but every day is more or less the same."
            "I’m enjoying myself so far.":#(+3)
                #happy
                toriel "That is encouraging. I was worried that the ruins would get boring quickly for someone like you. Of course, it is charming place to be, but every day is more or less the same."
            "I can’t wait to get out of here.":#(-4)
                #disappointed
                toriel "I must say, that is a little upsetting to hear. Ah well, I will not press the issue further."
        #/// If >(FP WITH FRISK ≥15)<, jump toriel_event1_Q2
        #/// If >(FP WITH FRISK -5<FP<15), jump toriel_event1_Q3
        #/// If the player on the other hand has been mean to Frisk (Below -5FP), and their relationship is negative – Toriel will take this chance to take the player out to the side and talk to them about their behaviour. She will reprimand them, and tell them that this behaviour will not be tolerated., jump toriel_event1_Q4
        jump toriel_event1



    label toriel_event1_Q2:
        #//INCREASE IN KINDNESS
        #//(+10)
        toriel "Although, even if you do eventually decide to leave – I wanted to take this opportunity to... show my gratitude for spending time with Frisk." 

        toriel "I am sure you have noticed now, that they appear to be happy, and they have never once complain about life down here with me, but... *worried* There is not much for them to do around these parts." 

        toriel "I do what I can to keep them entertained, but there are only so many times you can read a book before you know all the words inside out, and there are only so many days you can spend with the same toys before getting bored of them."

        toriel "It is your choice, and I do not want to push you into making a decision, but I thought that you should know Frisk was... very happy to meet another human after so long. I did not think I would ever see such a big smile on their face."
        toriel "So please, if you ever decide to step out – even if you do not plan on coming back at first, I want you to know that the doors to the ruins are always open."

        toriel "..."
        toriel "Oh! I had nearly forgot. I had some spare ingredients lying about, so I baked a small snail pie to show you my gratitude."

        toriel "If you are not in the mood to eat it now, feel free to take a slice and save it for later. Just... make sure to take the shells out before digging in. "
        #(snail pie +1)
        toriel "..." 
        toriel "Again, thank you. That was all I had to say."
        #return
        #jump toriel_ruins
        jump toriel_event1
    label toriel_event1_Q3:
        #//(+6)
        #*thoughtful*
        toriel "Although, if you do eventually decide to stay here for good – I would like to ask a favour of you. It is... about Frisk." 

        toriel "I am sure you have noticed now, that they appear to be happy, and they have never once complained about life down here with me but..." 
        #*worried* "
        toriel "There is not much for them to do around these parts."

        toriel "I do what I can to keep them entertained, but there are only so many times you can read a book before you know all the words inside out, and there are only so many days you can spend with the same toys before getting bored of them."
        #*worried smile* 
        toriel "Please, I hope I do not seem like I am coming on too strong, but they were just so happy to meet another human. I did not think I would ever see such a big smile on their face." 
        #*smile*
        toriel "I think that given the chance, the both of you could really hit it off."

        toriel "Well, it is just something to consider anyhow. Thank you giving up your time to hear this old goat talk."
        toriel "Please, do feel free to return to whatever you were doing before I stopped you."

        toriel "Oh hold on just one moment! I had nearly forgot. I actually baked a snail pie to show you my gratitude." 

        toriel "If you are not in the mood to eat it now, feel free to take a slice and save it for later." 
        #(snail pie +1)

        toriel "Make sure to take the shells out before you dig in!"
    
        #return
        #jump toriel_ruins
        jump toriel_event1
    label toriel_event1_Q4:

        #remember to bold certain text

        #*neutral*
        toriel "Actually, I have been meaning to talk to you. I wanted to know how you were getting along. Are you having fun in the ruins?"
        menu:
            toriel "Actually, I have been meaning to talk to you. I wanted to know how you were getting along. Are you having fun in the ruins?{fast}"

            "Yes, I love it here.": # //(-20)
                #*surprise*
                toriel "Oh, really? Somehow that comes across as a surprise – considering your recent behaviour."
            "I’m enjoying myself so far.":  #//(-20)
                #*surprise*
                toriel "Oh, really? Somehow that comes across as a surprise – considering your recent behaviour. "
            "I can’t wait to get out of here.": #//(-20)
                #*annoyed* 
                toriel "Hm. Perhaps that would be for the best. Especially considering your recent behaviour."

        #*annoyed* 
        toriel "Truthfully I do not care much for your wellbeing at the moment sweetheart, but I called you over because there is a subject that the two of us urgently need to discuss."

        toriel "Firstly, I thought you should know that I do not stand to lose any hair over your opinions towards me. You can throw insults in my direction like you can not tell wrong apart from right, and I can guarantee that I am, and always will be - much too old to care."

        toriel "That being said, There is one thing that I absolutely will not tolerate in my house, and that is any mistreatment of Frisk." 

        toriel "If I hear one more comment regarding them that will so much as rub them the wrong way – you will be promptly kicked out of the ruins, and will not be welcome here again. Do you understand?"

        menu:
            toriel "If I hear one more comment regarding them that will so much as rub them the wrong way – you will be promptly kicked out of the ruins, and will not be welcome here again. Do you understand?{fast}"

            "Yes.": #//(0)
                toriel "Good."

            "No.": #//(-15)
                toriel "I expected nothing more. Nevertheless, my terms still stand. So, if only for your own wellbeing – I implore you to think about your next actions very carefully."
            "Yes, sorry.": #//(+5)
                toriel "I accept your apology. As long as your behaviour changes, I am willing to put this in the past."
        #*smile* 
        toriel "Well, that will be that. I am glad we had this conversation."

        menu:
            "FP with Toriel >10?"
            "Yes":
                toriel "As a sign that I am willing to put this behind us, I had a spare piece of snail pie that I was going to save for later, but instead - I will give it to you. It would be a waste to let it get cold after all, would it not?"
                #(snail pie +1)
                toriel "Make sure to eat the shells. They are a bit crunchy."
                toriel "Please, do get back to whatever it is you were doing."
                jump toriel_event1
                #return
            "No":
                toriel "Please, do get back to whatever it is you were doing."
                jump toriel_event1
                #return

label toriel_event4:
#Event Name: The Stunted Golden Flower
#This flower can be watered every two 'days'. Since the game does not have a day/night system, the flower can be re-watered after the player goes to sleep (2) times. This flower has to be watered every two/three days, otherwise the timer resets, and the cycle has to be started over.
    "*this flower pot is home to a yellow flower, but the earth inside it is dry."
    menu:
        "*this flower pot is home to a yellow flower, but the earth inside it is dry.{fast}"
        "(water it)":
            #(0)
            "*it perks up immediately"
        "(don't water it)":
            #(-15)
            "*you must be thirstier, huh?"
    #if WATERED
    "*this flower pot is home to a yellow flower. It looks refreshed for now."
    #///If>(“WATERED PREVIOUS DAY”)<
    "*this flower pot is home to a yellow flower. The earth is still a little damp."

    #(If the player remembers to water the flower every two/three days for a consecutive of 10 or so days, their PERSEVERANCE increases greatly, and the stunted flower blooms [sprite changes?])

    #This opens up dialogue with TORIEL:
    toriel "Oh! I have great news. I do not know if you have noticed, but the stunted golden flower in our corridor has finally bloomed. I had been fretting over that poor thing so long, too. Ah well, no worries now I suppose. Maybe it was just shy."

    toriel "Still, it is quite strange is it not? It flowered only a little after you came. Perhaps you are some sort of good omen?"
        
    menu:
        toriel "Still, it is quite strange is it not? It flowered only a little after you came. Perhaps you are some sort of good omen?{fast}"

        "Or Perhaps I’ve actually been watering it.": #//(-5)
            #*sheepish* 
            toriel "Err, yes. I suppose that is also a possibility."
            toriel "Although, even if only through common sense – it appears you have a way with plants."
            #JUMP TO LABEL: 'FLOWER DATE'
        "It’s the power of friendship.": #//(+8FP)
            #///If >E(It’s the power of friendship.)<
            # *happy*
            toriel "Oh that’s a nice way to put it!"
            toriel "Although, friendship or no, - it appears you have a way with plants."
            #JUMP TO LABEL: 'FLOWER DATE'
        "It’s the power of love.":# //(+8DP)
            #///If >R(It’s the power of love.)<
            #*deep in thought*
            toriel "Ah yes. I suppose love is said to be the most powerful source... Still – you must have had a lot of love for that flower for it to bloom so fast..."
            toriel "Although, love or no – it appears you have a way with plants."
            #JUMP TO LABEL: 'FLOWER DATE'
    jump toriel_ruins

label toriel_flower_date:
    #LABEL: 'FLOWER DATE'
    toriel "That is already miles more than I can say for myself. It is not that I haven't tried. I have, and many times... but it seems I have a 'black thumb' of sorts. I am not terribly good at keeping anything alive for very long. Truthfully, it is impressive the flower survived as long as it did."

    toriel "If you have some spare time, perhaps sometime you'd like to help me out with the tree in front of our home? Any leaves that grow on it just drop off, regardless of weather or season. It really is quite a shame. However, I am sure that with your help, we could bring it back around."
    #CREATION OF DATE OPTION: 'SAVING THE TREE'
    menu:
        toriel "If you have some spare time, perhaps sometime you'd like to help me out with the tree in front of our home? Any leaves that grow on it just drop off, regardless of weather or season. It really is quite a shame. However, I am sure that with your help, we could bring it back around.{fast}"
        #Selection A
        "I’d love to.":#)                                 //(+5)
            toriel "Fantastic! Please approach me about it when you would like to start."
            #//END EVENT
        "That dead black thing? It’ll be tough.":#)         //(-5)
            toriel "Oh yes, I fully realise. You do not have to of course – just if you have a boring day and nothing to do.
                toriel: Either way, there is no need to worry about it for now. Just approach me if you would like to start."
            #//END EVENT
    
    jump toriel_ruins