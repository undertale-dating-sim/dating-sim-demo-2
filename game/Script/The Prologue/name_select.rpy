label name_select:
    
    #list of reactions
    $ taken_names = []
    $ taken_reactions = []

    $ taken_names.append("papyrus")
    $ taken_reactions.append("THAT NAME IS TAKEN HUMAN!")


    #Name input

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if taken_names.count(player_name.lower()) > 0:
        $ clean_name = player_name.lower()
        $ reaction = taken_reactions[taken_names.index(clean_name)]
        "[reaction]"
        jump name_select
    else:
        #We could add a function here to capitalize the name, or not.
        "Hello, [player_name]!"

    return