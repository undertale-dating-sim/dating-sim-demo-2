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


screen shop_box(shop):
    ### Main Shop Menu Box###
    frame pos(int(screen_width*.728),.74):
        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.talk_button_clickable,[renpy.curried_invoke_in_new_context(shop.say,"talk")],NullAction())] 
            textbutton "BUY" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.buy_button_clickable,NullAction(),NullAction())]
            textbutton "SELL" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.sell_button_clickable,renpy.curried_invoke_in_new_context(shop.say,"sell"),NullAction())]
            textbutton "EXIT" background "#000000" action [Play ("sound", "audio/click.wav"),If(shop.exit_button_clickable,renpy.curried_invoke_in_new_context(shop.say,"exit"),NullAction())]

screen buy_box(obj,shop):
    ###  ###
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                text shop.name size 25
                grid 2 len(obj)/2:
                    for item in obj:
                        $ cost = item[1]
                        $ itemTemp = item[0]
                        $ itemclass = item[2]
                        textbutton "[item[0]] - [item[1]]G" action [Play ("sound", "audio/click.wav"),Show("show_menu_button"),Show("buy_prompt",item = itemTemp,cost = cost,shop=shop,itemclass=itemclass)] background "#000000" 


init -1 python:
    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.template = payneShop.copy(self.name)

            self.sprites = ["sans","flowey"]
            self.scene = "background snowdin"

            self.talk_button_clickable = True
            self.buy_button_clickable = True
            self.sell_button_clickable = True
            self.exit_button_clickable = True

            self.items = []

            self.welcome = [ ["flowey normal","Welcome to my store!!"]]

            #talk would lead to several dialog options, but I'll leave it like this for now
            self.talk = [["sans normal","Hello"], ["flowey normal","testing talk"]]
            self.sell = [["sans normal","Hello"], ["flowey normal","testing sell"]]
            self.exit = [["sans normal","Hello"], ["flowey normal","testing exit"]]


        ###Shop Access Functions###

        def enter(self):
            renpy.show_screen("shop_box",self)
            renpy.scene()
            renpy.show(self.scene)
            self.say("welcome")


        ### Dialog Access Functions ###

        def say(self,choice):
            if choice == "welcome":
                self.enable_buttons()
            else:
                self.disable_buttons()
            renpy.show_screen("shop_box",self)
            for line in self.dialog(choice):
                self.hide_sprites()
                renpy.show(line[0])
                renpy.say(self.template,line[1])
            self.enable_buttons()
            self.enter()

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
