#This will hold all the main Shop() class and all instances of Shop()
# To add shops, make another label
init -1 python:
    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.items = []
            self.cost = []

            self.opening_dialog = ["Welcome to my parlour, dearie~"]

            self.talk_dialog = ["This is the talk dialog.","This is more dialog.","Yet more."]
            self.sell_dialog = ["This is my sell dialog.","There are many like it","But this one is mine"]
            self.exit_dialog = ["This is the exit dialog.","I should also make it so that","return is used at the end."]


            self.no_space_dialog = ["You have no space in your bag."]
            self.no_gold_dialog = ["You don't have enough gold.", "Get out."]

            self.images = []

        def set_name(self, name):
            self.name = name
        def add_items(self, item,cost,itemclass):
            self.items.append([item,cost,itemclass])

        def set_talk(self,talk_dialog):
            self.talk_dialog = talk_dialog
        def set_sell(self,sell_dialog):
            self.sell_dialog = sell_dialog
        def set_exit(self,talk_dialog):
            self.exit_dialog = exit_dialog

        

        def add_talk(self,talk_dialog):
            self.talk_dialog.append(talk_dialog)
        def add_sell(self,sell_dialog):
            self.sell_dialog.append(sell_dialog)
        def add_exit(self,exit_dialog):
            self.exit_dialog.append(exit_dialog)
            #return
        def start(self):
            #renpy.say(payneShop.copy(self.name),self.opening_dialog[0])
            #renpy.call_screen('shop_box',self)
            renpy.call(label='shop_opening',shop=self)


    
label Muffet_Shop:
    show screen show_menu_button
    $ spiderBakery = Shop()
    python:
        spiderBakery.set_name("Muffet")
        spiderBakery.add_items("Spider Donut",7,Spider_Donut())
        spiderBakery.add_items("Spider Cider",18,Spider_Cider())
        spiderBakery.add_items("Spider Cake",10,Spider_Cake())
        spiderBakery.add_items("Spider Waffle",7,Spider_Waffle())
        spiderBakery.start()
