
python early:

    def parse_shop(lex):
        lex.require(':')
        lex.expect_eol()
        lex.python_block()
        lex.advance()
        action = lex.subblock_lexer()
        action.expect_eol()
        action.python_block()
        action.advance()
        sbl = action.subblock_lexer()
       
        if action.keyword('talk'):
               return 'talk'
    def execute_shop(o):
        if str(o)=='talk':
            renpy.say(str(o),"talk works, hurray!!!")
        else:
            renpy.say(str(o),"nope, didn't work")
    renpy.register_statement("shop", parse=parse_shop, lint=None, execute=execute_shop, predict=None, next=None, scry=None, block=True, init=False, translatable=False)


screen shop_menu:
    #textbutton "Hide Shop" action [Play ("sound", "audio/click.wav"),Hide("shop_dialog_exit"),Hide("shop_dialog_talk"),Hide("shop_dialog_buy"),Hide("shop_menu"),Show("show_shop_button")] align(.70,.05) background Frame("text-box3.png",50, 21)
    frame pos(int(screen_width*.728),.74): #position within the screen
        background Frame("text-box3.png",21,21)
        vbox:
            anchor(-.25,0)
            
            maximum(int(screen_width*.24),int(screen_height*.215))
            minimum(int(screen_width*.24),int(screen_height*.215))
            textbutton "TALK"action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_test_talk")] background "#000000"
            textbutton "BUY" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_test_buy")] background "#000000"
            textbutton "SELL" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_test_sell")] background "#000000"
            textbutton "EXIT" action [Play ("sound", "audio/click.wav"),ui.callsinnewcontext("shop_test_exit")] background "#000000"

screen shop_dialog_buy:
    frame pos(int(screen_width*.02),.74):
        background Frame("text-box3.png",21,21)
        window xmargin -21 ymargin -21:
            maximum(shop_dialog_width,shop_dialog_height)
            minimum(shop_dialog_width,shop_dialog_height)
            vbox:
                text "ShopKeeper" size 25
                grid 2 2:
                    textbutton "item1" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "item2" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "item3" action [Play ("sound", "audio/click.wav")] background "#000000"
                    textbutton "item4" action [Play ("sound", "audio/click.wav")] background "#000000"