init python:

    import math
    
    #This is for the minimap that appears in the menu.

    class Minimap(renpy.Displayable):

        def __init__(self, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Minimap, self).__init__(**kwargs)

            # The width and height of us, and our child.
            self.width = 800
            self.height = 600

        def render(self, width, height, st, at):



            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            if world.current_area.name == "Toriel House":
                xmargin = 355
                ymargin = -400
            else:
                xmargin = 100
                ymargin = -300
            

            for r_name,r in world.current_area.rooms.iteritems():
                if r.mappable:
                    x = 800 - ((20 - r.x) * 50) + xmargin
                    y = 600 - (r.y * 40) + ymargin

                    render.canvas().rect("#FFF", (x-1,y-1, 12, 12))
                    if world.current_area.current_room == r:
                        render.canvas().rect("#0F0", (x,y, 10, 10))
                    elif len(r.monsters) > 0:
                        render.canvas().rect("#F00", (x,y, 10, 10))
                        #render.blit(renpy.render(Image("UI/tori_head.png"), width, height, st, at),(x-11,y-12))
                    elif r.has_events():
                        render.canvas().rect("#ffff00", (x,y, 10, 10))
                    elif r.visited == True:
                        render.canvas().rect("#d3d3d3", (x,y, 10, 10))
                    else:
                        render.canvas().rect("#000", (x,y, 10, 10))
                    #render.blit(renpy.render(Text("%d"%(r.visited)),width,height,st,at),(x,y))
            
            render.canvas().rect("#FFF", (197,57,132,92))
            render.canvas().rect("#000", (198,58,130,90))

            render.canvas().rect("#0F0", (200,70, 10, 10))
            render.blit(renpy.render(Text("You"),width,height,st,at),(220,60))

            render.canvas().rect("#F00", (200,100, 10, 10))
            render.blit(renpy.render(Text("Monster"),width,height,st,at),(220,90))

            render.canvas().rect("#ffff00", (200,130, 10, 10))
            render.blit(renpy.render(Text("Event"),width,height,st,at),(220,120))

            # Return the render.
            return render

        def event(self, ev, x, y, st):

            
            renpy.redraw(self, 0)

            return

screen show_testing_button:
    textbutton "Look Around" action [Play ("sound", "audio/sfx/click.wav"),ui.callsinnewcontext("current_room_description")] align(.95,.17) background Frame("UI/text-box3.png",50, 21)    

# screen show_map_button:
#     textbutton "Show Map (M)" action [Play ("sound", "audio/sfx/click.wav"),Show("show_map"),Hide("show_map_button")] align(.95,.15) background Frame("UI/text-box3.png",50, 21)
#     key 'm' action [Play ("sound", "audio/sfx/click.wav"),Show("show_map"),Hide("show_map_button")]
# screen show_map:
    
#     add "#0008"
#     modal True
#     #hide button
#     textbutton "Hide Map (M)" action [Play ("sound", "audio/sfx/click.wav"),Hide("show_map"),Show("show_map_button")] align(.95,.15)  background Frame("UI/text-box3.png",50, 21)
#     key 'm' action [Play ("sound", "audio/sfx/click.wav"),Hide("show_map"),Show("show_map_button")]


#     vbox xalign 0.5 ypos 0.12:
#             vbox:
#                 add Minimap():
#                     xalign 0.6
#                     yalign 0.5
            