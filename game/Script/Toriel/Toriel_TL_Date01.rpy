init:
    $ toriel_tl_route_open = True
    $ toriel_tl_date01_marryme_joke = False
    $ toriel_tl_date01_laughitoff = False
    $ toriel_tl_date01_crazyoldgoat = False
    $ toriel_tl_date01_q_blacktree = False
    $ toriel_tl_date01_stunning = False
    $ toriel_tl_date01_fineapple = False
    $ toriel_tl_date01_favcolor_picked = False
    $ toriel_tl_date01_favcolor_green = False

    #temp variables for testing
    $ toriel_fp = 50
    $ toriel_dp = 50
    $ toriel_hp = 50


#triggered when Toriel has been high enough toriel_fp/toriel_dp
#       and when all flirt options have been used
    
label toriel_tl_date_1(owner=get_toriel()):
    show toriel normal with Dissolve(.25)
    toriel "Dear, do you have a moment to talk?"
    toriel "I have noticed that you have been acting quite... straightforward with me. Now, I will not tell you whom you should be interested in, but you are aware that I am no spring chicken, correct?"
    toriel "I think you would be better off chasing a younger skirt."

label opening_menu:
    menu:
        "I LOVE YOU THE WAY YOU ARE! MARRY ME!" if toriel_tl_date01_marryme_joke == False:
            $ world.get_monster('Toriel').update_FP(-2)
            show toriel awkward with Dissolve(.25)
            toriel "I think that is going a bit too far, dear."
            $ toriel_tl_date01_marryme_joke = True
            menu:
                "I'm just kidding.":
                    show toriel sad with Dissolve(.25)
                    toriel "Well... Please do not joke like that. It is never kind to play with people’s feelings, yes?"
                    jump opening_menu
                "YOU'RE MY ONE AND ONLY GODDESS":
                    $ world.get_monster('Toriel').update_FP(-3)
                    toriel "I see you are feeling rather… strongly on that topic. But still, I must ask that you stop this kind of behavior. I do not appreciate it."
                    toriel "That was all I wished to ask you. Have a good day."
                    jump date_retry
        "No, actually, I would really like to go on a date with you.":
            $ toriel_dp += 2
            show toriel laughing with Dissolve(.25)
            toriel "Haha, you are adorable. Why on earth would you want to date {i}me{/i}?"
            menu:
                "No, I'm serious.":
                    $ toriel_dp +=2
                    show toriel smallsmile with Dissolve(.25)
                    toriel "Oh."
                    toriel "Well, I suppose there would be no harm in going on one date."
                    jump toriel_toriel_date_start
                "Ha... yeah... so funny...":
                    $ toriel_tl_date01_laughitoff = True
                    show toriel smallsmile with Dissolve(.25)
                    toriel "I'm glad we had this talk."
                    jump date_retry
                "Gosh, I don’t know. Why would someone ever want to date such a kind and experienced lady?":
                    $ toriel_dp +=4
                    show toriel blushing with Dissolve(.25)
                    toriel "I do not know. Will you tell me?"
                    menu:
                        "Only if you agree to go on a date with me.":
                            $ toriel_dp +=2
                            show toriel laughing with Dissolve(.25)
                            toriel "If I have no other choice..."
                            toriel "Alright, I suppose there would be no harm in going on one date."
                            jump toriel_date_start
                        "Sorry, can't":
                            $ world.get_monster('Toriel').update_FP(-2)
                            toriel "I do not appreciate being played with."
                            toriel "Perhaps we should just forget about all of this."
                            jump date_retry
        "Maybe some people would agree, but I don't think that.":
            $ toriel_hp += 1
            show toriel normal with Dissolve(.25)
            toriel "Well..."
            toriel "Only if you are really sure about this."
            show toriel smallsmile  with Dissolve(.25)
            toriel "I suppose there would be no harm in going on one date."
            jump toriel_date_start
        "I’m not doing anything. What are you talking about, you crazy old goat?":
            $ world.get_monster('Toriel').update_FP(-3)
            $ toriel_tl_date01_crazyoldgoat = True
            show toriel angry with Dissolve(.25)
            toriel "Well, in that case, I guess there is nothing to talk about."
            jump date_retry
            

