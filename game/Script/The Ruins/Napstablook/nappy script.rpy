# init:
#     define n = Character('Napstablook')
    
#     define seen_set = [ ]
    
#     $ done1 = False
#     while True:
#         if shade_pale = True and from_heaven = True and bandaid = True:
#             done1 = True

#     $ done2 = False
#     while True:
#         if bacon = True and how_are_you = True and you_okay = True:
#             done2 = True

#     $ shade_pale = False
#     $ from_heaven = False
#     $ bandaid = False
#     $ bacon = False
#     $ how_are_you = False
#     $ you_okay = False

# label start:
    
# #when clicking on Napstablook
# n "Oh.. hey.."
# jump choices


# label choices:
#     menu:
#         "Talk":
#             menu:
#                 "Flirt":
#                     jump flirt
                
#                 "Chat":
#                     jump chat
                    
#                 "Go back":
#                     jump choices
                
#         "Gift":
#             n "do you.. have something for me..?"
#             menu:
#                 #give gift menu here
            
#                 "Cancel":
#                     n "that's alright.. i don't expect gifts 
#                     anyway.."
#                     jump choices
                    
#         "Leave":
#             jump leave

# label flirt:
#     menu:
#         set seen_set
        
#         "You're a lovely shade of pale today.":
#             $ shade_pale = True
#             jump shade_pale
            
#         "Did it hurt when you fell from heaven?":
#             $ from_heaven = True
#             jump from_heaven
            
#         "Do you have a bandaid? I scraped my knee falling for you.":
#             $ bandaid = True
#             jump bandaid
            
#         "Go back":
#             jump choices
            
#         "You look like trash, may i take you out?" if done1:
#             jump like_trash
            
#         "Are you a magician? Because whenever I look at you 
#         everyone else disappears." if done1:
#             jump magician
            
#         "Sorry, I can’t hold on… I’ve already fallen for you." if done1:
#             jump cant_hold
            
# label shade_pale:
#     n "oh…… thanks, i guess? i didn’t realize i could be different 
#        shades of anything………"
#     jump flirt
    
# label from_heaven:
#     n "well…… uh… i don’t remember falling from anywhere, 
#        actually……… sorry……………"
#     jump flirt
    
# label bandaid:
#     n "sorry, i didn’t mean to hurt you…… that was an accident……
#        and i’m sorry i don’t carry around bandaids either…………"
#     jump flirt
    
# label like_trash:
#     n "i already know i’m trash. you don’t have to do anything 
#        about that………"
#     jump flirt
    
# label magician:
#     n "um…… i have no idea why that would happen? i think you 
#        should see a doctor."
#     jump flirt
    
# label cant_hold:
#     n "huh? hold on to what? oh, and, uh… sorry for hurting 
#        you, i guess?"
#     jump flirt
    
# label chat:
#     menu:
#         set seen_set
        
#         "What's shakin' bacon?":
#             $ bacon = True
#             jump bacon
            
#         "How are you doing?":
#             $ how_are_you = True
#             jump how_are_you
            
#         "You look a little down. Are you okay?":
#             $ you_okay = True
#             jump you_okay
            
#         "Go back":
#             jump choices
            
#         "What do you do for fun?" if done2:
#             jump for_fun
            
#         "Do you have a job?" if done2:
#             jump have_job
            
#         "Do you have any pets?" if done2:
#             jump pets
            
#         "Have you ever met Toriel?" if done2:
#             jump toriel
            
# label bacon:
#     n "um... oh...... nothing’s shaking..... and i don’t 
#        have any bacon.... awkward......."
#     jump chat
    
# label how_are_you:
#     n "i’m fine..........."
#     jump chat
    
# label you_okay:
#     n "oh, i guess.... this is just how i always look. 
#        but thanks for asking...... that’s nice of you 
#        to notice....."
#     jump chat
    
# label for_fun:
#     n "i like to listen to music, and.... sometimes.... i 
#        make my own too."
#     menu:
#         set seen_set
        
#         "What kind of music do you make?":
#             jump kind_music
            
#         "I like music too.":
#             #adds FP
#             jump like_music
            
#         "Oh, I don't really listen to music.":
#             #subtracts FP
#             jump dont_listen
            
# label kind_music:
#     n "oh...... all kinds...... i’m not a very good singer, 
#        though, so nothing with vocals......."
#     jump chat
    
# label like_music:
#     n "that’s nice...... i’m glad.... we have the same 
#        interests......."
#     jump chat
    
# label dont_listen:
#     n "oh...... oh no........ maybe you’d like it if you 
#        gave it another chance............"
#     jump chat
    
# label have_job:
#     n "um... yeah....... i’m a snail farmer...... it’s 
#        pretty quiet, now that i’m the only one working 
#        there........"
#     menu:
#         set seen_set
        
#         "Snail farmer? What does that entail?":
#             jump snail_farmer
            
#         "What happened to your coworkers?":
#             jump coworkers
            
# label snail_farmer:
#     n "um...... i just...... sell snails... on my 
#        farm........ it’s all in the title......."
#     jump chat
    
# label coworkers:
#     n "oh, nothing, they just....... all wanted to become 
#        corporeal........ but i stayed behind......."
#     n "someone needs to stay and look after the snails..."
#     jump chat
    
# label pets:
#     n "oh… well… i have snails. do those count?"
#     menu:
#         set seen_set
        
#         "Yes, of course they do.":
#             jump yes_snails
            
#         "Why would you have snails?":
#             jump why_snails
            
#         "Snails arent't pets. They're gross.":
#             jump gross
            
# label yes_snails:
#     n "oh, that’s good…"
#     jump chat
    
# label why_snails:
#     n "well… i sell them. People usually want them for food…"
#     jump chat
    
# label gross:
#     n "oh………………"
#     jump chat
    
# label toriel:
#     n "oh, uh, yeah. i’ve met toriel. but she’s kind of 
#        intimidating…"
#     menu:
#         set seen_set
        
#         "What about frisk? Do you know them?" if met_frisk:
#             jump frisk
            
#         "Why is she intimidating?":
#             jump intimidating
            
#         "She's not that bad.":
#             jump not_bad
            
#         "Yeah I'm pretty sure she secretly eats children.":
#             jump eat_child
            
# label frisk:
#     n "yeah, i know them too. they’re very nice, and they 
#        don’t intimidate me like toriel does."
#     jump chat
    
# label intimidating:
#     n "she’s just, like, really tall. and sometimes, when 
#        she smiles, i feel like she secretly wants to kill me…"
#     jump chat
    
# label not_bad:
#     n "uh… okay. i guess i’ll take your word for it."
#     jump chat
    
# label eat_child:
#     n "um, okay? i don’t know why you would think that but sure."
#     jump chat
    
# label leave:
#     n "...bye.."
#     return