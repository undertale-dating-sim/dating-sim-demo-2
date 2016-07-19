init python:

    import math

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


            xmargin = 100
            ymargin = -300
            

            for r in world.currentArea.rooms:
                x = 800 - ((20 - r.x) * 50) + xmargin
                y = 600 - (r.y * 40) + ymargin
                if world.currentArea.currentRoom == r:
                    render.canvas().rect("#0F0", (x,y, 10, 10))
                elif len(r.monsters) > 0:
                    render.canvas().rect("#F00", (x,y, 10, 10))
                elif r.visited == True:
                    render.canvas().rect("#d3d3d3", (x,y, 10, 10))
                else:
                    render.canvas().rect("#000", (x,y, 10, 10))
                # render.blit(renpy.render(Text("%d"%(r.visited)),width,height,st,at),(x,y))

            
            # Return the render.
            return render

        def event(self, ev, x, y, st):

            
            renpy.redraw(self, 0)

            return



screen show_map_button:
    textbutton "Show Map" action [Play ("sound", "audio/sfx/click.wav"),Show("show_map"),Hide("show_map_button")] align(.45,.05) background Frame("UI/text-box3.png",50, 21)

screen show_map:
    
    add "#0008"
    modal True
    #hide button
    textbutton "Hide Map" action [Play ("sound", "audio/sfx/click.wav"),Hide("show_map"),Show("show_map_button")] align(.45,.05)  background Frame("UI/text-box3.png",50, 21)
    


    vbox xalign 0.5 ypos 0.12:
            vbox:
                add Minimap():
                    xalign 0.6
                    yalign 0.5
