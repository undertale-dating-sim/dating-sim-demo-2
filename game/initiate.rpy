label initialize:
    


    #stupid stuff for demo
    image wilson large = im.FactorScale("avatar.png",4.0)
    image wilson ph = "characters/Wilson/avatar_hover.png"
    image wilson scary = im.FactorScale("characters/Wilson/nightmare_pupper.png",2.0)
    #background-images

    #toriel's house
    image background frisk_room = Frame("backgrounds/TorielsHouse/Background-Ruins-TorielHome-FrisksRoom.jpg")
    image background toriel_kitchen = Frame("backgrounds/TorielsHouse/background-ruins-kitchen.png")
    #snowdin
    image background snowdin = "backgrounds/snowdincropped.jpg"
    image background papyrus_room = "backgrounds/Background-PapyrusRoom.jpg"
    image background snowdin_bridge = "backgrounds/Background-Snowdin-Bridge-cropped.jpg"
    image background snowdin_forest = "backgrounds/Background-Snowdin-Gate2.jpg"
    image background snowdin_icegolf = "backgrounds/Background-Snowdin-Icegolf.png"
    image background snowdin_intersection = "backgrounds/Background-Snowdin-Intersection.png"
    image background snowdin_snowman = "backgrounds/Background-Snowdin-Snowman.png"

    image background papyrus_number = "characters/Papyrus-number.png"

    #prologue
    image background prologue1 = "backgrounds/prologue.jpg"
    image background intro = "backgrounds/background-intro.png"

    #random monsters
    image froggit normal = "characters/Froggit/Froggit_normal.png"
    image froggit happy = "characters/Froggit/Froggit_happy.png"

    image vegetoid normal = "characters/Vegetoid/vegetoid_normal.png"
    image vegetoid happy = "characters/Vegetoid/vegetoid_happy.png"

    image loox normal = "characters/Loox/loox_normal.png"
    image loox happy = "characters/Loox/loox_happy.png"
    image loox surprised = "characters/Loox/loox_surprised.png"

    image moldsmol normal = "characters/Moldsmol/moldsmol_normal.png"
    image moldsmol happy = "characters/Moldsmol/moldsmol_happy.png"
    image moldsmol nervous = "characters/Moldsmol/moldsmol_nervous.png"

    image napstablook normal = "characters/Napstablook/napstablook_normal.png"

    image whimsun normal = "characters/Whimsun/whimsun_normal.png"

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
        $ center = Position(xpos = 0.5, xanchor = 'center')
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
        world.set_current_time(700,True)
        cell_convo_count = 0
