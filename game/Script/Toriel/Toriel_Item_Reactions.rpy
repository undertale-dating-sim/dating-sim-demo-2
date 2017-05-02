

label give_Gift_Toriel_Unknown:
    show toriel awkward
    toriel "Err... I am not sure what you are trying to give me, dear."
    toriel "Perhaps you should take a moment to compose yourself and try again?"
    return False

label give_Gift_Toriel_Rejection(owner):
    show toriel angry
    $ owner.FP -= 10
    toriel "I would like to ask you to stop."
    return


label give_Gift_Toriel_Spider_Donut(count,owner):
    
    if count == 1:
        $ owner.update_FP(15)
        show toriel smile
        toriel "My, you got this from the Spider Bake Sale, didn’t you? That’s wonderfully charitable and kind of you to support their cause! Thank you very much, dear. I’ll be sure to enjoy it!"
    elif count == 2:
        $ owner.update_FP(10)
        show toriel smile
        toriel "I am very glad that you are continuing to donate to the spiders! They are very sweet. I buy from them whenever I can. I am happy you are too!"
    elif count == 3:
        $ owner.update_FP(5)
        show toriel smallsmile
        toriel "Thank you, but... Do you not want to have some? I do not want you spending so much money on me. These are very good, why not try some for yourself?"
    else:
        show toriel awkward
        toriel "Thank you, dear... I... I hope Frisk will eat some of these... I have too many for me to eat by myself... I will be running my own bakery soon at this rate..."

    return True
    
label give_Gift_Toriel_Butts_Pie(count,owner):

    if count == 1:
        $ owner.update_FP(5)
        show toriel smile
        toriel "Ah, Butterscotch Pie. Thank you, dear! This is an old recipe I have had for quite some time now. It is always so enjoyable to make. I think we should make some together sometime."
    elif count == 2:
        $ owner.update_FP(3)
        show toriel smallsmile
        toriel "... You know, I made this for you! You should enjoy it for yourself. I could always make another pie if I wanted some. But, thank you for your kind intentions."
    elif count == 3:
        show toriel sad
        toriel "Do... Do you not like it? Is that why you are giving it back to me?"
    else:
        $ owner.update_FP(-4)
        show toriel sad
        toriel "I... I understand if you do not like it. I shall not give it to you anymore."

    return True
        
label give_Gift_Toriel_Snail_Pie(count,owner):

    if  count == 1:
        $ owner.update_FP(15)
        show toriel surprised
        toriel "Oh! Oh my goodness!"
        show toriel smile
        toriel "Thank you very much, my dear! I do love Snail Pie. It has such a unique and artful taste to it. It has been one of my favorite foods for as long as I can remember."
    elif count == 2:
        $ owner.update_FP(10)
        show toriel laughing
        toriel "You know, I used to beg my parents to have this for dinner when I was a child almost every day! Hehehehe!"
        show toriel awkward
        toriel "..."
        toriel "... I... I do not know why... I told you that..."
    elif count == 3:
        $ owner.update_FP(5)
        show toriel awkward
        toriel "I suppose you are beginning to remember what I like! It’s very... Ah... Sweet of you. To remember what I enjoy."
    else:
        show toriel awkward
        toriel "Ah... Thank you, dear... I will... I will put it with the others."
    
    return True
    
label give_Gift_Toriel_Monster_Candy(count,owner):

    if count == 1:
        $ owner.update_FP(10)
        show toriel smile
        toriel "Why, thank you! I am glad you found that bowl I put there! I have always loved these. They are a bit of a soft spot of mine! Hehehe!"
        toriel "Now, I know it says, ‘Take one’, but you can take as many as you would like! Well, you and Frisk, that is."
    elif count == 2:
        $ owner.update_FP(5)
        show toriel smile
        toriel "Oh, thank you, dear! I actually used to put non-licorice flavored ones in the bowl, until I found out that Frisk did not like them." 
        toriel "Frisk needs a snack when they go out and play with the other monsters, otherwise they get too tired. So I switched to this flavor, and they seem to like it much more. I suppose you do too!"
    elif count == 3:
        $ owner.update_FP(3)
        show toriel smallsmile
        toriel "... You know, I could always get some myself. You don’t have to go through the trouble of getting some for me."
    else:
        $ owner.update_FP(0)
        show toriel normal
        toriel "Please, do not give yourself more work than you need. I am telling the truth when I say that I can get these things myself!"
    return True
    
