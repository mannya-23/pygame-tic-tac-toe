"""
This file contains all of our main code for our Tic-Tac-Toe game. 
It sets up the screens, formats each screen, has the main game code, and multiple functions that make the game functional.
The NovaSquare-Regular.ttf file imports the font we used in our game. 
The tic-tac-toe-png file is used as our grid for our main game. 
"""

import pygame
from sys import exit
import random

# Initialize Pygame
pygame.init()

# Setting up a 500 x 650 pixel screen
width = 500
height = 650
screen = pygame.display.set_mode((width, height))
screen.fill('darkblue')

# Set window name to Tic-Tac-Toe
pygame.display.set_caption('Tic-Tac-Toe')

# Adjusts background grid for gameplay
background_game = pygame.image.load("tic-tac-toe.png").convert()
grid_x = background_game.get_width() / 3
grid_y = (500 / 3)

# Randomizes player turns for each round 
def randomize_player():
    random_number = random.randint(1,2)
    if random_number == 1:
        player = True
    if random_number == 2:
        player = False
    return player

# Drawing of X 
def draw_x(cell_x, cell_y):
  # Define the size of the margin from the cell borders
  margin = 20  

  # Define the thickness of the 'X'
  line_thickness = 10

  # Define the color of the 'X'
  color = pygame.Color('darkblue')

  # Calculate the center of the grid cell
  center_x = (cell_x + 0.5) * grid_x
  center_y = (cell_y + 0.5) * grid_y 

  # Define half the size of the 'X'
  half_size = (grid_x - 2*margin) / 2

  # Calculate the end points of the two lines
  top_left = (center_x - half_size, center_y - half_size)
  bottom_right = (center_x + half_size, center_y + half_size)
  top_right = (center_x + half_size, center_y - half_size)
  bottom_left = (center_x - half_size, center_y + half_size)

  # Draw the two lines of the 'X'
  pygame.draw.line(screen, color, top_left, bottom_right, line_thickness)
  pygame.draw.line(screen, color, top_right, bottom_left, line_thickness)

# Drawing of O
def draw_o(cell_x, cell_y):
  # Define the size of the margin from the cell borders
  margin = 20  

  # Define the color of the 'O'
  color = pygame.Color('orange')

  # Define the thickness of the 'O' outline
  line_thickness = 10

  # Calculate the center of the grid cell
  center_x = (cell_x + 0.5) * grid_x
  center_y = (cell_y + 0.5) * grid_y

  # Define the radius of the 'O'
  radius = (grid_x - 2 * margin) / 2

  # Draw the 'O' as a circle
  pygame.draw.circle(screen, color, (int(center_x), int(center_y)), int(radius), line_thickness)

# Imports Font NovaSquare-Regular and stores it to variables with different font sizes
font_path = 'NovaSquare-Regular.ttf'
font = pygame.font.Font(font_path, 45)
font1 =  pygame.font.Font(font_path, 30)
font2 = pygame.font.Font(font_path, 15)


'''START PAGE'''
# Welcome to Tic-Tac-Toe on start screen
welcome = font.render('Welcome to', False, 'orange')
welcome_rect = welcome.get_rect(center = (250, 150))

welcome1 = font.render('Tic-Tac-Toe!', False, 'orange')
welcome1_rect = welcome1.get_rect(center = (250, 200))

# Intro message on start screen
intro1 = font2.render('Please press start to continue.', False, 'lightblue')
intro_rect = intro1.get_rect(center = (width/2, height/2))

intro2 = font2.render(' If you want to quit the game, press exit.', False, 'lightblue')
intro1_rect = intro2.get_rect(center = (width/2, height/2 + 20))

# Creates start button
start_button = font.render('Start!!', False, 'black')
start_button_rect = start_button.get_rect(center = (130, 500))

# Creates play again button
play_again_button = font.render('Play Again!!', False, 'black')
play_again_button_rect = play_again_button.get_rect(center = (width/2, height/2+170))

# Exit button on first screen
exit_button = font.render('Exit :(', False, 'black')
exit_button_rect = exit_button.get_rect(center = (370, 500))

# Exit button on end screen
exit_button1 = font.render('Exit :(', False, 'black')
exit_button_rect1 = exit_button1.get_rect(center = (width/2, height/2 + 240))

# Game Over
game_over = font.render('GAME OVER', False, 'Red')
game_over_rect = game_over.get_rect(center = (width/2, height/2 - 170))

'''PLAYER SELECTION'''
# Message for Player Selection on Second Screen
player_selection = font1.render('Choose a character to continue.', False, 'darkblue')
player_selection_rect = player_selection.get_rect(center = (250, 130))

