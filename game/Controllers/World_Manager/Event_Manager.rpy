init -10 python:

    class Event():
        def __init__(self,label = "flowey_hangout",perm = False,time = 0,arg = False):
            self.completed = False
            self.label = label
            self.owner = False
            self.permanent = perm
            self.arg = arg
            self.time = time

        def call_event(self):
            
            if self.permanent == False:
                self.completed = True
            world.timezone_action_count += self.time
            
            if self.arg:
                renpy.call(self.label,self.arg)
            else:
                renpy.call(self.label)

            
