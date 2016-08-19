


label flowey_default_conversation(owner):
    menu:
        "How are you?":
            hide flowey
            show flowey horror at left
            show wilson ph at right
            wilson "*types furiously*"
        "I think I need help...":
            "nyi"
        "What do you do for fun around here?":
            "nyi"
        "How would you describe your perfect day?":
            "nyi"
        "What's it like being a flower?":
            "nyi"
        "How's the weather down there?":
            "nyi"
        "What do you think about....":
            call flowey_ruins_think_about(owner)
        "Do you believe in fate or destiny?":
            call flowey_ruins_fate(owner)
    return

label flowey_ruins_think_about(owner):
    menu:
        "What do you think about..."
        "Toriel":
            call flowey_think_about_monster(owner,"Toriel")
        "Frisk":
            call flowey_think_about_monster(owner,"Frisk")
        "Napstablook":
            call flowey_think_about_monster(owner,"Napstablook")
        "Mattaton":
            call flowey_think_about_monster(owner,"Mattaton")
        "Sans":
            call flowey_think_about_monster(owner,"Sans")
        "Papyrus":
            call flowey_think_about_monster(owner,"Papyrus")
        "Undyne":
            call flowey_think_about_monster(owner,"Undyne")
        "Alphys":
            call flowey_think_about_monster(owner,"Alphys")
        "Asgore":
            call flowey_think_about_monster(owner,"Asgore")
    return

label flowey_think_about_monster(owner,monster):
    if owner.get_relationship() == 'Hated' or owner.get_relationship() == 'Disliked':
        show flowey annoyed
        flowey "Well they don’t waste my time as much as you."
        flowey "So on that note, from a scale of 1 to 10, you’re hell of a lot worse than they are."
        flowey "And yes, choosing a different person for me to critique will give you the exact same answer."
        show flowey normal
        flowey "So spare me repeating myself until you’re further acquainted with someone who cares about you."
        show flowey sideglance
        flowey "Which so far…"
        show flowey horror
        flowey "No one does."
    return


label flowey_ruins_fate(owner):
    
    $ r = owner.get_relationship()

    if r == 'Hated':
        show flowey smug
        flowey "I believe in burying people alive and hearing them scream."
    elif r == "Disliked":
        show flowey annoyed
        flowey "Is this really a question you should be bothering with now?"
        flowey "It's nice to see you have your priorities straightened out."
    else:
        show flowey annoyed
        flowey "Neither."
        flowey "Both are dumb."
    return