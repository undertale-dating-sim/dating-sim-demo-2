# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Main Game") action Start()
        # textbutton _("Testing Area") action ui.callsinnewcontext("testing_area")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Art Gallery") action ShowMenu("art_gallery")
        textbutton _("Mix and Match") action ShowMenu("mix_gallery")
        # textbutton _("Feedback") action Jump("Feedback")
        # textbutton _("Admin_Controls") action ShowMenu("admin_controls")
        # textbutton _("Update") action Jump("updater")
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"


label Feedback:
    $ webbrowser.open("https://goo.gl/forms/imVfvnNXL39SAD423")
    return
##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

init -3:
    $ ADMIN_ROOM_DESC = False

#######################################
# Admin Controls
# Customer Screen made by Wilson to control finer parts of the game.  Should be taken out of public release
#\

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen admin_controls():
    tag menu

    use navigation

    grid 3 1:

        style_group "prefs"
        xfill True

        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Room Descriptions [ADMIN_ROOM_DESC]")
                textbutton _("toggle") action ToggleVariable("ADMIN_ROOM_DESC")
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Test")
                textbutton _("Test") action Notify('test')
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Test")
                textbutton _("Test") action Notify('test')



screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0

##############################################################################

# Gallery of in-game artwork

##############################################################################

init +1 python:
    #list all the sprites here:
    gallery_spr_items = ["flowey normal", "flowey backside", "flowey annoyed", "flowey sideglance", "flowey surprised", "flowey blush",  "flowey wink", "flowey excited", "flowey laugh", "flowey sad", "flowey smug", "flowey horror",  "flowey suspicious", "flowey angry", "flowey sad",
                        "frisk angry", "frisk annoyed", "frisk bigsmile", "frisk blushing", "frisk disappointed", "frisk distant", "frisk giggly", "frisk hurtsurprised", "frisk normal", "frisk sad", "frisk somehappy", "frisk smallsmile", "frisk surprised", "frisk tearyeyes", "frisk upset",
                        "toriel placeholder", "toriel angry", "toriel annoyed", "toriel awkward", "toriel blushing", "toriel laughing", "toriel normal", "toriel reallysad", "toriel sad", "toriel smallsmile", "toriel smile", "toriel surprised",
                        "napstablook normal", "napstablook sad", "napstablook shyblush", "napstablook smallsmile", "napstablook smile", "napstablook surprised",
                        "grillby grillby1", "grillby grillby2", "grillby grillby3", "grillby grillby4", "grillby grillby5", "grillby grillby6", "grillby grillby7", "grillby grillby8", "grillby grillby9", "grillby grillby10", "grillby grillby11", "grillby grillby12"]
    #list all background art
    gallery_bkg_items = ["bg1", "bg2", "bg3", "bg4", "bg5", "bg6", "bg7", "bg8", "bg9", "bg10", "bg11", "bg12", "bg13", "bg14", "bg15", "bg16", "bg17", "bg18", "bg19", "bg20", "bg21", "bg22"]
    
    #how many rows and columns in the gallery screens?
    spr_rows = 1 # Mix n' match of sprites and scenes, selection menu
    spr_cols = 1
    bkg_rows = 1
    bkg_cols = 1
    
    art_rows = 2 # Art gallery of all background art
    art_cols = 3
    
    #thumbnail size in pixels:
    spr_x = 250
    spr_y = 375
    bkg_x = 400
    bkg_y = 600
    
    art_x = 267
    art_y = 150
    
    #generated for convenient use later- total number of imagebuttons per page
    spr_cells = spr_rows * spr_cols
    bkg_cells = bkg_rows * bkg_cols
    art_cells = art_rows * art_cols
    
    poss_indices = ((int(len(gallery_bkg_items))/bkg_cells) - 1)
    
    #creating gallery object for sprite selection menu
    g_spr = Gallery()
    spr_page = 0
    scene_background = "images/backgrounds/Ruins/background-ruins-blacktree.png" #Default background if none chosen
    spr_pos = "right"
    modifier = 0
    
    g_bkg = Gallery()
    bkg_page = 0
    
    g_art = Gallery()
    for gal_item in gallery_bkg_items:
        g_art.button(gal_item + " butt")
        g_art.image(gal_item)
        #g_art.unlock(gal_item) #unlock once seen- doesn't work yet
    g_art.transition = fade
    art_page=0
    
