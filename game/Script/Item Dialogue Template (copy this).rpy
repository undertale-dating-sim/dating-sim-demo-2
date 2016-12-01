#variables:
#itemsGivenToday, buttsPie, snailPie, monCandy
#spiDonut, spiCider, milkChoc, whiteChoc = 0

label torielItems(item="monCandy"):
    if item == "buttsPie":
        jump giveButtsPie
    elif item == "snailPie":
        jump giveSnailPie
    elif item == "monCandy":
        jump giveMonCandy
    elif item == "spiDonut":
        jump giveSpiDonut
    elif item == "spiCider":
        jump giveSpiCider
    elif item == "milkChoc":
        jump giveMilkChoc
    elif item == "whiteChoc":
        jump giveWhiteChoc
    else:
        t "Err... I am not sure what you are trying to give me, dear."
        t "Perhaps you should take a moment to compose yourself and try again?"
        jump end
    
label giveButtsPie:
    $ buttsPie += 1
    $ itemsGivenToday += 1
    
    if buttsPie == 1:
        #FP +=5
        #smile
        t "Ah, Butterscotch Pie. Thank you, dear! This is an old recipe I have had for quite some time now. It is always so enjoyable to make. I think we should make some together sometime."
    elif buttsPie == 2:
        #FP +=3
        #small smile
        t "... You know, I made this for you! You should enjoy it for yourself. I could always make another pie if I wanted some. But, thank you for your kind intentions."
    elif buttsPie == 3:
        #FP += 0
        #sad
        t "Do… Do you not like it? Is that why you are giving it back to me?"
    else:
        #FP -=4
        #sad
        t "I… I understand if you do not like it. I shall not give it to you anymore."
    jump gaveItem
        
label giveSnailpie:
    $ snailPie += 1
    $ itemsGivenToday += 1
    
    if  snailPie == 1:
        #FP +=15
        #surprised
        t "Oh! Oh my goodness!"
        #smile
        t "Thank you very much, my dear! I do love Snail Pie. It has such a unique and artful taste to it. It has been one of my favorite foods for as long as I can remember."
    elif snailPie == 2:
        #FP +=10
        #laugh
        t "You know, I used to beg my parents to have this for dinner when I was a child almost every day! Hehehehe!"
        #sudden awkward
        t "..."
        t "... I... I do not know why... I told you that..."
    elif snailPie == 3:
        #FP +=5
        #awkward
        t "I suppose you are beginning to remember what I like! It’s very… Ah... Sweet of you. To remember what I enjoy."
    else:
        #awkward
        t "Ah… Thank you, dear… I will… I will put it with the others."
    jump gaveItem
    
label giveMonCandy:
    $ monCandy += 1
    $ itemsGivenToday += 1
    
    if monCandy == 1:
        #FP +=10
        #smile
        t "Why, thank you! I am glad you found that bowl I put there! I have always loved these. They are a bit of a soft spot of mine! Hehehe!"
        t "Now, I know it says, ‘Take one’, but you can take as many as you would like! Well, you and Frisk, that is."
    elif monCandy == 2:
        #FP +=5
        #smile
        t "Oh, thank you, dear! I actually used to put non-licorice flavored ones in the bowl, until I found out that Frisk did not like them." 
        t "Frisk needs a snack when they go out and play with the other monsters, otherwise they get too tired. So I switched to this flavor, and they seem to like it much more. I suppose you do too!"
    elif monCandy == 3:
        # FP +=3
        #small smile
        t "... You know, I could always get some myself. You don’t have to go through the trouble of getting some for me."
    else:
        #FP +=0
        #neutral
        t "Please, do not give yourself more work than you need. I am telling the truth when I say that I can get these things myself!"
    jump gaveItem

