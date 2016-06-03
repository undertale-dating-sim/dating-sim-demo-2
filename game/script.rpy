
#This takes place after the MC has heard about Frisk from Toriel.
label start:
    stop music

    jump dev_label
    #jump frisk_start




label dev_label:
    show screen show_menu_button
    while True:
        menu:
            "Where would you like to go?"
            "Undersnail":
                jump demo_undersnail
            "Prologue":
                jump prologue
            "Name Select":
                jump name_select
            "The Fall":
                jump the_fall
            "Random Encounters":
                menu:
                    "Vegetoid":
                        jump vegetoid_start
                    "Whimsun":
                        jump whimsun_start
            "Frisk":
                jump frisk_start
            "Flowey":
                jump flowey_start
label demo_end:
    "This demo ends here. Thanks for playing!"
    "Stay determined..."