init +1 python:
    #creating thumbnails
    for gal_item in gallery_spr_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), spr_x, spr_y))
    for gal_item in gallery_bkg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), bkg_x, bkg_y))     # For mix n' match
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), art_x, art_y))     # For art gallery
        renpy.image (gal_item + " butt dis", im.Grayscale(ImageReference(gal_item + " butt")))
        
screen mix_gallery:
    python:
        for gal_item in gallery_spr_items:
            g_spr.button(gal_item + " butt")
            g_spr.image(scene_background,gal_item)
            g_spr.unlock(gal_item)
        g_spr.transition = fade
        for gal_item in gallery_bkg_items:
            g_bkg.button(gal_item + " butt")
            g_bkg.image(gal_item)
        g_bkg.transition = fade
    tag menu
    frame:
        #use navigation
        background "backgrounds/ui/journal.png"
        
        $ next_spr_page = spr_page + 1                               # Functions to change "pages" for mix n' match gallery
        $ prev_spr_page = spr_page - 1
        $ next_bkg_page = bkg_page + 1
        $ prev_bkg_page = bkg_page - 1
#        $ set_bkg = gallery_bkg_items[(bkg_page+modifier)*bkg_cells]
        $ set_spr_pos = 1
        
        if prev_bkg_page < 0:
            $ prev_bkg_page = int(len(gallery_bkg_items)/bkg_cells)
        
        imagebutton idle "images/UI/showleft.png" xpos 500 ypos 200 focus_mask None action [SetVariable('spr_pos', set_spr_pos)] at scalearrow
        imagebutton idle "images/UI/showmid.png" xpos 500 ypos 300 focus_mask None action [SetVariable('spr_pos', set_spr_pos)] at scalearrow
        imagebutton idle "images/UI/showright.png" xpos 500 ypos 400 focus_mask None action [SetVariable('spr_pos', set_spr_pos)] at scalearrow
##        imagebutton idle "images/UI/generate.png" xalign .98 yalign .99 focus_mask True action [SetVariable('spr_pos', set_spr_pos)] at scalearrow

##        imagebutton idle gallery_bkg_items[bkg_page] xpos 500 ypos 200 focus_mask None action [If(next_bkg_page > 21, SetVariable('bkg_page', 0), SetVariable('bkg_page', (bkg_page + 1)))] at scalearrow

        imagebutton idle "images/UI/right_arrow.png" xpos 300 ypos 450 focus_mask True action [SetVariable('spr_page', next_spr_page)] at scalearrow
        imagebutton idle "images/UI/left_arrow.png" xpos 75 ypos 450 focus_mask True action [SetVariable('spr_page', prev_spr_page)] at scalearrow


############################ THE BUG IS HERE ##########################################

        ## Currently trying to squish a bug where the background in the composite sprite + background image lags one selection behind the one displayed in the menu. This code does not crash.
        imagebutton idle "images/UI/right_arrow.png" xpos 650 ypos 450 focus_mask True action [If(next_bkg_page > poss_indices, SetVariable('bkg_page', 0), SetVariable('bkg_page', next_bkg_page)), SetVariable('scene_background', gallery_bkg_items[bkg_page])] at scalearrow
        imagebutton idle "images/UI/left_arrow.png" xpos 425 ypos 450 focus_mask True action [If(prev_bkg_page > poss_indices, SetVariable('bkg_page', poss_indices), SetVariable('bkg_page', prev_bkg_page)), SetVariable('scene_background', gallery_bkg_items[bkg_page])] at scalearrow

        ## This code no longer has the background bug, but will crash the game once you reach image #22 (index = 21)
