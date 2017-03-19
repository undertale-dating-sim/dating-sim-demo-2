label call_Napstablook_Unknown:
    return

label call_Napstablook_Cave_Room(monster,call_count):
 
    if call_count == 1:
        napstablook "is this where you fell? oh...... sorry........ that must’ve been traumatic...."
    else:
        napstablook "i don’t really go there often....... not much to see......"
    return

label call_Napstablook_Grass_Room(monster,call_count):

    if call_count == 1:
        napstablook "this room? sometimes old stuff falls down here....... i never take anything, though... none of it belongs to me"

    else:
        napstablook "did you take some of that old stuff? oh, i didn’t mean to make you feel bad about it......"

    return

label call_Napstablook_Ruins_Entrance(monster,call_count):

    if call_count == 1:
        napstablook "it’s the entrance to the ruins...... i don’t know where the vines came from, they’ve just always been there...."
    else:
        napstablook "maybe they grew down here from the surface..?"
    return
    
label call_Napstablook_Tunnels(monster,call_count):
    if call_count == 1:
        napstablook "these puzzles have been disabled for awhile.. i’m not sure but i think Frisk was the one who did it"
    elif cell_convo_count == 1:
        napstablook "... they probably just got tired of having to go through them all the time…"
    else:
        napstablook "i know i would have gotten tired of doing puzzles.... you know..… if i couldn’t float over them"
    return

label call_Napstablook_Dummy_Room(monster,call_count):

 
    if call_count == 1:
        napstablook "oh....... that’s where i first saw you...... sorry i left...... i was just surprised to see you....... sorry........"
    else:
        napstablook "sorry........"
    return

label call_Napstablook_Froggit_Room(monster,call_count):

    if call_count == 1:
        napstablook "those leaves sound crunchy... i can hear you stepping on them......"
    else:
        napstablook "it might be fun to play in the leaves..... if, you know...... i was corporeal"
        napstablook "but that’s okay.... it’s fine.........."
    return

label call_Napstablook_Sassy_Rock_Room(monster,call_count):
 
    if call_count == 1:
        napstablook "that rock...... doesn’t like to be pushed..... i understand, i wouldn’t either...... if i was a rock...."

    else:
        napstablook "..."
    return

label call_Napstablook_Blooky_Room(monster,call_count):

    if call_count == 1:
        napstablook "oh hey.... this is where we met... "
    else:
        napstablook "i like to sleep here, sometimes... it’s pretty quiet...."
    return

label call_Napstablook_Spider_Bakery(monster,call_count):

    if call_count == 1:
        napstablook "the spiders here are pretty nice... they all want to get back to hotland, but i don’t know why.... "

    else:
        napstablook "i think it’s fine here in the ruins....."

    return

label call_Napstablook_Snail_Hunter(monster,call_count):

    if call_count == 1:
        napstablook "you’re in Toriel’s garden.... there are some snails here...... i guess you already knew that, because you can see them...."

    else:
        napstablook "the yellow snail’s my favorite. well, my favorite snail that’s in the ruins...... i have others back home...."
    return

label call_Napstablook_Tunnel_Divide(monster,call_count):
    if call_count == 1:
        napstablook "isn’t there some poem…. about two roads diverged..?"
    else:
        napstablook "… well i suppose it doesn’t really matter which you pick"
    return

label call_Napstablook_Overlook(monster,call_count):

    if call_count == 1:
        napstablook "this is a pretty nice view....... well, if you’re restricted by gravity. i like to fly up to the ceiling, that’s where you can get the best view of the ruins......"
    else:
        napstablook "oh, i’m sorry....... you can’t fly.... that was inconsiderate....... sorry........"
    return

label call_Napstablook_Black_Tree_Room(monster,call_count):
    
    if call_count == 1:
        napstablook "Toriel’s house? she invites me over sometimes.... she always makes me food, but i can’t eat it because it’s not ghost food... it goes right through me........"
    else:
        napstablook "i don’t have the courage to tell her........"
return



