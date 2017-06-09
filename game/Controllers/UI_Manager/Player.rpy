init -1 python:

# 
# This is the Player Class.  It contains all of the stats of the main player.  Most of the variable names are common sense.
# 
    class Player():
        def __init__(self):
            self.name           = "Bob"
            self.current_health = 20
            self.total_health   = 20
            self.gold           = 10
            self.fucks          = 0
            self.dumped_on      = False

            #the stats go positive or negative, do not know the maximum values yet.
            self.patience_impulsiveness = 0
            self.integrity_deceit     = 0
            self.bravery_cowardice        = 0
            self.perseverance_surrender   = 0
            self.kindness_cruelty       = 0
            self.justice_apathy        = 0
            self.current_room = "Nowhere"

            self.equipped_item = False

            self.time = 0
            self.safe_room = "Your Room"
            self.pass_out_label = "player_passes_out"
            self.die_label = "player_dies"

            self.current_snails = 5
            self.max_snails = 10
            self.last_snail_day = False
            self.variables = {}

        # 
        # This is a really long gross list of sets for the stats.  There is a simpler way to do this with arrays but I'm not sure
        # of the benefit now that it is done.   If we end up revamping the stats then we will redo these.
        # 
        def modify_patience(self,amount):
            self.patience_impulsiveness += amount

        def modify_integrity(self,amount):
            self.integrity_deceit   += amount

        def modify_bravery(self,amount):
            self.bravery_cowardice  += amount

        def modify_perseverance(self,amount):
            self.perseverance_surrender += amount

        def modify_kindness(self,amount):
            self.kindness_cruelty   += amount

        def modify_justice(self,amount):
            self.justice_apathy += amount

        def modify_impulsiveness(self,amount):
            self.patience_impulsiveness -= amount

        def modify_deceit(self,amount):
             self.integrity_deceit  -= amount

        def modify_cowardice(self,amount):
            self.bravery_cowardice  -= amount

        def modify_surrender(self,amount):
            self.perseverance_surrender -= amount

        def modify_cruelty(self,amount):
            self.kindness_cruelty   -= amount

        def modify_apathy(self,amount):
            self.justice_apathy -= amount
            
        #################
        #    This is currently called after every action the player does.  We should put all of the logic for the player
        #   in this function.
        ##################
        def update_player(self):
            if self.current_health <= 0:
                renpy.call_in_new_context(self.die_label)

##########
    # This function should be called when the player needs to wake up.

    # day_change currently does nothing

    # Currently sets the time to 480, which is the first minute of Morning.
#############
label player_waking_up(day_change = 1, health_refill = player.total_health):
    $ world.set_current_time(480,True)
    $ player.current_health += 10
    
    if player.current_health > player.total_health:
        $ player.current_health = player.total_health
        
    "You feel refreshed!"
    "Now that you've slept, you feel a little bit better."
    "(+10 Health)"
    return

######################
    # It will move them to their safe_room.

    # Currently the safe_room will then call 'player_waking_up' to complete the scene.

#####################

label player_passes_out:
    "The world goes dark."
    scene
    with fade
    "Oh no, it looks like they ran out of energy."
    "Let's carry them home..."
    $ world.move_to_room(player.safe_room)

####################
    # Called when the player dies.
    # Calls the game over screen and plays an animation/changes the music.

####################

