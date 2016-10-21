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

label word_scroll(stat_changed="Default", value_changed="1"):
    if int(value_changed) >= 0:
        $ changed_text = stat_changed + " +" + value_changed
    else:
        $ changed_text = stat_changed + " " + value_changed
    $ fading_text("[changed_text]", 1, .5, .33, .5, .1 , color="ffffff", size=24, font="font/DTM-Mono.otf")