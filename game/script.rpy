# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alex")
image a happy = "image0.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show a happy

    # These display lines of dialogue.

    a "Hello there!"

    a "I'm so glad you came!"

    a "Take a seat!"

    a "You are such as beautiful girl..."
    a "guy?"
    a "Edritch abomination?"

    a "Whatever"

    # This ends the game.

    return
