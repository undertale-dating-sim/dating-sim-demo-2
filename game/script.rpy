#character-images
init:
    image flowey normal = "Character-Flowey-Normal.png"



#This takes place after the MC has heard about Frisk from Toriel.
label start:
    stop music
    "test"
    #jump FlappySans

    jump dev_label
    #jump frisk_start




label dev_label:
    show screen show_menu_button
    #show screen show_map_button
    while True:
        menu:
            "Where would you like to go?"
            "Movement Demo":
                show screen show_menu_button
                show screen show_nav_button
                jump load_room
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
                jump flowey_ruins
            "Toriel":
                jump toriel_ruins
            "Shop Test":
                jump Muffet_Shop

label demo_end:
    "This demo ends here. Thanks for playing!"
    "Stay determined..."