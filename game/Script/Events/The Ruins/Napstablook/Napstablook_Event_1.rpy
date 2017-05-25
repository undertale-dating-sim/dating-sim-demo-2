label napstablook_event_1:
    #Event Name: Like Karaoke, but Without the Lyrics on the Screen
    #Event Trigger: Returning to Napstablook's room after all rooms in the Ruins have been explored
    #Synopsis: Napstablook offers to let you listen to a new song he made. How will you respond?
    
    stop music
    scene background ruins_blooky_room
    show napstablook normal at napstabob with dissolve
    
    napstablook "oh...... hi. i didn't think you'd come back here...."
    napstablook "i'm glad you did, though....... i mean, i've been working on a new song and i was wondering if..... maybe....... you'd want to listen to it?"
    napstablook "you don't have to, if you don't want......"
    
    menu:
        "Sure, I'd love to!":
            $world.get_monster('Napstablook').update_FP(3)
            napstablook "wow, i didn't think you'd......"
            napstablook "okay, i'll put it on.... just a minute...."
            $ listened_music = True
            napstablook "um...... okay.... this isn't even that good, and it's not done.... i mean, i think it's done, but i always end up changing things later so it's probably not done...."
            napstablook "and... i know it doesn't have lyrics...... and some people don't like that.... but i'm not a very good singer, so...."
            jump blook_hangout_listened_music
            
        "I can't, I'm busy.":
            $world.get_monster('Napstablook').update_FP(-2)
            napstablook "that's okay.... i understand......."
            return
                
    label blook_hangout_listened_music:
        menu:
            "Just turn it on, the anticipation is killing me!":
                $world.get_monster('Napstablook').update_FP(-2)
                napstablook "oh.... okay...... sorry......."
            "I'm sure it's fine.":
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "maybe..... um, i'll turn it on now......."
            "Maybe I could sing along?":
                $world.get_monster('Napstablook').update_FP(3)
                napstablook "o-oh.... uh...."
                show napstablook smallsmile with dissolve
                napstablook "ha.... okay.... if you want...."
                $ issinger = True
        
        play music "audio/home.mp3" ###### NYI- SPOOKTUNES HERE
        
        show napstablook normal with dissolve
        napstablook "so.... this is it......."
        
        menu:
            "I like it!":
                $world.get_monster('Napstablook').update_FP(1)
                $ likedmusic = True
                
                napstablook "really?"
                napstablook "oh....... i wasn't expecting that...."
                napstablook "thank you......"
                jump blook_hangout_likedit
                
            "It's not really my style…":
                $world.get_monster('Napstablook').update_FP(-2)
                napstablook "sorry....... i'll turn it off now...."
                $ dislikedmusic = True
                
            "Dance":
                $world.get_monster('Napstablook').update_FP(3)
                napstablook "what are you... doing?"
                $ isdancer = True
                $ likedmusic = True
                menu:
                    "I'm dancing, obviously!":
                        $world.get_monster('Napstablook').update_FP(1)
                        napstablook "oh... i couldn't tell......"
                        napstablook "oh, um.. don't take that the wrong way... i was trying to be funny.... you're, uh.... a really good dancer..........."
                        jump blook_hangout_obviouslydancing
                
                    "Oh, nothing…": #(+0 FP)
                        "You stop dancing."
                        napstablook "oh... okay......"
                        napstablook "you, uh.... didn't have to stop.."
                        
            "Sing along" if issinger:
                show napstablook smile with dissolve
                $ likedmusic = True
                napstablook "ha...... haha...."
                napstablook "oh, sorry, you have a good voice, it's just.... i guess the song wasn't really meant to have lyrics... "
                napstablook "not that yours aren't.... creative.... haha... "
                
                menu:
                    "Hey, my lyrics are genius! A true masterpiece!":
                        $world.get_monster('Napstablook').update_FP(2)
                        show napstablook smile with dissolve
                        napstablook "ha.... yeah.... definitely......."
                    "Haha… yeah I guess you're right. I shouldn't have ruined your song with my crappy singing.": #(+0 FP)
                        show napstablook sad with dissolve
                        napstablook "oh.... no...... it's okay.... you don't have to stop.... i don't mind......."
                    "You try singing, I bet you can't do better!":
                        $world.get_monster('Napstablook').update_FP(-1)
                        show napstablook normal with dissolve
                        napstablook "oh..... you're right.... i can't...."
                        jump blook_hangout_yousing
        jump end_blook_hangout1
                        
    label blook_hangout_likedit:
        menu:
            "Yeah! You should make an album.":
                $world.get_monster('Napstablook').update_FP(2)
                napstablook "oh..... i don't know.... that sounds kind of daunting......."
                napstablook "but maybe.... i'll think about it......."
            "Have you showed this to anyone else?":
                napstablook "um, no.... just you so far...."
                menu:
                    "That's probably for the best.":
                        $world.get_monster('Napstablook').update_FP(-4)
                        napstablook "oh....... if you say so......."
                    "You should, I bet people would love it!":
                        $world.get_monster('Napstablook').update_FP(2)
                        napstablook "oh....... you think so?"
                        napstablook "maybe.... i could show it to Frisk.... they always like my music, even when it's bad......"
            "It's actually starting to get a little repetitive...":
                $world.get_monster('Napstablook').update_FP(-2)
                napstablook "sorry....... i'll turn it off now...."
                $ likedmusic = False
                $ dislikedmusic = True
        jump end_blook_hangout1
                
    label blook_hangout_obviouslydancing:
        menu:
            "That's okay, I know I suck.":
                $world.get_monster('Napstablook').update_FP(-1)
                napstablook "oh........"
                napstablook "...."
                napstablook "can i ask, um.... why do you do it, then?"
                menu:
                    "Because it's fun… I don't have to be good at something to enjoy it.":
                        $world.get_monster('Napstablook').update_FP(4)
                        napstablook "oh... i see......."
                        napstablook "that's nice.... sounds like a pretty good outlook to have on things......"
                    "Because I like to make people laugh, even if it's at my own expense.":
                        $world.get_monster('Napstablook').update_FP(2)
                        napstablook "that's nice of you.... but you didn't have to do that...."
                        napstablook "oh, no.... and i didn't even laugh.... i'm sorry......."
                    "I don't know… because I can?":
                        $world.get_monster('Napstablook').update_FP(-1)
                        napstablook "oh, um.... okay then......."
            "Damn right I am!":
                $world.get_monster('Napstablook').update_FP(-2)
                napstablook "um....... yeah........"
            "Dance with me?":
                $world.get_monster('Napstablook').update_DP(2)
                show napstablook shyblush with dissolve
                napstablook "oh.... i don't know.... i'm not very good......."
                menu:
                    "That's okay, I'm not either.":
                        $world.get_monster('Napstablook').update_FP(1)
                        show napstablook sad with dissolve
                        napstablook "oh, no.... you're...... okay... "
                    "You don't know until you try!":
                        $world.get_monster('Napstablook').update_FP(-1)
                        show napstablook normal with dissolve
                        napstablook "i have tried, though... that's how i know........"
                show napstablook normal with dissolve
                napstablook "um.... i think i'll pass this time.... sorry....."
        jump end_blook_hangout1

    label blook_hangout_yousing:
        menu:
            "So you're saying I win?":
                $world.get_monster('Napstablook').update_FP(-1)
                napstablook "oh.... yeah, i guess......."
            "C'mon… just try? I promise I won't laugh, or anything.":
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "um... well.... i suppose i could try....."
                "Napstablook starts singing so quietly that you can't even understand them."
                menu:
                    "Come on… belt it out!":
                        $world.get_monster('Napstablook').update_FP(-2)
                        napstablook "um... i'd rather not.... sorry to disappoint you...."
                    "If it makes you uncomfortable, you don't have to.":
                        $world.get_monster('Napstablook').update_FP(2)
                        napstablook "okay.... that's a relief...... thanks........"
                    "That's nice… you should incorporate some vocals into your next song. Maybe we could sing a duet?":
                        $world.get_monster('Napstablook').update_DP(4)
                        show napstablook shyblush with dissolve
                        napstablook "ha... ha... you would really do that?"
                        napstablook "that might be fun....."
        jump end_blook_hangout1

    label end_blook_hangout1:
    #Napstablook is leaving.
        stop music
        show napstablook normal with dissolve
        napstablook "well.... that's all i have...."
        napstablook "i should go now.... thanks for listening........"
        hide napstablook with dissolve
        $ napstablook_friendship_hangout1_complete = True
        return
        