label give_Gift_Toriel_Spider_Cider(count,owner):

    if count == 1:
        $ owner.update_FP(10)
        show toriel smile
        toriel "This must be the new product that the Spider Bake Sale is selling! Thank you, dear. It looks wonderful! I believe they just announced recently that they were going to be selling something new."
        toriel "It is wonderful that they are adding more variety to their wears. I think it will greatly increase their sales! Thank you for the cider, and thank you for helping the spiders."
    elif count == 2:
        $ owner.update_FP(8)
        show toriel smallsmile
        toriel "I’m not sure what flavor this is supposed to be, but it must be good! I always love the food from the bake sale. Thank you, dear."
    elif count == 3:
        $ owner.update_FP(3)
        show toriel normal
        toriel "... How much cider is in each of these jugs? They must not be very cheap... Please don’t spend too much on my account. Even if you are trying to help others, you still need to take care of yourself as well!"
    else:
        $ owner.update_FP(0)
        show toriel awkward
        toriel "... You really are giving me a lot of this... Maybe I could find a dessert to make out of these? I will have too much than I know what to do with if I can not use it all..."
    return True
    
label give_Gift_Toriel_Milk_Chocolate(count,owner):

    if count == 1:
        $ owner.update_FP(2)
        call word_scroll("-15")
        show toriel awkward
        toriel "... I am not one for chocolate... It actually makes me ill to eat it."
        show toriel normal
        toriel "But I know you were only trying to be kind. It is alright, dear. It’s the thought that counts."
    elif count == 2:
        $ owner.update_FP(0)
        show toriel awkward
        toriel "... Maybe you did not understand me the first time? I am allergic to chocolate. I cannot eat it."
        show toriel normal
        toriel "Ah, However, I am not upset with you! Trust me, dear. I understand your intentions. I will just give it to Frisk. Hopefully they like chocolate..."
    elif count == 3:
        $ owner.update_FP(-3)
        show toriel annoyed
        toriel "... Are... Are you trying to give this to me again? Did you want me to give it to Frisk? You know, you can always give it to Frisk, yourself."
        toriel "I’m sure they would not mind at all taking it from you. In fact, I think they would greatly appreciate it."
    else:
        $ owner.update_FP(-5)
        show toriel angry
        toriel "... Are you {i}trying{/i} to get me to eat this?!"
    return False

label give_Gift_Toriel_White_Chocolate(count,owner):
    
    if count == 1:
        $ owner.update_FP(3)
        show toriel awkward
        toriel "Oh... Although this does not have any actual chocolate in it, I am still allergic, and can not eat this."
        show toriel normal
        toriel "But I am glad that you wanted to give it to me. That was very sweet of you."
    elif count == 2:
        $ owner.FP += 0
        show toriel awkward
        toriel "Ah... My dear... I was telling the truth when I said I could not eat this. I hope you understand..."
    elif count == 3:
        $ owner.update_FP(-3)
        show toriel annoyed
        toriel "... I’ve... I’ve already asked you to stop giving this to me... I have no use for this."
    else:
        $ owner.update_FP(-5)
        show toriel angry
        toriel "... I ask you to please stop giving me this. I do not want this."
    return False

label Toriel_Gift_Count_Reaction(owner):
    

    if owner.given_today_count == 1:
        pass
    elif owner.given_today_count == 2:
        show toriel blushing
        toriel "I am very flattered at your generosity from giving me so many gifts! Thank you, my dear."
    elif owner.given_today_count == 3:
        show toriel smile
        toriel "I sincerely appreciate your gifts, but... I do hope you are not going through much trouble to get me them. I would not want you to go through so much just to please a little lady like me!"
    elif owner.given_today_count == 4:
        show toriel awkward
        toriel "... Dear, I know your intentions are good, but you really do not need to give me so many things. I am not sure if I even have enough space in my house for everything..."
    else:
        $ owner.update_FP(-3)
        show toriel awkward
        toriel "... I... I would like to ask you to stop, dear. You are beginning to worry me."
    return
    
