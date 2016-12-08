init python:
    def fading_text(text, t, x, y, move_x, move_y, *args, **kwargs):
        ui.add(At(Text(text, *args, **kwargs), fade_move_with_pars(t, x, y, move_x, move_y)))

transform fade_move_with_pars(t, x, y, move_x, move_y):
    parallel:
        alpha 1.0
        linear t alpha 0
    parallel:
        align (x, y)
        linear t align (move_x, move_y)
        
label choosemenu:
    scene black
    while True:
        menu:
            "friendship":
                call word_scroll("FP", "3")
            "flirt":
                call word_scroll("DP", "-1")
            "nice":
                call word_scroll("Kindness", "1")
            "...":
                call word_scroll
            "end":
                jump end

label word_scroll(value_changed="1"):
    if int(value_changed) >= 0:
        $ changed_text = " +" + "%s" % value_changed
        $ fcolor = '00ff00'
    else:
        $ changed_text = "%s" % value_changed
        $ fcolor = 'ff0000'
    $ fading_text("[changed_text]", 2, .20, .5, .20, .1 , color=fcolor, size=24, font="font/DTM-Mono.otf")