# Please write your intitials message  
player_selection_cont = font1.render('Please write your initials!', False, 'darkblue')
player_selection_cont_rect = player_selection.get_rect(center = (300, 165))

# Player X option next to textbox
x_display = font1.render('Player X:', False, 'black')
x_display_rect = x_display.get_rect(center = (180, 275))

# Player O option next to textbox
o_display = font1.render('Player O:', False, 'black')
o_display_rect = o_display.get_rect(center = (180, 370))

# Play Button Second Screen
play_button = font.render('Play!!', False, 'lightblue')
play_button_rect = play_button.get_rect(center = (250, 550))

# Sets up Start Screen with messages, buttons, and gets mouse position and mouse key to proceed to next page
def start_menu():

    # Sets running variable as True
    running = True

    # While running is true, display everythng on start screen, unless exit button is pressed
    while running:
        
        # Quitting screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        # Grabbing mouse position and mouse key
        pos = pygame.mouse.get_pos()
        leftclicked = pygame.mouse.get_pressed()[0]

        # Drawing welcome
        screen.blit(welcome, welcome_rect)
        screen.blit(welcome1, welcome1_rect)

        # Drawing intro message 
        screen.blit(intro1, intro_rect)
        screen.blit(intro2, intro1_rect)

        # Drawing start_button
        pygame.draw.rect(screen, 'green', start_button_rect)
        pygame.draw.rect(screen, 'green', start_button_rect, 10)
        screen.blit(start_button, start_button_rect)

        # Drawing exit_button
        pygame.draw.rect(screen, 'red', exit_button_rect)
        pygame.draw.rect(screen, 'red', exit_button_rect, 10)
        screen.blit(exit_button, exit_button_rect)
        
        # Depending on mouse position and mouse key, either proceed to next screen or quit game
        if start_button_rect.collidepoint(pos) and leftclicked:
            player_pick()
        if exit_button_rect.collidepoint(pos) and leftclicked:
            pygame.quit()

        # Update Display
        pygame.display.update()
       

# Sets up text boxes and overall screen for player input
def player_pick():
    running = True

    # Text Boxes for Player X and O
    player_x = ''
    player_x_input = pygame.Rect(250, 255, 140, 40)

    player_o = ''
    player_o_input = pygame.Rect(250, 355, 140, 40)

    # Variables for if the text boxes are selected
    text_x_selected = False
    text_o_selected = False

    # Adding the color for when something is selected and when something isn't
    color_selected_x = pygame.Color('black')
    color_unselected_x = pygame.Color('gray')

    color_x = color_unselected_x

    color_selected_o = pygame.Color('black')
    color_unselected_o = pygame.Color('gray')

    color_o = color_unselected_o

    # Initializing player scores and the rounds to 0
    player_x_score = 0
    player_o_score = 0
    player_score = 0

    while running:

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Clicking text box and changing player selection
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_x_input.collidepoint(event.pos):
                    text_x_selected = True
                else:
                    text_x_selected = False

                if player_o_input.collidepoint(event.pos):
                    text_o_selected = True
                else:
                    text_o_selected = False

            # Typing in the text boxes
            if event.type == pygame.KEYDOWN:
                if text_x_selected == True:
                    if event.key == pygame.K_BACKSPACE:
                        player_x = player_x[:-1]
                    else:
                        player_x += event.unicode

                if text_o_selected == True:
                    if event.key == pygame.K_BACKSPACE:
                        player_o = player_o[:-1]
                    else:
                        player_o += event.unicode


        screen.fill('lightblue')

        # Grabbing position of mouse
        pos = pygame.mouse.get_pos()

        # Variable for when something is leftclicked
        leftclicked = pygame.mouse.get_pressed()[0]

        # Changing color of text box 
        if text_x_selected:
            color_x = color_selected_x
        else:
            color_x = color_unselected_x

        if text_o_selected:
            color_o = color_selected_o
        else:
            color_o = color_unselected_o

        # Writing player selection at the bottom
        screen.blit(player_selection, player_selection_rect)
        screen.blit(player_selection_cont, player_selection_cont_rect)

        # Drawing X
        screen.blit(x_display, x_display_rect)

        # Drawing O
        screen.blit(o_display, o_display_rect)

        '''drawing text boxes'''

        # Player X and Name Input
        pygame.draw.rect(screen, color_x, player_x_input, 2)
        text_surface_x = font1.render(player_x, True, 'black')
        screen.blit(text_surface_x, (player_x_input.x + 5, player_x_input.y + 5))
        player_x_input.w = max(100, text_surface_x.get_width() + 10)

        # Player O and Name Input
        pygame.draw.rect(screen, color_o, player_o_input, 2)
        text_surface_o = font1.render(player_o, True, 'black')
        screen.blit(text_surface_o, (player_o_input.x + 5, player_o_input.y + 5))
        player_o_input.w = max(100, text_surface_o.get_width() + 10)

        # Drawing Play Button
        pygame.draw.rect(screen, 'darkblue', play_button_rect)
        screen.blit(play_button, play_button_rect)

        # Setting the grid state to empty for rungame, grid state represented as a 3x3 matrix filled with None
        grid_state = [['' for _ in range(3)] for _ in range(3)]
        
        # Randomizing the player_turn so the game start is random
        player_turn = randomize_player()

        # If the play_button is pressed, go to rungame screen
        if play_button_rect.collidepoint(pos) and leftclicked:
            rungame(player_x, player_o, player_x_score, player_o_score, grid_state, player_score, player_turn)


        # Update everything and Frames
        pygame.display.update()
       


