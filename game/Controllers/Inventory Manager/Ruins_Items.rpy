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

##EQUIPPABLES
    class Heart_Locket(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Heart Locket"
            self.neutral_text = "It looks just like new, but it has an antique style to it. Someone must have cherished this locket."
            self.sprite = "items/item_heartlocket.png"
            self.menu_desc = "A Heart Locket."
            self.equip = True

        def equip_self(self):
            player.patience_impulsiveness += 10

        def unequip_self(self):
            player.patience_impulsiveness -= 10
       
    class Broken_Mirror(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Broken Mirror"
            self.neutral_text = "It’s cracked down the middle, but you can still see your reflection in it."
            self.sprite = "items/item_brokenmirror.png"
            self.equip = True

        def equip_self(self):
            player.integrity_deceit += 10

        def unequip_self(self):
            player.integrity_deceit -= 10

    class Stick(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Stick"
            self.pickup_text = "It's a stick."
            self.sprite = "items/item_stick.png"
            self.menu_desc = "It's a stick."
            self.equip = True

        def equip_self(self):
            player.bravery_cowardice += 10

        def unequip_self(self):
            player.bravery_cowardice -= 10

    class Rose(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Rose"
            self.neutral_text = "You ripped it from its place when you fell, but it still seems to be doing well."
            self.sprite = "items/item_rose.png"
            self.menu_desc = "You ripped it from its place when you fell, but it still seems to be doing well."
            self.equip = True

        def equip_self(self):
            player.kindness_cruelty += 10

        def unequip_self(self):
            player.kindness_cruelty -= 10


##USABLE
    class Spider_Donut(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Donut"
            self.use_text = "You bite down, but something stops you. It had a coin in it?  What was the point of buying this?"
            self.pickup_text = "It is a donut. Made of spiders. Crunchy!"
            self.sprite = "items/item_spiderdonut.png"
            self.menu_desc = "It is a donut. \nRestore 10 Stamina"

    class Butts_Pie(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Butterscotch Pie"
            self.use_text = "You eat the pie. It tastes like placeholder?"
            self.pickup_text = "It's a pie."
            self.sprite = "items/item_buttspie.png"
            self.menu_desc = "Placeholder. \nRestore xx Stamina"

    class Snail_Pie(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Snail Pie"
            self.use_text = "You eat the pie. It tastes like placeholder?"
            self.pickup_text = "It's a pie."
            self.sprite = "items/item_snailpie.png"
            self.menu_desc = "Placeholder. \nRestore xx Stamina"

    class White_Chocolate(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "White Chocolate"
            self.use_text = "You eat the chocolate. It tastes like placeholder?"
            self.pickup_text = "It's a chocolate."
            self.sprite = "items/item_whitechocolate.png"
            self.menu_desc = "Placeholder. \nRestore xx Stamina"

    class Milk_Chocolate(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Milk Chocolate"
            self.use_text = "You eat the chocolate. It tastes like placeholder?"
            self.pickup_text = "It's a chocolate."
            self.sprite = "items/item_milkchocolate.png"
            self.menu_desc = "Placeholder. \nRestore xx Stamina"
            
    class Monster_Candy(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Monster Candy"
            self.use_text = "You eat the candy. It tastes like placeholder?"
            self.pickup_text = "It's a candy."
            self.sprite = "items/item_monstercandy.png"
            self.menu_desc = "Placeholder. \nRestore xx Stamina"

    class Spider_Cider(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Spider Cider"
            self.sale_cost = 5
            self.use_text = "Spiders pour over your face. It had "+str(self.sale_cost)+" coin(s) in it.  What was the point of buying this?"
            self.pickup_text = "A bottle full of spiders. You can hear coins jiggle if you shake it."
            self.sprite = "items/item_spidercider.png"
            self.menu_desc = "This bubbly drink is sure to hit the spot! \nRestore 50 Stamina"

    class Sleeping_Potion(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Game Over Potion"
            self.sale_cost = 5
            self.use_text = "You drink the thick, white goop.  It tastes disgusting."
            self.pickup_text = "You find a potion. Smells like a reset?"
            self.sprite = "items/item_spidercider.png"
            self.menu_desc = "Puts you to sleep."

        def use(self):
            player.current_stamina = 0
            player.update_player()

    class Snail(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Snail"
            self.sale_cost = 5
            self.use_text = "It's a normal snail.  Smells like a placeholder."
            self.pickup_text = "Oh look, a snail."
            self.sprite = "items/item_snailpie.png"
            self.menu_desc = "Snell" 





