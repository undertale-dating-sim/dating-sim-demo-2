
label buy_item(item, cost, shop,itemclass):
    show screen show_menu_button
    show screen shop_box(shop)
    show screen buy_box(shop.items,shop)
    python:
        if inventory.has_space() and player.gold>=cost:
            player.gold -= cost
            inventory.add(itemclass)
        else:

            renpy.hide_screen("buy_box")
            if not inventory.has_space():
                renpy.call("shop_text",shop=shop,dialog=shop.no_space_dialog)
            else:
                renpy.call("shop_text",shop=shop,dialog=shop.no_gold_dialog)
            renpy.call_screen("buy_box",shop.items,shop)
    #hide screen shop_box


screen buy_prompt(item,cost,shop,itemclass):
    #takes in shop class

    frame align(.5,.5):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                text "Would you like to buy [item] for [cost]G?"
            
                grid 2 1:
                    textbutton "Yes" background "#000000" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("buy_item",item = item,cost = cost,shop=shop,itemclass=itemclass),Hide ("buy_prompt")] 
                    textbutton "No" background "#000000" action [Hide ("buy_prompt")]

screen buy_box(obj,shop):
    # clicking outside the box will make it leave buy box screen. Any way to make it stay? Like, a label?
    # takes in shop class
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                text shop.name size 25
                grid 2 len(obj)/2: #Find a way to count this stuff. Len(obj)? 
                # or if there are more items, add a button to lead to another page
                    for item in obj:
                        $ cost = item[1]
                        $ itemTemp = item[0]
                        $ itemclass = item[2]
                        textbutton "[item[0]] - [item[1]]G" action [Play ("sound", "audio/click.wav"),Show("show_menu_button"),Show("buy_prompt",item = itemTemp,cost = cost,shop=shop,itemclass=itemclass)] background "#000000" 


screen shop_box(shop):
    frame pos(int(screen_width*.728),.74):
        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK" action [Play ("sound", "audio/click.wav"),Hide("buy_box"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.talk_dialog) ] background "#000000"
            textbutton "BUY" action [Play ("sound", "audio/click.wav"),Show("buy_box",transition=None,obj=shop.items, shop = shop)] background "#000000"
            textbutton "SELL" action [Play ("sound", "audio/click.wav"),Hide("buy_box"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.sell_dialog)] background "#000000"
            textbutton "EXIT" action [Play ("sound", "audio/click.wav"),Hide("buy_box"),ui.callsinnewcontext("shop_text", shop=shop,dialog = shop.exit_dialog)] background "#000000"
