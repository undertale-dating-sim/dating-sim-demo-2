
init -1 python:
    class store_menu():
        def __init__(self):
            self.shopkeeper_name = "Temmie"
            self.items = []
            self.dialogs = []
            self.button = "ITEM"
            self.sprite = None
        def modify_name(self,name):
            self.shopkeeper_name = name
        def add_item(self,item):
            self.item += item
        def add_dialog(self,dialog):
            self.dialogs += dialog
        def set_sprite(self,sprite):
            self.sprite = sprite
screen show_shop_button:
    textbutton "Show Shop" action [Play ("sound", "audio/click.wav"),Show("shop"),Hide("show_shop_button")] align(.70,.05) background Frame("text-box3.png",50, 21)

#I need to smack my head repeatedly on a wall for not realizing that "dialogue" can handle most of the stuff this needs ><
screen shop(dialogue,items=None):
    textbutton "Hide Shop" action [Play ("sound", "audio/click.wav"),Hide("shop"),Show("show_shop_button")] align(.70,.05)  background Frame("text-box3.png",50, 21)
    frame pos(.01,.75):
        background Frame("text-box3.png",21,21)
        hbox:
            xysize(screen_width*.965,screen_height*.205)  # I found it easier to use xysize since it sets up both xsize and ysize
            vbox xalign 0.15 ypos 0.05:
                xysize(.7,1)
                text "Dialog Test Dialog"
                text "Dialog Test Dialog Test"
                text "Dialog Test Dialog Test Dialog"
                text "Dialog Test Dialog Test Dialog Test"
                
            vbox xalign 0 ypos 0.05:
                xysize(.2,1)
                text "Shop Test"
                text "Shop Test"
                text "Shop Test"
                text "Shop Test"