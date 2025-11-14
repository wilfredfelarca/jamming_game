# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elysia")
define s = Character("Schariac")


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

    "Noises echo through my apartment walls as I sink deeper into my couch— reruns of Scooby Doo playing in the background as my mind drifts to anywhere but this room."

    e "What a day…"

    "While I munch away mindlessly, my ears perk up at the sound of my show being interrupted by a sudden news flash. Apparently, a blood moon was going to happen again after 3 years, and this time it will last for 4 days."

    "Personally, I don't really care for it. I mean, the moon turns red — I doubt it does anything other than make evenings a tad bit spookier."

    "Oh, how wrong I was. I didn’t know that the blood moon did something other than turn the moon red. Apparently, it strengthens the connection of the spiritual realm to earth."

    "I didn’t believe it at first when I found out, but it all changed because of this one particular night."

    "Having had enough of pizza and Scooby Doo, I decided to call it a night. Before heading to bed, I left my dirty dishes on the sink. I can just deal with them tomorrow. I hear my bed calling, and I’m more than ready to sleep."

    "..."

    "CLANG CLANG"

    "I look at the clock on my nightstand."

    "12:03 am"

    "I sit up and rub my eyes. I heard something… I think it came from the kitchen."

    "What the- did a raccoon get into my apartment? Impossible. I remember I locked this… Weird."

    "*Rattle Rattle*"

    "Where is that noise coming from— wait… could it be a ghost!?"

    "..."

    "Oh please, Elysia, ghosts aren’t real. It’s probably some rogue animal or… maybe a robber!?"

    e "I should get something to defend myself…"

    menu:
        "Get stale baguette":
            e "Uh... this should work."

    "Now to look around"

    $ randRoom = renpy.random.randint(1, 3)
    $ searchNum = 0
    label searchRoom:
        if searchNum == 2:
            jump day1
        menu:
            "Check Cupboard":
                if randRoom == 1:
                    jump encounter
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    e "It is a bit chilly here."
                    $ searchNum += 1
                    jump searchRoom

            "Check Fridge":
                if randRoom == 2:
                    jump encounter
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    $ searchNum += 1
                    jump searchRoom

            "Check Sink":
                if randRoom == 3:
                    jump encounter
                else:
                    "Huh—?"
                    e "I never cleaned or organized these dishes… have I?"
                    $ searchNum += 1
                    jump searchRoom

        label encounter:
            "*Rattle, Rattle*"
            e "There you are."

            "I quickly grab the door open, my other hand ready to strike anything that comes ou-"

            e "Empty…?"

            "Am I going crazy? I heard something move- no, I SAW it move."

            e "Come out, come out wherever you are~"

            "???" "Yes?"

        label day1:
            "It's a new day"



    # This ends the game.

    return
