init -10 python:
    
    class Monster():

        def __init__(self,name="bob"):
            self.name = name
            self.specialEvents = []
            self.schedule = {"Sunday":{},"Monday":{},"Tuesday":{},"Wednesday":{},"Thursday":{},"Friday":{},"Saturday":{}}
            self.default_sprite = None
            self.currentRoom = None
            self.default_event = Event('default_event',self)
            self.default_room = "Dead Room"
            self.FP_events = {}
            self.FP = 0
            self.visited = False
            self.dialogue_toggle = False
            self.hover_sprite = None

        def reset_schedule(self):
            self.schedule = {"Sunday":{},"Monday":{},"Tuesday":{},"Wednesday":{},"Thursday":{},"Friday":{},"Saturday":{}}
        
        def get_relationship(self):

            if self.FP <= 20:
                return "Hated"
            elif self.FP <= 40:
                return "Disliked"
            elif self.FP <= 60:
                return "Neutral"
            elif self.FP <= 80:
                return "Friend"
            else:
                return "Loved"
            
            
        def move_to_room(self,room):
            for an,a in world.areas.iteritems():
                for rn,r in a.rooms.iteritems():
                    if r.name == room:
                        #we found the room, so move them there
                        if self.currentRoom:
                            self.currentRoom.monsters.remove(self)
                        self.currentRoom = r
                        self.currentRoom.monsters.append(self)
                        return

            renpy.notify("Can't find room "+room)


        #will need to add math about the FP
        def get_current_event(self):
        
        #get the normal events
            timezone = world.get_current_timezone()
            day = world.get_current_day()
            if day in self.schedule:
                if timezone in self.schedule[day]:
                    for x,t in self.schedule[day][timezone].iteritems():
                        return t
            return self.default_event

        def give_gift(self,item = False):
            renpy.say(self.name,"You shouldn't see this.")

        def update_schedule(self,day,timezone,location,event):

            self.schedule[day][timezone] = {location:event}

            return

label give_item(owner,item):
    python:
        if owner.give_gift(item):
            inventory.drop(item)
    return


screen gift_item_menu(owner):
    add "#0008"
    modal True
    frame pos(0.2,0.4):
        vbox:
            for item in inventory.items:
                textbutton "[item.name]":
                    action [SetVariable("menu_selected_item",item)]
                    background "#000000"
            for i in range(0,inventory.max_items - len(inventory.items)):
                textbutton "----------":
                    background "#000000"
 
            hbox:
                textbutton "Exit":
                    action [Hide("gift_item_menu"),Return('cancel')]
                    background "#000000"

    if menu_selected_item:
        frame pos(0.5,0.4):
            hbox:
                vbox:
                    image menu_selected_item.sprite
                    textbutton "Give":
                        action [If(menu_selected_item,ui.callsinnewcontext("give_item",owner,menu_selected_item)),SetVariable("menu_selected_item",False),Hide("gift_item_menu"),Return()]
                        background "#000000"
                vbox:
                    box_wrap True
                    spacing 6
                    xmaximum 200
                    text "[menu_selected_item.name]"
                    text "[menu_selected_item.pickup_text]"
                    

