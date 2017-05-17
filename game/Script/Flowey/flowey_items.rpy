define butt_pie_choice = 0
define snail_pie_choice = 0
define monster_candy_choice = 0
define spider_donut_choice = 0
define spider_cider_choice = 0
define milk_choco_choice = 0
define white_choco_choice = 0
define menu_count = 0

label flowey_item_start:
    if menu_count == 2:
        show flowey sad
        flowey "Why are you being... So nice to me? What sort of... weird joke is this?"
    
    if menu_count == 3:
        show flowey sad
        flowey "You keep giving me stuff... But why? I don't understand..."
        flowey "Don't you get it? Being nice will only get you... nowhere fast."
        
    if menu_count == 4:
        show flowey annoyed
        flowey "Okay, now you're just being kinda weird."
        flowey "It's just getting creepy. Stop it."
        
    if menu_count >= 5:
        show flowey annoyed
        flowey "You know, monsters will deduct friendship points if you give them too many items in one sitting. From this point on, it'll just freak them out."
        show flowey sideglance
        flowey "You don't want them to hate you, right?"
        show flowey horror
        flowey "You'll lose {i}all{/i} your freinds that way."
        show flowey sideglance
        flowey "And I'm not an exception, either. So cool it with the gift spam."
    jump choices
    
label choices:
    menu:
        "Give":
            menu:
                "Butterscotch Pie":
                    $ menu_count += 1
                    jump butt_pie
                    
                "Snail Pie":
                    $ menu_count += 1
                    jump snail_pie
                    
                "Monster Candy":
                    $ menu_count += 1
                    jump monster_candy
                    
                "Spider Donut":
                    $ menu_count += 1
                    jump spider_donut
                    
                "Spider Cider":
                    $ menu_count += 1
                    jump spider_cider
                    
                "Milky Chocolate":
                    $ menu_count += 1
                    jump milk_choco
                    
                "White Chocolate":
                    $ menu_count += 1
                    jump white_choco
                    
                "Back":
                    jump choices
                    
label butt_pie:
    if butt_pie_choice == 0:
        $ butt_pie_choice += 1
        #adds 10 FP
        show flowey surprised
        flowey "What?! Where did you get this?"
        show flowey sad
        flowey "I mean..."
        flowey "Thanks... I guess..."
        jump start
        
    if butt_pie_choice == 1:
        $ butt_pie_choice += 1
        #adds 0 FP
        show flowey annoyed
        flowey "Okay, seriously, where did you get this?! Why do you keep giving it to me?!"
        jump start
        
    if butt_pie_choice == 2:
        $ butt_pie_choice += 1
        #adds 0 FP
        show flowey annoyed
        flowey "Are you trying to get me to say something?!"
        flowey "You're just wasting your time..."
        flowey "And {i}mine{/i}"
        jump start
    
    if butt_pie_choice >= 3:
        $ snail_pie_choice += 1
        #subtracts 5 FP
        show flowey angry
        flowey "Hey! Cut it out!"
        flowey "You're enjoying this, aren't you?! Freak!"
        jump start
        
label snail_pie:
    if snail_pie_choice == 0:
        $ snail_pie_choice += 1
        #adds 10 FP
        show flowey excited
        flowey "Woah! Seriously?!"
        show flowey surprised
        flowey "....."
        show flowey normal
        flowey "uh... I mean... Whatever..."
        jump start
        
    if snail_pie_choice == 1:
        $ snail_pie_choice += 1
        #adds 5 FP
        show flowey normal
        flowey "Pffft. You honestly think I'd want another one of these?"
        flowey "......"
        flowey "...But I guess I'll take it. You know, since you offered. Not for any other reason in particular, really."
        jump start
        
    if snail_pie_choice == 2:
        $ snail_pie_choice += 1
        #adds 0 FP
        show flowey annoyed
        flowey "...Are you trying to win me over? It won't work."
        jump start
        
    if snail_pie_choice >= 3:
        $ snail_pie_choice +=1
        #subtracts 3 FP
        show flowey angry
        flowey "You are trying to win me over, aren't you!? Stop it! And get away from me, you sicko!"
        jump start
        
label monster_candy:
    if monster_candy_choice == 0:
        $ monster_candy_choice += 1
        #subtracts 3 FP
        show flowey annoyed
        flowey "Bleh! These things are beyond gross!"
        flowey "What'd you expect me to do with this?! Eat it?!"
        flowey "Yeah, as if."
        flowey "I'd rather eat whatever's stuck on the bottom of your shoe."
        jump start
        
    if monster_candy_choice == 1:
        $ monster_candy_choice += 1
        #subtracts 5 FP
        show flowey annoyed
        flowey "I told you these are gross! Stop giving them to me, you idiot!"
        jump start
        
    if monster_candy_choice == 2:
        $ monster_candy_choice += 1
        #subtracts 8 FP
        show flowey angry
        flowey "Are you trying to gross me out?! Knock it off!"
        jump start
        
    if monster_candy_choice >= 3:
        $ monster_candy_choice += 1
        #subtracts 10 FP
        show flowey angry
        flowey "You're irritating me on purpose! Get lost, ya loser!"
        jump start
        