#activated next time Toriel is clicked on, add to menu
label date_retry:
    "About earlier... I actually do want to date you."
    show toriel awkward with Dissolve(.25)
    toriel "You could have just said so, dear."
    menu:
        "I... uh... panicked?":
            $ toriel_dp -=1
            toriel "I admit, I was being rather confrontational."
            toriel "Though, I must say, a date does sound nice."
            menu:
                "Yeah, I think so, too.":
                    $ toriel_dp +=2
                    show toriel blushing with Dissolve(.25)
                    toriel "It is a date, then."
                    jump toriel_date_start
                "Yup, you were pretty rude!":
                    $ world.get_monster('Toriel').update_FP(-4)
                    show toriel angry with Dissolve(.25)
                    toriel "Well, I am sorry to have been an annoyance!"
                    toriel "I am going to forget any of this ever happened, and I suggest you do the same."
                    jump bad_end
        "You could say that I was just being baa-shful.":
            $ world.get_monster('Toriel').update_FP(+4)
            show toriel laughing with Dissolve(.25)
            toriel "That is a sheep pun, dear."
            menu:
                "Then wool ewe go on a date with me?":
                    $ toriel_dp +=2
                    show toriel laughing with Dissolve(.25)
                    toriel "Yes, I believe I wool! You have won me over through shear determination."
                    jump toriel_date_start
                "Should I have used a goat pun?":
                    $ toriel_dp -=1
                    show toriel smallsmile with Dissolve(.25)
                    toriel "No, no. It is quite alright, dear."
                    toriel "And yes, I would like to have a date with you."
                    jump toriel_date_start
        "I didn't mean to insult you. Sorry." if toriel_tl_date01_laughitoff == False:
            $ world.get_monster('Toriel').update_FP(1)
            show toriel normal with Dissolve(.25)
            toriel "You should be more careful with your words."
            show toriel smallsmile with Dissolve(.25)
            toriel "But... Apology accepted."
            menu:
                "Thank you. Then… can I dare to ask you on a date again?":
                    $toriel_dp +=1
                    show toriel blushing with Dissolve(.25)
                    toriel "I do not know, {i}can{/i} you?"
                    menu:
                        "Sigh":
                            show toriel smallsmile with Dissolve(.25)
                            toriel "Let us have a date then."
                            jump toriel_date_start
                        "{i}May{/i} I dare to ask you on a date again?":
                            $toriel_dp +=2
                            show toriel smallsmile with Dissolve(.25)
                            toriel "Why, of course you may, my dear!"
                            toriel "I may even say yes."
                            jump toriel_date_start
                        "You're awful.":
                            $world.get_monster('Toriel').update_FP(2)
                            show toriel laughing with Dissolve(.25)
                            toriel "Why, thank you, dear."
                            toriel "And to answer your question, yes. I would like to go on a date with you."
                            jump toriel_date_start
                "I'm glad; I wouldn't want us to be on bad terms.":
                    $world.get_monster('Toriel').update_FP(2)
                    toriel "Oh, do not worry about that. I know you did not intend any harm, dear."
                    toriel "Perhaps we should put all of this behind us."
                    jump bad_end
        "I like crazy ol' goat ladies." if toriel_tl_date01_crazyoldgoat == True:
            show toriel blushing with Dissolve(.25)
            toriel "I... um..."
            menu:
                "I'm serious.":
                    $toriel_dp +=3
                    show toriel smallsmile with Dissolve(.25)
                    toriel "...Oh."
                    toriel "Well, I suppose there would be no harm in going on a date."
                    jump toriel_date_start
                "And you're the craziest of all the goat ladies I know.":
                    $toriel_dp +=2
                    show toriel laughing with Dissolve(.25)
                    toriel "I am the only 'goat lady' you know!"
                    toriel "Well then, are you sure you want to accompany this ‘crazy goat lady’?"
                    menu:
                        "Yes":
                            $toriel_dp +=1
                            show toriel smile with Dissolve(.25)
                            toriel "It is a date, then."
                            jump toriel_date_start
                        "No":
                            $world.get_monster('Toriel').update_FP(-4)
                            show toriel angry with Dissolve(.25)
                            toriel "Are you serious?"
                            toriel "I am not a toy for your amusement, to be played with as you please."
                            toriel "I am going to forget any of this ever happened, and I suggest you do the same."
                            jump bad_end
                "I mean, you did leave me to wander and underground cave full of monsters.":
                    show toriel annoyed with Dissolve(.25)
                    toriel "A cave full of monsters who will not harm you. Because I had to tend to an emergency."
                    menu:
                        "You can't know that they won't harm me.":
                            $world.get_monster('Toriel').update_FP(-2)
                            toriel "Monsters are peaceful creatures, and they will no longer harm anyone. Do not judge them like this."
                            menu:
                                "They will {i}‘no longer’{/i} harm anyone? What’s that supposed to mean?":
                                    $world.get_monster('Toriel').update_FP(-4)
                                    show toriel awkward with Dissolve(.25)
                                    toriel "Well, in the past, monsters {i}were{/i} known to sometimes- Look, it does not matter anymore. Please do not speak of this from now on."
                                    toriel "And… I suppose a date is out of the question now. I do not think this would work."
                                    toriel "Please do not ask again."
                                    jump bad_end
                                "Okay, I guess.":
                                    toriel "I am glad you understand."
                                    show toriel awkward with Dissolve(.25)
                                    toriel "But I believe this has proven that a date is out of the question. I do not think this would work."
                                    toriel "Please do not ask again."
                                    jump bad_end
                        "You could've just taken me with you.":
                            toriel "Perhaps I could have. It does not matter now."
                            toriel "Either way, I do not think that we should go on any sort of date."
                            toriel "Please do not ask again."
                            jump bad_end
                        "Alright then, if you say so. I trust you.":
                            $toriel_dp +=1
                            show toriel normal with Dissolve(.25)
                            toriel "Oh. Well... Thank you."
                            toriel "Anyway... Did you say that you wanted to go on a date?"
                            menu:
                                "Yes.":
                                    $toriel_dp +=1
                                    show toriel smallsmile with Dissolve(.25)
                                    toriel "In that case, it is a date."
                                    jump toriel_date_start
                                "No.":
                                    $world.get_monster('Toriel').update_FP(-4)
                                    show toriel angry with Dissolve(.25)
                                    toriel "Are you serious?"
                                    toriel "I am not a toy for your amusement, to be played with as you please."
                                    toriel "I am going to forget any of this ever happened, and I suggest you do the same."
                                    jump bad_end
                "Frisk must've gotten it from you.": #if max undernsail in meeting frisk
                    show toriel awkward with Dissolve(.25)
                    toriel "Oh, um..."
                    toriel "I believe I remember you saying you want to go on a date?"
                    menu:
                        "Yes.":
                            $toriel_dp +=1
                            show toriel smallsmile with Dissolve(.25)
                            toriel "In that case, it is a date."
                            jump toriel_date_start
                        "No.":
                            $world.get_monster('Toriel').update_FP(-4)
                            show toriel angry with Dissolve(.25)
                            toriel "Are you serious?"
                            toriel "I am not a toy for your amusement, to be played with as you please."
                            toriel "I am going to forget any of this ever happened, and I suggest you do the same."
                            jump bad_end
        "You're kinda hard to argue with." if toriel_tl_date01_laughitoff == True:
            show toriel sad with Dissolve(.25)
            toriel "Well, I do not mean to come across as someone you cannot talk to."
            menu:
                "Either way, you do.":
                    $world.get_monster('Toriel').update_FP(-4)
                    show toriel annoyed with Dissolve(.25)
                    toriel "I guess it is a good thing we never decided to go on a date, then."
                    toriel "Please do not ask me again."
                    jump bad_end
                "Maybe next time, try being a bit less… forceful.":
                    $toriel_dp -=2
                    show toriel annoyed with Dissolve(.25)
                    toriel "I will take that into consideration."
                    toriel "I am glad we had this talk."
                    jump bad_end
                "It’s not your fault. I just didn’t want to offend you.":
                    $toriel_dp +=2
                    show toriel laughing with Dissolve(.25)
                    toriel "Oh, in that case, I guess I am not sorry. So, you mentioned a date?"
                    menu:
                        "I did.":
                            $toriel_dp +=1
                            show toriel smile with Dissolve(.25)
                            toriel "It sounds like a good idea. I would be happy to go out with you."
                            jump toriel_date_start
                        "Never mind.":
                            show toriel normal with Dissolve(.25)
                            toriel "Well then, I will see you later, dear."
                            jump bad_end
    return