# Main game loop with grid in the background
def rungame(player_x, player_o, player_x_score, player_o_score, grid_state, player_score, player_turn):
    running = True

    # Drawing player scores on screen
    player_x_score_display = font.render(player_x + ': ' + str(player_x_score), False, 'darkblue')
    player_x_score_display_rect = player_x_score_display.get_rect(center = (130, 535))

    player_o_score_display = font.render(player_o + ': ' + str(player_o_score), False, 'orange')
    player_o_score_display_rect = player_o_score_display.get_rect(center = (370, 535))

    # Setting the screen background to blue
    background_game.set_colorkey((255, 255, 255))

    while running:
        # Screen cleared and replaced with grid in background
        screen.fill('lightblue')
        screen.blit(background_game, (0, 0))

        # Function for drawing players' turn
        def draw_turn(player):
            turn_text = font1.render(player + ' turn', True, 'black')
            screen.blit(turn_text, (width // 2 - turn_text.get_width() // 2, (height // 2 - turn_text.get_height() // 2) + 290))
        
        # Checking the 3x3 grid and looking for which characters are filled in and which are not, the ones that are filled in will draw and X or and O on the screen
        for row_index, row in enumerate(grid_state):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    draw_x(col_index, row_index)
                if cell == 'O':
                    draw_o(col_index, row_index)

        
        for event in pygame.event.get():

            # Quitting the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Drawing X depending on location of mouse
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                # Finding mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Variables for where the mouse position is
                cell_x = int(mouse_x // grid_x)
                cell_y = int(mouse_y // grid_y)

                # Finding where the mouse has clicked and adding character to the 3x3 grid
                if 0 <= cell_x < 3 and 0 <= cell_y < 3:
                    if grid_state[cell_y][cell_x] == '':
                        grid_state[cell_y][cell_x] = 'X'
                        player_turn = False

            # Drawing O depending on location of mouse
            if event.type == pygame.MOUSEBUTTONDOWN and not player_turn:
                # Finding mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Variables for where the mouse position is
                cell_x = int(mouse_x // grid_x)
                cell_y = int(mouse_y // grid_y)

                # Finding where the mouse has clicked and adding character to the 3x3 grid
                if 0 <= cell_x < 3 and 0 <= cell_y < 3:
                    if grid_state[cell_y][cell_x] == '':
                        grid_state[cell_y][cell_x] = 'O'
                        player_turn = True

        # Stores check_winner result to variable and prints output for whoever wins or results in draw 
        winner_result = check_winner(grid_state)
        
        # Checks whos turn it is and displays player initials on the screen
        if player_turn:
            draw_turn(player_x)
        
        if not player_turn:
            draw_turn(player_o)

        # Checking winner depending on character returned by other function check_winner
        if winner_result == 'X':

            # Increasing player score
            player_x_score += 1

            # If player score reaches 2, and the player x's score is more than player_o's score, then move to endgame
            if player_x_score >= 2:
                    if player_x_score > player_o_score:
                        endgame(player_x)
            
            # If the game hasn't ended:
            else:
                # Draw the last character drawn on the grid
                draw_last_move(player_turn, grid_state)
                
                # Draw who has won on the screen
                draw_winner_text(player_x)

                # Updating screen
                pygame.display.update()

                # Delaying time so people can view who has won
                pygame.time.delay(1000)

                # Resetting the grid
                grid_state = [['' for _ in range(3)] for _ in range(3)]

                # Randomizing the player's turn
                player_turn = randomize_player()

                # Recursively calling rungame and redisplaying the screen with an increase in the player scores.
                rungame(player_x, player_o, player_x_score, player_o_score, grid_state, player_score, player_turn)

        # If the winner is O
        elif winner_result == 'O':
            # Increasing player score
            player_o_score += 1
        # If player score reaches 2, and the player x's score is more than player_o's score, then move to endgame   
            if player_o_score >= 2:
                    endgame(player_o)
            
            # If the game hasn't ended
            else:

                # Draw the last character drawn on the grid
                draw_last_move(player_turn, grid_state)

                # Draw winner of the round
                draw_winner_text(player_o)

                # Updating display so it shows on the screen
                pygame.display.update()
                
                # Delaying time so people can view who has won
                pygame.time.delay(1000)
                
                # Emptying the grid
                grid_state = [['' for _ in range(3)] for _ in range(3)]

                # Randomizing player's turn
                player_turn = randomize_player()

                # Recursively running rungame and increasing player scores 
                rungame(player_x, player_o, player_x_score, player_o_score, grid_state, player_score, player_turn)

        # If there is a tie
        elif winner_result == 'No winner': 
            # Drawing the last character on the screen
            draw_last_move(player_turn, grid_state)

            # Updating the display
            pygame.display.update()

            # Delaying the time so that people can view the tie
            pygame.time.delay(1000)

            # Refreshing the grid
            grid_state = [['' for _ in range(3)] for _ in range(3)]

            # Randomizing the player's turn
            player_turn = randomize_player()

        # Function to display the winner in a text pop-up in center of screen
        def draw_winner_text(player):
            winner_text = font1.render(player + ' wins!', True, 'black')
            screen.blit(winner_text, (width // 2 - winner_text.get_width() // 2, height // 2 - winner_text.get_height() // 2))
    
        # Displaying Player X and their score 
        screen.blit(player_x_score_display, player_x_score_display_rect)

        # Displaying Player O and their score 
        screen.blit(player_o_score_display, player_o_score_display_rect)

        # Drawing the last move displays the last character on the last move before the round ends 
        def draw_last_move(player_turn, grid_state):

            # Going through the grid state and drawing the last character on the grid depending on whether it is X or O 
            for row_index, row in enumerate(grid_state):
                for col_index, cell in enumerate(row):
                    if cell == 'X':
                        draw_x(col_index, row_index)
                    if cell == 'O':
                        draw_o(col_index, row_index)

        # Update everything/frames
        pygame.display.update()
       
      
# Function to determine who is the winner of the round depending on character placement
def check_winner(grid_state):
   # Checks all rows for the same character or not
   for row in grid_state:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'

    # Checks all columns for the same character or not
   for col in range(3):
        if all(grid_state[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(grid_state[row][col] == 'O' for row in range(3)):
            return 'O'

    # Checks all diagonals for the same character or not
   if all(grid_state[i][i] == 'X' for i in range(3)) or all(grid_state[i][2 - i] == 'X' for i in range(3)):
        return 'X'
   elif all(grid_state[i][i] == 'O' for i in range(3)) or all(grid_state[i][2 - i] == 'O' for i in range(3)):
        return 'O'
   elif all(cell != '' for row in grid_state for cell in row):
       return 'No winner'
      
# Ends game after player wins 2/3 rounds      
def endgame(player):

    # Font styling for winner announcement on end screen
    end_screen = font.render(player, False, 'orange')
    end_screen1 = font1.render(player + ' won the game!!', False, 'orange')
    
    # Positioning for winner announcement
    end_screen_rect = end_screen.get_rect(center = (width/2, height /2 - 30))
    end_screen_rect1 = welcome.get_rect(center = (width/2, height/2 + 20))
    
    # Sets running variable as True 
    running = True

    while running:

        # If player clicks quit button/exits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill('darkblue')

        # Grabbing mouse position and mouse key and storing them to variables
        pos = pygame.mouse.get_pos()
        leftclicked = pygame.mouse.get_pressed()[0]

        # Displays winner of game on screen
        screen.blit(end_screen1, end_screen_rect1)

        # Drawing start_button
        pygame.draw.rect(screen, 'green', play_again_button_rect)
        pygame.draw.rect(screen, 'green', play_again_button_rect, 10)
        screen.blit(play_again_button, play_again_button_rect)

        # Drawing exit_button
        pygame.draw.rect(screen, 'red', exit_button_rect1)
        pygame.draw.rect(screen, 'red', exit_button_rect1, 10)
        screen.blit(exit_button1, exit_button_rect1)

        # Draw game over
        screen.blit(game_over, game_over_rect)
        
        # If player clicks play again, restart from player input page
        if play_again_button_rect.collidepoint(pos) and leftclicked:
            player_pick()
            
        # If player clicks to quit, quit the game
        if exit_button_rect1.collidepoint(pos) and leftclicked:
            pygame.quit()

        # Update frames/display
        pygame.display.update()
    


# Runs full program   
start_menu()
