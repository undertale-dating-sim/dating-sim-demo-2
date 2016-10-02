init -4 python:
    # class Item():
    #     def __init__(self):
    #         self.name =         "default"
    #         self.pickup_text =  "default"
    #         self.drop_text =    "default"
    #         self.negative_text = "default"
    #         self.positive_text = "default"
    #         self.sale_cost = 1
    #         self.shop_text = "default"
    #         self.use_text = ""
    #         self.sprite = ""
    #         self.menu_desc = ""

    #     def give(self,character):
    #         return

    #     def use(self):
    #         player.gold += self.sale_cost
    #         inventory.drop(self)
    #         return
            # self.patience_impulsiveness = 0
            # self.integrity_deceit     = 0
            # self.bravery_cowardice        = 0
            # self.perseverance_surrender   = 0
            # self.kindness_cruelty       = 0
            # self.justice_apathy        = 0
    class Heart_Locket(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Heart Locket"
            self.use_text = "The Item does nothing."
            self.pickup_text = "It doesn't seem to open, but it is pretty nonetheless, golden and strung on a pretty chain."
            self.sprite = "items/item_heartlocket.png"
            self.menu_desc = "A Heart Locket."
            self.equip = True

        def equip_self(self):
            player.patience_impulsiveness += 10

        def unequip_self(self):
            player.patience_impulsiveness -= 10
       
    class Mirror(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Mirror"
            self.use_text = "It doesn't seem to open, but it is pretty nonetheless: golden and strung on a pretty chain."
            self.pickup_text = "It is a donut. Made of spiders. Crunchy!"
            self.sprite = "items/item_brokenmirror.png"
            self.menu_desc = "It is a donut. \nRestore 10 Stamina"
            self.equip = True

        def equip_self(self):
            player.integrity_deceit += 10

        def unequip_self(self):
            player.integrity_deceit -= 10

    class Stick(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Stick"
            self.use_text = "It doesn't seem to open, but it is pretty nonetheless: golden and strung on a pretty chain."
            self.pickup_text = "It is a donut. Made of spiders. Crunchy!"
            self.sprite = "items/item_stick.png"
            self.menu_desc = "It is a donut. \nRestore 10 Stamina"
            self.equip = True

        def equip_self(self):
            player.bravery_cowardice += 10

        def unequip_self(self):
            player.bravery_cowardice -= 10

    class Flower(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Flower"
            self.use_text = "It doesn't seem to open, but it is pretty nonetheless: golden and strung on a pretty chain."
            self.pickup_text = "It is a donut. Made of spiders. Crunchy!"
            self.sprite = "items/item_rose.png"
            self.menu_desc = "It is a donut. \nRestore 10 Stamina"
            self.equip = True

        def equip_self(self):
            player.kindness_cruelty += 10

        def unequip_self(self):
            player.kindness_cruelty -= 10


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

    class Sleeping_Potion(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Sleeping_Potion"
            self.sale_cost = 5
            self.use_text = "You drink the thick, white goop.  It tastes disgusting."
            self.pickup_text = "You find a potion. It is warm to the touch?"
            self.sprite = "items/item_spidercider.png"
            self.menu_desc = "Puts you to sleep."

        def use(self):
            player.current_stamina = 0
            player.update_player()