# 'q' stands for question. So, q_start = questions start, etc.
label toriel_date_start:
    #scene change ruins overlook
    show toriel normal with Dissolve(.25)
    toriel "Here we are. What do you think?"
    menu:
        "You look stunning.":
            $toriel_tl_date01_stunning = True
            $toriel_dp +=5
            show toriel blushing with Dissolve(.25)
            toriel "Oh! Well... Thank you, dear."
            jump q_start
        "What's cooking, good looking?":
            $toriel_dp +=2
            $world.get_monster('Toriel').update_FP(3)
            show toriel laughing with Dissolve(.25)
            toriel "Nothing much, honey bunch."
            jump q_start
        "All of this, just for me?":
            $toriel_hp +=2
            show toriel smile with Dissolve(.25)
            toriel "Well, you are the first to ask me out like this in quite a while, my dear."
            jump q_start
        "...":
            show toriel smile with Dissolve(.25)
            toriel "Speechless? I would not blame you… It is a beautiful view."
            toriel "This place is rather out of the way, and not many people come here."
            toriel "I thought a quiet place could be nice."
            menu:
                "Seems like you know this place well.":
                    show toriel sad with Dissolve(.25)
                    toriel "I lived here once, a lifetime ago. At the time, there was not much I could do in my free time other than explore. You could say I know every secret this place has to hide, even some the other residents do not."
                    menu:
                        "That's sad.":
                            show toriel normal with Dissolve(.25)
                            toriel "It is what it is."
                            toriel "But enough about me."
                            toriel "Umm... What is your favorite color?"
                            jump q_favcolor
                        "Did you not have people you could talk to?":
                            toriel "Some more than others."
                            toriel "But there is only so much you can talk about with someone before you both start to repeat yourselves and go stir crazy."
                            show toriel smallsmile with Dissolve(.25)
                            toriel "Speaking of, I want to get to know you, as well."
                            toriel "So..."
                            toriel "What is your favorite color?"
                            jump q_favcolor
                        "Seems like you made the best of what you had.":
                            $world.get_monster('Toriel').update_FP(2)
                            show toriel smallsmile with Dissolve(.25)
                            toriel "Hardly. There are many things I would go back and change if I could."
                            show toriel awkward with Dissolve(.25)
                            toriel "But..."
                            toriel "Things turned out the best way they could, I would say. So there are not many things I should regret."
                            toriel "Does that make sense?"
                            menu:
                                "It’s natural to want to change bad things that happened.":
                                    show toriel laughing with Dissolve(.25)
                                    toriel "Advice I have given many times over the years, yet I still have no idea how to follow it, myself."
                                    menu:
                                        "Trust your git feeling.":
                                            $toriel_dp +=3
                                            show toriel smallsmile with Dissolve(.25)
                                            toriel "In the end it is all we can do."
                                            toriel "Oh! I rambled for so long that you have had no chance to talk!"
                                            toriel "Tell me about yourself. What is your favorite color?"
                                            jump q_favcolor
                                        "You should listen to others' advice.":
                                            $toriel_hp +=2
                                            show toriel sad with Dissolve(.25)
                                            toriel "You are right. Others’ experiences can be useful where I am lacking."
                                            show toriel smallsmile with Dissolve(.25)
                                            toriel "But what about you? You have been so quiet about yourself."
                                            toriel "Tell me something... What is your favorite color?"
                                            jump q_favcolor
                                        "Just... trust yourself to learn from the whole experience.":
                                            $toriel_dp +=1
                                            show toriel sad with Dissolve(.25)
                                            toriel "I think that if I could have done so, I already would have."
                                            show toriel smallsmile with Dissolve(.25)
                                            toriel "But let us talk about something happier. This is a date, after all."
                                            toriel "Tell me, what is your favorite color?"
                                            jump q_favcolor
                                        "Don't look at me. I'm just as lost as you are.":
                                            $world.get_monster('Toriel').update_FP(3)
                                            show toriel laughing with Dissolve(.25)
                                            toriel "Then I guess we will both have to wing it. Seems we are two birds of the same feather after all!"
                                            show toriel smile with Dissolve(.25)
                                            toriel "Oh dear, I kept rambling about myself. Now it is your turn to talk. So tell me… What is your favorite color?"
                                            jump q_favcolor
                                "Not at all.":
                                    $toriel_dp -=2
                                    show toriel sad with Dissolve(.25)
                                    toriel "I assumed so."
                                    toriel "So I suppose on these date things people ask each other questions."
                                    show toriel awkward with Dissolve(.25)
                                    toriel "..."
                                    toriel "What is your favorite color?"
                                    jump q_favcolor
                                "I think I get that.":
                                    $toriel_dp +=2
                                    show toriel smallsmile with Dissolve(.25)
                                    toriel "I think everyone has to come to that realization sooner or later, or else they will be forever at war with their past."
                                    show toriel sad with Dissolve(.25)
                                    toriel "I know I was."
                                    show toriel awkward with Dissolve(.25)
                                    toriel "..."
                                    show toriel normal with Dissolve(.25)
                                    toriel "But enough about the past. This is a date after all, and we should get to know each other!"
                                    toriel "Umm... What is your favorite color?"
                                    jump q_favcolor
                                "Sometimes bad things need to happen.":
                                    $toriel_hp +=2
                                    show toriel awkward with Dissolve(.25)
                                    toriel "Well... I suppose you are right. A perfect life is not possible, after all."
                                    show toriel normal with Dissolve(.25)
                                    toriel "Now, let us move away from this depressing subject, shall we?"
                                    toriel "So... Tell me more about yourself. What is your favorite color?"
                                    jump q_favcolor
                "Do you come here a lot?":
                    show toriel sad with Dissolve(.25)
                    toriel "Not as much as I used to."
                    toriel "Now, I only ever come here when I am on my way to get supplies. Or if I am with Frisk."
                    show toriel smile with Dissolve(.25)
                    toriel "For some reason, they really like it here."
                    menu:
                        "It's a gorgeous view.":
                            $world.get_monster('Toriel').update_FP(2)
                            show toriel sad with Dissolve(.25)
                            toriel "It is beautiful in the same way the black tree is."
                            jump q_blacktree
                        "But you {i}used{/i} to come here a lot.":
                            show toriel smile with Dissolve(.25)
                            toriel "My, you are observant."
                            menu:
                                "Thanks, I try.":
                                    $toriel_dp +=2
                                    $world.get_monster('Toriel').update_FP(3)
                                    show toriel laughing with Dissolve(.25)
                                    toriel "Yes, I can tell."
                                    toriel "But enough about me. Let us talk about you. What is your favorite color?"
                                    jump q_favcolor
                                "Tone it down a little, would you?":
                                    $toriel_dp -=2
                                    $world.get_monster('Toriel').update_FP(-1)
                                    show toriel awkward with Dissolve(.25)
                                    toriel "Well, if you do not appreciate this sort of humor, I suppose I will try."
                                    toriel "Let us try something else, then. What is your favorite color?"
                                    jump q_favcolor
                                "Um... yeah. Thanks.":
                                    $toriel_dp -=2
                                    show toriel awkward with Dissolve(.25)
                                    toriel "..."
                                    toriel "Um."
                                    toriel "...You are welcome."
                                    toriel "..."
                                    toriel "So, uh... What is your favorite color?"
                                    jump q_favcolor
                        "So you've moved on?":
                            show toriel awkward with Dissolve(.25)
                            toriel "..."
                            toriel "I would like to think so."
                            toriel "..."
                            show toriel smile with Dissolve(.25)
                            toriel "But enough about the past. This is a date after all."
                            toriel "Tell me about yourself. What is your favorite color?"
                            jump q_favcolor
                        "I saw Frisk here the other day.":
                            show toriel awkward with Dissolve(.25)
                            toriel "Yes, they seem... oddly attached to this area. I do not quite understand their fascination with it."
                            menu:
                                "Maybe they think it's beautiful... just like you.":
                                    $toriel_dp +=3
                                    show toriel laughing with Dissolve(.25)
                                    toriel "I doubt they think that, but I appreciate the sentiment."
                                    show toriel normal with Dissolve(.25)
                                    toriel "Now, I doubt Frisk would appreciate us gossiping about them. Let us move on to a different topic, shall we?"
                                    toriel "What is your favorite color?"
                                    jump q_favcolor
                                "Did you ever ask them?":
                                    toriel "I did, once. But they did not answer me, and they had this strange look on their face..."
                                    show toriel normal with Dissolve(.25)
                                    toriel "Oh, never mind that. We should not gossip about them, anyway."
                                    toriel "So, tell me... What is your favorite color?"
                                    jump q_favcolor
                                "Have you noticed that they act... off, sometimes?": #if frisk_event1_complete == True
                                    toriel "I... do know what you are talking about. But that is not your concern."
                                    show toriel smallsmile with Dissolve(.25)
                                    toriel "This is a date, after all. We should be getting to know each other."
                                    toriel "Say, uh... What is your favorite color?"
                                    jump q_favcolor
                "Did you want to come here so we could get away from Frisk and have a more... adult conversation?":
                    $toriel_dp +=2
                    show toriel blushing with Dissolve(.25)
                    toriel "You are practically reading my mind."
                    toriel "Would you like it if we went back to my place..."
                    show toriel smile with Dissolve(.25)
                    toriel "...And did the taxes?"
                    menu:
                        "What? Oh, no, I meant... uh... Never mind.":
                            $toriel_dp -=2
                            toriel "I know what you meant, dear; I am just teasing."
                            toriel "Well, let us forget about the 'adult talk' for now and get back to our date."
                            toriel "Um... What is your favorite color?"
                            jump q_favcolor
                        "Hey now, don’t you think it’s too early in our relationship for something like that?":
                            $toriel_dp +=2
                            $world.get_monster('Toriel').update_FP(3)
                            show toriel laughing with Dissolve(.25)
                            toriel "Are you suggesting we save the {i}adult stuff{/i} for later?"
                            menu:
                                "Yeah. Don’t want to rush into things, you know?":
                                    $toriel_dp +=1
                                    show toriel smile with Dissolve(.25)
                                    toriel "Maybe you are right. Let us leave the taxes for later in our relationship."
                                    toriel "So, tell me about yourself. What is your favorite color?"
                                    jump q_favcolor
                                "Well... Maybe if you're {i}sure{/i} about it...":
                                    show toriel normal with Dissolve(.25)
                                    toriel "Oh, no, I do not want to do anything you are uncomfortable with."
                                    toriel "Let us move on from this, then."
                                    toriel "So, tell me about yourself. What is your favorite color?"
                                    jump q_favcolor
                                "Depends on the kind of adult stuff you’re suggesting.":
                                    show toriel blushing with Dissolve(.25)
                                    toriel "Ha! Well, this might be a conversation best saved for another time, and not on the first date."
                                    show toriel awkward with Dissolve(.25)
                                    toriel "So... um... Tell me about yourself. What is your favorite color?"
                                    jump q_favcolor
                        "How about we take it a step further and balance the checkbooks?":
                            $toriel_dp +=4
                            toriel "Oh dear, are you sure you want to go to that level already?"
                            menu:
                                "Only if you want to.":
                                    $toriel_dp +=1
                                    show toriel smile with Dissolve(.25)
                                    toriel "Hm... Let us save something like this for a later point in our relationship. We do not want to rush into things, after all."
                                    toriel "So, tell me about yourself. What is your favorite color?"
                                    jump q_favcolor
                                "There's nothing I like more than crunching numbers.":
                                    $toriel_dp +=3
                                    toriel "I hate to break this to you, but you seem like a very boring person."
                                    menu:
                                        "Says the one who wants to do taxes.":
                                            $toriel_dp +=1
                                            show toriel smile with Dissolve(.25)
                                            toriel "I guess you have a point. We seem to be equally boring, then, do we not?"
                                            toriel "So, on that note, tell me about yourself. What is your favorite color?"
                                            jump q_favcolor
                                        "What can I say? I just love adult talk.":
                                            $toriel_dp +=3
                                            toriel "I can tell."
                                            show toriel smile with Dissolve(.25)
                                            toriel "Well, I regret to inform you that I have had enough of this ‘adult talk’."
                                            toriel "Instead, how about you tell me something about yourself? Like... What is your favorite color?"
                                            jump q_favcolor
                                "Well... Maybe not.":
                                    show toriel smile with Dissolve(.25)
                                    toriel "That is fine. I do not want you rushing into things you are not prepared for."
                                    toriel "Now, how about we get away from this 'adult talk'?"
                                    toriel "Tell me something about yourself... What is your favorite color?"
                                    jump q_favcolor
                "Good thinking.":
                    $toriel_dp -=1
                    show toriel awkward with Dissolve(.25)
                    toriel "Yes, it is."
                    toriel "..."
                    toriel "So I suppose, as is customary on dates, we should ask each other questions."
                    toriel "..."
                    toriel "What is your favorite color?"
                    jump q_favcolor

