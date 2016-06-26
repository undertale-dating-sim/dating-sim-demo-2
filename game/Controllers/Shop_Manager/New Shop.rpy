#shop_dialog()
#viewing dialogs from shop() and handles renpy commands
#shop_system()
#buying and selling, adding to inventory
#shop()
#hold instances like items and dialog
#adds item and dialogs

init:
    $ screen_width = config.screen_width # 800
    $ screen_height = config.screen_height # 600
    $ shop_dialog_width = int(screen_width*.70)
    $ shop_dialog_height = int(screen_height*.215)

define payneShop = Character('PayneGray',
    window_background=Frame("text-box3.png",21,21),
    window_left_margin = int(screen_width*.02),
    window_right_margin = int(screen_width*.265),
    window_top_margin = -6,
    window_bottom_margin = 16,
    window_top_padding = 10,
    window_bottom_padding = 10,
    window_left_padding = 15,
    window_right_padding = 15)


init -1 python:

    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.template = payneShop.copy(self.name)

            self.scene = "background snowdin"
            self.sprites = ["sans","flowey"]

            self.items = []

            #self.test_text = [{"sprite"="image", "dialogue" = "This is a test"}]
            #default text that is always called after the end of any dialog
            self.welcome = [ ["flowey normal","testing welcome"]]#dicts

            self.talk = [["sans normal","Hello"], ["flowey normal","testing talk"]] #image within array #also think about talk topics
            self.sell = [["sans normal","Hello"], ["flowey normal","testing sell"]] #will either show buttons from a 
            self.exit = [["sans normal","Hello"], ["flowey normal","testing exit"]] 
            #on shop_dialog(), if exit dialog is used, return

            self.no_space = ["Hello", "testing talk"]
            self.no_gold = ["Hello", "testing talk"]

            self.thanks = ["Hello", "testing talk"]
        def name(self,name): 
            self.name = name
            self.template = payneShop.copy(name)

        def clear_all(self):
            self.name = ""
            self.items = []
            self.welcome = []
            self.talk = []
            self.sell = []
            self.exit = [] 
            self.no_space = []
            self.no_gold = []
            self.thanks = []

        def add_item(self,item): self.items.append(item)
        def add_talk(self,sprite,string): self.talk.append([sprite,string])
        def add_sell(self,sprite,string): self.sell.append([sprite,string])
        def add_exit(self,sprite,string): self.exit.append([sprite,string])
        def add_no_space(self,sprite,string): self.no_space.append([sprite,string])
        def add_no_gold(self,sprite,string): self.no_gold.append([sprite,string])
        def add_thanks(self,sprite,string): self.thanks.append([sprite,string])

        def buy_item(self, item):
            cost = item.cost
            if not inventory.has_space():
                self.say("no_space")
            #    return self.no_space
            elif player.gold<cost:
                self.say("no_gold")
            #    return self.no_gold
            else:
                player.gold -= cost
                inventory.add(item)
                self.say("thanks")
            #    return self.thanks
        #def print_dialog(self, dialogues):
        #    for d in dialogues: 
        #        renpy.show(d.sprite)
        #        renpy.say(self.name,d.dialogue)
        def enter(self):
            renpy.show_screen("shop_box",self)
            renpy.scene()
            renpy.show(self.scene)

            self.say("welcome")
            self.enter()
            #call a label that calls the screens
            #talk dialog box
            # buy box
            #show needed screens
            #print welcome dialog
            #at the end of each dialog, print out welcome dialog again
        def exit(self):
            
            #renpy.hide()
            renpy.call(label='shop_exit')
            #print exit dialog
            #close all screens
            #return.renpy_statement
        #enter exit store
        def dialog(self,choice):
            if choice == "talk":
                return self.talk
            elif choice == "sell":
                return self.sell
            elif choice == "exit":
                return self.exit
            elif choice == "no_space":
                return self.no_space
            elif choice == "no_gold":
                return self.no_gold
            elif choice == "thanks":
                return self.thanks
            else:
                return self.welcome
        def hide_sprites(self):
            for i in self.sprites:
                renpy.hide(i)
        def say(self,choice):
            #place these in new function hideallimages
            
            renpy.show_screen("shop_box",self)
            for line in self.dialog(choice):
                self.hide_sprites()
                renpy.show(line[0])
                renpy.say(self.template,line[1])

        def show_shop_box(self):
            renpy.show_screen("shop_box",self)


        def running(self,bool):
            if bool == False:
                self.exit()
screen shop_box(shop):
    frame pos(int(screen_width*.728),.74):
        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK" action [Play ("sound", "audio/click.wav"),renpy.curried_invoke_in_new_context(shop.say,"talk") ] background "#000000"
            textbutton "BUY" action [Play ("sound", "audio/click.wav")] background "#000000"
            textbutton "SELL" action [Play ("sound", "audio/click.wav"),renpy.curried_invoke_in_new_context(shop.say,"sell")] background "#000000"
            textbutton "EXIT" action [Play ("sound", "audio/click.wav"),renpy.curried_invoke_in_new_context(shop.say,"exit")] background "#000000"


label Muffet_Shop:
    python:
        muffetShop = Shop()

        muffetShop.enter()
label shop_exit:
    return