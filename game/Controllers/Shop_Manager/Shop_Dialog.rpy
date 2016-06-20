# Handles the Shop dialog boxes
#remember to show menu button on each label

init:
    $ screen_width = config.screen_width # 800
    $ screen_height = config.screen_height # 600
    $ shop_dialog_width = int(screen_width*.70)
    $ shop_dialog_height = int(screen_height*.215)

#a LOT of guesswork went into this one
define payneShop = Character('PayneGray',
    window_background=Frame("text-box3.png",21,21),
    window_left_margin = int(screen_width*.02),
    window_right_margin = int(screen_width*.265),
    window_top_margin = -6,
    window_bottom_margin = 16,
    window_top_padding = 10,
    window_bottom_padding = 10,
    window_left_padding = 15,
    window_right_padding = 15)
define niceCreamShop = payneShop.copy('Nice Cream Guy')


label shop_text(shop,dialog):
    show screen show_menu_button
    show screen shop_box(shop)
    python:
        for line in dialog:
            renpy.say(payneShop.copy(shop.name),line)
    show screen empty_dialog
    # Bug: clicking the empty dialog makes this move to the next label, shop_item. A fix would be to make the dialog box unclickable. Or prompt a hidden menu
    # Fixed: Separated shop_text and shop_item into different files

    call shop_opening(shop=shop)

screen empty_dialog:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)

label shop_opening(shop):
    show screen shop_box(shop=shop)
    hide screen buy_box
    call shop_text(shop=shop,dialog=shop.opening_dialog)