init 1 python:

#we want the mouse to be able to change to any of the 4 arrows if there is a room in that direction to move to.
#up = images/ui/Arrow_Up.png
#left = images/ui/Arrow_Left.png
#right = images/ui/Arrow_Right.png
#down = images/ui/Arrow_Down.png

    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "up":
            setattr(config, "mouse",{"default": [("images/ui/Arrow_Up.png", 0, 0)]})
        elif type == "down":
            setattr(config, "mouse",{"default": [("images/ui/Arrow_Down.png", 0, 0)]})
        elif type == "left":
            setattr(config, "mouse",{"default": [("images/ui/Arrow_Left.png", 0, 0)]})
        elif type == "right":
            setattr(config, "mouse",{"default": [("images/ui/Arrow_Right.png", 0, 0)]})


screen direction_buttons:

    imagemap:
        hotspot (0,0,50,50) hovered change_cursor("up") unhovered change_cursor()
