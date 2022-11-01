import pygame

# Initializes pygame and sets window to 800 x-axis and 600 y-axis.
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Next few lines define name of window, the symbol of window, and defines the background and symbols.
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('tictactoesymbol2.png')
pygame.display.set_icon(icon)

background = pygame.image.load('tictactoebackground.png')
osymbol = pygame.image.load('tictactoeO.png')
xsymbol = pygame.image.load('tictactoeX.png')
restartbutton = pygame.image.load('restartbutton.png')

# Main game loop requirement.
running = True

# The 3 activespots lists. The activespots is activespotso and activespotsx combined.
activespots = []
activespotso = []
activespotsx = []

# This is just a starting statement so the restart button is not there when activated.
restartbuttonactive = False

# Font for future text.
font = pygame.font.Font('freesansbold.ttf', 32)

# When a click is in a valid area, and games checks if to add it to a loaded spot if it isn't already loaded.
# It will also have an alternation symbol so new spots alternate between being an o or and x.
alternationnum = 1


def addactivespot(spotnum):
    if spotnum not in activespots:
        activespots.append(spotnum)
        global alternationnum
        if (alternationnum % 2) == 0:
            activespotso.append(spotnum)
        else:
            activespotsx.append(spotnum)
        alternationnum += 1


# Big If/Elif checklist to check if a team has gotten 3 in a row.
def checkifwon(activechecklist):
    if 5 in activechecklist:
        if 3 in activechecklist and 7 in activechecklist:
            someonewon(activechecklist)
        elif 9 in activechecklist and 1 in activechecklist:
            someonewon(activechecklist)
        elif 2 in activechecklist and 8 in activechecklist:
            someonewon(activechecklist)
        elif 4 in activechecklist and 6 in activechecklist:
            someonewon(activechecklist)
    if 1 in activechecklist:
        if 4 in activechecklist and 7 in activechecklist:
            someonewon(activechecklist)
        if 2 in activechecklist and 3 in activechecklist:
            someonewon(activechecklist)
    if 9 in activechecklist:
        if 7 in activechecklist and 8 in activechecklist:
            someonewon(activechecklist)
        if 3 in activechecklist and 6 in activechecklist:
            someonewon(activechecklist)


# Function if someone has won, and currently assigns the 'valueforwhowontext' variable for then printing in the GUI
# of who won the game.
def someonewon(sidethatwon):
    global valueforwhowontext
    global restartbuttonactive

    if sidethatwon == activespotso:
        valueforwhowontext = True
    else:
        valueforwhowontext = False

    # This true statement activates the loading of the restart button, and the click checks for it.
    # It also cancels the click checks for the spots, so you can't just keep playing.
    restartbuttonactive = True


# NOTE: This is the grid for num in list compared to tile for visual use:
#   1 4 7
#   2 5 8
#   3 6 9
# Main game loop. If it ends, game stops.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Event for what happens with mouse down clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mouseposition = pygame.mouse.get_pos()
            posx = mouseposition[0]
            posy = mouseposition[1]
            # There is an alternation system here; if the game is in progress, the game only checks for clicks at
            # spots, not at where the restart button would be. However, if the game ended (someone won) it swaps,
            # and it will then only check for clicks at the now loaded restart button and not at any of the spots.
            if restartbuttonactive == False:
                # Here checks is the click is within one of the 9 areas for where an x or o can be.
                if 316 > posx > 196 and 216 > posy > 96:  # Top Left
                    # print('Top Left')
                    addactivespot(1)

                if 316 > posx > 196 and 360 > posy > 240:  # Left Edge
                    # print('Left Edge')
                    addactivespot(2)

                if 316 > posx > 196 and 504 > posy > 384:  # Bottom Left
                    # print('Bottom Left')
                    addactivespot(3)

                if 460 > posx > 340 and 216 > posy > 96:  # Top Edge
                    # print('Top Edge')
                    addactivespot(4)

                if 460 > posx > 340 and 360 > posy > 240:  # Center
                    # print('Center')
                    addactivespot(5)

                if 460 > posx > 340 and 504 > posy > 384:  # Bottom Edge
                    # print('Bottom Edge')
                    addactivespot(6)

                if 604 > posx > 484 and 216 > posy > 96:  # Top Right
                    # print('Top Right')
                    addactivespot(7)

                if 604 > posx > 484 and 360 > posy > 240:  # Right Edge
                    # print('Right Edge')
                    addactivespot(8)

                if 604 > posx > 484 and 504 > posy > 384:  # Bottom Right
                    # print('Bottom Right')
                    addactivespot(9)
            else:
                if 178 > posx > 50 and 180 > posy > 100:  # Restart button clicked
                    # Sets the restart button value to false to basically reset the game.
                    # Also clears all the lists, since empty lists are necessary to play again.
                    restartbuttonactive = False
                    activespots.clear()
                    activespotsx.clear()
                    activespotso.clear()
    # Loads the background.
    screen.fill((255, 255, 255))
    screen.blit(background, (196, 96))
    screen.convert_alpha()
    # An if statement so the restart button is only loaded when a player has won / game isn't in progress.
    # It also checks for who won, and with that prints the appropriate message of who won now in the GUI, not terminal.
    if restartbuttonactive == True:

        screen.blit(restartbutton, (50, 100))
        if valueforwhowontext == True:
            wontext = font.render('O is the winner!', True, (0, 0, 0))
        else:
            wontext = font.render('X is the winner!', True, (0, 0, 0))
        screen.blit(wontext, (55, 60))

    # For each loaded spot...
    for spot in activespots:
        if spot <= 3:
            currentx = 216
        elif spot <= 6:
            currentx = 360
        else:
            currentx = 504
        for num in [1, 4, 7]:
            if spot == num:
                currenty = 116
        for num in [2, 5, 8]:
            if spot == num:
                currenty = 260
        for num in [3, 6, 9]:
            if spot == num:
                currenty = 404
        # Now location is decided, time to load!
        # We now check if the spot is an x spot or o spot, and load it via that.
        if spot in activespotsx:
            screen.blit(xsymbol, (currentx, currenty))
        else:
            screen.blit(osymbol, (currentx, currenty))
    # This here is just a small optimization to only check if someone has won if the player has 3 or more spots covered.
    if restartbuttonactive == False:
        if len(activespotsx) > 2:
            checkifwon(activespotsx)
        if len(activespotso) > 2:
            checkifwon(activespotso)

    # Final thing in game loop is always the line to update the display.
    pygame.display.update()
print("GAME ENDED")
