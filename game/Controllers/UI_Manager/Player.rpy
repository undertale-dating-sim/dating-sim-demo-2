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
            self.fucks          = 1

            #the stats go positive or negative, do not know the maximum values yet.
            self.patience_impulsiveness = 0
            self.integrity_deceit     = 0
            self.bravery_cowardice        = 0
            self.perseverance_surrender   = 0
            self.kindness_cruelty       = 0
            self.justice_apathy        = 0
            self.current_room = "Nowhere"
            self.current_stamina = 100
            self.max_stamina = 100

            self.equipped_item = False

            self.time = 0
            self.safe_room = "Your Room"

        def give_fuck(self):
            if self.fucks > 0:
                renpy.say(self.name,'Fuck')
                self.fucks -= 1
            else:
                renpy.notify("OUT OF FUCKS")
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
            if self.current_stamina <= 0:
                renpy.call_in_new_context("player_passes_out")

##########
    # This function should be called when the player needs to wake up.

    # day_change currently does nothing
    # stam_refill is how much stamina the player should regain when they wake up.  Default is max.

    # If the players stamina goes over max, it will go down to the max.

    # Currently sets the time to 480, which is the first minute of Morning.
#############
label player_waking_up(day_change = 1, stam_refill = player.max_stamina):
    $ world.set_current_time(480,True)
    $ player.current_stamina += stam_refill
    if player.current_stamina > player.max_stamina:
        $ player.current_stamina = player.max_stamina
    "You feel refreshed! (Stamina refilled)"
    return

######################
    # This label is called automatically in update_player when the player runs out of stamina.
    # It will move them to their safe_room.

    # Currently the safe_room will then call 'player_waking_up' to complete the scene.

#####################

label player_passes_out:
    "Oh no, you ran out of stamina..."
    "The world goes dark."
    scene
    with fade
    "Oh no, it looks like they ran out of energy."
    "Let's carry them home..."
    $ world.move_to_room(player.safe_room)

            
            
