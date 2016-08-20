init -1 python:
    class Item():
        def __init__(self):
            self.name =         "default"
            self.pickup_text =  "default"
            self.drop_text =    "default"
            self.negative_text = "default"
            self.positive_text = "default"
            self.sale_cost = 1
            self.shop_text = "default"
            self.use_text = ""
            self.sprite = ""
            self.menu_desc = ""

        def give(self,character):
            return

        def use(self):
            player.gold += self.sale_cost
            inventory.drop(self)
            return

    class Spider_Donut(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Donut"
            self.use_text = "You bite down, but something stops you. It had a coin in it?  What was the point of buying this?"
            self.pickup_text = "It is a donut. Made of spiders. Crunchy!"
            self.sprite = "items/item_spiderdonut.png"
            self.menu_desc = "It is a donut. \nRestore 10 Stamina"

            

    class Spider_Cider(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Cider"
            self.sale_cost = 5
            self.use_text = "Spiders pour over your face. It had "+str(self.sale_cost)+" coin(s) in it.  What was the point of buying this?"
            self.pickup_text = "A bottle full of spiders. You can hear coins jiggle if you shake it."
            self.sprite = "items/item_spidercider.png"
            self.menu_desc = "A bottle full of spiders. \nRestore 50 Stamina"


    class Inventory():
        def __init__(self):
            self.items = []
            self.max_items = 5
            
        def add(self, item): # a simple method that adds an item;
            if self.has_space():
                self.items.append(item)

                
        def drop(self, item):
            if self.items.count(item) > 0:
                self.items.remove(item)

        def has_space(self):
            if len(self.items) < self.max_items:
                return True
            return False


    menu_selected_item = False
    #move to global portion of initiate.rpy later
    inventory = Inventory()
    inventory.add(Spider_Cider())
    inventory.add(Spider_Donut())
    

screen items:
        frame pos(0.3,0.05):
            vbox:
                for item in inventory.items:
                    textbutton "[item.name]":
                        action [SetVariable("menu_selected_item",item)]
                        background "#000000"
                for i in range(0,inventory.max_items - len(inventory.items)):
                    textbutton "----------":
                        background "#000000"

      
                hbox:
                    textbutton "Use":
                        action [If(menu_selected_item,ui.callsinnewcontext("use_item",menu_selected_item)),SetVariable("menu_selected_item",False)]
                        background "#000000"

                    textbutton "Info":
                        action [If(menu_selected_item,ui.callsinnewcontext("show_item_description",menu_selected_item)),SetVariable("menu_selected_item",False)]
                        background "#000000"
                        
                    textbutton "Drop":
                        action [If(menu_selected_item,ui.callsinnewcontext("drop_item",menu_selected_item)),SetVariable("menu_selected_item",False)]
                        background "#000000"

        if menu_selected_item:
            frame pos(0.3,0.5):
                hbox:
                    image menu_selected_item.sprite
                    vbox:
                        box_wrap True
                        spacing 5
                        xmaximum 150
                        text "[menu_selected_item.name]"
                        text "[menu_selected_item.menu_desc]"


                        
                        

label show_item_description(item):
    "[item.pickup_text]"
    return

label inventory_full:
    "Your bag is full."
    return

label use_item(item):
    "You use the [item.name]."
    if item.use_text != "":
        "[item.use_text]"
    $ item.use()
    return

label drop_item(item):
    "You drop the [item.name]."
    $ inventory.drop(item)
    return

label pickup_item(item):
    if inventory.has_space():
        $ inventory.add(item)
        "[item.pickup_text]"
    else:
        call inventory_full from _call_inventory_full
    return
