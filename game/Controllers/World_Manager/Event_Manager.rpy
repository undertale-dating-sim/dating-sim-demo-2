init -10 python:

    class Event():
        def __init__(self,label = "flowey_hangout",perm = False,arg = False):
            self.completed = False
            self.label = label
            self.owner = False
            self.permanent = perm
            self.arg = arg

        def call_event(self):
            
            if self.permanent == False:
                self.completed = True
            
            if self.arg:
                renpy.call(self.label,self.arg)
            else:
                renpy.call(self.label)

            