label q_blacktree:
    menu:
        "The black tree?" if toriel_tl_date01_q_blacktree == False:
            $ toriel_tl_date01_q_blacktree = True
            toriel "The tree in front of our house. It was planted before we explored the rest of the caverns."
            toriel "Its leaves always fall before they can grow to full size."
            toriel "I cannot look at it without being reminded of..."
            toriel "..."
            jump q_blacktree
        "There is a certain beauty to preserving what would otherwise be long gone.":
            $toriel_dp -=3
            show toriel annoyed with Dissolve(.25)
            toriel "I think you will find that some things are not worth preserving, whether they be items or... other things."
            show toriel normal with Dissolve(.25)
            toriel "But enough about that. This is a date after all, so let us talk about something else."
            toriel "Tell me... What is your favorite color?"
            jump q_favcolor
        "Bad memories, huh?":
            toriel "I have many bad memories, as I am sure we all do. However, let us not dwell on that for now. This is not the occasion."
            show toriel normal with Dissolve(.25)
            toriel "Let us talk about something happier. Tell me... What is your favorite color?"
            jump q_favcolor

label q_start:         #Selection 30
    menu:
        "How are you?":
            $world.get_monster('Toriel').update_FP(2)
            show toriel normal with Dissolve(.25)
            toriel "I am doing very well, thank you."
            toriel "Although I have to admit, I have not exactly gone on a date in a while, so I am sorry if I make a mistake."
            menu:
                "You can't exactly date a person the wrong way.":
                    $toriel_dp +=3
                    show toriel smile with Dissolve(.25)
                    toriel "Thank you for your vote of confidence."
                    show toriel normal with Dissolve(.25)
                    toriel "You know, it really has been a long time. There are a few monsters here and there, but most of them struggle to carry on a conversation so I have been mostly alone."
                    toriel "..."
                    show toriel smile with Dissolve(.25)
                    toriel "And then Frisk came along."
                    toriel "And now you, too."
                    toriel "I truly am glad to have someone to talk to."
                    toriel "So... Would you like to hear a joke?"
                "Don't worry, I'll show you how it's done.":
                    $toriel_hp +=1
                    show toriel awkward with Dissolve(.25)
                    toriel "Oh..."
                    show toriel laughing with Dissolve(.25)
                    toriel "Well, that is a relief."
                    toriel "However, to be honest, I am not sure where we should begin."
                    show toriel smile with Dissolve(.25)
                    toriel "Oh, wait! I know!"
        "So... Come here often?":
            show toriel awkward with Dissolve(.25)
            toriel "The way you said that..."
            toriel "It sounds like you were making a joke, but I do not quite get it..."
            show toriel normal with Dissolve(.25)
            toriel "Oh, I think I have one..."
        "If you were a fruit, you'd be a fineapple.":
            $ toriel_tl_date01_fineapple = True
            $toriel_dp +=2
            $world.get_monster('Toriel').update_FP(3)
            show toriel smile with Dissolve(.25)
            toriel "Very funny!"
            toriel "However, I think I have a joke for you as well..."
    
    show toriel smile with Dissolve(.25)
    toriel "What do you call a belt made of watches?"
    menu:
        "What?":
            $world.get_monster('Toriel').update_FP(1)
            toriel "A waist of time!"
        "...":
            $toriel_dp -=1
            $toriel_hp +=2
            toriel "A waist of time!"
            show toriel awkward with Dissolve(.25)
            toriel "..."
            toriel "...A waist of time."
        "A monstrosity?":
            $toriel_dp +=1
            show toriel laughing with Dissolve(.25)
            toriel "Not quite!"
            toriel "...It’s a waist of time!"
    #answer
    menu:
        "I see what you did there.":
            $world.get_monster('Toriel').update_FP(2)
            show toriel smile with Dissolve(.25)
            toriel "Thank you. I am glad I found another person that appreciates puns."
            menu:
                "Another person?":
                    toriel "Yes. You see, sometimes I talk with someone from outside the Ruins."
                    toriel "We have never actually met in person, because I keep the door shut, but we can both hear each other."
                    toriel "He is very nice. He enjoys puns as much as I do, it seems."
                    menu:
                        "Gasp... Toriel... Are you cheating on me?!":
                            $toriel_dp +=1
                            show toriel blushing with Dissolve(.25)
                            toriel "What? We are not..."
                            show toriel surprised with Dissolve(.25)
                            toriel "Oh!"
                            show toriel smile with Dissolve(.25)
                            toriel "I see you, too, are adept at the art of telling jokes."
                            toriel "I may have to step up my game."
                            toriel "Instead of telling jokes, perhaps we should move on. After all, I believe we are supposed to be getting to know each other better."
                            toriel "So…"
                            show toriel awkward with Dissolve(.25)
                            toriel "..."
                            toriel "What is your favorite color?"
                            jump q_favcolor
                        "Are you two involved in any way?":
                            show toriel blushing with Dissolve(.25)
                            toriel "If you mean romantically, oh heavens, no."
                            toriel "We are just friends."
                            menu:
                                "If you don’t mind me saying... I hope it stays that way.":
                                    $toriel_dp +=3
                                    show toriel smile with Dissolve(.25)
                                    toriel "Oh, stop it, you."
                                    toriel "But enough about him. This is our date, after all... We should be getting to know each other better."
                                    toriel "So…"
                                    show toriel awkward with Dissolve(.25)
                                    toriel "..."
                                    toriel "What is your favorite color?"
                                    jump q_favcolor
                                "Maybe you should consider not talking to strangers. Someone might want to take advantage of you.":
                                    $toriel_hp +=4
                                    show toriel sad with Dissolve(.25)
                                    toriel "Do you really think so?"
                                    toriel "..."
                                    toriel "Thank you for the advice. We shall see..."
                                    show toriel smallsmile with Dissolve(.25)
                                    toriel "So…"
                                    show toriel awkward with Dissolve(.25)
                                    toriel "..."
                                    toriel "What is your favorite color?"
                                    jump q_favcolor
                                "Sorry, I was just curious.":
                                    $world.get_monster('Toriel').update_FP(2)
                                    #show toriel smallsmile
                                    toriel "Oh, that is fine. Thank you for understanding."
                                    toriel "But enough about him. This is our date, after all... We should be getting to know each other better."
                                    toriel "So…"
                                    show toriel awkward
                                    toriel "..."
                                    toriel "What is your favorite color?"
                                    jump q_favcolor
                        "He sounds like a nice person.":
                            $world.get_monster('Toriel').update_FP(1)
                            show toriel smile with Dissolve(.25)
                            toriel "Yes, he is! It is great that you think so."
                            toriel "But enough about him. This is our date, after all... We should be getting to know each other better."
                            toriel "So…"
                            show toriel awkward with Dissolve(.25)
                            toriel "..."
                            toriel "What is your favorite color?"
                            jump q_favcolor
                "...":
                    toriel "..."
                    toriel "Instead of telling jokes, perhaps we should move on. After all, I believe we are supposed to be getting to know each other better."
                    toriel "So..."
                    show toriel awkward with Dissolve(.25)
                    toriel "..."
                    toriel "What is your favorite color?"
                    jump q_favcolor
        "I don't get it.":
            $toriel_dp -=1
            show toriel normal
            toriel "Well, because a belt is worn around the waist, and..."
            show toriel smallsmile with Dissolve(.25)
            toriel "Oh, never mind."
            toriel "Instead of telling jokes, perhaps we should move on. After all, I believe we are supposed to be getting to know each other better."
            toriel "So..."
            show toriel awkward with Dissolve(.25)
            toriel "..."
            toriel "What is your favorite color?"
            jump q_favcolor
            
        "Ha, I know you have better ones than that, Tori.":
            $toriel_hp +=1
            show toriel awkward with Dissolve(.25)
            toriel "Oh... Perhaps you are right."
            toriel "Do not worry. I will come up with something better."
            show toriel normal with Dissolve(.25)
            toriel "But, in the meantime... I do believe we are supposed to be getting to know each other."
            show toriel awkward with Dissolve(.25)
            toriel "..."
            toriel "What is your favorite color?"
            jump q_favcolor
    
    
