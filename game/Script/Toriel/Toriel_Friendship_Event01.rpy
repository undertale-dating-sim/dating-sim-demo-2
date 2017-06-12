
#trigger: spending 3 consecutive nights at the ruins
label toriel_friendship_event_1(owner=get_toriel()):
    if world.get_monster('Frisk').FP < 5:
        show toriel normal with Dissolve(.25)
        toriel "Actually, I have been meaning to talk to you. I wanted to know how you were getting along. Are you having fun in the ruins?"
        menu:
            "Yes, I love it here.":
                $ world.get_monster('Toriel').update_FP(-20)
                show toriel surprised with Dissolve(.25)
                toriel "Oh, really? Somehow that comes across as a surprise – considering your recent behaviour."
            "Yes, I'm enjoying myself so far.":
                $ world.get_monster('Toriel').update_FP(-20)
                show toriel surprised with Dissolve(.25)
                toriel "Oh, really? Somehow that comes across as a surprise – considering your recent behaviour."
            "I can't wait to get out of here.":
                $ world.get_monster('Toriel').update_FP(-20)
                show toriel annoyed with Dissolve(.25)
                toriel "Hm. Perhaps that would be for the best. Especially considering your recent behaviour."
        show toriel annoyed with Dissolve(.25)
        toriel "Truthfully I do not care much for your wellbeing at the moment {b}dear{/b}, but I called you over because there is a subject that the two of us urgently need to discuss."
        toriel "Firstly, I thought you should know that I do not stand to lose any hairs over your opinions towards me. You can throw insults in my direction like you cannot tell wrong from right. I can guarantee that I am, and always will be - much too old to care."
        toriel "That being said, There is one thing that I absolutely will not tolerate in my house, and that is {b}any{/b} mistreatment of Frisk."
        toriel "If I hear one more comment regarding them that so much as rub them the wrong way – you will be promptly kicked out of the Ruins, and you {i}will not be welcome{/i} here again. Do you understand?"
        menu:
            "Yes.":
                toriel "Good."
            "No.":
                $ world.get_monster('Toriel').update_FP(-15)
                toriel "I expected nothing more. Nevertheless, my terms still stand. So, if only for your own wellbeing, I implore you to think very carefully about your future actions."
            "Yes, sorry.":
                $ world.get_monster('Toriel').update_FP(5)
                toriel "I accept your apology. As long as your behaviour changes, I am willing to leave this in the past."
        show toriel smile with Dissolve(.25)
        toriel "Well, that is that. I am glad we had this conversation."
        if world.get_monster('Toriel').FP > 10:
            toriel "As a sign that I am willing to put this behind us, I had a spare piece of snail pie that I was going to save for later, but, instead, I will give it to you. After all, it would be a waste to let it get cold, would it not?"
            $ inventory.add(Snail_Pie())
            "* You get a piece of Snail Pie! ... yay?"
            toriel "Make sure to eat the shells. They are a bit crunchy."
        toriel "Now, please, do get back to whatever it is you were doing."
        
    else:
        show toriel smile with Dissolve(.25)
        toriel "Actually, I have been meaning to talk to you. It is nothing serious, do not be concerned! I just wanted to know how you were getting along. Have you had time to adjust to the ruins yet?"
        menu:
            "Yes, I love it here.":
                $ world.get_monster('Toriel').update_FP(5)
                toriel "That is wonderful. I was worried that the Ruins would get boring quickly for someone like you. Of course, it is a charming place to be, but every day is more or less the same."
            "I'm enjoying myself so far.":
                $ world.get_monster('Toriel').update_FP(3)
                toriel "That is wonderful. I was worried that the ruins would get boring quickly for someone like you. Of course, it is a charming place to be, but every day is more or less the same."
            "I can't wait to get out of here.":
                $ world.get_monster('Toriel').update_FP(-4)
                show toriel sad with Dissolve(.25)
                toriel "I must say, that is a little upsetting to hear. Ah well, I will not press the issue further."
        if world.get_monster('Frisk').FP < 15:
            $ world.get_monster('Toriel').update_FP(6)
            show toriel normal with Dissolve(.25)
            toriel "Although, if you do eventually decide to stay here for good, I would like to ask a favour of you. It concerns... Frisk."
            toriel "I am sure you have noticed now that they appear to be happy, and they have never once complained about life down here with me, but... There is not much for them to do around these parts."
            toriel "I do what I can to keep them entertained, but there are only so many times you can read a book before you know all of the words by heart, and there are only so many days you can spend with the same toys before growing bored of them."
            show toriel smallsmile with Dissolve(.25)
            toriel "Please, I hope I do not seem like I am coming on too strong, but they were just so happy to meet another human. I did not think I would ever see such a big smile on their face."
            toriel "I think that given the chance, the both of you could really hit it off."
            toriel "Well, it is just something to consider. Thank you for taking the time to hear this old goat talk. Please, do feel free to return to whatever you were doing before I stopped you."
            
            if world.get_monster('Toriel').FP > 5:
                toriel "Oh, hold on just one moment! I nearly forgot. I actually baked a snail pie to show you my gratitude. "
                toriel "If you are not in the mood to eat it now, feel free to take a slice and save it for later. "
                $ inventory.add(Snail_Pie())
                "* You get a piece of Snail Pie! ... yay?"
                toriel "Make sure to take the shells out before you dig in!"
            
        else:
            #$ Kindess +=1
            $ world.get_monster('Toriel').update_FP(10)
            show toriel normal with Dissolve(.25)
            toriel "Although, even if you do eventually decide to leave, I wanted to take this opportunity to... show my gratitude for spending time with Frisk."
            toriel "I am sure you have noticed now, that they appear to be happy, and they have never once complained about life down here with me, but..."
            show toriel awkward with Dissolve(.25)
            toriel "There is not much for them to do around these parts."
            toriel "I do what I can to keep them entertained, but there are only so many times you can read a book before you know all of the words by heart, and there are only so many days you can spend with the same toys before growing bored of them."            
            toriel "It is your choice, and I do not want to push you into making a decision, but I thought that you should know Frisk was... very happy to meet another human after so long. I did not think I would ever see such a big smile on their face."
            toriel "So please, if you ever decide to step out – even if you do not plan on coming back at first - I want you to know that the doors to the Ruins are always open."
            if world.get_monster('Toriel').FP > 0:
                toriel "..."
                show toriel surprised with Dissolve(.25)
                toriel "Oh! I nearly forgot. I had some spare ingredients lying about, so I baked a small snail pie to show you my gratitude."
                toriel "If you are not in the mood to eat it now, feel free to take a slice and save it for later. Just... make sure to take the shells out before digging in."
                $ inventory.add(Snail_Pie())
                "* You get a piece of Snail Pie! ... yay?"

            show toriel normal with Dissolve(.25)
            toriel "..."
            toriel "Again, thank you. That was all I had to say."
    $ player.variables['Toriel_Friendship_1_Complete'] = True
    return 
    