#        imagebutton idle "images/UI/right_arrow.png" xpos 650 ypos 450 focus_mask True action [If(next_bkg_page > poss_indices, SetVariable('bkg_page', 0), SetVariable('bkg_page', next_bkg_page)), SetVariable('scene_background', gallery_bkg_items[bkg_page+1])] at scalearrow
#        imagebutton idle "images/UI/left_arrow.png" xpos 425 ypos 450 focus_mask True action [If(prev_bkg_page > poss_indices, SetVariable('bkg_page', poss_indices), SetVariable('bkg_page', prev_bkg_page)), SetVariable('scene_background', gallery_bkg_items[bkg_page])] at scalearrow

############################ THE BUG IS HERE ##########################################
        
##        SetVariable('scene_background', gallery_bkg_items[bkg_page])
        
        grid spr_rows spr_cols:
            xpos 100
            ypos 75
            
            if next_spr_page > int(len(gallery_spr_items)/spr_cells):    # "Overflow" functions
                $ next_spr_page = 0
            if prev_spr_page < 0:
                $ prev_spr_page = int(len(gallery_spr_items)/spr_cells)
                
            $ i = 0
            for gal_item in gallery_spr_items:
                $ i += 1
                if i <= (spr_page+1)*spr_cells and i>spr_page*spr_cells:
                    add g_spr.make_button(gal_item + " butt", gal_item + " butt", im.Scale("images/UI/locked.png", spr_x, spr_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (spr_page+1)*spr_cells): #we need this to fully fill the grid
                null
                        
        grid bkg_rows bkg_cols:
            xpos 425
            ypos 100
            
            $ i = 0
            for gal_item in gallery_bkg_items:
                if i < (bkg_page+1)*bkg_cells and i>=bkg_page*bkg_cells:
                    add g_bkg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("images/UI/locked.png", bkg_x, bkg_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                $ i += 1
            for j in range(i, (bkg_page)*bkg_cells): #we need this to fully fill the grid
                null
        
#        if (next_bkg_page > poss_indices):
#            $ set_bkg = gallery_bkg_items[0]
#            text ("%s" % "Works"):
#                xalign .06
#                yalign .02
#        else:
#            $ set_bkg = gallery_bkg_items[(bkg_page+1)*bkg_cells]
#            text ("%i" % next_bkg_page):
#                xalign .06
#                yalign .02

        text ("%s" % "bkg_page: "):
            xalign .02
            yalign .02

        text ("%i" % bkg_page):
            xalign .2
            yalign .02

        vbox:
            style_group "gm_nav"
            xalign .98 yalign .02
            textbutton _("Return") action Return()
            textbutton _("Help") action Help()
            textbutton _("Quit") action Quit(confirm=False)
        
screen art_gallery:
#The art gallery screen is more or less copy pasted from the spr screen above, I only changed "make_button" to include a grayscale thumbnail for locked items
    tag menu
    use navigation
    frame background None xpos 10:
        grid art_rows art_cols:
            ypos 10
            $ i = 0
            $ next_art_page = art_page + 1
            $ prev_art_page = art_page - 1
            if next_art_page > int(len(gallery_bkg_items)/art_cells):
                $ next_art_page = 0
            if prev_art_page < 0:
                $ prev_art_page = int(len(gallery_bkg_items)/art_cells)
            for gal_item in gallery_bkg_items:
                $ i += 1
                if i <= (art_page+1)*art_cells and i>art_page*art_cells:
                    add g_art.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (art_page+1)*art_cells):
                null
        
        imagebutton idle "images/UI/right_arrow.png" xpos 400 ypos 500 focus_mask True action [SetVariable('art_page', next_art_page), ShowMenu("art_gallery")] at scalearrow
        imagebutton idle "images/UI/left_arrow.png" xpos 100 ypos 500 focus_mask True action [SetVariable('art_page', prev_art_page), ShowMenu("art_gallery")] at scalearrow
    

init -2:
    transform scalearrow:
        on idle:
            zoom 1.0
        on hover:
            zoom 1.05

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