label player_dies:
    $ slow_cps = 1
    
    init:
        image heartbreak = Animation("images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death1a.png", 0.1,
                                    "images/animations/death/death1b.png", 0.1,
                                    "images/animations/death/death2.png", 1.1,
                                    "images/animations/death/death3.png", 0.05,
                                    "images/animations/death/death4.png", 0.07,
                                    "images/animations/death/death5.png", 0.1,
                                    "images/animations/death/death6.png", 0.2,
                                    "images/animations/death/death7.png", 0.2,
                                    "images/animations/death/death8.png", 0.2,
                                    "images/animations/death/death9.png", 0.2,
                                    "images/animations/death/death10.png", 0.2,
                                    "images/animations/death/death11.png", 0.2,
                                    "images/animations/death/death12.png", 0.2)
        image black = "#000000"
        image gameover1 = Text("{size=150}{b}GAME{/b}{/size}", slow=True, scope=None, substitute=None, slow_done=None)
        image gameover2 = Text("{size=150}{b}OVER{/b}{/size}", slow=True, scope=None, substitute=None, slow_done=None)
    
    #equeue music [ "<silence .7>", "audio/sfx/heartbreak.wav"]
    # if player.dumped_on == True:
    #     #$ renpy.music.queue( "audio/music/dogsong.mp3", channel="music", loop=True, clear_queue=False, fadein=0, tight=True)
    # else:
        #$ renpy.music.queue( "audio/music/determination.wav", channel="music", loop=True, clear_queue=False, fadein=0, tight=True)
    
    scene heartbreak with fade
    
    $ renpy.pause(2.7, hard=True)
    
    scene black
    
    show gameover1 at Position(xpos=200, ypos=30, xanchor=0, yanchor=0)
    show gameover2 at Position(xpos=200, ypos=150, xanchor=0, yanchor=0)
    with fade
    
    $ renpy.pause(2.0, hard=True)

    if player.dumped_on == False:
        $ sayingnum = renpy.random.randint(1, 12)
    else:
        $ sayingnum = 13
    
    ##"[sayingnum]"             ######     FOR TESTING PURPOSES      ######
    ##$sayingnum = 4
    
    if sayingnum == 1:
        call saying1
    if sayingnum == 2:
        call saying2
    if sayingnum == 3:
        call saying3
    if sayingnum == 4:
        call saying4
    if sayingnum == 5:
        call saying5  
    if sayingnum == 6:
        call saying6
    if sayingnum == 7:
        call saying7
    if sayingnum == 8:
        call saying8
    if sayingnum == 9:
        call saying9
    if sayingnum == 10:
        call saying10
    if sayingnum == 11:
        call saying11
    if sayingnum == 12:
        call saying12
    if sayingnum == 13:
        call saying13
    
    if player.dumped_on:
        $ pause_res = renpy.pause (600.0)
        if pause_res == False:
            $ renpy.music.queue( "audio/music/dog.mp3", channel="music", loop=True, clear_queue=True, fadein=0, tight=True)
        else:
            $ player.current_health += 10
    else:
        $ renpy.pause ()
        $ player.current_health += 10