label q_favcolor:      #Selection 37
    if toriel_tl_date01_favcolor_picked == False:
        call favcolor_1
    menu:
        "What's {i}your{/i} favorite color?":
            $toriel_dp +=1
            show toriel smile with Dissolve(.25)
            toriel "I am particularly fond of green, believe it or not. Grass is not something commonly found in the Ruins."
            menu:
                "Well, there’s some grass at the place I landed. Why don’t you just go there?":
                    toriel "I go there sometimes to take care of the flowers, and to see if anyone has fallen."
                    show toriel awkward with Dissolve(.25)
                    toriel "Not... because of the grass."                    
                "That's... actually pretty sad.":
                    toriel "Oh, I have learned to live with it. You will find that most monsters here do not even remember grass. So, in a way, I am lucky."
                "Hey, we have the same favorite color!" if toriel_tl_date01_favcolor_green == True:
                    $toriel_dp +=3
                    show toriel laughing with Dissolve(.25)
                    toriel "Indeed, we do! It is a good color."
        "I’ve been wondering... How long have you been taking care of Frisk?":
            show toriel normal with Dissolve(.25)
            toriel "Oh, you know, a few years. Ever since they fell down."
            menu:
                "Do you know why they fell down?":
                    show toriel sad with Dissolve(.25)
                    toriel "No, I actually do not know. And honestly, I am not sure if I even want to."
                "They must really like this place, then.":
                    $world.get_monster('Toriel').update_FP(2)
                    show toriel smallsmile with Dissolve(.25)
                    toriel "I hope so. It can get very lonely. But Frisk is handling that problem in their own way, I believe."
                "Don't you think it's bad keeoing them cooped up in here?":
                    $toriel_hb +=1
                    show toriel awkward with Dissolve(.25)
                    toriel "Well... Maybe. I have been smothering them a bit, have I not? Perhaps I should be a bit more lenient. I just do not want them to be harmed."
                    menu:
                        "I understand. You should do what you think is right.":
                            $toriel_dp +=2
                            show toriel smallsmile with Dissolve(.25)
                            toriel "Thank you. You are very kind."
                        "If you ever want advice, feel free to come to me.":
                            $toriel_hp +=1
                            $toriel_dp +=1
                            show toriel smallsmile with Dissolve(.25)
                            toriel "That is very kind of you. I am certain I will."
                        "You should really get this figured out.":
                            $dp -=2
                            toriel "I am aware..."
        "Hey, is it hot in here, or is it just you?":
            $toriel_dp +=3
            show toriel laughing with Dissolve(.25)
            toriel "I confess, it must be me. Do not worry, this happens quite often in my presence."
    
    show toriel normal with Dissolve(.25)
    toriel "Anyway, I have been meaning to ask... How long do you plan to stay in the Ruins?"
    menu:
        "As long as you plan to stay here.":
            $toriel_dp +=5
            show toriel blushing with Dissolve(.25)
            toriel "Ah, well... You might be staying a while, then."
            menu:
                "That's fine with me.":
                    $toriel_dp +=3
                    show toriel smile with Dissolve(.25)
                    toriel "That is very reassuring to hear, thank you."
                "Don't worry, , I’m sure I’ll be able to get you out of your shell at some point.":
                    $toriel_dp -=2
                    show toriel awkward with Dissolve(.25)
                    toriel "Ha, yes. Right."
        "As long as I feel like it.":
            $toriel_dp -=2
            toriel "Oh... Well, hopefully you will not leave soon, then."
            menu:
                "Probably not.":
                    toriel "That is good. If you left, you would be missed."
                "Don't count on it.":
                    $world.get_monster('Toriel').update_FP(-3)
                    $toriel_dp -=3
                    show toriel annoyed with Dissolve(.25)
                    toriel "Why did you ask me out on this date, then? Is this just a game to you?"
                    menu:
                        "You have no idea.":
                            $world.get_monster('Toriel').update_FP(-2)
                            show toriel angry with Dissolve(.25)
                            toriel "Then enlighten me, dear."
                            menu:
                                "You know what, never mind.":
                                    $world.get_monster('Toriel').update_FP(-3)
                                    toriel "Alright, I see how it is then. I am starting to think that perhaps we should not have gone on this date."
                                    jump date_goodbye
                                "It doesn't matter.":
                                    $world.get_monster('Toriel').update_FP(-3)
                                    toriel "Maybe to you it does not. However, I am starting to think that perhaps we should not have gone on this date."
                                    jump date_goodbye
                                "...":
                                    $world.get_monster('Toriel').update_FP(-3)
                                    toriel "You know what, I am starting to think that we should not have gone on this date in the first place."
                                    jump date_goodbye
                        "No, you have to understand. I just don’t like being cooped up in one place.":
                            $world.get_monster('Toriel').update_FP(-1)
                            $toriel_dp -=2
                            show toriel angry with Dissolve(.25)
                            toriel "You know what? I do not understand."
                            menu:
                                "Well, if you made the slightest effort, maybe you could.":
                                    $world.get_monster('Toriel').update_FP(-5)
                                    toriel "Do not {i}dare{/i} make assumptions about me. You know, maybe we should not have gone on this date."
                                    jump date_goodbye
                                "Okay, okay, geez. Calm down.":
                                    $world.get_monster('Toriel').update_FP(-3)
                                    toriel "Oh, trust me, I {i}am{/i} calm. But perhaps we should end this date before it escalates."
                                    jump date_goodbye
                        "Hey, relax. This is just for fun, right?":
                            $toriel_dp -=4
                            show toriel angry with Dissolve(.25)
                            toriel "Maybe to {i}you{/i} it is, but we clearly went into this with different expectations."
                            menu:
                                "You know, you don’t have to be so rude.":
                                    $world.get_monster('Toriel').update_FP(-5)
                                    toriel "Oh, {i}I{/i} am the one being rude? Look... We probably should not have gone on this date in the first place."
                                    jump date_goodbye
                                "What, you thought this was serious?":
                                    $world.get_monster('Toriel').update_FP(-5)
                                    toriel "Yes, because- because I had faith that you were not going to try to {i}humiliate{/i} me. Let us just end the date now, alright?"
                                    jump date_goodbye
                                "Hey, calm down.":
                                    $world.get_monster('Toriel').update_FP(-3)
                                    toriel "Oh, trust me, I {i}am{/i} calm. But perhaps we should end this date before it escalates."
                                    jump date_goodbye
                        "Sorry, I just meant that I will want to explore outside the Ruins a bit.":
                            show toriel awkward with Dissolve(.25)
                            toriel "Is that all? I am sorry for overreacting, then. It is my mistake."
        "What, you don't want me around?":
            $toriel_hp +=2
            show toriel surprised with Dissolve(.25)
            toriel "No, it is not that! You are very welcome here. I am just... curious."
            menu:
                "Ha, good. I’m not about to let you go anytime soon.":
                    $toriel_hp +=1
                    show toriel awkward with Dissolve(.25)
                    toriel "That, uh, might go two ways, I suppose."
                "Alright, I was scared for a minute.":
                    $toriel_dp +=1
                    show toriel laughing with Dissolve(.25)
                    toriel "Well, I am sorry to scare you, then. You are welcome in my house as long as you like."
                "Are you sure? If you don’t want me here, just say so.":
                    $world.get_monster('Toriel').update_FP(-2)
                    show toriel blushing with Dissolve(.25)
                    toriel "No, no, of course I want you here! Please do not think otherwise. I would never throw you out."
                    
    show toriel awkward with Dissolve(.25)
    toriel "..."
    show toriel smallsmile with Dissolve(.25)
    toriel "Oh, right, I was wondering... You and Frisk have still been getting along well, yes?"
    menu:
        "Yeah, we’re good friends.":
            $toriel_dp +=2
            show toriel smile with Dissolve(.25)
            toriel "Yes, that is what they have been telling me! I am glad about that, I am glad to hear that. It is good that you keep each other from being lonely."
        "I just let them think we're close.":
            $toriel_dp -=3
            show toriel annoyed with Dissolve(.25)
            toriel "...Well. That is a bit rude, do you not think?"
            menu:
                "Why? They're just a kid.":
                    $toriel_dp -=3
                    toriel "Listen, {i}dear{/i}, they are not some... some inanimate doll for you to play around with."
                    menu:
                        "I didn't think they were.":
                            toriel "Maybe you should act like it, then."
                        "Well, what do you know about kids?":
                            $toriel_dp -=4
                            $world.get_monster('Toriel').update_FP(-4)
                            show toriel angry with Dissolve(.25)
                            toriel "Certainly more than {i}you{/i}."
                            menu:
                                "You know, you don’t have to be so rude.":
                                    $world.get_monster('Toriel').update_FP(-4)
                                    toriel "Oh, {i}I{/i} am the one being rude? Look... We probably should not have gone on this date in the first place."
                                    jump date_goodbye
                                "Hey, calm down.":
                                    $world.get_monster('Toriel').update_FP(-5)
                                    toriel "Oh, trust me, I {i}am{/i} calm. But perhaps we should end this date before it escalates."
                                    jump date_goodbye
                                "...":
                                    toriel "You know what, I am starting to think that we should not have gone on this date in the first place."
                                    jump date_goodbye
                        "...":
                            toriel "What, nothing to say for yourself? Luckily for you, I will take this to mean that you see your mistake."
                "...":
                    toriel "What, nothing to say for yourself? Luckily for you, I will take this to mean that you see your mistake."
                "They’re happy, right? Why does it matter?":
                    $toriel_dp -=3
                    $world.get_monster('Toriel').update_FP(-2)
                    show toriel angry with Dissolve(.25)
                    toriel "It {i}matters{/i} because you do not have the right to treat people like objects to manipulate."
                    menu:
                        "Look, you’re taking this way too seriously.":
                            $world.get_monster('Toriel').update_FP(-4)
                            toriel "Or perhaps you are not taking this seriously {i}enough{/i}. If you are going to be like this, then I think we might have to forget about dating, alright?"
                            jump date_goodbye
                        "Hey, calm down.":
                            $world.get_monster('Toriel').update_FP(-5)
                            toriel "Oh, trust me, I {i}am{/i} calm. But perhaps we should end this date before it escalates."
                            jump date_goodbye
                        "...":
                            toriel "You know what, I am starting to think that we should not have gone on this date in the first place."
                            jump date_goodbye
    
    show toriel normal with Dissolve(.25)
    toriel "Oh dear, it is getting a bit late..."
    menu:
        "Should we end our date then?":
            show toriel smile with Dissolve(.25)
            toriel "Yes, maybe we should!"
            jump date_end
        "I'm sure we can stay up longer.":
            toriel "Ah, well, I would rather not leave Frisk alone for too long, so I am afraid I must take my leave soon."
            jump date_end
        "It {i}is{/i} getting rather late, isn't it?":
            toriel "Yes, it is. I am afraid we have to finish this up soon."
            jump date_end
            
            
            
