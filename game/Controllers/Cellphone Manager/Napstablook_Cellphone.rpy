label call_Napstablook:
    
    napstablook "Oh hello."


    $ location = world.currentArea.currentRoom
    $ loc_name = "call_Napstablook_"+location.name.replace(" ","_")
    #Ruins
    if renpy.has_label(loc_name):
        if not renpy.seen_label(loc_name):
            call expression loc_name pass (True)
        else:
            call expression loc_name pass (False)
    else:
        call call_Napstablook_Unknown

    return

label call_Napstablook_Unknown:
    return

label call_Napstablook_Cave_Room(first_visit = False):

    if first_visit:
        "test"
    else:
        "test 2"

    return

label call_Napstablook_Grass_Room(first_visit = False):
    
    return

label call_Napstablook_Ruins_Entrance(first_visit = False):
    
    return
    
label call_Napstablook_Tunnels(first_visit = False):
    return

label call_Napstablook_Dummy_Room(first_visit = False):
    return

label call_Napstablook_Froggit_Room(first_visit = False):
    return

label call_Napstablook_Sassy_Rock_Room(first_visit = False):
    return

label call_Napstablook_Blooky_Room(first_visit = False):
    return

label call_Napstablook_Spider_Bakery(first_visit = False):
    return

label call_Napstablook_Snail_Hunter(first_visit = False):
    return

label call_Napstablook_Tunnel_Divide(first_visit = False):
    return

label call_Napstablook_Overlook(first_visit = False):
    return

label call_Napstablook_Black_Tree_Room(first_visit = False):
    return




#     Cave room
# [1st call]NAPSTABLOOK: is this where you fell? oh...... sorry........ that must’ve been traumatic....

# [2nd call]NAPSTABLOOK: i don’t really go there often....... not much to see......

# Grass room
# [1st call]NAPSTABLOOK: this room? sometimes old stuff falls down here....... i never take anything, though... none of it belongs to me.

# [2nd call]NPASTABLOOK: did you take some of that old stuff? oh, i didn’t mean to make you feel bad about it......

# Entrance to Ruins
# [1st call]NAPSTABLOOK: it’s the entrance to the ruins...... i don’t know where the vines came from, they’ve just always been there....

# [2nd call]NAPSTABLOOK: maybe they grew down here from the surface?

# Dummy room
# [1st call]NAPSTABLOOK: oh....... that’s where i first saw you...... sorry i left...... i was just surprised to see you....... sorry........

# [2nd call]NAPSTABLOOK: sorry........

# Froggit w/ leaves room
# [1st call]NAPSTABLOOK: those leaves sound crunchy... i can hear you stepping on them......

# [2nd call]NAPSTABLOOK: it might be fun to play in the leaves..... if, you know...... i was corporeal.

# NAPSTABLOOK: but that’s okay.... it’s fine..........

# Sassy rock room
# [1st call]NAPSTABLOOK: that rock...... doesn’t like to be pushed..... i understand, i wouldn’t either...... if i was a rock....

# [2nd call]NAPSTABLOOK: ...

# Blooky room
# [1st call]NAPSTABLOOK: oh hey.... this is where we met... 

# [2nd call]NAPSTABLOOK: i like to sleep here, sometimes... it’s pretty quiet....

# Spider bakery
# [1st call]NAPSTABLOOK: the spiders here are pretty nice... they all want to get back to hotland, but i don’t know why.... 

# [2nd call]NAPSTABLOOK: i think it’s fine here in the ruins.....

# Toriel’s garden/snail race
# [1st call]NAPSTABLOOK: you’re in Toriel’s garden.... there are some snails here...... i guess you already knew that, because you can see them....

# [2nd call]NAPSTABLOOK: the yellow snail’s my favorite. well, my favorite snail that’s in the ruins...... i have others back home....

# Ruin overlook/knife room
# [1st call]NAPSTABLOOK: this is a pretty nice view....... well, if you’re restricted by gravity. i like to fly up to the ceiling, that’s where you can get the best view of the ruins......

# [2nd call]NAPSTABLOOK: oh, i’m sorry....... you can’t fly.... that was inconsiderate....... sorry........

# Black tree/Toriel’s home front
# [1st call]NAPSTABLOOK: Toriel’s house? she invites me over sometimes.... she always makes me food, but i can’t eat it because it’s not ghost food... it goes right through me........

# [2nd call]NAPSTABLOOK: i don’t have the courage to tell her........