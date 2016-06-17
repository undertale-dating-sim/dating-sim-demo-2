
#split this to multiple files
screen buy_box(obj,shop):

    #takes in shop class
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                #text name size 25
                grid 2 len(obj)/2: #Find a way to count this stuff. Len(obj)? 
                # or if there are more items, add a button to lead to another page
                # don't let player.gold be less than 0
                    for item in obj:
                        $ cost = item[1]
                        textbutton "[item[0]] - [item[1]]G" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("buy_item",cost = cost,shop=shop)] background "#000000" 


screen shop_box(shop):
    frame pos(int(screen_width*.728),.74):
        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.talk_dialog) ] background "#000000"
            textbutton "BUY" action [Play ("sound", "audio/click.wav"),Show("buy_box",transition=None,obj=shop.items, shop = shop)] background "#000000"
            textbutton "SELL" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.sell_dialog)] background "#000000"
            textbutton "EXIT" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.exit_dialog)] background "#000000"



screen empty_dialog:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)


label shop_text(shop,dialog):
    show screen shop_box(shop)
    python:
        for line in dialog:
            renpy.say(payneShop.copy(shop.name),line)
    show screen empty_dialog
    # Bug: clicking the empty dialog makes this move to the next label, shop_item. A fix would be to make the dialog box unclickable. Or prompt a hidden menu
    pause
init -1 python:
    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.items = []
            self.cost = []
            self.talk_dialog = ["This is the talk dialog.","This is more dialog.","Yet more."]
            self.sell_dialog = ["This is my sell dialog.","There are many like it","But this one is mine"]
            self.exit_dialog = ["This is the exit dialog.","I should also make it so that","return is used at the end."]


            self.no_space_dialog = []
            self.no_gold_dialog = []

            self.images = []

        def set_name(self, name):
            self.name = name
        def add_items(self, item,cost):
            self.items.append([item,cost])

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
        def start(self):
            renpy.call_screen('shop_box',self)

label buy_item(cost, shop):
    #make sure that player gold doesn't go lower than zero
    # show a dialog box that shows why they can't buy the item
    show screen shop_box(shop)
    show screen buy_box(shop.items,shop)
    $ player.gold -= cost
    #$ inventory.add(item)

    
label Muffet_Shop:
    show screen show_menu_button
    $ spiderBakery = Shop()
    python:
        spiderBakery.set_name("Muffet")
        spiderBakery.add_items("Spider Donut",7)
        spiderBakery.add_items("Spider Cider",18)
        spiderBakery.add_items("Spider Cake",10)
        spiderBakery.add_items("Spider Waffle",7)
        spiderBakery.start()