label favcolor_1:
    if toriel_tl_date01_favcolor_picked == False:
        menu:
            "The color of your eyes.":
                $toriel_dp +=4
                if (toriel_tl_date01_stunning == True and toriel_tl_date01_fineapple == True):
                    show toriel awkward with Dissolve(.25)
                    toriel "Um. Thank you, again? You seem to be very fond of these compliments."
                else:
                    show toriel blushing
                    toriel "That is very kind of you!"
            "Bastard Amber.":
                show toriel awkward with Dissolve(.25)
                toriel "...Do you not think that is a bit rude?"
                menu:
                    "No, that’s what the color is actually called.":
                        toriel "Well... That is still a rude name to call something."
                    "You’re right. I guess we should just call it Amber.":
                        $world.get_monster('Toriel').update_FP(2)
                        toriel "That is not right. It is special; it should not be lumped with regular amber. That would hurt its feelings."
            "Blue.":
                show toriel smallsmile with Dissolve(.25)
                toriel "Blue is very nice, yes."
            "Fulvous.": 
                show toriel normal with Dissolve(.25)
                toriel "I am... Not quite sure what kind of color that would be, honestly."
            "Green.": 
                $ toriel_tl_date01_favcolor_green = True
                show toriel smallsmile with Dissolve(.25)
                toriel "Green is a wonderful color! I am glad you like it."
            "More options ->":
                jump favcolor_2
        $ toriel_tl_date01_favcolor_picked = True
