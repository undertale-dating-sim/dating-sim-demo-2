
label shop_test_talk:
    #show screen show_menu_button
    #show screen shop_menu
    nvl clear
    #shop declarations
    #set dialogs, buttons, everything
    #show
    #set. then show.

    

    payneShop "Testing the Shop Dialog Talk Button, click on this, and we'll have more text."
    payneShop "Of course, there's not much to say."
    jump shop_test_talk



label shop_test_sell:
    show screen show_menu_button
    show screen shop_menu
    nvl clear
    payneShop "Sell dialog goes here. These never worked Undertale, except for the Temmie Shop"
    jump shop_test_sell

label shop_test_exit:
    show screen show_menu_button
    show screen shop_menu
    nvl clear
    payneShop "This is when we leave."
    payneShop "Just add return to the end of this label."
    jump shop_test_exit
