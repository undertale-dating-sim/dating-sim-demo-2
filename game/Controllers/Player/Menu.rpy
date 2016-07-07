
screen show_menu_button:
    textbutton "Show Menu" action [Play ("sound", "audio/sfx/click.wav"),Show("show_menu"),Hide("show_menu_button"),Show("stats")] align(.95,.05) background Frame("UI/text-box3.png",50, 21)

screen show_menu:
    add "#0008"
    modal True
    #hide button
    textbutton "Hide Menu" action [Play ("sound", "audio/sfx/click.wav"),Hide("show_menu"),Show("show_menu_button"),Hide("items"),Hide("stats"),Hide("cell"),Hide("show_item_description")] align(.95,.05)  background Frame("UI/text-box3.png",50, 21)
    vbox xalign 0.1 ypos 0.1:
        frame:
            background Frame("UI/text-box3.png",21, 21)       
            vbox:
                text "[player.name]"
                text "Day: [day]"
                text "HP:  [player.current_health]/[player.total_health]"
                text "G:   [player.gold]"

        frame  ypos 0.5:
            background Frame("UI/text-box3.png",21, 21)
            vbox:
                textbutton "ITEM" action [Play ("sound", "audio/sfx/click.wav"),Show("items"),Hide("stats"),Hide("cell")] background "#000000"
                textbutton "STAT" action [Play ("sound", "audio/sfx/click.wav"),Show("stats"),Hide("items"),Hide("cell")] background "#000000"
                textbutton "CELL" action [Play ("sound", "audio/sfx/click.wav"),Show("cell"),Hide("stats"),Hide("items")] background "#000000"



screen stats:
    frame pos(0.3,0.05):
        background Frame("UI/text-box3.png",21, 21)
        hbox:
            vbox:
                text "Patience:"
                text "Integrity:"
                text "Bravery:"
                text "Perseverance:"
                text "Kindness:"    
                text "Justice:"
            vbox:
                text "[player.patience_impulsiveness]"
                text "[player.integrity_deceit]"
                text "[player.bravery_cowardice]"
                text "[player.perseverance_surrender]"
                text "[player.kindness_cruelty]"
                text "[player.justice_apathy]"                    