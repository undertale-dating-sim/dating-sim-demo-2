
label call_Frisk_Unknown:
    return

label call_Frisk_Cave_Room(cell_convo_count = 0):
 
    if cell_convo_count == 0:
        frisk  "This is where I first fell into the ruins. Good thing that bed of flowers was there, it really cushioned my fall…"
        frisk  "Oh, you’re probably glad for that too, huh? I forget that I’m not the only one who’s fallen down through there."
    elif cell_convo_count == 1:
        frisk  "...Do you ever want to go back?"
        frisk  "I know how strange it was for me, to discover this world of monsters living beneath our feet..."
        frisk  "I imagine it’s kind of the same for you."
    else:
        frisk  "But I’m happy here. I wouldn’t want to leave Mom. So in a way, I guess I’m glad I fell down here."
    return

label call_Frisk_Grass_Room(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk  "It’s kind of dark in here, isn’t it...? All kinds of things crawl around in the dark.  ... But, um, I’m sure it’ll be fine."
    else:
        frisk  "There’s no reason to be scared of the dark... Really."
    return

label call_Frisk_Ruins_Entrance(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk  "This is the entrance to the ruins. It seemed so big the first time I went through it, but I was pretty overwhelmed then. "
        frisk  "It’s a lot less intimidating now."
    else:
        frisk  "Oh! This room has a bunch of cool vines and leaves! "
        frisk  "It almost makes me feel like I’m in a forest. "
        frisk  "It smells like a forest too, don’t you think?"
    return
    
label call_Frisk_Tunnels(cell_convo_count = 0):
    frisk  "Hi!"
    frisk  "This room used to have a bunch of puzzles in it."
    frisk  "Mom used to think they were too dangerous for me and made me hold her hand as we went through them.  "
    frisk  "But, as I got older, she let me do them by myself."
    frisk  "Eventually it just started just getting annoying, so I asked her to take them out. So that’s why it’s so empty in there."
    return

label call_Frisk_Dummy_Room(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk  "Mom first tried to teach me how to handle conflict here. ...That dummy wasn’t much of a conversationalist though."
    else:
        frisk  "I’ve tried talking to it before, but it never seems to want to talk back. "
        frisk  "And if you ignore it, it’ll just leave the room and you’ll end up talking to a wall."

    return

label call_Frisk_Froggit_Room(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk   "That Froggit is quite friendly actually. I was a bit nervous when I first met him... "
        frisk   "He tried to attack me at first.. But he turned out to not be so bad!"
    else:
        frisk  "I’m actually really good friends with all of the Froggits now. "
        frisk  "Life is a little hard for them, but they’re a good Monster to be friends with."

        
    return

label call_Frisk_Sassy_Rock_Room(cell_convo_count = 0):
 
    if cell_convo_count == 0:
        frisk  "Oh, hey, have you met the talking rock? It’s actually a pretty cool person once you get to know it."
    elif cell_convo_count == 1:
        frisk  "Oh, rocks actually respond pretty well to politeness."
    else:
        frisk  "Well, if you see any talking rocks, tell them I say ‘hi.’"
        
    return

label call_Frisk_Blooky_Room(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk  "You might encounter a sleeping ghost in here. But don’t worry, they’re nice!"
    elif cell_convo_count == 1:
        frisk  "They’re really shy at first, but once you get to know them, they’re actually pretty cool!"
    else:
        frisk  "I’ve gotten kinda close to them. They show me the music that they made a lot. And it’s surprisingly good. "
    return

label call_Frisk_Spider_Bakery(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk  "To be honest, I don’t like the taste of the stuff they sell here... But I like to donate anyway."
    else:
        frisk  "Mom buys things from them sometimes as well but I think she actually enjoys their pastries."
        frisk  "Um, I’d appreciate it if you don’t tell the spiders that I said I don’t like their stuff.    "
    return

label call_Frisk_Snail_Hunter(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk  "Did you need something? "
        frisk  "The Snail Hunting Room, huh? Mom and I come here a lot. She really likes snails.I’m not too big on them myself, but I like seeing Mom happy, so it’s always fun to go.    "
    else:
        frisk  "I have yet to win one of these races. Is it possible to be too encouraging?        "
    return

label call_Frisk_Tunnel_Divide(cell_convo_count = 0):

    frisk  "Heya!"
    frisk  "Is the other Froggit still there? They’re kinda funny. They’re afraid of Mom for some reason. I can’t imagine why, though."
    return

label call_Frisk_Overlook(cell_convo_count = 0):

    if cell_convo_count == 0:
        frisk   "... ... ... Nice view, huh?"
    else:
        frisk  "It’s a shame no one else lives here. No one else can enjoy this view."
    return

label call_Frisk_Black_Tree_Room(cell_convo_count = 0):
    
    frisk  "Hey!"
    frisk  "That’s our house. It’s cozy looking even from the outside, isn’t it? "
    frisk  "Although, I always thought that tree was pretty weird. What kind of tree just stays black like that? "
    frisk  "I’ve tried asking Mom about it, but she always just dismisses it. It makes you wonder, huh?"
    return


# -Black Tree/ Toriel’s Home Front 
# frisk  *"happy* Mom’s home is just up ahead."
#     else:
#         frisk  "It’s really fun to play in the leaves, but Mom doesn’t like if you spread them around too much, you’ll have to clean them up if you do."
#  