label giveSpiDonut:
    $ spiDonut += 1
    $ itemsGivenToday += 1
    
    if spiDonut == 1:
        #FP +=15
        #smile
        t "My, you got this from the Spider Bake Sale, didn’t you? That’s wonderfully charitable and kind of you to support their cause! Thank you very much, dear. I’ll be sure to enjoy it!"
    elif spiDonut == 2:
        #FP +=10
        #smile
        t "I am very glad that you are continuing to donate to the spiders! They are very sweet. I buy from them whenever I can. I am happy you are too!"
    elif spiDonut == 3:
        #FP +=5
        #small smile
        t "Thank you, but... Do you not want to have some? I do not want you spending so much money on me. These are very good, why not try some for yourself?"
    else:
        #FP +=0
        #awkward
        t "Thank you, dear… I… I hope Frisk will eat some of these… I have too many for me to eat by myself... I will be running my own bakery soon at this rate…"
    jump gaveItem
    
label giveSpiCider:
    $ spiCider += 1
    $ itemsGivenToday += 1
    
    if spiCider == 1:
        #FP +=10
        #smile
        t "This must be the new product that the Spider Bake Sale is selling! Thank you, dear. It looks wonderful! I believe they just announced recently that they were going to be selling something new."
        t "It is wonderful that they are adding more variety to their wears. I think it will greatly increase their sales! Thank you for the cider, and thank you for helping the spiders."
    elif spiCider == 2:
        #FP +=8
        #small smile
        t "I’m not sure what flavor this is supposed to be, but it must be good! I always love the food from the bake sale. Thank you, dear."
    elif spiCider == 3:
        #FP +=3
        #neutral
        t "... How much cider is in each of these jugs? They must not be very cheap… Please don’t spend too much on my account. Even if you are trying to help others, you still need to take care of yourself as well!"
    else:
        #FP +=0
        #awkward
        t "... You really are giving me a lot of this... Maybe I could find a dessert to make out of these? I will have too much than I know what to do with if I can not use it all..."
    jump gaveItem
    
label giveMilkChoc:
    $ milkChoc += 1
    $ itemsGivenToday += 1
    
    if milkChoc == 1:
        #FP +=2
        #awkward
        t "... I am not one for chocolate… It actually makes me ill to eat it."
        #neutral
        t "But I know you were only trying to be kind. It is alright, dear. It’s the thought that counts."
    elif milkChoc == 2:
        #FP +=0
        #awkward
        t "... Maybe you did not understand me the first time? I am allergic to chocolate. I cannot eat it."
        #neutral
        t "Ah, However, I am not upset with you! Trust me, dear. I understand your intentions. I will just give it to Frisk. Hopefully they like chocolate..."
    elif milkChoc == 3:
        #FP -=3
        #annoyed
        t "... Are… Are you trying to give this to me again? Did you want me to give it to Frisk? You know, you can always give it to Frisk, yourself."
        t "I’m sure they would not mind at all taking it from you. In fact, I think they would greatly appreciate it."
    else:
        #FP -=5
        #angry
        t "... Are you {i}trying{/i} to get me to eat this?!"
    jump gaveItem

label giveWhiteChoc:
    $ whiteChoc += 1
    $ itemsGivenToday += 1
    
    if whiteChoc == 1:
        #FP +=3
        #awkward
        t "Oh... Although this does not have any actual chocolate in it, I am still allergic, and can not eat this."
        #neutral
        t "But I am glad that you wanted to give it to me. That was very sweet of you."
    elif whiteChoc == 2:
        #FP += 0
        #awkward
        t "Ah… My dear… I was telling the truth when I said I could not eat this. I hope you understand..."
    elif whiteChoc == 3:
        #FP -=3
        #annoyed
        t "... I’ve… I’ve already asked you to stop giving this to me… I have no use for this."
    else:
        #FP -=5
        #angry
        t "... I ask you to please stop giving me this. I do not want this."
    jump gaveItem

label gaveItem:
    if itemsGivenToday == 1:
        pass
    elif itemsGivenToday == 2:
        #blush
        t "I am very flattered at your generosity from giving me so many gifts! Thank you, my dear."
    elif itemsGivenToday == 3:
        #smile
        t "I sincerely appreciate your gifts, but… I do hope you are not going through much trouble to get me them. I would not want you to go through so much just to please a little lady like me!"
    elif itemsGivenToday == 4:
        #awkward
        t "... Dear, I know your intentions are good, but you really do not need to give me so many things. I am not sure if I even have enough space in my house for everything..."
    else:
        #FP -=3
        #awkward
        t "... I... I would like to ask you to stop, dear. You are beginning to worry me."
    jump end
    
