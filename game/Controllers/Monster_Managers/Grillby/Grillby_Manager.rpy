init -9 python:

    class Grillby(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Toriel_manager_default",True,self)
            self.default_room = "Toriel's Room"
            self.name = "Grillby"
            self.FP = 40
            self.seed_default_schedule()
            self.default_sprite = "grillby grillby1"

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
                        renpy.call_in_new_context("%s_Gift_Count_Reaction" % self.name,self)

            else:
                renpy.call_in_new_context("give_Gift_%s_Unknown" % self.name)
            return
        
        def handle_special_events(self):

          
            return
            

        # def seed_default_schedule(self):
            # self.reset_schedule() 
            # #night
            # self.update_schedule("Sunday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Monday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Tuesday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Wednesday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Thursday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Friday","Night","Toriel's Room",self.default_event)
            # self.update_schedule("Saturday","Night","Toriel's Room",self.default_event)
            # #morning
            # self.update_schedule("Sunday","Morning","Kitchen",self.default_event)
            # #self.update_schedule("Monday","Morning","Kitchen",self.default_event)
            # self.update_schedule("Monday","Morning","Basement Door",self.default_event)
            # self.update_schedule("Tuesday","Morning","Kitchen",self.default_event)
            # self.update_schedule("Wednesday","Morning","Kitchen",self.default_event)
            # self.update_schedule("Thursday","Morning","Kitchen",self.default_event)
            # self.update_schedule("Friday","Morning","Kitchen",self.default_event)
            # self.update_schedule("Saturday","Morning","Kitchen",self.default_event)
            # #day
            # self.update_schedule("Sunday","Day","Cave Room",self.default_event)
            # #self.update_schedule("Monday","Day","",self.default_event)
            # self.update_schedule("Tuesday","Day","Cave Room",self.default_event)
            # #self.update_schedule("Wednesday","Day","",self.default_event)
            # self.update_schedule("Thursday","Day","Cave Room",self.default_event)
            # #self.update_schedule("Friday","Day","",self.default_event)
            # self.update_schedule("Saturday","Day","Cave Room",self.default_event)
            # #afternoon
            # self.update_schedule("Sunday","Afternoon","Spider Bakery",self.default_event)
            # self.update_schedule("Monday","Afternoon","Dummy Room",self.default_event)
            # self.update_schedule("Tuesday","Afternoon","Sassy Rock Room",self.default_event)
            # self.update_schedule("Wednesday","Afternoon","Dummy Room",self.default_event)
            # self.update_schedule("Thursday","Afternoon","Sassy Rock Room",self.default_event)
            # self.update_schedule("Friday","Afternoon","Dummy Room",self.default_event)
            # self.update_schedule("Saturday","Afternoon","Sassy Rock Room",self.default_event)
            # #evening
            # self.update_schedule("Sunday","Evening","Toriel's Room",self.default_event)
            # self.update_schedule("Monday","Evening","Living Room",self.default_event)
            # self.update_schedule("Tuesday","Evening","Living Room",self.default_event)
            # self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            # self.update_schedule("Thursday","Evening","Living Room",self.default_event)
            # self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            # self.update_schedule("Saturday","Evening","Living Room",self.default_event)
            


init:
    
    image grillby grillby1 = "characters/Grillby/Grillby1.png"
    image grillby grillby2 = "characters/Grillby/Grillby2.png"
    image grillby grillby3 = "characters/Grillby/Grillby3.png"
    image grillby grillby4 = "characters/Grillby/Grillby4.png"
    image grillby grillby5 = "characters/Grillby/Grillby5.png"
    image grillby grillby6 = "characters/Grillby/Grillby6.png"
    image grillby grillby7 = "characters/Grillby/Grillby7.png"
    image grillby grillby8 = "characters/Grillby/Grillby8.png"
    image grillby grillby9 = "characters/Grillby/Grillby9.png"
    image grillby grillby10 = "characters/Grillby/Grillby10.png"
    image grillby grillby11 = "characters/Grillby/Grillby11.png"
    image grillby grillby12 = "characters/Grillby/Grillby12.png"


    define grillby = ('Grillby')
    define grillbyChar = Character('Grillby', color="#FFFFFF")
    python:
        def grillby(text, *args, **kwargs):
               grillbyChar(text, *args, **kwargs)


