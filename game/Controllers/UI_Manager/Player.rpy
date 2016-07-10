init -1 python:
    class Player():
        def __init__(self):
            self.name           = "Bob"
            self.current_health = 20
            self.total_health   = 20
            self.gold           = 10

            #the stats go positive or negative, do not know the maximum values yet.
            self.patience_impulsiveness = 0
            self.integrity_deceit     = 0
            self.bravery_cowardice        = 0
            self.perseverance_surrender   = 0
            self.kindness_cruelty       = 0
            self.justice_apathy        = 0
            self.current_room = "Nowhere"
            self.stamina = 100


            self.time = 0

        def modify_patience(self,amount):
            self.patience_impulsiveness += amount

        def modify_integrity(self,amount):
            self.integrity_deceit   += amount

        def modify_bravery(self,amount):
            self.bravery_cowardice  += amount

        def modify_perseverance(self,amount):
            self.perseverance_surrender += amount

        def modify_kindness(self,amount):
            self.kindness_cruelty   += amount

        def modify_justice(self,amount):
            self.justice_apathy += amount

        def modify_impulsiveness(self,amount):
            self.patience_impulsiveness -= amount

        def modify_deceit(self,amount):
             self.integrity_deceit  -= amount

        def modify_cowardice(self,amount):
            self.bravery_cowardice  -= amount

        def modify_surrender(self,amount):
            self.perseverance_surrender -= amount

        def modify_cruelty(self,amount):
            self.kindness_cruelty   -= amount

        def modify_apathy(self,amount):
            self.justice_apathy -= amount
            
           
            
            
            
            
