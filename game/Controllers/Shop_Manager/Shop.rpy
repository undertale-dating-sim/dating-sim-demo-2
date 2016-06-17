screen buy_box(name,obj):
    #takes in shop class
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                #text name size 25
                grid 2 len(obj)/2: #Find a way to count this stuff. Len(obj)? 
                #if there are more items, add a button to lead to another page
                    for item in obj:
                        textbutton "[item]" action [Play ("sound", "audio/click.wav")] background "#000000" #action, add to inventory, subtract from gold

screen shop_box(shop):
    #ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.talk_dialog)
    #textbutton "Hide Shop" action [Play ("sound", "audio/click.wav"),Hide("shop_dialog_exit"),Hide("shop_dialog_talk"),Hide("shop_dialog_buy"),Hide("shop_menu"),Show("show_shop_button")] align(.70,.05) background Frame("text-box3.png",50, 21)
    frame pos(int(screen_width*.728),.74): #position within the screen
        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.talk_dialog) ] background "#000000"
            textbutton "BUY" action [Play ("sound", "audio/click.wav"),Show("buy_box",transition=None,name = shop.name,obj=shop.items)] background "#000000" #call buy box
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
    #payneShop.copy("[shop.name]") "[shop.talk_dialog[1]]"
    python:
        for line in dialog:
            renpy.say(payneShop.copy(shop.name),line)
    show screen empty_dialog
init -1 python:
    class Shop():
        def __init__(self):
            self.name = "PayneGray"
            self.items = []
            self.cost = []
            self.talk_dialog = ["This is the talk dialog.","This is more dialog.","Yet more."]
            self.sell_dialog = ["This is my sell dialog.","There are many like it","But this one is mine"]
            self.exit_dialog = ["This is the exit dialog.","I should also make it so that","return is used at the end."]
            self.images = []
        def set_name(self, name):
            self.name = name
        def add_items(self, item):
            self.items.append(item)
        def add_cost(self, cost):
            self.cost.append(cost)
        def set_talk(self,talk_dialog):
            self.talk_dialog = talk_dialog
        def set_sell(self,sell_dialog):
            self.sell_dialog = sell_dialog
        def set_exit(self,talk_dialog):
            self.exit_dialog = exit_dialog

        def call_talk_dialog(self,num):
            return self.talk_dialog[num]
        def len_talk_dialog(self,talk_dialog):
            return len(talk_dialog)
        def add_talk(self,talk_dialog):
            self.talk_dialog.append(talk_dialog)
        def add_sell(self,sell_dialog):
            self.sell_dialog.append(sell_dialog)
        def add_exit(self,exit_dialog):
            self.exit_dialog.append(exit_dialog)
        def start(self):
            renpy.call_screen('shop_box',self)
            #renpy.call_in_new_context('shop_text',self, self.talk_dialog))
            #,self.name,self.items,self.talk_dialog,self.sell_dialog,self.exit_dialog,
    #class Shop_Menu():
        
        #accesses dialog boxes
        #show buybox
        #assign dialogs to shop box

label Muffet_Shop:
    $ spiderBakery = Shop()
    python:
        spiderBakery.set_name("Muffet")
        spiderBakery.add_items("Spider Donut")
        spiderBakery.add_items("Spider Cider")
        spiderBakery.add_items("Spider Cake")
        spiderBakery.add_items("Spider Waffle")
        spiderBakery.add_items("Spider Cake")
        spiderBakery.add_items("Spider Waffle")
        spiderBakery.start()
