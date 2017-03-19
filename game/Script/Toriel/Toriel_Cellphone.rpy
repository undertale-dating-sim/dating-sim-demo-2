
label call_Toriel_Unknown():
    toriel "Oh, have you turned your location off? I can not seem to find where you are.  Maybe it is just the signal."
    return

label call_Toriel_Cave_Room(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "Oh, this was where Frisk and you fell, was it not? It must have been quite a hard landing."
    toriel "I am glad those flowers were there to break your fall, at least!"
    toriel "I can only imagine if they had not-"
    toriel "Never mind me, dear. Do be careful out there, though."
    return

label call_Toriel_Grass_Room(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "Sometimes, in this room, a little yellow flower pops up from the patch of grass sitting in the sunlight."
    toriel "It may not look it, but it is quite the troublemaker. Do not ever agree to follow it to any place where you will be unable to call me, alright?"
    toriel "Take care!"
    return

label call_Toriel_Ruins_Entrance(owner,call_count):
    
    if call_count > 1:
        toriel "I suppose the vines do have a certain aesthetic appeal."
    else:
        toriel "Hello, Toriel here!"
        toriel "This room has a lot petals and vines. I wanted to clean them up, but Frisk insisted that it looked nice the way it was - so I left them."
        
        menu:
            "What do you think?"
            "It's nice.":
                toriel "Hm. I do not think it is anything special, but if the both of you seem to agree then perhaps I am wrong."
            "It's dirty.":
                $ owner.FP += 1
                toriel "That is what I would say. Still, I cannot bring myself to get rid of the leaves if Frisk likes them so much. I hope you understand."
    return
    
label call_Toriel_Tunnels(owner,call_count):
    
    if call_count > 1:
        toriel "Hello, Toriel here!"
        toriel "Oh! I have a fun fact concerning these rooms!"
        toriel "They used to be full of puzzles that you had to solve before you could get through. Some of them were a little dangerous, so I did my best to remove as many of them as I could."
        toriel "I hope that does not upset you."
    else:
        toriel "To be perfectly honest, I think you may have found repeating the same puzzles every day a little boring."
    return

label call_Toriel_Dummy_Room(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "Feel free to talk to the dummy! It is not much for conversation, but I am sure it would appreciate listening to someone anyway."
    return

label call_Toriel_Froggit_Room(owner,call_count):
    
    if call_count > 1:
        toriel "Hello, Toriel here!"
        toriel "I hope the Froggits caused you no trouble. They do not mean to, but they can get carried away sometimes."
        toriel "If they want to fight, just give them this look."
        "* Toriel sends an emoji. It looks angry."
    else:
        toriel "No one is bothering you, are they?"
    return

label call_Toriel_Monster_Candy_Room(owner,call_count):
    toriel "Hello, Toriel here!"
    toriel "Feel free to take a piece of candy, if you would like!"
    return

label call_Toriel_Sassy_Rock_Room(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "Have you met the rock who lives here? Do not pay much mind to him. He likes to tease newcomers."
    toriel "If he starts being a big nuisance, just let him know that you are with me - I am sure he will listen to whatever you have to say."
    return

label call_Toriel_Blooky_Room(owner,call_count):
    
    if call_count == 1:
        toriel "Hello, Toriel here!"
        toriel "Believe it or not, there used to be a little ghost here blocking the path. They stopped appearing after the first few times I saw them, but Frisk told me that they still come sometimes, if they think there is no one around."
    else:
        toriel "They seem nice, albeit awfully shy. If you see them, do be sure to tell them they can come over for Snail Pie any time."
    return

label call_Toriel_Spider_Bakery(owner,call_count):
    
    if call_count  == 1:
        toriel "Hello, Toriel here!"
        toriel "You must be in the room with the spider bake sale!"
        toriel "The spiders here are very friendly. If I happen to be in the mood for a spider donut when I am on my morning walk, I will buy a couple for myself and Frisk."
        toriel "Apparently, they are collecting money for a good cause, though I have never stopped long enough to ask what it is."
    else:
        toriel "Tell the spiders that Frisk and I send our regards."

    return

label call_Toriel_Snail_Hunter(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "Are you in the mood to catch some snails?" 
    #if the player has caught snails today and gave them to Toriel:
    toriel "We actually have enough for today, but I do appreciate the enthusiasm!"
    #if the player has not brought snails to Toriel:
    toriel "If you catch any, feel free to bring them back home!"
    return

label call_Toriel_Tunnel_Divide(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "Unless I am wrong, you are at the crossroads right now. Go north to come back home, and east to go to nowhere in particular!"
    return

label call_Toriel_Overlook(owner,call_count):
    
    if call_count == 1:
        toriel "Hello, Toriel here!"
        toriel "The view from here is really something, is it not? Sometimes I walk here in the evening to watch all the lights turn on as the monsters return to their homes."
        toriel "I suppose it reminds me of the city, sometimes."
        toriel "I wonder how everyone is doing up there."
    else:
        toriel "Isn’t it spectacular?"
    return

label call_Toriel_Black_Tree_Room(owner,call_count):
    
    toriel "Hello, Toriel here!"
    toriel "You must be just outside our house. Be careful, or you might trip over the leaves." 
    toriel "That pesky black tree keeps dropping them no matter how many times I try to clean them up."
    return

label call_Toriel_Same_Room(owner,call_count):
    if call_count == 1:
        show toriel normal
        toriel "Hello? Oh!"
        show toriel laughing
        toriel "You are so silly!"
    else:
        show toriel smile
        toriel "I will not fall for that one again!"
    return