label spider_donut:
    if spider_donut_choice == 0:
        $ spider_donut_choice += 1
        #subtracts 3 FP
        show flowey annoyed
        flowey "Ugh. Those spiders probably made you buy this, didn't they?"
        flowey "Jeez. They're so obnoxious. The way they rant about their missing spider clan or whatever."
        show flowey suspicious
        flowey "Why would you put spiders in your donuts? It's disgusting."
        jump start
        
    if spider_donut_choice == 1:
        $ spider_donut_choice += 1
        #subtracts 5 FP
        show flowey annoyed
        flowey "I don't care about those stupid spiders! They can go die in the cold for all I care."
        flowey "So you can stop giving me these disgusting things!"
        jump start
        
    if spider_donut_choice == 2:
        $ spider_donut_choice += 1
        #subtracts 8 FP
        show flowey annoyed
        flowey "I don't want anymore of these dumb sponges they dare to call {i}donuts{/i}. Stop it."
        jump start
        
    if spider_donut_choice >=3:
        $ spider_donut_choice += 1
        #subtracts 10 FP
        show flowey angry
        flowey "You're {i}really{/i} starting to get on my nerves with this. You {i}might{/i} wanna stop."
        show flowey horror
        flowey "...Before I get {i}really{/i} mad."
        jump start
        
label spider_cider:
    if spider_cider_choice == 0:
        $ spider_cider_choice += 1
        #subtracts 3 FP
        show flowey annoyed
        flowey "This is the only thing worse than spider donuts! It tastes like dirt!"
        show flowey sideglance
        flowey "And that's really saying something... Get it? Because I'm a flower!"
        show flowey laugh
        flowey "Hahahahahah!"
        show flowey normal
        flowey "But seriously, this is disgusting."
        jump start
        
    if spider_cider_choice == 1:
        $ spider_cider_choice += 1
        #subtracts 5 FP
        show flowey annoyed
        flowey "Okay, but seriously, I really do think it's gross. Don't give me anymore, got it?"
        jump start
        
    if spider_cider_choice == 2:
        $ spider_cider_choice += 1
        #subtracts 8 FP
        show flowey annoyed
        flowey "You're {i}really{/i} starting to tick me off, buddy."
        jump start
        
    if spider_cider_choice >= 3:
        $ spider_cider_choice += 1
        #subtracts 10 FP
        show flowey angry
        flowey "And here I thought the only dirt was this cider."
        flowey "But you're starting to remind me of dirt youreself, {i}bucko{/i}."
        jump start
        
label milk_choco:
    if milk_choco_choice == 0:
        $ milk_choco_choice += 1
        #adds 5 FP
        show flowey normal
        flowey "Huh. The last time I saw this brand was..."
        show flowey sad
        flowey "....."
        flowey "Nevermind. Thanks...or whatever."
        jump start
        
    if milk_choco_choice == 1:
        $ milk_choco_choice += 1
        #adds 3 FP
        show flowey sideglance
        flowey "Uh, you already gave me one of these. But okay."
        flowey "Thanks"
        jump start
        
    if milk_choco_choice == 2:
        $ milk_choco_choice += 1
        #adds 0 FP
        show flowey annoyed
        flowey "You know, I can only eat so much of this. Have you even noticed how small I am?"
        flowey "I don't need any more."
        jump start
        
    if milk_choco_choice >= 3:
        $ milk_choco_choice += 1
        #subtracts 3 FP
        show flowey annoyed
        flowey "Okay, {i}stop it{/i}. I know you're probably trying to kill me at this point from some suger overdose."
        flowey "It won't work. Give up, I don't want any more."
        jump start
        
label white_choco:
    if white_choco_choice == 0:
        $ white_choco_choice += 1
        #subtracts 5 FP
        show flowey annoyed
        flowey "What's this garbage!?"
        flowey "It has the nerve to call itself \"Chocolate\"?"
        show flowey suspicious
        flowey "Tch! There's not even chocolate in it! Disgusting."
        flowey "I'll take it off your hands, but only so I can throw it in the trash for you."
        flowey "You're welcome."
        jump start
        
    if white_choco_choice == 1:
        $ white_choco_choice += 1
        #subtracts 8 FP
        show flowey annoyed
        flowey "Why are you giving me this imposter of a candy again?! Get this \"Humanstrocity\" out of my face."
        jump start
        
    if white_choco_choice == 2:
        $ white_choco_choice += 1
        #subtracts 10 FP
        show flowey angry
        flowey "You know, you're {i}really{/i} starting to remind me of this bar of junk."
        flowey "You know."
        flowey "Disgusting, unwanted and {i}very much{/i} a disgrace to all of man and monsterkind."
        jump start
        
    if white_choco_choice >= 3:
        $ white_choco_choice += 1
        #subtracts 12 FP
        show flowey smug
        flowey "Well, I guess you're turning into quite a sadist, aren't you? I can't blame you, though."
        show flowey wink
        flowey "I mean, look who you're talking to!"
        flowey "I'll admit I'm a little sadistic myself."
        flowey "But perhaps there's a difference between sadistic and just plain stupid."
        show flowey laugh
        flowey "Hahahahah!"
        jump start