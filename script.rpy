# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Wolven", color="#fffb03")
define p = Character("Grumpy Customer", color="#ff0000")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene aldi

    "The clock strikes 6:00 PM."

    "The sun is setting."

    show purgatory man

    p "Oi mate, I need a refund."
    p "I bought this yesterday, and it doesn't work anymore."
    p "I want my money back."

    hide purgatory man
    show wolven

    "*Sigh*"
    w "Man my shift has ended yea?"
    w "I don't want to deal with this right now."
    w "I just want to go home."
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    

    # This ends the game.

    return
