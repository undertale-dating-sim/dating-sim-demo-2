#character images


#background images


#character settings
define diary = ('Diary')
define frisk = ('Frisk')
define xxxfrisk = ('XXX')
define toriel = ('Toriel')


#sprite positions
init:
    $ left = Position(xpos = 0.25, xanchor = 'left')
    $ center = Position(xpos = 0.5, xanchor = 'center')
    $ right = Position(xpos = 0.75, xanchor = 'right')

#default-font
init python:
    style.default.font = "font/DTM-Mono.otf"

#This takes place after the MC has heard about Frisk from Toriel.
label start:
    stop music

    jump dev_label
    #jump frisk_start

label demo_end:
    "This demo ends here. Thanks for playing!"
    "Stay determined..."