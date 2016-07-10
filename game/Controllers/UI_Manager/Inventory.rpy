init -1 python:
    class Item():
        def __init__(self):
            self.name =         "default"
            self.pickup_text =  "default"
            self.drop_text =    "default"
            self.negative_text = "default"
            self.positive_text = "default"
    class Empty(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "--------"
            self.pickup_text = ""
    class Inventory():
        def __init__(self):
            self.items = []
            self.max_items = 5
            self.fill_empty_space()

        def add(self, item): # a simple method that adds an item;
            if self.has_space():
                self.items.insert(self.first_empty(),item)
                self.items.pop()

                
        def drop(self, item):
            if self.items.count(item) > 0:
                self.items.remove(item)
                self.fill_empty_space()

        def has_space(self):
            for item in self.items:
                if isinstance(item,Empty):
                    return True
            return False

        def first_empty(self):
            for item in self.items:
                if isinstance(item,Empty):
                    return self.items.index(item)

        def fill_empty_space(self):
            while len(self.items) < self.max_items:
                self.items.append(Empty())

    #holds the description for the menu.  HAS to be a better way to do this
    menu_selected_item = False
    #move to global portion of initiate.rpy later
    inventory = Inventory()
    

screen items:
        frame pos(0.3,0.05):
            background Frame("UI/text-box3.png",21, 21)
            vbox:
                for item in inventory.items:
                    if isinstance(item,Empty):
                        textbutton "[item.name]":
                            background "#000000"
                    else:
                        textbutton "[item.name]":
                            action [SetVariable("menu_selected_item",item)]
                            background "#000000"

      
                hbox:
                    textbutton "Use":
                        action [If(menu_selected_item,ui.callsinnewcontext("show_item_description")),SetVariable("menu_selected_item",False)]
                        background "#000000"

                    textbutton "Info":
                        action [If(menu_selected_item,ui.callsinnewcontext("show_item_description")),SetVariable("menu_selected_item",False)]
                        background "#000000"
                        
                    textbutton "Drop":
                        action [If(menu_selected_item,ui.callsinnewcontext("drop_item")),SetVariable("menu_selected_item",False)]
                        background "#000000"
                        

label show_item_description:
    "[menu_selected_item.pickup_text]"
    return

label inventory_full:
    "Your bag is full."
    return

label drop_item():
    "You drop the [menu_selected_item.name]"
    $ inventory.drop(menu_selected_item)
    return

label pickup_item(item):
    if inventory.has_space():
        $ inventory.add(item)
        "[item.pickup_text]"
    else:
        call inventory_full from _call_inventory_full
    return

#items

init -1 python:
    

    class Heart_Locket(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Heart Locket"
            self.pickup_text = "It doesn't seem to open, but it is pretty nonetheless, golden and strung on a red ribbon."

    class Spider_Donut(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Donut"
            self.pickup_text = "Made with real spiders."
            self.cost = 7
    class Spider_Cider(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Cider"
            self.pickup_text = "Made with real spiders."
            self.cost = 18
    class Spider_Waffle(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Waffle"
            self.pickup_text = "Made with real spiders."
            self.cost = 10
    class Spider_Cake(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Cake"
            self.pickup_text = "Made with real spiders."
            self.cost = 20