##### GAME OVER QUOTES #####
if sayingnum == -1: # Keeps these label blocks from being accidentally executed until they're called.
    label saying1(playername = player.name):    
        init:
            image text1 = Text("{size=30}You cannot give{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text2 = Text("{size=30}up just yet...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text3 = Text("{size=30}Stay determined!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            #### TRYING TO CHANGE FONT SIZE OF PLAYER NAME
            ##$ string1 = "Temmie"
            ##$ string1 = player.name
            ##image text3 = Text("[string1]", slow=True, scope=None, substitute=None, slow_done=None)
            ##Images must be defined in the init block, but player.name will not be passed in until runtime. Due to the way RenPy works, "Aeris" will display, but player.name will throw a KeyError.
        
        $playername = playername + "!"
        
        show text1 at Position(xpos=260, ypos=380, xanchor=0, yanchor=0)
        show text2 at Position(xpos=280, ypos=420, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text playername at Position(xpos=280, ypos=390, xanchor=0, yanchor=0)
        show text3 at Position(xpos=280, ypos=420, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
    
    label saying2(playername = player.name):
        init:
            image text4 = Text("{size=30} This is just{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text5 = Text("{size=30}a bad dream...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text6 = Text("{size=30} Wake up! It's not over!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + ","
        $adj_xpos = 280 - len(playername)*11
        
        show text playername at Position(xpos=adj_xpos, ypos=395, xanchor=0, yanchor=0)
        show text4 at Position(xpos=320, ypos=390, xanchor=0, yanchor=0)
        show text5 at Position(xpos=280, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text6 at Position(xpos=200, ypos=380, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying3(playername = player.name):    
        init:
            image text7 = Text("{size=30}It's like he says...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text8 = Text("{size=30}You have to stay determined!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
        
        $playername = playername + "!"
        $adj_xpos = 280 - len(playername)*11
        
        show text playername at Position(xpos=adj_xpos, ypos=390, xanchor=0, yanchor=0)
        show text7 at Position(xpos=320, ypos=390, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text8 at Position(xpos=180, ypos=390, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying4(playername = player.name):
        init:
            image text9 = Text("{size=30} Please don't give up...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text10 = Text("{size=30}Have some determination!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
        
        $playername = playername + "!"
        
        show text9 at Position(xpos=220, ypos=390, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text playername at Position(xpos=220, ypos=390, xanchor=0, yanchor=0)
        show text10 at Position(xpos=220, ypos=420, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying5(playername = player.name):
        init:
            image text11 = Text("{size=30}You can't quit!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text12 = Text("{size=30}Stay determined...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + "!"
        
        show text playername at Position(xpos=280, ypos=390, xanchor=0, yanchor=0)
        show text11 at Position(xpos=280, ypos=420, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text12 at Position(xpos=280, ypos=390, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return

    label saying6(playername = player.name):
        init:
            image text11 = Text("{size=30} is this{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text12 = Text("{size=30}a kind of joke?{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text13 = Text("{size=30}Cut it out!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text14 = Text("{size=30}Wake up!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + ","
        $adj_xpos = 320 - len(playername)*11
        
        show text playername at Position(xpos=adj_xpos, ypos=395, xanchor=0, yanchor=0)
        show text11 at Position(xpos=340, ypos=390, xanchor=0, yanchor=0)
        show text12 at Position(xpos=280, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text13 at Position(xpos=320, ypos=390, xanchor=0, yanchor=0)
        show text14 at Position(xpos=320, ypos=440, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return

    label saying7(playername = player.name):
        init:
            image text15 = Text("{size=30} it's not{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text16 = Text("{size=30}time to leave!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text17 = Text("{size=30}Hold on!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + ","
        $adj_xpos = 320 - len(playername)*11
        
        show text playername at Position(xpos=adj_xpos, ypos=395, xanchor=0, yanchor=0)
        show text15 at Position(xpos=340, ypos=390, xanchor=0, yanchor=0)
        show text16 at Position(xpos=280, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text17 at Position(xpos=320, ypos=390, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying8(playername = player.name):
        init:
            image text18 = Text("{size=30} gather{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text19 = Text("{size=30}your strength!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text20 = Text("{size=30}Stay determined!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + ","
        $adj_xpos = 320 - len(playername)*11
        
        show text playername at Position(xpos=adj_xpos, ypos=395, xanchor=0, yanchor=0)
        show text18 at Position(xpos=340, ypos=390, xanchor=0, yanchor=0)
        show text19 at Position(xpos=280, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text20 at Position(xpos=280, ypos=390, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return

    label saying9(playername = player.name):
        init:
            image text21 = Text("{size=30} you have{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text22 = Text("{size=30}to keep going{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text23 = Text("{size=30}Our fate rests{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text24 = Text("{size=30}upon you...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + ","
        $adj_xpos = 320 - len(playername)*10
        
        show text playername at Position(xpos=adj_xpos, ypos=395, xanchor=0, yanchor=0)
        show text21 at Position(xpos=340, ypos=390, xanchor=0, yanchor=0)
        show text22 at Position(xpos=280, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text23 at Position(xpos=280, ypos=390, xanchor=0, yanchor=0)
        show text24 at Position(xpos=320, ypos=440, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying10():
        init:
            image text25 = Text("{size=30}You're going to{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text26 = Text("{size=30}be alright!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text27 = Text("{size=30}Don't lose hope!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
        
        show text25 at Position(xpos=260, ypos=390, xanchor=0, yanchor=0)
        show text26 at Position(xpos=280, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text27 at Position(xpos=260, ypos=390, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying11(playername = player.name):
        init:
            image text28 = Text("{size=30}Don't lose hope!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text29 = Text("{size=30}It cannot end now!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            
        $playername = playername + "!"
        
        show text28 at Position(xpos=260, ypos=390, xanchor=0, yanchor=0)
        
        call next_screen
        
        show text playername at Position(xpos=350, ypos=395, xanchor=0, yanchor=0)
        show text29 at Position(xpos=260, ypos=440, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying12(playername = player.name):
        init:
            image text30 = Text("{size=30}This cannot{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text31 = Text("{size=30}be the end!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text32 = Text("{size=30}Stay determined!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
        
        $playername = playername + "!"

        show text30 at Position(xpos=280, ypos=390, xanchor=0, yanchor=0)
        show text31 at Position(xpos=290, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen

        show text playername at Position(xpos=370, ypos=390, xanchor=0, yanchor=0)
        show text32 at Position(xpos=280, ypos=420, xanchor=0, yanchor=0)
        
        $ renpy.pause(2.0, hard=True)
        return
        
    label saying13():
        init:
            image text33 = Text("{size=30}geeettttttt{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text34 = Text("{size=30}dumped on!!!{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text35 = Text("{size=30}if we're really{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text36 = Text("{size=30}friends...{/size}", slow=True, scope=None, substitute=None, slow_done=None)
            image text37 = Text("{size=30}you won't come back.{/size}", slow=True, scope=None, substitute=None, slow_done=None)

        show text33 at Position(xpos=260, ypos=390, xanchor=0, yanchor=0)
        show text34 at Position(xpos=260, ypos=440, xanchor=0, yanchor=0)
        
        call next_screen

        show text35 at Position(xpos=260, ypos=390, xanchor=0, yanchor=0)
        show text36 at Position(xpos=260, ypos=440, xanchor=0, yanchor=0)

        call next_screen
        
        show text37 at Position(xpos=240, ypos=390, xanchor=0, yanchor=0)

        $ renpy.pause(2.0, hard=True)
        return
        
    label next_screen(): #Redisplaying the GAME OVER text whenever I have to clear the screen for more text.
        
        $ renpy.pause(2.0, hard=True)
        
        scene black
        
        show gameover1 at Position(xpos=200, ypos=30, xanchor=0, yanchor=0)
        show gameover2 at Position(xpos=200, ypos=150, xanchor=0, yanchor=0)
        
        return