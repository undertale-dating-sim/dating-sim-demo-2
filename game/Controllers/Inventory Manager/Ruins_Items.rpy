init -1 python:
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
            
    class Heart_Locket(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Heart Locket"
            self.use_text = "It doesn't seem to open, but it is pretty nonetheless: golden and strung on a pretty chain."
            self.pickup_text = "It is a donut. Made of spiders. Crunchy!"
            self.sprite = "items/item_spiderdonut.png"
            self.menu_desc = "It is a donut. \nRestore 10 Stamina"

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