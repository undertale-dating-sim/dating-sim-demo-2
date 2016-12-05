label give_Gift_Frisk_Unknown:
    "PLACE HOLDER OH NO TELL WILSON"
    return False

label give_Gift_Frisk_Stick(count,owner):
    show frisk normal
    frisk "A stick?"
    show frisk smallsmile
    frisk "I picked up one of those when I first came to the Underground."
    frisk "I thought I might have to defend myself…"
    show frisk normal
    frisk "Luckily, I didn’t need to fight anyone."
    return False

label give_Gift_Frisk_Heart_Locket(count,owner):
    show frisk soulless
    frisk "..."
    frisk "I can't accept this..."
    return False

label give_Gift_Frisk_Rose(count,owner):
    show frisk smallsmile
    frisk "Um..."
    frisk "No, thanks. You should hold onto that."
    return False

label give_Gift_Frisk_Broken_Mirror(count,owner):
    show frisk normal
    frisk "What's this?"
    frisk "Hey, look. It's me!"
    frisk "You should hang onto this... You never know when you might need it."
    return False

label give_Gift_Frisk_Spider_Donut(count,owner):
    if count == 1:
        $ owner.FP += 3
        show frisk bigsmile
        frisk "For me? Thanks! I love these donuts!"
        frisk "Whenever I have extra coins, I’ll buy a half dozen of these for Mom and me to share."
        frisk "I usually end up eating most of them myself, though..."
    elif count == 2:
        $ owner.FP += 1
        show frisk smallsmile
        frisk "Another donut? Don’t mind if I do!"
    else:
        show frisk normal
        frisk "Uh, well… At least you donated to the Spider Bake Sale!"
    return True

label give_Gift_Frisk_Butts_Pie(count,owner):
    if count == 1:
        $ owner.FP += 4
        show frisk bigsmile
        frisk "For me? Thanks!"
        frisk "I love this kind of pie. It reminds me of Mom."
        frisk "She made it for me when I first fell down here."
    elif count == 2:
        $ owner.FP += 2
        show frisk smallsmile
        frisk "More pie? Thanks!"
    elif count == 3:
        $ owner.FP += 1
        show frisk normal
        frisk "Thanks, but where do you keep getting all of this pie?"
    else:
        frisk "Oh... more pie? Thanks..."
    return True

label give_Gift_Frisk_Snail_Pie(count,owner):
    if count == 1:
        $ owner.FP += 2
        show frisk normal
        frisk "Did Mom give you that?"
        show frisk smallsmile
        frisk "It would probably hurt her feelings if you didn't eat it yourself..."
        frisk "...But I guess I could take a piece of it off your hands if you really want me to."
    elif count == 2:
        show frisk disappointed
        frisk "Oh, I couldn't take another piece... It wouldn't feel right."
        frisk "You keep it."
        return False

    return True

label give_Gift_Frisk_Monster_Candy(count,owner):
    if count == 1:
        show frisk smallsmile
        frisk "Monster Candy? Thanks! You only took one though, right?"
        $ owner.FP += 2

    else:
        #show frisk giggle
        frisk "Hey, you did take more than one!"
        frisk "...Thanks!"

    return True

label give_Gift_Frisk_Spider_Cider(count,owner):
    if count == 1:
        show frisk smallsmile
        $ owner.FP += 2
        frisk "Thanks! Spider Cider isn't my favorite, but at least it goes to a good cause!"
    elif count == 2:
        $ owner.FP += 1
        show frisk normal
        frisk "You must've donated a lot to the Spider Bake Sale."
    else:
        show frisk normal
        frisk "I'm starting to get sick of this cider."
    return True

label give_Gift_Frisk_White_Chocolate(count,owner):
    if count == 1:
        $ owner.FP += 3
        show frisk soulless
        frisk "...Chocolate."
    else:
        show frisk upset
        frisk "Sorry, but... I don't think I want anymore chocolate."
        return False
    #dirty way to do this but Frisk shares white and milk choco reactions
    $ owner.given_items['Milk_Chocolate'] = owner.get_total_specific_item(Milk_Chocolate()) + 1
    return True

label give_Gift_Frisk_Milk_Chocolate(count,owner):
    if count == 1:
        $ owner.FP += 3
        show frisk soulless
        frisk "...Chocolate."
    else:
        show frisk upset
        frisk "Sorry, but... I don't think I want anymore chocolate."
        return False
    $ owner.given_items['White_Chocolate'] = owner.get_total_specific_item(White_Chocolate()) + 1
    return True

label give_Gift_Frisk_Bandage(count,owner):
    $ owner.FP += 3
    show frisk normal
    frisk "W-where did you find that?  I lost it forever ago..."
    frisk "Thank you."
    return True

label give_Gift_Frisk_Toy_Knife(count,owner):
    $ owner.FP -= 3
    show frisk soulless
    frisk "..."
    show frisk sad
    frisk "I'm not sure you should give this to me..."
    return False

label give_Gift_Frisk_Butterfly_Net(count,owner):    
    show frisk smallsmile
    frisk "Hey, I gave you that!"
    frisk "You should hold onto it."
    return False

label Frisk_Consumable_Warning:
    show frisk normal
    frisk "You're just like Mom... Always making sure I'm getting enough to eat."
    frisk "I'm full, I promise!"
    return

label Frisk_Consumable_Reject(owner):
    show frisk annoyed
    $ owner.FP -= 3
    frisk "I'm full, seriously"
    return

label Frisk_Equip_Warning:
    show frisk normal
    frisk "You're giving me a lot of stuff... Maybe you should slow down."
    frisk "I feel kind of guilty accepting all of this!"
    return

label Frisk_Equip_Reject(owner):
    $ owner.FP -= 3
    show frisk disappointed
    frisk "Uh... I don't think I can take this."
    show frisk annoyed
    frisk "You're giving me too many things... I don't even have room to carry all of it!"
    return




