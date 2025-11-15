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
            jump day2
        menu:
            "Search the kitchen":
                if randRoom == 1:
                    jump encounter1
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    e "It is a bit chilly here."
                    $ searchNum += 1
                    jump searchRoom1

            "Search the living room":
                scene bg house_night with dissolve
                if randRoom == 2:
                    jump encounter1
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    e "It is a bit chilly here."
                    $ searchNum += 1
                    jump searchRoom1
                    
            "Search the storage room":
                if randRoom == 3:
                    jump encounter1
                else:
                    "Nothing here seems out of place, everything seems fine..."
                    e "It is a bit chilly here."
                    $ searchNum += 1
                    jump searchRoom1
        

        label encounter1:
            "I see Constance lingering, her curious eyes darting around the current room she’s in."

            s "You know, Ms. Elysia, I find it amusing how alike you are to this protagonist from a book I loved so dearly."

            "I felt myself choke on my spit, my ears heating up at Constance’s random comment."

            e "M-Me? Um… I doubt I’m like any of the protagonists from books you’ve read-"

            s "It’s true! You’re quite aloof, yet on your feet- like an adventurer ready to dash in at any given moment. You act all grumpy and strong but I can sense a little softie within."

            e "..."

            s "..."

            s "Kinda like this hero in my books… they aren’t a person with some grand destiny, they travel to find their purpose and maybe help others on the way."

            "Listening to Constance talk, I can’t help but feel flustered. To be compared to a character from a book she loved dearly, I feel like she’s holding me to such a high regard, despite just meeting me."

            menu:
                "Ask her about her interest":
                    "I can’t help but be captivated by her. What kind of person was Constance? What were her hobbies and interests? What things did she like?"

                    s "Oh!- My hobbies and interests, you say?"

                    s "As you can tell, I’m fond of reading novels."

                    e "Oh, really? What kind of novels do you like?"

                    "Constance smiled sheepishly and answered timidly."

                    s "I indulged a lot in romance novels, specifically damsel in distress stories, as I enjoyed them quite a lot."

                    s "But other than that, I also took part in horseback riding and playing the piano."

                    e "We surprisingly have a lot in common. I also played an instrument- well, used to. And I’m also fond of reading manga and light novels. Anyways… I hardly have time for that nowadays with work and all."

                    "As I explained my hobbies to her, Constance had a look of pure curiosity on whatever’s behind that ghostly apparition she puts up."

                    s "Man-ga? Oh! You mean Mangoes? I heard from my father that it’s a rare foreign fruit that nobles eat in its country of origin  – so you too must be a noble!"

                    e "Ah- You have me mistaken, I’m not a noble. And no, I don’t like Mangoes – Well, I do, but Manga isn’t Mangoes."

                    e "It’s well- Like um… Picture books?"

                    s "Like what children read?"

                    e "What? No- Well, children can read some of them. But Manga is for all ages, sometimes they even tackle topics that only adults are capable of understanding."

                    "I led her towards the chaotic shelf in my living room."

                    e "The best way I could describe them is that they’re like picture books, but more elaborate and detailed. Here, let me show you how they usually look."

                    "I grab one of my mangas from the shelf and open up a random page for Constance to see."

                    "Oh, that’s two women kissing-"

                    menu:
                        "I quickly shut the manga":
                            e "HMM! Must’ve been the wind…"

                    "Constance tilts her head curiously, puzzled by my behavior. Before she could ask more about it, I picked out another manga and flipped open a more appropriate page."

                    "..."

                    "The more I explained about my ‘modern’ hobbies, the more Constance emanates this curious energy about her. She seemed so captivated the more I talk, which I honestly find quite adorable-"

                    "WHAT AM I THINKING? That’s a dead woman’s spirit, get yourself together Elysia Leclerc."

                    s "You know, Ms. Elysia, I envy you…"

                    e "Me? How come?"

                    s "Your life just feels so… unrestricted, free… It’s such a contrast to how I lived my life back then."

                    e "What do you mean?"

                    "Constance chortled sheepishly, immediately changing the topic to divert the topic away from her personal life."

                    s "Anyways! Enough about me, I think we should coordinate a get-together where we read a book together."

                    s "Especially since it’s the first time I’ve ever met you, the tenant of this place. Usually when I wake up during the blood moon, there’s nothing but empty space and silence who greets me…"

                    "Before I could protest against Constance’s plan, she let out a tired yawn."

                    s "I guess that’s my cue to leave then. I feel… sleepy yawns. I’ll see you tomorrow evening then, ta-ta!"

                    e "Wait! But where do I find you?"

                    "I sigh as Constance’s ghostly figure phases through a wall. There she goes, I guess."

                    "Spending time with her was… interesting, to say the least."

                    jump day2

                "Disregard her interest":
                    e "Zip it, okay? I’m not in the mood for whatever shenanigans you’re up to. I’m exhausted from work."

                    "It seems mean, but I decided to brush her off. It’s better if I just avoid her. I don’t know what her intentions are, and whether she’s harmless or not."

                    "Constance noticed that I brushed her off. She looks a bit discouraged as I hear her mumbling something."

                    s "I don’t see the need for you to be so rude… You are just like him."

                    s "I guess not all heroes are one-to-one with that of a novel’s."

                    "I turn to Constance, who’s still mumbling incoherently and sighed. I am not in the mood for this."

                    e "I know it’s the blood moon, but why are you even here? Can you not, I don’t know- leave? I’m so confused…"

                    s "I’m just as confused as you are… I don’t even recall how I arrived in this place."

                    "Constance looks at me with hope in her eyes."

                    s "Perhaps… My manor and your ‘apartment’ are within the same plot of land?"

                    "Is she serious? I pinched the bridge of my nose as I looked at her with a tired expression."

                    e "No way, really?!"

                    "At my exasperated reply, I notice Constance’s eyes grow dreary. I feel kinda bad, but I could not care any less."

                    "I just want her out of my home."

                    s "Well um… From novels I’ve read, ghouls who usually have unfinished business turn into ghosts-"

                    e "Then do what you must to finish your unfinished business."

                    jump day2

            




    label day2:
        "its a new day"



    # This ends the game.
    return
