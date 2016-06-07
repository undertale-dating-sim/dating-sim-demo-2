
init -1 python:
    class Shop():
        def __init__(self):
            self.shopkeeper_name = "Temmie"
            self.items = []
            self.dialogs = []
            self.button = "ITEM"
            self.sprite = None
            self.font = None
        def modify_name(self,name):
            self.shopkeeper_name = name
        def add_item(self,item):
            self.item += item
        def add_dialog(self,dialog):
            self.dialogs += dialog
        def set_sprite(self,sprite):
            self.sprite = sprite
        def set_font(self,font):
            self.font = font
screen show_shop_button:
    textbutton "Show Shop" action [Play ("sound", "audio/click.wav"),Show("shop_menu"),Show("show_shop_button"),Show("shop_dialog_talk"),Hide("shop_dialog_buy"),Hide("shop_dialog_sell"),Hide("shop_dialog_exit")] align(.70,.05) background Frame("text-box3.png",50, 21)

            
screen shop_menu:
    textbutton "Hide Shop" action [Play ("sound", "audio/click.wav"),
        Hide("shop_dialog_exit"),
        Hide("shop_dialog_talk"),
        Hide("shop_dialog_buy"),
        Hide("shop_menu"),
        Show("show_shop_button")] align(.70,.05)  background Frame("text-box3.png",50, 21)
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
            maximum(int(screen_width*.68),int(screen_height*.215))
            minimum(int(screen_width*.68),int(screen_height*.215))
            has vbox:
                text "Sans" size 25
                text "heya. Wanna buy some fried snow?"
                # This is working well somehow. I need to figure out how to click to continue through text

screen shop_dialog_buy:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(int(screen_width*.68),int(screen_height*.215))
            minimum(int(screen_width*.68),int(screen_height*.215))
            has vbox:
                text "Sans" size 25
                hbox:
                    textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
                hbox:
                    textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
        #vbox align(0.01,0.01) box_wrap True:
        #        #xmaximum int(screen_width*.65)
        #        anchor(0,0)
        #        maximum(int(screen_width*.68),int(screen_height*.215))
        #        minimum(int(screen_width*.68),int(screen_height*.215))
        #        vbox:
        #            text "Sans" size 25
        #        vbox: #make grid of 4
        #            hbox:
        #                textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
        #                textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
        #            hbox:
        #                textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
        #                textbutton "Fried Snow - 50G" action [Play ("sound", "audio/click.wav")] background "#000000"
screen shop_dialog_sell:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(int(screen_width*.68),int(screen_height*.215))
            minimum(int(screen_width*.68),int(screen_height*.215))
            has vbox:
                text "Sans" size 25
                text "no can do. haven't you played undertale?"

screen shop_dialog_exit:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)

        window xmargin -21 ymargin -21:
            maximum(int(screen_width*.68),int(screen_height*.215))
            minimum(int(screen_width*.68),int(screen_height*.215))
            has vbox:
                text "Sans" size 25
                text "goodbye."
                # This is working well somehow. I need to figure out how to click to continue through text
# Hide other menus when an option is pressed
# Text depends on class input