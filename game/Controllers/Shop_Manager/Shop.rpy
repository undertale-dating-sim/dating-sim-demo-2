
init -1 python:
    class Shop():
        def __init__(self):
            self.keeper = "Sans"
            self.item = ["Fried Snow - 50G","Old Sock - 100G","Blue Jacket - 500","Red Scarf - 5000G"]
            self.talk_dialog = ["heya. Wanna buy some fried snow?"]
            self.sell_dialog = ["hahaha. nope. no can do. haven't you played undertale?"]
            self.exit_dialog = ["see ya."]
            self.button = ["ITEM"]
            self.sprite = "characters/sans-normal.png"
            self.font = None
        def modify_name(self,name):
            self.keeper = name
        def add_item(self,item):
            self.item += item
        #def remove_item(self,item):
        #    pop(self.item)
        def set_sprite(self,sprite):
            self.sprite = sprite
        def set_font(self,font):
            self.font = font

screen show_shop_button:
    
    textbutton "Show Shop" action [Play ("sound", "audio/click.wav"),Show("shop_menu"),Show("show_shop_button"),Show("shop_dialog_talk"),Hide("shop_dialog_buy"),Hide("shop_dialog_sell"),Hide("shop_dialog_exit")] align(.70,.05) background Frame("text-box3.png",50, 21)
#screen shop_description:
    #hopefully, I can show an image+item description in the middle of the screen whenever a button is clicked
    #Buy and cancel buttons
screen shop_menu:
    textbutton "Hide Shop" action [Play ("sound", "audio/click.wav"),
        Hide("shop_dialog_exit"),
        Hide("shop_dialog_talk"),
        Hide("shop_dialog_buy"),
        Hide("shop_menu"),
        Show("show_shop_button")] align(.70,.05) background Frame("text-box3.png",50, 21)
    frame pos(int(screen_width*.728),.74): #position within the screen

        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK" action [Play ("sound", "audio/click.wav"),Show("shop_dialog_talk"),Hide("shop_dialog_buy"),Hide("shop_dialog_sell"),Hide("shop_dialog_exit")] background "#000000"
            textbutton "BUY" action [Play ("sound", "audio/click.wav"),Hide("shop_dialog_talk"),Show("shop_dialog_buy"),Hide("shop_dialog_sell"),Hide("shop_dialog_exit")] background "#000000" 
            textbutton "SELL" action [Play ("sound", "audio/click.wav"),Hide("shop_dialog_talk"),Hide("shop_dialog_buy"),Show("shop_dialog_sell"),Hide("shop_dialog_exit")] background "#000000"
            textbutton "EXIT" action [Play ("sound", "audio/click.wav"),Hide("shop_dialog_talk"),Hide("shop_dialog_buy"),Hide("shop_dialog_sell"),Show("shop_dialog_exit")] background "#000000"
#
screen shop_dialog_talk:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            has vbox:
                text "[shop.keeper]" size 25
                text "[shop.talk_dialog[0]]"
                # This is working well somehow. I need to figure out how to click to continue through text

screen shop_dialog_buy:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                text "[shop.keeper]" size 25
                #grid
                hbox:
                    textbutton "[shop.item[0]]" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "[shop.item[1]]" action [Play ("sound", "audio/click.wav")] background "#000000"
                hbox:
                    textbutton "[shop.item[2]]" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "[shop.item[3]]" action [Play ("sound", "audio/click.wav")] background "#000000"
screen shop_dialog_sell:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)

            has vbox:
                text "[shop.keeper]" size 25
                text "[shop.sell_dialog[0]]"

screen shop_dialog_exit:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)

        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)

            has vbox:
                text "[shop.keeper]" size 25
                text "[shop.exit_dialog[0]]"
                # This is working well somehow. I need to figure out how to click to continue through text
# Hide other menus when an option is pressed
# Text depends on class input