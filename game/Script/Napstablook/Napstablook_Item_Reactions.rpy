# normal
# sad
# shyblush
# smallsmile
# smile
# surprised

label give_Gift_Napstablook_Unknown:
    show napstablook normal at napstabob with dissolve
    napstablook "i don't know what to do with this"
    return False

label give_Gift_Napstablook_Stick(count,owner):
    show napstablook normal at napstabob with dissolve
    napstablook "oh, nice stick.. but... you should probably keep that, right?"
    return False

label give_Gift_Napstablook_Heart_Locket(count,owner):
    show napstablook normal at napstabob with dissolve
    napstablook "that's very pretty, but... it's not really for me"
    return False

label give_Gift_Napstablook_Red_Rose_Special(count,owner):
    show napstablook normal at napstabob with dissolve
    napstablook "it's red, you don't see many flowers like that around here.... You should keep it with you"
    return False

label give_Gift_Napstablook_Red_Rose(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        napstablook "oh... um... "
        napstablook "this is for me?"
        napstablook "oh... uh...."
        napstablook "thanks?"
    else:
        napstablook "another one?"
        napstablook "oh no... this is too much..."
    return False

label give_Gift_Napstablook_Yellow_Rose(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        $ owner.FP += 10
        napstablook "oh, thats a pretty rose..."
        napstablook "wait, you're giving it to me?"
        napstablook "thanks"
    else:
        napstablook "um, you can give this to someone else..."
        napstablook "i don't really need it"
    return False


label give_Gift_Napstablook_Broken_Mirror(count,owner):
    show napstablook normal at napstabob with dissolve
    napstablook "that's a really nice mirror. you should probably take care of it"
    return False

label give_Gift_Napstablook_Spider_Donut(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        napstablook "aren't these made with spiders?"
        napstablook "that's kind of weird......"
        napstablook "sorry, no offense if you like them."
    elif count == 2:
        napstablook "um... sorry, but i really don't want any."
        napstablook "did i confuse you......?"
    else:
        napstablook "oh...."
        napstablook "did i confuse you again?"
        napstablook "you can stop trying to give me donuts"
    return False

label give_Gift_Napstablook_Butts_Pie(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        napstablook "hey, nice pie."
        napstablook "i usually like the kind with snails better, though..."
    else:
        napstablook "um, thanks again"
        napstablook "this pie isn't my favourite though, you can stop giving it to me"
    return True

label give_Gift_Napstablook_Snail_Pie(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        $ owner.FP += 10
        napstablook "is this made of snails?"
        napstablook "wow, thank... i love snails"
    elif count == 2:
        $ owner.FP += 10
        napstablook "another one?"
        napstablook "oh... thanks"
        napstablook "you don't have to waste all this on me, though"
    else:
        napstablook "you keep on giving me these... do you not like snails?"

    return True

label give_Gift_Napstablook_Monster_Candy(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        $ owner.FP += 10
        show napstablook normal
        napstablook "oh...."
        napstablook "uh...."
        napstablook "thanks, i guess?"
        napstablook "people don't usually give me candy... or anything, really....."
    if count == 2:
        napstablook "not that i'm ungrateful... but didn't you already give me one of these?"
        napstablook "sorry, it's okay if you forgot......"
    else:
        napstablook "did you forget again?"
        napstablook "i already have some of these....."
        napstablook "i don't want you to waste all your stuff on me"
    return True

label give_Gift_Napstablook_Spider_Cider(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        napstablook "oh... uh.... spider cider."
        napstablook "you know, sometimes i wonder why spiders use spiders to make their stuff."
        napstablook "maybe it's a hotland thing?"
    else:
        napstablook "um, you can keep that."
        napstablook "i'm not a huge fan of spiders."
        napstablook "they're too crunchy and they kind of.... go right through me"
    return False

label give_Gift_Napstablook_White_Chocolate(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        $ owner.FP += 10
        napstablook "hey, this is my favourite kind of chocolate..."
        napstablook "thanks"
    elif count == 2:
        $ owner.FP += 5
        napstablook "oh, you have more?"
        napstablook "thanks, i really like it"
    else:
        napstablook "um, even though i like this, you don't have to keep on giving it to me..."
    return True

label give_Gift_Napstablook_Milk_Chocolate(count,owner):
    show napstablook normal at napstabob with dissolve
    if count == 1:
        $ owner.FP += 10
        napstablook "oh, thanks"
        napstablook "milk chocolate is pretty good..."
        napstablook "white chocolate is better though"
    elif count == 2:
        napstablook "more chocolate?"
        napstablook "um, thank you"
        napstablook "that's... very nice"
    else:
        napstablook "i really don't need this much chocolate..."
        napstablook "you should keep some for yourself"
    return True

label give_Gift_Napstablook_Bandage(count,owner):
    show napstablook normal at napstabob with dissolve
    napstablook "ew, it looks like it's been used..."
    napstablook "i guess that's cool"
    return False

label give_Gift_Napstablook_Toy_Knife(count,owner):
    show napstablook normal at napstabob with dissolve
    napstablook "well, it doesn't look very dangerous"
    return False

label give_Gift_Napstablook_Rejection(owner):
    show napstablook sad at napstabob with dissolve
    $ owner.FP -= 10
    napstablook "sorry, but..."
    napstablook "why do you keep on giving me things?"
    napstablook "that's kind of weird"
    return

label Napstablook_Gift_Count_Reaction(owner):       
    if owner.given_today_count >= 5:
        call give_Gift_Napstablook_Rejection(owner)
    return
