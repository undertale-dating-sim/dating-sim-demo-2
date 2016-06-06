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
screen show_store_button:
    textbutton "Show Store" action [Play ("sound", "audio/click.wav"),Show("storekeeper"),Show("store_dialog"),Hide("show_store_button")] align(.70,.05) background Frame("text-box3.png",50, 21)

screen storekeeper:
    textbutton "Hide Store" action [Play ("sound", "audio/click.wav"),Hide("storekeeper"),Hide("store_dialog"),Show("show_store_button")] align(.70,.05)  background Frame("text-box3.png",50, 21)
    frame pos(.8,.8):
        background Frame("text-box3.png",21,21)
        hbox:
            vbox:
                text "Patience:"
                text "Integrity:"
                text "Bravery:"
                text "Perseverance:"
screen store_dialog:
    frame pos(0,.8):
        background Frame("text-box3.png",21, 21)
        hbox:
            vbox:
                text "Patience:"
                text "Integrity:"
                text "Bravery:"
                text "Perseverance:"               
#        def add_button(self,button):
            #check to see if buttons are already in place
#            textbutton button action [Play ("sound", "audio/click.wav"),Show("show_menu"),Hide("show_menu_button"),Show("stats")] align(.95,.05) background Frame("text-box3.png",50, 21)
    #class store_dialog():
    #    def __init__(self):
    #show the screen and then access dialog

#screen show_menu_button:
#    textbutton "Show Menu" action [Play ("sound", "audio/click.wav"),Show("show_menu"),Hide("show_menu_button"),Show("stats")] align(.95,.05) background Frame("text-box3.png",50, 21)

#screen show_menu:
#    add "#0008"
#    modal True
#    #hide button
#    textbutton "Hide Menu" action [Play ("sound", "audio/click.wav"),Hide("show_menu"),Show("show_menu_button"),Hide("items"),Hide("stats"),Hide("cell"),Hide("show_item_description")] align(.95,.05)  background Frame("text-box3.png",50, 21)
#    vbox xalign 0.1 ypos 0.1:
#        frame:
#            background Frame("text-box3.png",21, 21)       
#            vbox:
#                text "[player.name]"
#                text "Day: [day]"
#                text "HP:  [player.current_health]/[player.total_health]"
#                text "G:   [player.gold]"

#        frame  ypos 0.5:
#            background Frame("text-box3.png",21, 21)
#            vbox:
#                textbutton "ITEM" action [Play ("sound", "audio/click.wav"),Show("items"),Hide("stats"),Hide("cell")] background "#000000"
#                textbutton "STAT" action [Play ("sound", "audio/click.wav"),Show("stats"),Hide("items"),Hide("cell")] background "#000000"
#                textbutton "CELL" action [Play ("sound", "audio/click.wav"),Show("cell"),Hide("stats"),Hide("items")] background "#000000"



#screen stats:
#    frame pos(0.3,0.05):
#        background Frame("text-box3.png",21, 21)
#        hbox:
#            vbox:
#                text "Patience:"
#                text "Integrity:"
#                text "Bravery:"
#                text "Perseverance:"
#                text "Kindness:"    
#                text "Justice:"
#            vbox:
#                text "[player.patience_impulsiveness]"
#                text "[player.integrity_deceit]"
#                text "[player.bravery_cowardice]"
#                text "[player.perseverance_surrender]"
#                text "[player.kindness_cruelty]"
#                text "[player.justice_apathy]"                    

#show two screens
#plans later

#first screen will be replaced with another screen when other dialogs are added
#label storekeeper:
#    screen store_menu_box:
#        tag example
#        zorder 1
#        modal False

#        text "Hello, World."

# plans:
    # There should be a class where we can show sprites
    # Inventory
    # changes gold amount
    # increase friendship with storekeeper?
    # Dialog options accessed from the script


#python:
#    def menu_template(items=[],gold):
#        for i in len(0,len(items)-1):
