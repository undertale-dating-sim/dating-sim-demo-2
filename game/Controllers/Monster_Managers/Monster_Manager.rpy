init -10 python:
    
    class Monster():

        def __init__(self,name="bob"):
            self.name = name

            #This event will be used to override the schedule
            self.special_event = None

            self.schedule = {"Sunday":{},"Monday":{},"Tuesday":{},"Wednesday":{},"Thursday":{},"Friday":{},"Saturday":{}}
            self.default_sprite = None
            self.current_room = None
            self.default_event = Event('default_event',self)
            self.default_room = "Dead Room"
            self.FP_events = {}
            self.FP = 0
            self.DP_events = {}
            self.DP = 0
            self.HB_events = {}
            self.HB = 0
            self.visited = False
            self.dialogue_toggle = False
            self.hover_sprite = None

            #An array to store the items they have been given
            self.given_items = {}
            self.given_today_count = 0

            #an array to hold various variables
            self.variables = {}
            self.flirt_count = 0
            self.chat_count = 0


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

            if room == 'Random':
                room = random.choice(world.current_area.rooms.keys())

            for an,a in world.areas.iteritems():
                for rn,r in a.rooms.iteritems():
                    if r.name == room:
                        #we found the room, so move them there
                        if self.current_room:
                            self.current_room.monsters.remove(self)
                        self.current_room = r
                        self.current_room.monsters.append(self)
                        return

            renpy.notify("Can't find room "+room)

        def set_special_event(self,event):
            if renpy.has_label(event):
                self.special_event = Event(event,True,self)
            else:
                renpy.notify("Couldn't find event [event]")

        def get_current_event(self):
        
            if self.special_event and self.special_event.completed == False:
                return self.special_event
            #get the normal events
            timezone = world.get_current_timezone()
            day = world.get_current_day()
            if day in self.schedule:
                if timezone in self.schedule[day]:
                    for x,t in self.schedule[day][timezone].iteritems():
                        return t
            return self.default_event


        #iterates through the given items array and adds up the totals
        def get_total_given_items(self):
            total = 0
            
            for item_name,count in items.iteritems():
                total = total + count

            return total

        def get_total_specific_item(self,item):

            if item.get_class_name() in self.given_items:
                return self.given_items[item.get_class_name()]
            else:
                return 0

        def give_item(self,item = False):

            # give_Gift_name_itemclassname
            # builds the label and calls it with current count + 1
            label_name = "give_Gift_%s_%s" % (self.name,item.get_class_name())

            if renpy.has_label(label_name):

                if self.given_today_count >= 5:
                    renpy.call_in_new_context("give_Gift_%s_Rejection" % self.name,self)
                else:
                    response = renpy.call_in_new_context(label_name,self.get_total_specific_item(item) + 1,self)
                    self.given_items[item.get_class_name()] = self.get_total_specific_item(item) + 1
                    if response:
                        self.given_today_count += 1
                        inventory.drop(item)
                        renpy.call_in_new_context("%s_Gift_Count_Reaction" % self.name,self)
                        return True

            else:
                renpy.call_in_new_context("give_Gift_%s_Unknown" % self.name)
            return False

        def handle_special_events(self):
            return False

        def update_schedule(self,day,timezone,location,event):

            self.schedule[day][timezone] = {location:event}

            return

        def update_FP(self,amount):
            self.FP += amount
            renpy.call("word_scroll",amount)
        def update_DP(self,amount):
            self.DP += amount
            renpy.call("word_scroll",amount)
        def update_HB(self,amount):
            self.HB += amount
            renpy.call("word_scroll",amount)


screen remember(owner):
    
    text "[owner.name] will remember that." xpos .01 ypos .2
    timer 1.0 action [Hide("remember",transition=dissolve)]
    

label give_item(owner,item):
    python:
        if owner.give_item(item):
            inventory.drop(item)
    return


screen gift_item_menu(owner):
    add "#0008"
    modal True
    frame pos(0.1,0.4):
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
        frame pos(0.45,0.4):
            hbox:
                vbox:
                    image im.Scale(menu_selected_item.sprite,200,150)
                    textbutton "Give":
                        action [If(menu_selected_item,ui.callsinnewcontext("give_item",owner,menu_selected_item)),SetVariable("menu_selected_item",False),Hide("gift_item_menu"),Return()]
                        background "#000000"
                vbox:
                    box_wrap True
                    spacing 6
                    xmaximum 200
                    text "[menu_selected_item.name]"
                    text "[menu_selected_item.menu_desc]"
                    

