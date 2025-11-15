# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Elysia"), color="#ddaacc")
define s = Character(_("Constance"), color="#91caca")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg house_night

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Noises echo through my apartment walls as I sink deeper into my couch— reruns of Scooby Doo playing in the background as my mind drifts to anywhere but this room."

    e "What a day..."

    "While I munch away mindlessly, my ears perk up at the sound of my show being interrupted by a sudden news flash."

    "Apparently, a blood moon was about to occur, three years after the last time. Supposedly, it'll last for four days."

    "Personally, I don't really care for it. I mean, the moon turns red — I doubt it does anything other than make evenings a tad bit spookier."

    "Oh, how wrong I was. I didn’t know that the blood moon did something other than turn the moon red. Apparently, it strengthens the connection of the spiritual realm to earth."

    "I didn’t believe it at first when I found out, but it all changed because of this one particular night."

    "Having had enough of pizza and Scooby Doo, I decided to call it a night. Before heading to bed, I leave my dirty dishes on the sink."

    "I can just deal with them tomorrow. I hear my bed calling, and I’m more than ready to sleep."

    "..."

    "CLANG CLANG"

    "I look at the clock on my nightstand."

    "12:03 am."

    "I sit up and rub my eyes. I heard something... I think it came from the kitchen."

    "What the- did a raccoon get into my apartment? Impossible. I remember I locked this... Weird."

    "{i}Rattle, rattle...{/i}"

    "Where is that noise coming from— wait... could it be a ghost!?"

    "..."

    "Oh please, Elysia, ghosts aren’t real. It’s probably some rogue animal or... maybe a robber!?"

    e "I should get something to defend myself..."

    menu:
        "Get stale baguette":
            e "Uh... this should work."

    "Now to look around"

    $ randRoom = renpy.random.randint(1, 3)
    ## Since this is the tutorial, we'll let the player have infinite tries to search.
    label searchRoom:
        menu:
            "Check Cupboard":
                if randRoom == 1:
                    jump encounter
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    e "It is a bit chilly here."
                    jump searchRoom

            "Check Fridge":
                if randRoom == 2:
                    jump encounter
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    jump searchRoom

            "Check Sink":
                if randRoom == 3:
                    jump encounter
                else:
                    "Huh—?"
                    e "I never cleaned or organized these dishes... have I?"
                    jump searchRoom

        label encounter:
            "{i}Rattle, rattle...{/i}"
            e "There you are."

            "I quickly grab the door open, my other hand ready to strike anything that comes ou-"

            e "Empty...?"

            "Am I going crazy? I heard something move- no, I SAW it move."

            e "Come out, come out wherever you are~"

            ## Makes character appear with fade-in (dissolve) and scales them properly
            show ghost normal with dissolve: 
                xalign 0.5
                yalign 0.55
                zoom 0.8

            "???" "Yes?"

            "--!?"

            ## vpunch shakes the screen vertically, hpunch does similarly horizontally
            e "{size=70}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/size}" with vpunch 

            "A foggy figure appears right in front of me, her form not quite whole."

            show ghost happy
            "???" "That’s quite a... unique weapon there, dearie, do you need something? Perhaps a better weapon, ehe~"

            e "Need something-!? What the- Who are you?!"

            show ghost surprise
            "???" "Oh, that's quite unlady-like of me."

            show ghost normal
            s "I am Constance Claire Juliette, from house DuFontaine."

            e "..."

            show ghost happy
            s "..."
            
            show ghost awkward
            s "Uhm... you can call me Constance."

            show ghost normal
            s "And hm... this isn’t my father's manor."

            "I really think I’m losing it, first, I’m seeing and hearing things that aren’t really there— now I’m listening to this... {i}THING{/i} talks about my apartment being some sort of Manor!"

            e "I’m sorry, what?"

            s "My sincerest apologies there, last I remember I was on my way to-"
            
            show ghost awkward
            s "Oh, good heavens! I should not bear to you my life story— that is unlady-like of me."

            "Manor...? Ladylike-ness? Either I’m going insane or this is a ghost...
            So I’m going insane."

            e "Hold on there, so are you implying you’re a ghost?"

            show ghost dumpy with dissolve
            "The ghostly blur seems to twist and turn— suddenly turning back to me."

            show ghost normal with dissolve
            s "A ghoul, ghostly apparition or a geist— either way, you seem to be correct Miss..."

            e "Elysia."

            show ghost happy
            s "Ms. Elysia! Such a beautiful name."

            s "It seems the sun is about to rise— I do feel a tad tired... {i}(yawn...){/i}"

            e "Wait-!"

            menu:
                "Can I see your true form?":
                    show ghost normal
                    s "Maybe not now... I’ve only just known you, Ms. Elysia. Maybe when we’re closer, I’ll show you my real form..."

                    show ghost happy
                    s "Don’t worry, call me a romantic but something tells me this won’t be our last meeting, you’ll have plenty of chances to get to know me~"

                    e "How can you be so sure?"

                    show ghost normal
                    s "Well, I may be a ghost but I can’t be everywhere." 

                    show ghost happy
                    s "Maybe when the room feels eerie- Boo! I’ll be there, ehe~"

                    s "I am a busy woman, so please don’t take too long finding me— if you do, the sun may rise and I’ll be left a distant ‘what if?’ of the night~"

                    jump day1

                "Nevermind... rest well.":
                    show ghost normal
                    s "You truly are sweet... rest well too there, Ms. Elysia."

                    jump day1



