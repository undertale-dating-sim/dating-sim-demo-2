
label call_Frisk_Unknown:
    return

label call_Frisk_Cave_Room(monster,call_count):
 
    if call_count == 1:
        frisk  "This is where I first fell into the ruins. Good thing that bed of flowers was there, it really cushioned my fall…"
        frisk  "Oh, you’re probably glad for that too, huh? I forget I’m not the only one who’s fallen down through there."
    elif call_count == 2:
        frisk  "...Do you ever want to go back?"
        frisk  "I know how strange it was for me, to discover this world of monsters living beneath our feet..."
        frisk  "I imagine it’s kind of the same for you."
    else:
        frisk  "But I’m happy here. I wouldn’t want to leave Mom. So in a way, I guess I’m glad I fell down here."
        $ player.variables['Frisk_Cellphone_Cave_Room_Complete'] = True
    return

label call_Frisk_Grass_Room(monster,call_count):

    if call_count == 1:
        frisk  "It’s kind of dark in here, isn’t it...? All kinds of things crawl around in the dark... But, um, I’m sure it’ll be fine."
    else:
        frisk  "There’s no reason to be scared of the dark... Really."
        $ player.variables['Frisk_Cellphone_Grass_Room_Complete'] = True
    return

label call_Frisk_Ruins_Entrance(monster,call_count):

    if call_count == 1:
        frisk  "This is the entrance to the ruins. It seemed so big the first time I went through it, but I was pretty overwhelmed then. "
        frisk  "It’s a lot less intimidating now."
    else:
        frisk  "Oh! This room has a bunch of cool vines and leaves! "
        frisk  "It almost makes me feel like I’m in a forest. "
        frisk  "It smells like a forest too, don’t you think?"
        $ player.variables['Frisk_Cellphone_Ruins_Entrance_Complete'] = True
    return
    
label call_Frisk_Tunnels(monster,call_count):
    frisk  "Hi!"
    frisk  "This room used to have a bunch of puzzles in it."
    frisk  "Mom used to think they were too dangerous for me and made me hold her hand as we went through them.  "
    frisk  "But, as I got older, she let me do them by myself."
    frisk  "Eventually it just started just getting annoying, so I asked her to take them out. That’s why it’s so empty in there."
    $ player.variables['Frisk_Cellphone_Tunnels_Complete'] = True
    return

label call_Frisk_Dummy_Room(monster,call_count):

    if call_count == 1:
        frisk  "Mom first tried to teach me how to handle conflict here. ...That dummy wasn’t much of a conversationalist, though."
    else:
        frisk  "I’ve tried talking to it before, but it never seems to want to talk back. "
        frisk  "And if you ignore it, it’ll just leave the room and you’ll end up talking to a wall."
        $ player.variables['Frisk_Cellphone_Dummy_Room_Complete'] = True

    return

label call_Frisk_Froggit_Room(monster,call_count):

    if call_count == 1:
        frisk   "That Froggit is quite friendly, actually. I was a bit nervous when I first met him... "
        frisk   "He tried to attack me at first... But he turned out to not be so bad!"
    else:
        frisk  "I’m actually really good friends with all of the Froggits now. "
        frisk  "Life is a little hard for them, but they’re good monsters to be friends with."
        $ player.variables['Frisk_Cellphone_Froggit_Room_Complete'] = True

    return

label call_Frisk_Monster_Candy_Room(monster,call_count):
    if call_count == 1:
        frisk   "You shouldn’t take more than one… Leave some for everyone else!"
        $ player.variables['Frisk_Cellphone_Monster_Candy_Room_Complete'] = True
    return

label call_Frisk_Sassy_Rock_Room(monster,call_count):
 
    if call_count == 1:
        frisk  "Oh, hey, have you met the talking rock? He’s actually a pretty cool person once you get to know him."
    elif call_count == 2:
        frisk  "Rocks actually respond well to politeness."
    else:
        frisk  "Well, if you see any talking rocks, tell them I say ‘Hi.’"
        $ player.variables['Frisk_Cellphone_Sassy_Room_Complete'] = True
        
    return

label call_Frisk_Blooky_Room(monster,call_count):

    if call_count == 1:
        frisk  "You might encounter a sleeping ghost in here. But don’t worry, they’re nice!"
    elif call_count == 2:
        frisk  "They’re really shy at first, but once you get to know them, they’re actually kinda cool!"
    else:
        frisk  "Blooky and I are good friends. They like to show me the music they make, and it's surprisingly good."
        frisk  "They're to nervous to show most people, though... It's a shame."
        $ player.variables['Frisk_Cellphone_Blooky_Room_Complete'] = True
    return

label call_Frisk_Spider_Bakery(monster,call_count):

    if call_count == 1:
        frisk  "I love the donuts here! Plus, it goes to a good cause, so why not donate?"
    else:
        frisk  "Mom buys things from them sometimes as well, but I think she enjoys their cider more."
        $ player.variables['Frisk_Cellphone_Spider_Bakery_Complete'] = True
    return

label call_Frisk_Snail_Hunter(monster,call_count):

    if call_count == 1:
        frisk  "Did you need something? "
        frisk  "The Snail Hunting Room, huh? Mom and I come here a lot. She really likes snails. "
        frisk  "I’m not too big on them myself, but I like seeing Mom happy, so it’s always fun to go."
        $ player.variables['Frisk_Cellphone_Snail_Hunter_Complete'] = True
    return

label call_Frisk_Tunnel_Divide(monster,call_count):

    frisk  "Heya!"
    frisk  "Is the other Froggit still there? They’re kinda funny. They’re afraid of Mom for some reason. I can’t imagine why, though."
    $ player.variables['Frisk_Cellphone_Tunnel_Divide_Complete'] = True
    return

label call_Frisk_Overlook(monster,call_count):

    if call_count == 1:
        frisk   "... ... ... Nice view, huh?"
    else:
        frisk  "It’s a shame no one else lives here. They're really missing out!"
        $ player.variables['Frisk_Cellphone_Overlook_Complete'] = True
    return

label call_Frisk_Black_Tree_Room(monster,call_count):
    
    if call_count == 1:
        frisk  "Home is just up ahead!"
    elif call_count == 2:
        frisk  "It’s really fun to play in the leaves, but Mom doesn’t like it if you spread them around too much." 
        frisk  "You’ll have to clean them up if you do."
    else:
        frisk  "Our house is cozy looking even from the outside, isn’t it?"
        frisk  "Although, I always thought that tree was pretty weird. What kind of tree stays black like that?"
        frisk  "I’ve tried asking Mom about it, but she always just dismisses it. It makes you wonder, huh?"
        $ player.variables['Frisk_Cellphone_Black_Tree_Room_Complete'] = True
    return

label call_Frisk_Same_Room(monster,call_count):
    if call_count == 1:
        show frisk normal with Dissolve(.25)
        frisk  "Hello...?"
        frisk  "Oh!"
        frisk  "..."
        show frisk distant with Dissolve(.25)
        frisk  "Really?"
    else:
        show frisk soulless with Dissolve(.25)
        frisk  "..."
        $ player.variables['Frisk_Cellphone_Same_Room_Complete'] = True
    return