label favcolor_2:
    if toriel_tl_date01_favcolor_picked == False:
        menu:
            "Magenta.":
                show toriel normal with Dissolve(.25)
                toriel "Honestly, I have always thought of magenta as a stuck-up version of purple."
                show toriel smallsmile with Dissolve(.25)
                toriel "But, if it is your favorite, then perhaps I should reconsider."
            "Orange.": 
                show toriel normal with Dissolve(.25)
                toriel "Ah, orange. The color of oranges."
                toriel "..."
                toriel "That might be obvious, but I am not wrong."
            "Puke.":
                show toriel awkward
                toriel "...Puke? That is your favorite color? Well..."
                show toriel laughing with Dissolve(.25)
                toriel "I will try not to judge."
            "Purple.":
                show toriel normal with Dissolve(.25)
                toriel "Personally, I have gotten a bit tired of seeing purple everywhere."
            "More options <-":
                jump favcolor_1
            "More options ->":
                jump favcolor_3
        $ toriel_tl_date01_favcolor_picked = True
label favcolor_3:
    if toriel_tl_date01_favcolor_picked == False:
        menu:
            "Red.":
                show toriel normal with Dissolve(.25)
                toriel "Ah, yes, the color of... hm. The color of my eyes, actually."
            "Smaragdine.":
                show toriel normal with Dissolve(.25)
                toriel "Are you sure that is a color, dear? It sounds more like a... well, like a misspelling."
            "Wenge.":
                show toriel awkward with Dissolve(.25)
                toriel "Wait, what?"
                toriel "Oh, for a second I thought you said wench- Well, let us agree to forget about this, alright?"
            "Yellow.":
                show toriel normal with Dissolve(.25)
                toriel "Yellow is fine, although not the best for interior decorating."
            "Well, I don’t know about 'favorite' color, but I’m starting to hate purple.":
                $world.get_monster('Toriel').update_FP(2)
                show toriel laughing with Dissolve(.25)
                toriel "What a coincidence. I also hate purple. It is practically the only color I have seen for too many years. I should have packed more clothes."
            "More options <-":
                jump favcolor_2
    $ toriel_tl_date01_favcolor_picked = True



