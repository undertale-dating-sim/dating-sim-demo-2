init python:

    import math

    class Appearing(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Appearing, self).__init__(**kwargs)

            # The child.
            self.child = renpy.displayable(child)

            # The distance at which the child will become fully opaque, and
            # where it will become fully transparent. The former must be less
            # than the latter.
            self.opaque_distance = opaque_distance
            self.transparent_distance = transparent_distance

            # The alpha channel of the child.
            self.alpha = 0.0

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):

            # Create a transform, that can adjust the alpha channel of the
            # child.
            t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))

            # Return the render.
            return render

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.
            distance = math.hypot(x - (self.width / 2), y - (self.height / 2))

            # Base on the distance, figure out an alpha.
            if distance <= self.opaque_distance:
                alpha = 1.0
            elif distance >= self.transparent_distance:
                alpha = 0.0
            else:
                alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            # If the alpha has changed, trigger a redraw event.
            if alpha != self.alpha:
                self.alpha = alpha
                renpy.redraw(self, 0)

            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


screen show_map_button:
    textbutton "Show Map" action [Play ("sound", "audio/click.wav"),Show("show_map"),Hide("show_map_button")] align(.45,.05) background Frame("UI/text-box3.png",50, 21)

screen show_map:
    
    add "#0008"
    modal True
    #hide button
    textbutton "Hide Map" action [Play ("sound", "audio/click.wav"),Hide("show_map"),Show("show_map_button")] align(.45,.05)  background Frame("UI/text-box3.png",50, 21)
    


    vbox xalign 0.5 ypos 0.12:
        frame:
            background Frame("UI/text-box3.png",21, 21)
            xminimum screen_width-20
            yminimum screen_height-80
            xmaximum screen_width-20
            ymaximum screen_height-80
            vbox:
                add Appearing("CoffeeSnail.png", 100, 200):
                    xalign 0.6
                    yalign 0.5
