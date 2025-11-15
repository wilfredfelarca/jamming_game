# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(_("Elysia"), color="#ddaacc")
define s = Character(_("Constance"), color="#91caca")

## Affection value determines the ending, increases with good interaction
default affection = 0

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
                scene bg kitchen with dissolve
                if randRoom == 1:
                    jump encounter1
                else:
                    "Hmmm... These dishes are still piled up from where I left them last time."
                    "Seems like she’s not here."
                    $ searchNum += 1
                    jump searchRoom1

            "Search the living room":
                scene bg house_night with dissolve
                if randRoom == 2:
                    jump encounter1
                else:
                    "Huh... I swore I heard noises coming from here."
                    "Turns out I was wrong, it’s just me and that spot of mold on the wall."
                    $ searchNum += 1
                    jump searchRoom1
                    
            "Search the storage room":
                scene bg storage with dissolve
                if randRoom == 3:
                    jump encounter1
                else:
                    "My eyes must be deceiving me... I thought I saw a shadow move towards here."
                    "There’s nothing but dust particles in this room. Looks like she’s not around."
                    $ searchNum += 1
                    jump searchRoom1
        

        label encounter1:
            "I see Constance lingering, her curious eyes darting around the room."

            show ghost happy with dissolve: 
                xalign 0.5
                yalign 0.55
                zoom 0.8
            s "You know, Ms. Elysia, I find it amusing how alike you are to this protagonist from a book I loved so dearly."

            "I felt myself choke on my spit, my ears heating up at Constance’s random comment."

            e "M-Me? Um... I doubt I’m like any of the protagonists from books you’ve read-"

            show ghost normal
            s "It’s true! You’re quite aloof, yet on your feet- like an adventurer ready to dash in at any given moment.
            You act all grumpy and strong, but I can sense a little softie within."

            e "..."

            s "..."

            show ghost happy2
            s "Kinda like this hero in my books... they aren’t a person with some grand destiny, they travel to find their purpose and maybe help others on the way."

            "Listening to Constance talk, I can’t help but feel flustered. To be compared to a character from a book she loved dearly, I feel like she’s holding me to such a high regard, despite just meeting me."

            menu:
                "Ask her about her interest":
                    $ affection += 1
                    $ renpy.notify("Constance bond up!")

                    "I can’t help but be captivated by her. What kind of person was Constance? What were her hobbies and interests? What things did she like?"

                    show ghost surprise
                    s "Oh!- My hobbies and interests, you say?"

                    show ghost normal
                    s "As you can tell, I’m fond of reading novels."

                    e "Oh, really? What kind of novels do you like?"

                    show ghost happy
                    "Constance smiled sheepishly and answered timidly."

                    s "I indulged a lot in romance novels, specifically damsel in distress stories, as I enjoyed them quite a lot."

                    s "But other than that, I also took part in horseback riding and playing the piano."

                    e "We surprisingly have a lot in common. I also played an instrument- well, used to. And I’m also fond of reading manga and light novels. Anyways... I hardly have time for that nowadays with work and all."

                    show ghost confused
                    "As I explained my hobbies to her, Constance had a look of pure curiosity on whatever’s behind that ghostly apparition she puts up."

                    s "Man-ga? Oh! You mean mangoes? I heard from my father that it’s a rare foreign fruit that nobles eat in its country of origin  – so you must be a noble too!"

                    e "Ah- You have me mistaken, I’m not a noble. And no, I don’t like mangoes – Well, I do, but Manga isn’t mangoes."

                    e "It’s well- Like um... picture books?"

                    show ghost normal
                    s "Like what children read?"

                    e "What? No- Well, children can read some of them. But manga is for all ages, sometimes they even tackle topics that only adults are capable of understanding."

                    if randRoom == 2:
                        "I led her to the chaotic shelf by the wall."
                    else:
                        scene bg house_night with dissolve
                        show ghost normal with dissolve: ## Because scene clears all the characters shown, we need to reinitialize them.
                            xalign 0.5
                            yalign 0.55
                            zoom 0.8
                        "I led her towards the chaotic shelf in my living room."

                    e "The best way I could describe them is that they’re like picture books, but more elaborate and detailed. Here, let me show you how they usually look."

                    "I grab one of my manga from the shelf and open up a random page for Constance to see."

                    "Oh, that’s two women kissing-"

                    menu:
                        "I quickly shut the manga":
                            e "Hmm! Must’ve been the wind..."

                    show ghost confused
                    "Constance tilts her head curiously, puzzled by my behavior. Before she could ask more about it, I picked out another manga and flipped open a more appropriate page."

                    show ghost normal
                    "..."

                    "The more I explained about my ‘modern’ hobbies, the more Constance emanates this curious energy about her. She seemed so captivated the more I talk, which I honestly find quite adorable-"

                    "What am I thinking?! That’s a dead woman’s spirit, get yourself together, Elysia Leclerc!"

                    show ghost happy
                    s "You know, Ms. Elysia, I envy you..."

                    e "Me? How come?"

                    show ghost normal
                    s "Your life just feels so... unrestricted, free... It’s such a contrast to how I lived my life back then."

                    e "What do you mean?"

                    "Constance chortled sheepishly, immediately changing the topic to divert the topic away from her personal life."

                    show ghost happy
                    s "Anyways! Enough about me, I think we should coordinate a get-together where we read a book together."

                    s "Especially since it’s the first time I’ve ever met you, the tenant of this place. Usually when I wake up during the blood moon, there’s nothing but empty space and silence who greets me..."

                    "Before I could protest against Constance’s plan, she let out a tired yawn."

                    show ghost normal
                    s "I guess that’s my cue to leave then. I feel... sleepy. I’ll see you tomorrow evening then, ta-ta!"

                    hide ghost with dissolve
                    e "Wait! But where do I find you?"

                    "I sigh as Constance’s ghostly figure phases through a wall. There she goes, I guess."

                    scene bg black with dissolve
                    "Spending time with her was... interesting, to say the least."

                    jump day2

                "Disregard her interest":
                    show ghost surprised
                    e "Zip it, okay? I’m not in the mood for whatever shenanigans you’re up to. I’m exhausted from work."

                    "It seems mean, but I decided to brush her off. It’s better if I just avoid her. I don’t know what her intentions are, and whether she’s harmless or not."

                    "Constance noticed that I brushed her off. She looks a bit discouraged as I hear her mumbling something."

                    show ghost sad
                    s "I don’t see the need for you to be so rude... You are just like him."

                    s "I guess not all heroes are one-to-one with that of a novel’s."

                    "I turn to Constance, who’s still mumbling incoherently and sighed. I am not in the mood for this."

                    e "I know it’s the blood moon, but why are you even here? Can you not, I don’t know- leave? I’m so confused..."

                    show ghost confused
                    s "I’m just as confused as you are... I don’t even recall how I arrived in this place."

                    show ghost normal
                    "Constance looks at me with hope in her eyes."

                    s "Perhaps... My manor and your ‘apartment’ are within the same plot of land?"

                    "Is she serious? I pinched the bridge of my nose as I looked at her with a tired expression."

                    e "No way, really?!"

                    "At my exasperated reply, I notice Constance’s eyes grow dreary. I feel kinda bad, but I could not care any less."

                    "I just want her out of my home."

                    s "Well um... From novels I’ve read, ghouls who usually have unfinished business turn into ghosts-"

                    scene bg black with dissolve
                    e "Then do what you must to finish your unfinished business."

                    jump day2

            


    label day2:
        if affection == 1:

            scene bg house_night with dissolve
            "To my surprise, I never expected that I’d get along well with a ghost that’s haunting my own home."

            "My bleak and lonely nights started becoming bearable because of this unexpected visitor."

            "Strangely enough, I even find myself looking forward to seeing what she’s up to this evening."

            "After another draining day at work, I’m finally back at my apartment. As soon as I entered my home, I was greeted with that familiar sensation."

            "That same tingle in my spine which I felt when I first encountered Constance."

            "She must be nearby."

            $ randRoom = renpy.random.randint(1, 3)
            $ searchNum = 0

            label searchRoom2:
                if searchNum >= 2:
                    "Huh... No matter how hard I looked, she's not here."
                    "Maybe I’ll see her tomorrow."
                    scene bg black with dissolve
                    jump day3
                menu:
                    "Search the kitchen":
                        scene bg kitchen with dissolve
                        if randRoom == 1:
                            jump encounter2
                        else:
                            "Hmmm... These dishes are still piled up from where I left them last time."
                            "Seems like she’s not here."
                            $ searchNum += 1
                            jump searchRoom2

                    "Search the living room":
                        scene bg house_night with dissolve
                        if randRoom == 2:
                            jump encounter2
                        else:
                            "Huh... I swore I heard noises coming from here."
                            "Turns out I was wrong, it’s just me and that spot of mold on the wall."
                            $ searchNum += 1
                            jump searchRoom2
                            
                    "Search the storage room":
                        scene bg storage with dissolve
                        if randRoom == 3:
                            jump encounter2
                        else:
                            "My eyes must be deceiving me... I thought I saw a shadow move towards here."
                            "There’s nothing but dust particles in this room. Looks like she’s not around."
                            $ searchNum += 1
                            jump searchRoom2
        

                label encounter2:
                    show ghost happy with dissolve:
                            xalign 0.5
                            yalign 0.55
                            zoom 0.8
                    s "I see you’ve eagerly taken up my offer on a reading session then, Ms. Elysia?"

                    "Constance smiled, clearly teasing me."

                    "I guess I looked extra tired after work today, because even Constance noticed how different I behaved compared to last night."

                    show ghost normal
                    "Constance hovered closer, eyeing me up and down with those curious eyes of hers."

                    s "Is something the matter?"

        else:

            scene bg house_night with dissolve
            "After another draining day at work, I’m finally back at my apartment. As soon as I entered my home, I was greeted with that familiar sensation."

            "That same tingle in my spine which I felt when I first encountered Constance."

            "She must be nearby."

            $ randRoom = renpy.random.randint(1, 3)
            $ searchNum = 0

            label searchRoom2Bad:
                if searchNum >= 2:
                    $ searchNum = 0
                    "Huh... No matter how hard I looked, she's not here."
                    "Maybe I’ll see her tomorrow."
                    scene bg black with dissolve
                    jump day3
                menu:
                    "Search the kitchen":
                        scene bg kitchen with dissolve
                        if randRoom == 1:
                            jump encounter2Bad
                        else:
                            "Hmmm... These dishes are still piled up from where I left them last time."
                            "Seems like she’s not here."
                            $ searchNum += 1
                            jump searchRoom2Bad

                    "Search the living room":
                        scene bg house_night with dissolve
                        if randRoom == 2:
                            jump encounter2Bad
                        else:
                            "Huh... I swore I heard noises coming from here."
                            "Turns out I was wrong, it’s just me and that spot of mold on the wall."
                            $ searchNum += 1
                            jump searchRoom2Bad
                            
                    "Search the storage room":
                        scene bg storage with dissolve
                        if randRoom == 3:
                            jump encounter2Bad
                        else:
                            "My eyes must be deceiving me... I thought I saw a shadow move towards here."
                            "There’s nothing but dust particles in this room. Looks like she’s not around."
                            $ searchNum += 1
                            jump searchRoom2Bad

                label encounter2Bad:
                    show ghost awkward:
                            xalign 0.5
                            yalign 0.55
                            zoom 0.8
                    "Constance looks timid as soon as I enter the room. I can tell she hesitated for a moment before she hovered over to me."

                    "I guess I looked extra tired after work today, because even Constance noticed how different I behaved compared to last night."

                    "She hovered closer, eyeing me up and down with those curious eyes of hers."

                    s "Is something the matter?"

        menu:
            "Open up to Constance":
                e "If I’m going to be completely honest? No."

                scene bg couch with dissolve
                "I sighed as I let my feet carry me to my couch, before sinking down and letting the plush cushions soothe my exhausted body and mind."

                show ghost normal with dissolve:
                            xalign 0.5
                            yalign 0.55
                            zoom 0.8
                "From the corner of my eye, I see Constance hovering after me. She tried to sit on the same couch, but her body just phased through instead of resting atop the cushiony seats."\

                show ghost happy
                s "Well… If you are comfortable, I can always lend a shoulder."
                
                show ghost awkward
                s "Well, not physically."

                e "I uh… thank you there, Constance."

                show ghost normal
                "I take a deep breath and glance at the ghost beside me."

                "It feels silly —- here I am, talking to a deceased person’s spirit. You’d expect I’d talk to a friend about this, but no. I’m talking to a ghost."

                e "You know what I find funny? The idea of someone envying how I live my life."

                "..."

                e "I’m not as carefree as you think I am."

                e "My entire life, I’ve felt aimless. I’m stuck working at a job I don’t even like."

                show ghost sad
                e "I have no one but myself to blame for it. This is the price I paid for choosing the solace a mundane lifestyle brings."

                e "I don’t bear many regrets in life yet, I often wonder what could've been... if I wasn’t so scared."

                e "I always did try to hold myself back- afraid of the concept of not being comfortable…
                Safe, at the cost of my own freedom, my passion for well… anything."

                hide ghost with dissolve
                "I glance at the blood moon outside the window for a moment."

                show ghost sad with dissolve:
                            xalign 0.5
                            yalign 0.55
                            zoom 0.8
                "I then look at Constance. She has this unreadable look visible in her eyes. Understanding? Pity? I’m not quite sure what it is, but I can feel all of her attention directed at me."

                "Before I knew it, me and Constance had been talking for hours. She was an amazing listener, and I’m starting to feel grateful from the companionship she provides."

                e "Constance, I-"

                show ghost normal
                "For some reason, I struggled to get my words out. I feel heat rising up my neck and my ears."

                s "Yes?"

                "She looked at me with those expressive eyes of hers, and I felt even more flustered. I stammered my words out, not wanting to creep her out."

                e "I, uhm... Thanks. It’s been a while since I had someone actually listen to me, who’d thought that someone would be some hundred year old ghost. It makes me feel bad that I was a jerk to you at first."

                show ghost surprise
                "I notice Constance's eyes widen, shock evident in those expressive eyes of hers."

                show ghost happy
                s "It’s my pleasure, Ms. Elysia! You do not need to concern yourself with thanking me for something as simple as lending an ear."

                s "Besides, it’s the least I could do for being an unwelcome guest here in your home."

                hide ghost with dissolve
                "And just like that, time passes and Constance excused herself once again, yawning as she phased through walls."

                $ affection += 1
                $ renpy.notify("Constance bond up!")
                scene bg black with dissolve

                jump day3

            "Close yourself off from her":
                scene bg couch with dissolve
                e "No, yeah. Everything’s fine."

                show ghost normal with dissolve:
                            xalign 0.5
                            yalign 0.55
                            zoom 0.8
                "I sigh and let my feet lead me to the living room couch and let my body sink into the comfortable cushions."

                e "Just tired from work, that’s all."

                show ghost confused
                "I probably did a terrible job of lying, because Constance gave me a look that said she didn’t believe me."

                s "Are you certain? You don’t seem fine."

                e "I am. I don’t need a pity party. Especially not from some ghost who’s had her entire life served to her on a silver platter."

                show ghost sad
                "Constance’s eyes averted my gaze as they drooped sadly."

                s "I won’t press you for any further details then…"

                hide ghost with dissolve
                "There was a tinge of sadness in Constance’s voice as she floated away in my apartment."

                scene bg black with dissolve
                "Constance couldn’t help but feel sad. She wanted to trust this human, and felt like they both missed out on something. She thought they could have gotten along, but maybe she was wrong."

                "But alas, she was naught but an unwanted visitor who was bound in somebody else’s home."

                jump day3




    label day3:
        "Almost like clockwork- my mind and body wake up, hearing the familiar sounds of objects clanging against each other and the occasional door creek."

        "She must be awake…"

        if affection == 2:
            "An uncharacteristic grin emerges from my face, I haven’t been this cheery since well… since forever."

            e "This is the last night of the blood moon… which means-"

            "Hold on Elysia, why are YOU thinking of this? She’s just a ghost, you can’t fall for someone this soon, especially someone DEAD. Besides, after tonight, she’ll be a distant memory- well, a distant memory till the next bloodmoon, IF she’ll be there in the next bloodmoon."

            "A distant memory… Why does the idea make my heart churn? I’ve had my fair shares of heartbreak and unrequited ventures, this feeling should be normal to me."

            "Loving and Liking- they’re just one and the same. She isn’t even special, she’s just a spirit. A fragment of her time. One fragment can’t give you the full picture on what Love should or could be-"

            "Clank clank"

            e "She seems quite active tonight, might as well say ‘hello’"

            label searchRoom3:
                $ inLivingRoom = False
                if searchNum >= 2:
                    $ searchNum = 0
                    "Huh... No matter how hard I looked, she's not here."
                    "Maybe I’ll see her tomorrow."
                    scene bg black with dissolve
                    jump day4
                    menu:
                        "Search the kitchen":
                            scene bg kitchen with dissolve
                            if randRoom == 1:
                                jump encounter3
                            else:
                                "Hmmm... These dishes are still piled up from where I left them last time."
                                "Seems like she’s not here."
                                $ searchNum += 1
                                jump searchRoom3

                        "Search the living room":
                            scene bg house_night with dissolve
                            if randRoom == 2:
                                $ inLivingRoom = True
                                jump encounter3
                            else:
                                "Huh... I swore I heard noises coming from here."
                                "Turns out I was wrong, it’s just me and that spot of mold on the wall."
                                $ searchNum += 1
                                jump searchRoom3
                                
                        "Search the storage room":
                            scene bg storage with dissolve
                            if randRoom == 3:
                                jump encounter3
                            else:
                                "My eyes must be deceiving me... I thought I saw a shadow move towards here."
                                "There’s nothing but dust particles in this room. Looks like she’s not around."
                                $ searchNum += 1
                                jump searchRoom3

                label encounter3:
                    e "Constance?"

                    s "Hm- Oh, did you rest well Ms. Elysia?"

                    e "It was fine, nothing like a good coffee couldn’t fix"

                    "Constance’s gaze moves to the window, her eyes growing ever so weary. The temperature drops, the hairs beyond my neck standing as my arms shiver, looking for a sense of warmth."

                    s "The moon is beautiful, isn’t it?"

                    e "Of course the ghost would like the blood moon."

                    s "..."

                    e "..."

                    e "I’m sorry- I should’ve known it would remind you about your past"

                    s "No no, it’s fine. It’s about something else, something a lot more relevant."

                    s "Strange, isn’t it? Four days, in some place I’d never heard of, with someone I barely know yet somehow- I ended up enjoying it more than any ballroom or tea party my life can offer."

                    s "Such a shame it’ll be gone so soon, what I’d do to feel something like this again."

                    "Her eyes hang a sense of sorrow- fear even, what comes to her existence after this blood moon sets is beyond both of our comprehension. The blurry figure turns around, her glowing eyes meeting with mine, locking our gazes exclusively for each other."

                    menu:
                        "apologize":
                            e "I'm sorry, I can't make a difference."

                            s "Why are you apologizing for? You weren’t the reason why the blood moon is rising~"

                        "Remain quiet":
                            e "..."

                    s "Whether it’s been four nights or four years, my opinion stays the same. The time I’ve had with you, is like a fairy tale coming true. Call me shallow but, you’ve done what my suitors couldn’t in my whole thirty-two years of life."

                    s "So quit with the self-deprecating words, you DID make a difference Ms. Elysia. Even with the snarky attitude and questionable reading habits~."

                    "Constance's eyes hang low, her blurry figure drifting to the window, watching the city lights flood her eyes as she speaks."

                    s "You asked me about my past… correct?"

                    menu:
                        "Agree":
                            e "I did, but don’t think you’re obligated to tell me! I’d rather not force you t-"

                            "Constance lets out a low “shhh”- my voice falling silent as it happens."

                        "Remain quiet":
                            e "..."


                    s "You told me your story, it’s only fair if I told mine."

                    s "For as long as I can remember, I had always heard from my father that my hand is to be wedded off to some neighbouring noble. I learned how to present my vows before I could write my own name…"

                    s "My life was surrounded in glamor, servants at my beck and call, a line of suitors ready to take my hand at a moment's notice yet- something felt too perfect, too well woven for my life."

                    s "I always assumed love was something meaningless, reserved for princesses stuck at towers or lost maidens seeking for a knight to save them. Love is meant for fantasies, you can’t sustain your life purely on love"

                    s "But as per duty for my family, after some time of convincing and well… researching, I had found a suitable partner to marry. He wasn’t the kindness nor the most chivalrous but he did leave my family in a better position in the country than without his name"

                    s "I didn’t love him, I felt like something was wrong with me. Every man they threw my way never seemed to reach what I truly wanted, which was strange."

                    e "Is it because they aren’t the knightly protectors from your books?"

                    s "--!"

                    s "You have a good eye there Ms. Elysia, but no."

                    s "Many of them were knights or some form of travellers, but even with those attributes, they’ve never truly piqued my interest. I must be strange"

                    s "But I’m getting side-tracked. We didn’t talk much, even after we accepted the engagement- it’s like we returned to being complete strangers… waiting till the day we stand at the altar."

                    "As she spoke, her voice trailed flat. The moment she attempts to speak again, her voice comes shaky, fear engulfs every crevice they can hide in her words."

                    e "Const-"

                    s "I’m fine- I waited and waited… and waited till our wedding had arrived. But it didn’t"

                    s "I remember that night like it was just yesterday. I was getting ready with my handmaidens for my wedding in this very room. I was aimlessly reading my favorite book ‘Skyward Bound: Adrift in Time’ when suddenly…"

                    "The air seemed to have dropped temperature, my already freezing body now slowly reduced to a numbing mess."

                    s "Before I knew it, I heard trumpets, soldiers footsteps and screaming… my fiance had come to take my land and my head."

                    e "No wonder you stalk these halls, I always had assumed your life would be tragic but… my goodness"

                    "Elysia feels a gust of wind run to her back, causing the young woman to shut her eyes tight."

                    s "Turn around."

                    "Upon the ghost’s command, I turn around and my eyes widen- the being in front of me isn’t some blurry apparition no- it was something else… someone else."

                    "The woman had light seafoam blue hair, some cascading to the side of her face, slightly covering her left eye. She wore a white gown and veil, as if she was waiting for someone to greet her down the aisle… and her eyes bore aeons of grief, sorrow and regret."

                    s "Ta-da… how do I look?"

                    menu:
                        "stutter":
                            e "Um..Y-you l-"

                        "Fully compliment":
                            e "You look amazing there- I just didn’t think you’d look well.. Um"

                    s "No need to get shy, it’s just a simple wedding dress, nothing more."

                    "I gaze upon her figure once more, taking in every minute detail I can before the morning takes her away from me. My gaze falls to a book tucked tightly at her belt."

                    e "I assume that was that book you passed with?"

                    s "Right on the money~ I always dreamed that my wedding would have a dance like the knight and the princess in this book… such a shame that he took it away from me."

                    "My mind is filled with a sense of… anger? Frustration? Why am I getting so pressed over some dead guy. I mean yeah, he was a devil for killing Constance at her wedding day but what the heck can I do? That deed has been done and dusted. I can’t alter the past."

                    "Yet… just before this night ends, I want to change one thing. Just before my mind could form the thought, my mouth acted upon itself."

                    e "Lady Constance, May I have a dance?"

                    "She stood in front of me… frozen. Did I mess up? She probably found me stupid for even trying to dance with a ghost-"

                    s "I would love to… Ms. Elysia~"

                    "She said yes?"

                    if inLivingRoom == False:
                        s "This place isn’t the best area for a dance, shall we head to the living room? It’s far more spacious."
                        scene bg house_night with dissolve

                    e "R-right!"

                    "As the living room holds the light of the moon, I feel her light touch upon my hand. It’s cold, numbing even yet I did not wish to pull away."

                    s "Just follow my steps ok?"

                    e "Y-yes Ma’am!"

                    "Upon the first step of the dance, Constance started humming. As if the medley had taken over me, I had started to swing to the sound of her voice. Her eyes were closed, focused on maintaining a consistent tune- She was quite taller than me, even I was to estimate her height without those old heels, she towers over my figure."

                    "That smile, that voice, this woman in front of me- they all deserve better. Whatever I’m feeling, whether it’s love or something else, I don’t know and I don’t care. I only wish you’d have lived the life you wanted. One of leisure, one where the concept of “Love” isn’t a form of fantasy."

                    "As we glided across the living room, the corner of my eye had caught the glimpse of dawn approaching. Oh sweet sunrise; don’t shine your rays upon this moment, not when she’s in a moment of bliss."

                    "As I tried to hold onto her figure, Constance started to feel lighter and lighter. My steps had grown faulty, missing beats and tripping over myself."

                    s "Just keep your eyes on me, don’t let the dawn tear you away from this moment."

                    "Her voice echoed through my mind as I keep up with her pace, the weight of her touch feeling fainter till-"

                    s "You’re quite a good dancer- I wish… I knew you sooner."

                    "I couldn’t muster a word."

                    "Before I could even try to tell her something… anything." 

                    "She was gone."

                    "The sun had risen… It's time to go back to work- yet why do I feel so empty?"

        if affection < 2:
            "I wake up to the sound of clanking again."

            "Honestly? I can’t be bothered, all she’s done was keep me awake. If she has some unfinished business then it’s her problem, not mine."

            "I’m going back to bed."

            "zzzzz"

        else:
            "It’d been two weeks since the Constance incident had happened and to be honest- I can’t tell whether it was real or not."

            "Her touch, voice and smile all felt so real yet the moment she faded to the dawn… it felt like I was the lead of some sappy romance movie."

            "I can’t get her name out of my mouth, everytime someone knocks on my door- some part of me wishes it was her, ready to bother me about some book she’s read."

            "I shouldn’t be reminiscing on this, I have to get this code ready by thursday or else the manager will really have my head-"

            "???" "Leclerc!"

            "As I heard my name, I rushed towards the source of the noise and… that was my boss. He rubs his temples as he shoves a stack of paper upon me which seems to look like- training sheets?"

            "Manager" "You’re one of the more loyal mutts in this company, go tour the new hire. She’s part of the marketing division so don’t get too attached."

            "Manager" "Also, do be nice, she may be new but she’s a couple years older than you."

            "A new hire? Great, usually they’re such bright eyed kids or some coding know-it-all from some big company who only joined to flex on people. Even worse that’s she’s older, she might mess things up and they’ll contact me again-"

            "???" "Are you Ms. Leclerc?"

            "--!"

            s "I’m Constance Dominique, it’s really nice to meet you!"

            e "It’s nice to meet you again-"

            s "Again? Have we met before?"

            e "Ah no! You just look like someone I remembered, I got you two all mixed up ahaha…"

            e "Elysia Leclerc, it’s nice to meet you, Ms. Constance."



    # This ends the game.
    return
