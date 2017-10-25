init python:
    def fading_text(text, t, x, y, move_y, *args, **kwargs):
        ui.add(At(Text(text, *args, **kwargs), fade_move_with_pars(t, x, y, move_y)))


transform fade_move_with_pars(t, x, y, move_y):
    parallel:
        alpha 1.0
        linear t*2 alpha 0
    parallel:
        align (x, y)
        linear t yalign move_y
        
label choosemenu:
    scene black
    while True:
        menu:
            "friendship":
                show screen word_scroll_left("3")
                show screen word_scroll_right("3")
            "end":
                return

# label word_scroll():
#     if int(value_changed) >= 0:
#         $ changed_text = " +" + "%s" % value_changed
#         $ fcolor = '00ff00'
#     else:
#         $ changed_text = "%s" % value_changed
#         $ fcolor = 'ff0000'
#     if side == "left":
#         $ xval = .20
#     else:
#         $ xval = .80
#     $ fading_text("[changed_text]", 1, xval, .5, .1 , color=fcolor, size=40, font="font/DTM-Mono.otf")
#     $ renpy.pause(1,hard=True)


screen word_scroll_left(value_changed="1"):
    if int(value_changed) >= 0:
        $ changed_text = " +" + "%s" % value_changed
        $ fcolor = '00ff00'
    else:
        $ changed_text = "%s" % value_changed
        $ fcolor = 'ff0000'

    $ xval = .20

    
    text "{color=[fcolor]}{size=40}[changed_text]{/size}{/color}" outlines [ (1, "000000", 0, 0 ) ] at Move((xval,.5),(xval,.1), 2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    timer 2.0 action [Hide("word_scroll_left",transition=dissolve)]

screen word_scroll_right(value_changed="1"):
    if int(value_changed) >= 0:
        $ changed_text = " +" + "%s" % value_changed
        $ fcolor = '00ff00'
    else:
        $ changed_text = "%s" % value_changed
        $ fcolor = 'ff0000'

    $ xval = .80
    text "{color=[fcolor]}{size=40}[changed_text]{/size}{/color}" outlines [ (1, "000000", 0, 0 ) ] at Move((xval,.5),(xval,.1), 2, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    timer 2.0 action [Hide("word_scroll_right",transition=dissolve)]