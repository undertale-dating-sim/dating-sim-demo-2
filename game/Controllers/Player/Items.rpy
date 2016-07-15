#items

init -1 python:
    

    class Heart_Locket(Item):
        def __init__(self):
            Item.__init__(self)
            self.name = "Heart Locket"
            self.pickup_text = "It doesn't seem to open, but it is pretty nonetheless, golden and strung on a red ribbon."
