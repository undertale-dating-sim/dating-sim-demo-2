init:
    $ screen_width = config.screen_width # 800
    $ screen_height = config.screen_height # 600
    $ shop_dialog_width = int(screen_width*.70)
    $ shop_dialog_height = int(screen_height*.215)



define payneShop = Character('PayneGray',
    window_background=Frame("text-box3.png",21,21),
    window_left_margin = int(screen_width*.02),
    window_right_margin = int(screen_width*.265),
    window_top_margin = int(screen_height*(-.05)),#-30,
    window_bottom_margin = 16,
    window_top_padding = 10,
    window_bottom_padding = 10,
    window_left_padding = 15,
    window_right_padding = 15)

screen shop_box(shop):
    ### Main Shop Menu Box###
    frame pos(int(screen_width*.73),.688):#int(screen_height*.00117)
        background Frame("text-box3.png",21,21)
        #maximum(int(screen_width*.24),int(screen_height*.269))
        #minimum(int(screen_width*.24),int(screen_height*.269))
        vbox:
            anchor(-.25,0)
            #maximum(int(screen_width*.24),int(screen_height*.215))
            #minimum(int(screen_width*.24),int(screen_height*.215))
            maximum(int(screen_width*.24),int(screen_height*.267))
            minimum(int(screen_width*.24),int(screen_height*.267))
            #change this into text prompt stuff
            #if buy is clicked = What would you like to buy?
            #and make sure to have an exit
            textbutton "BUY" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.buy_button_clickable,NullAction(),NullAction())]
            textbutton "SELL" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.sell_button_clickable,renpy.curried_invoke_in_new_context(shop.say,"sell"),NullAction())]
            textbutton "TALK" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.talk_button_clickable,[renpy.curried_invoke_in_new_context(shop.say,"talk")],NullAction())] 
            textbutton "EXIT" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.exit_button_clickable,renpy.curried_invoke_in_new_context(shop.say,"exit"),NullAction())]
            hbox:
                #anchor(0,0)
                vbox:
                    anchor(42,0)
                    text "[player.gold]G" xalign 0.5

                vbox:
                    #anchor(-40,0)
                    text "[inventory.empty_spaces]/[inventory.max_items]" text_align 1.0
screen buy_box:
    ###  ###
    #frame pos(int(screen_width*.02),.10):
    frame pos(int(screen_width*.02),.688):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                textbutton "Test - 5G" background "#000000" 
                textbutton "Test - 5G" background "#000000" 
                textbutton "Test - 5G" background "#000000" 
                textbutton "Test - 5G" background "#000000" 
                textbutton "Exit" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.buy_button_clickable,NullAction(),NullAction())]

init -1 python:
    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.template = payneShop.copy(self.name,window_top_margin = int(screen_height*(-.064)))
            self.sprites = ["sans","flowey"]
            self.scene = "background snowdin"

            self.talk_button_clickable = True
            self.buy_button_clickable = True
            self.sell_button_clickable = True
            self.exit_button_clickable = True

            self.items = [["Snow Sans",50],["Snow Sans",50],["Snow Sans",50],["Snow Sans",50]]

            self.welcome = [ ["flowey normal","Welcome to my store!!\nHurray!\nHurray!\nHurray!"]]

            #talk would lead to several dialog options, but I'll leave it like this for now
            self.talk = [["sans normal","Hello"], ["flowey normal","testing talk"]]
            self.sell = [["sans normal","Hello"], ["flowey normal","testing sell"]]
            self.exit = [["sans normal","Hello"], ["flowey normal","testing exit"]]


        ###Shop Access Functions###

        def enter(self):
            #renpy.say(self.buy_template,"Testing")
            #renpy.show_screen("buy_box",self)
            renpy.scene()
            
            renpy.show(self.scene)

            #renpy.show_screen("shop_box",self)
            self.say("welcome")
            
            
            #nvl_show
            #self.buy()
        #def buy(self):
            
        ### Dialog Access Functions ###

        def say(self,choice):
            if choice == "welcome":
                self.enable_buttons()
            else:
                self.disable_buttons()
                #call a label that hides the window, do your stuff, and show it again
            renpy.show_screen("shop_box",self)
            for line in self.dialog(choice):
                self.hide_sprites()
                renpy.show(line[0])
                renpy.say(self.template,line[1])

            self.enable_buttons()
            renpy.call_in_new_context(label="window_hide",shop=self)
            #if choice = buy
            #show buy box
            #if exit is clicked, then self.enter
            self.enter()
        #def shop_text():

        def enable_buttons(self):
            self.talk_button_clickable = True
            self.buy_button_clickable = True
            self.sell_button_clickable = True
            self.exit_button_clickable = True

        def disable_buttons(self):
            self.talk_button_clickable = False
            self.buy_button_clickable = False
            self.sell_button_clickable = False
            self.exit_button_clickable = False

        def dialog(self,choice):
            dialog = {"talk":self.talk,"sell":self.sell,"exit":self.exit,"welcome":self.welcome}
            return dialog[choice]

        def hide_sprites(self):
            for i in self.sprites:
                renpy.hide(i)

        ### Shop Functions ###
        def add_item(self,item): self.items.append(item)

label Muffet_Shop:
    python:
        muffetShop = Shop()
        muffetShop.enter()

label nvl_clear:
    nvl clear
label window_hide(shop):
    window hide
    show screen buy_box
    show screen shop_box(shop)
    pause
    pause
    window show
#label window_show:
#    window show