label bad_end:
    $ toriel_tl_route_open = False
    return
    
label date_end:
    if toriel_dp > 75:
        show toriel smile with Dissolve(.25)
        toriel "I believe this has gone quite well!"
        toriel "I- I am- well, I do not want to say surprised, but..."
        toriel "If you want, we could do this again sometime, alright?"
        toriel "And, remember, whatever happens, my home is always open to you."
        toriel "Until next time, dear."
    elif toriel_dp > 50:
        show toriel normal with Dissolve(.25)
        toriel "So, this date has..."
        toriel "Hm."
        toriel "I am not exactly sure how it has gone, honestly."
        toriel "Maybe we could try again and see if it goes better next time?"
        show toriel smile with Dissolve(.25)
        toriel "I will see you later."
    else:
        show toriel normal with Dissolve(.25)
        toriel "So... This date..."
        toriel "I think we can agree it has not gone too well, correct?"
        show toriel laughing with Dissolve(.25)
        toriel "I guess we will not be doing this again. Nothing personal, dear. I just feel that it is best for us to remain friends."
        toriel "I will see you later."
        jump bad_end
    return
    
label date_goodbye:
    show toriel awkward with Dissolve(.25)
    toriel "..."
    show toriel annoyed with Dissolve(.25)
    toriel "Look."
    toriel "I am not particularly interested in spending any more time with you after this, but I will not go so far as to kick you out of my home. On that note, I also do not want all of our time to be spent antagonizing each other."
    show toriel normal with Dissolve(.25)
    toriel "So, perhaps we should start over with a clean slate?"
    toriel "I doubt I will ever agree to date you again, but perhaps, in time, we can go back to being friends."
    toriel "So, with that, I will take my leave. Enjoy the rest of your day."
    $world.get_monster('Toriel').FP =0
    jump bad_end