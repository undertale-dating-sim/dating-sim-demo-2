init -5 python:
    class Item():
        def __init__(self):
            self.name =         "default"
            self.pickup_text =  "default"
            self.drop_text =    "default"
            self.truelove_text = "default"
            self.heartbreak_text = "default"
            self.neutral_text = "default"
            self.friendship_text = "default"
            self.menu_desc = "default"
            self.sale_cost = 1
            self.use_text = ""
            self.sprite = ""
            self.usable = True
            self.equip = False

        def give(self,character):
            return

        def use(self):
            player.gold += self.sale_cost
            inventory.drop(self)
            return

        def get_class_name(self):
            return self.__class__.__name__

init -1 python:
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
            else:
                renpy.notify(item.name+ " not found")

        def has_space(self):
            if len(self.items) < self.max_items:
                return True
            return False

        def get_count(self,item):
            count = 0
            for i in items:
                if isinstance(i,item):
                    count += 1
            return count




    menu_selected_item = False
    #move to global portion of initiate.rpy later
    inventory = Inventory()
    # inventory.add(Sleeping_Potion())
    # inventory.add(Spider_Donut())
    # inventory.add(Milk_Chocolate())
    # inventory.add(Broken_Mirror())
    # inventory.add(Rose())
    

screen items:
        frame pos(0.4,0.05):
            vbox:
                for item in inventory.items:
                    textbutton "[item.name]":
                        action [SetVariable("menu_selected_item",item)]
                        background "#000000"
                for i in range(0,inventory.max_items - len(inventory.items)):
                    textbutton "----------":
                        background "#000000"

      
                hbox:
                    if menu_selected_item:
                        if menu_selected_item.equip:
                            textbutton "Equip":
                                action [If(menu_selected_item,ui.callsinnewcontext("equip_item",menu_selected_item)),SetVariable("menu_selected_item",False)]
                                background "#000000"

                            textbutton "Info":
                                action [If(menu_selected_item,ui.callsinnewcontext("show_item_description",menu_selected_item)),SetVariable("menu_selected_item",False)]
                                background "#000000"
                            
                            # textbutton "Unequip":
                            #     action [If(menu_selected_item,ui.callsinnewcontext("unequip_item",menu_selected_item)),SetVariable("menu_selected_item",False)]
                            #     background "#000000"

                        else:
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
                    image im.Scale(menu_selected_item.sprite,200,150)
                    vbox:
                        box_wrap True
                        spacing 5
                        xmaximum 150
                        text "[menu_selected_item.name]"
                        text "[menu_selected_item.menu_desc]"


                        
                        

label show_item_description(item):
    "[item.neutral_text]"
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

#nasty function.
label equip_item(item):
    if item.equip: #if we can equip the item
        if player.equipped_item:
            if inventory.has_space():
                $ inventory.add(player.equipped_item)
                $ player.equipped_item.unequip_self()
                $ player.equipped_item = item
                $ item.equip_self()
                if item in inventory.items:
                    $ inventory.drop(item)
                "You equip the [item.name]."
            else:
                "Can't equip. No space for current item."
        else:
            $ player.equipped_item = item
            $ item.equip_self()
            if item in inventory.items:
                    $ inventory.drop(item)
            "You equip the [item.name]."

    else:
        "EQUIPMENT FAILURE: CODE WILSON"
    return

label unequip_item():
    $ player.equipped_item = False
    return

label pickup_item(item):
    if inventory.has_space():
        $ inventory.add(item)
        "[item.pickup_text]"
    else:
        call inventory_full from _call_inventory_full
    return