label day1:

    scene bg black with dissolve

    "..."

    "{i}“Don’t worry, call me a romantic but something tells me this won’t be our last meeting, you’ll have plenty of chances to get to know me~”{/i}"

    "Constance’s words kept me up as I tossed and turned all over my bed.
    What does she mean by that? Does she plan to linger in my apartment?"

    scene bg bedroom_night with dissolve

    "I look outside the window and the blood moon greets me back, the giant orb irritatingly red, as if mocking my current predicament."

    "Four days, huh? Maybe that has something to do with her."

    "Before I even get the chance to lose myself in my thoughts, I hear sounds coming from another room."

    "She must be around."

    $ randRoom = renpy.random.randint(1, 3)
    $ searchNum = 0

    label searchRoom1:
        if searchNum >= 2:
            $ searchNum = 0
            "Huh... No matter how hard I looked, she's not here."
            "Maybe I’ll see her tomorrow."
            scene bg black with dissolve
            jump day2
        menu:
            "Search the kitchen":
                if randRoom == 1:
                    e "I see Constance standing by my bookshelf, her curious eyes going over the numerous books messily strewn about gathering dust."
                    jump encounter1
                else:
                    "Hmmm... These dishes are still piled up from where I left them last time."
                    "Seems like she’s not here."
                    $ searchNum += 1
                    jump searchRoom1

            "Search the living room":
                scene bg house_night with dissolve
                if randRoom == 2:
                    e "I see Constance standing by my bookshelf, her curious eyes going over the numerous books messily strewn about gathering dust."
                    jump encounter1
                else:
                    "Huh... I swore I heard noises coming from here."
                    "Turns out I was wrong, it’s just me and that spot of mold on the wall."
                    $ searchNum += 1
                    jump searchRoom1
                    
            "Search the storage room":
                if randRoom == 3:
                    e "I see Constance standing by my bookshelf, her curious eyes going over the numerous books messily strewn about gathering dust."
                    jump encounter1
                else:
                    "My eyes must be deceiving me... I thought I saw a shadow move towards here."
                    "There’s nothing but dust particles in this room. Looks like she’s not around."
                    $ searchNum += 1
                    jump searchRoom1
        

        label encounter1:
            s "You know, Ms. Elysia, I find it amusing how alike you are to this protagonist from a book I loved dearly."

            "I felt myself choke on my spit, my ears heating up at Constance’s random comment."

            e "M-Me? Um... I doubt I’m like any of the protagonists from books you’ve read-"



    label day2:
        "its a new day"



    # This ends the game.
    return
