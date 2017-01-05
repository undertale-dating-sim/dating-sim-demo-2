init -10 python:

    class Event():
        def __init__(self,label = "flowey_hangout",perm = False,arg = False):
            self.completed = False
            self.label = label
            self.owner = False
            self.permanent = perm
            self.arg = arg
            
        def __init__(self,label = "frisk_hangout",perm = False,arg = False):
            self.completed = False
            self.label = label
            self.owner = False
            self.permanent = perm
            self.arg = arg


        def call_event(self):
            if self.arg:
                renpy.call_in_new_context(self.label,self.arg)
            else:
                renpy.call_in_new_context(self.label)
            if self.permanent == False:
                self.completed = True
