# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Ah welcome to Astro Fes, I should probably find my friends."

    e "Now where is he.... Huh-!?"

    e "Izumi Sena: Please, one at a time..."

    e "Izumu Sena:Are you ok?"

    menu:
        "I'm Fine, thanks though...":
            jump Option1

        "I'm trying to find Airi, not you":
            jump Option2

    label Option1:
        e "Izumu Sena: Don't worry about me, Karasu."
        pass

    label Option2:
        e "Izumu Sena: Fuck you too damn!"
        pass

    # This ends the game.

    return
