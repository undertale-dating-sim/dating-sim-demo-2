label initialize:
    #prologue
    image background prologue1 = "backgrounds/prologue.jpg"
    image background intro = "backgrounds/background-intro.png"

    #random monsters
    image froggit normal = "characters/Froggit/Froggit_normal.png"
    image froggit happy = "characters/Froggit/Froggit_happy.png"

    image vegetoid normal = im.FactorScale("characters/Vegetoid/vegetoid_normal.png",.5)
    image vegetoid happy = im.FactorScale("characters/Vegetoid/vegetoid_happy.png",.5)

    image loox normal = "characters/Loox/loox_normal.png"
    image loox happy = "characters/Loox/loox_happy.png"
    image loox surprised = "characters/Loox/loox_surprised.png"

    image moldsmol normal = "characters/Moldsmol/moldsmol_normal.png"
    image moldsmol happy = "characters/Moldsmol/moldsmol_happy.png"
    image moldsmol nervous = "characters/Moldsmol/moldsmol_nervous.png"

    image napstablook normal = "characters/Napstablook/napstablook_normal.png"

    image whimsun normal = "characters/Whimsun/whimsun_normal.png"
    image whimsun fetal1 = "characters/Whimsun/whimsun_fetal1.png"
    image whimsun fetal2 = "characters/Whimsun/whimsun_fetal2.png"
    image whimsun happy = "characters/Whimsun/whimsun_happy.png"

    image migosp normal = "characters/Migosp/migosp_normal.png"
    image migosp angry = "characters/Migosp/migosp_angry.png"

    image dummy normal = "characters/Dummy/Dummy_Normal.png"

    image dummy blush =  "characters/Dummy/Dummy_Blush.png"


    #initialize the monsters
    call initialize_toriel from _call_initialize_toriel
    call initialize_napstablook from _call_initialize_napstablook
    call initialize_frisk from _call_initialize_frisk
    call initialize_flowey from _call_initialize_flowey

    #character-settings
    #character settings
    define diary = ('Diary')
    define narration = Character(kind=nvl)
    define system = Character('', color="#FFFFFF")
    define papyrusChar = Character('Papyrus', color="#FFFFFF", what_prefix='{font=font/Parchment-MF.ttf}{size=40}', what_suffix='{/size}{/font}')
    define xxxpapyrus = Character('xxx', color="#FFFFFF", what_prefix='{font=font/Parchment-MF.ttf}{size=40}', what_suffix='{/size}{/font}')
    define xxxsans = Character('xxx', color="#FFFFFF", what_prefix='{font=font/ComicRelief.ttf}{size=20}', what_suffix='{/size}{/font}')
    define sans = Character('Sans', color="#FFFFFF", what_prefix='{font=font/ComicRelief.ttf}{size=20}', what_suffix='{/size}{/font}')
    define wilsonChar = Character('Wilson', color="#FFFFFF")
    define froggit = Character('Froggit', color="#FFFFFF")
    define whimsun = Character('Whimsun', color="#FFFFFF")
    define loox = Character('Loox', color="#FFFFFF")
    define moldsmol = Character('Moldsmol', color="#FFFFFF")
    define vegetoid = Character('Vegetoid', color="#FFFFFF")
    define migosp = Character('Migosp', color="#FFFFFF")
    define dummy = Character('Dummy' , color="#FFFFFF")
    define floweyChar = Character('Flowey' , color="#FFFFFF")
    #sprite positions
    init:
        $ left = Position(xpos = 0.0, xanchor = 'left')
        $ center = Position(xpos = 0.5,ypos=.5, xanchor = 'center', yanchor = 'center')
        $ right = Position(xpos = .95, xanchor = 'right')


    init python:
        # Wrapper to capitalize Papyrus' text
        def papyrus(text, *args, **kwargs):
            papyrusChar(text, *args, **kwargs)

        def wilson(text, *args, **kwargs):
            wilsonChar(text, *args, **kwargs)

    #default-font
    init python:
        import webbrowser
        style.default.font = "font/DTM-Mono.otf"
        player = Player()
        menu_state = "stats"
        world = World()
        world.set_current_time(700,False)
        cell_convo_count = 0
