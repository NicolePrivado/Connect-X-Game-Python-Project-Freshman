#PRIVADO, ANDREA NICOLE G.
#CMSC 12 T-2L
#This program is called connect-x. It is somehow similar to connect-four. Here, the user could choose between two board sizes to play with (8x7 and 7x6). This program also saves the board and the number of moves of each of the player while playing. 
#-----------------------------------------------------------------------------------------

import os     #importing a module that contains functions allowing the program to interact with the operating system(could be windows,linux, mac, etc.)

#function for clearing the screen
def clear():
    if os.name=='nt':       #check if the user's os is windows('nt' is the os name of windows)
        os.system('cls')    #this command clears the terminal/python shell for windows
    else:
        os.system('clear')      #this command clears the terminal/oython shell for mac,linux or other os

#printing of title
#from  https://onlineasciitools.com/convert-text-to-ascii-art
def title():
    print("        ______ ____   _   __ _   __ ______ ______ ______     _  __")
    print("       / ____// __ \ / | / // | / // ____// ____//_  __/    | |/ /")
    print("      / /    / / / //  |/ //  |/ // __/  / /      / / ____  |   / ")
    print("     / /___ / /_/ // /|  // /|  // /___ / /___   / / /___/ /   | ")
    print("     \____/ \____//_/ |_//_/ |_//_____/ \____/  /_/       /_/|_| ")
    print() 
#Printing of menu
def menu(): 
    print()                                                                                                                                       
    print("                     --------------------------")
    print("                      A.      7x6 Board        ")
    print("                     --------------------------")
    print()
    print("                     --------------------------")
    print("                      B.       8x7 Board       ")
    print("                     --------------------------")
    print()
    print("                     --------------------------")
    print("                      C.  Load Previous Match  ")
    print("                     --------------------------")
    print()
    print("                     --------------------------")
    print("                      D.      Exit Game        ")
    print("                     --------------------------")
    print()
                                    
    
#creating the board1(7x6)
def board1():
    board1=[]
    for i in range(6):
        board1.append([["(___)"],["(___)"],["(___)"],["(___)"],["(___)"],["(___)"],["(___)"]])                    
    return board1

#creating the board2 (8x7)    
def board2():
    board2=[]
    for i in range(7):
        board2.append([["(___)"],["(___)"],["(___)"],["(___)"],["(___)"],["(___)"],["(___)"], ["(___)"]])               
    return board2

#function for printing boards enclosed with a box
def printboard(board_name,columns):
    title()
    #labels for columns
    if columns==7: #for 7x6 board
        print("        _____________________________________________________")
        print("       |                                                     |")
        print("       |     1      2      3      4      5      6      7     |")
    else:      #for 8x7 board
        print("     __________________________________________________________")
        print("    |                                                          |")
        print("    |    1      2      3      4      5      6      7      8    |")
    if columns==7:   #for 7x6 board
        print("       |    ___    ___    ___    ___    ___    ___    ___    |")
    else:     #for 8x7 board
        print("    |   ___    ___    ___    ___    ___    ___    ___    ___   |")
    #printing the elements in board
    if columns==7:   #for 7x6 board
        for row in range (len(board_name)):       
            for element in range(len(board_name[row])):
                if element == 0:
                    print("       |   ", end="")
                    print(board_name[row][element][0], end="  ")
                elif element == 6:
                    print(board_name[row][element][0],"  |" ,end="  ")
                else:
                    print(board_name[row][element][0], end="  ")
            print()
        print("       |_____________________________________________________|")
    else:   #for 8x7 board
        for row in range (len(board_name)):       
            for element in range(len(board_name[row])):
                if element == 0:
                    print("    |  ", end="")
                    print(board_name[row][element][0], end="  ")
                elif element == 7:
                    print(board_name[row][element][0]," |" ,end="  ")
                else:
                    print(board_name[row][element][0], end="  ")
            print()
        print("    |__________________________________________________________|")

#printing of board and player moves 
def print_afterturn(board_name,columns,x,y):
    printboard(board_name,columns)
    print()
    print("        PLAYER 1 (X) =", x, "moves","       PLAYER 2 (O) =", y, 'moves')
    print()
    print("                   Player needs", columns-3, "pieces to win :)")
    print()


#function for placing piece on the board
def drop_piece(board, row, col, piece):
    board[row][col-1] = piece

#checking if the chosen column is free or not full
def iscolumnfree(board,col):
    return board[0][col-1] == ["(___)"]

#getting the next open row for possible dropping
def next_openrow(board,row,col):
    for r in range(row-1,-1,-1):
        if board[r][col-1] == ["(___)"]:
            return r

#checking for winning patterns for board 7x6
def winning_move1(board,piece):
    #check horizontal locations for winning patterns
    for co in range(4):         
        for ro in range(6):    
            if board[ro][co] == piece and board[ro][co+1] == piece and board[ro][co+2] == piece and board[ro][co+3] == piece :
                return True
    #check vertical locations for winning patterns
    for co in range(7):
        for ro in range(3):
            if board[ro][co] == piece and board[ro+1][co] == piece and board[ro+2][co] == piece and board[ro+3][co] == piece :
                return True
    #check negatively sloped diagonals
    for co in range(4):
        for ro in range(3):
            if board[ro][co] == piece and board[ro+1][co+1] == piece and board[ro+2][co+2] == piece and board[ro+3][co+3] == piece :
                return True
    #check positively sloped diagonals
    for co in range(4):
        for ro in range(3,6):
            if board[ro][co] == piece and board[ro-1][co+1] == piece and board[ro-2][co+2] == piece and board[ro-3][co+3] == piece :
                return True

#checking for winning patterns for board 8x7
def winning_move2(board,piece):
    #check horizontal locations for winning patterns
    for co in range(4):
        for ro in range(7):
            if board[ro][co] == piece and board[ro][co+1] == piece and board[ro][co+2] == piece and board[ro][co+3] == piece and board[ro][co+4] == piece :
                return True
    #check vertical locations for winning patterns
    for co in range(8):
        for ro in range(3):
            if board[ro][co] == piece and board[ro+1][co] == piece and board[ro+2][co] == piece and board[ro+3][co] == piece and board[ro+4][co] == piece :
                return True
    #check negatively sloped diagonals pattern
    for co in range(4):
        for ro in range(3):
            if board[ro][co] == piece and board[ro+1][co+1] == piece and board[ro+2][co+2] == piece and board[ro+3][co+3] == piece and board[ro+4][co+4] == piece:
                return True
    #check positively sloped diagonals
    for co in range(4):
        for ro in range(3,6):
            if board[ro][co] == piece and board[ro-1][co+1] == piece and board[ro-2][co+2] == piece and board[ro-3][co+3] == piece and board[ro-4][co+4] == piece :
                return True

#checking if the board is already full
def board_full(board_name,col):
    counter = 0
    for colu in range(col):
        if board_name[0][colu] != ["(___)"]:
            counter += 1
    if counter == col:
        return True   
    else:
        return False

#from https://onlineasciitools.com/convert-text-to-ascii-art
def game_over():
    print("        _____  _____  _____  _____    _____  _____  _____  _____")
    print("       |   __||  _  ||     ||   __|  |     ||  |  ||   __|| __  |")
    print("       |  |  ||     || | | ||   __|  |  |  ||  |  ||   __||    _|")
    print("       |_____||__|__||_|_|_||_____|  |_____| \___/ |_____||__|__|")

#function for asking if the player wants to play a new game
def end_of_match():
    print()
    print("            ---------------           ------------------")
    print("               Main Menu                   Exit Game    ")
    print("               (Press 0)                (Press any key) ")
    print("            ---------------           ------------------")
    print()
    ans = input("     Your choice: ")
    if ans.isdigit():
        ans = int(ans)
        if ans == 0:      
            newgame()
        else:
            exit()
    else:           #exits the game if no
        exit()

#function for loading the game
def loadgame():
    boardd = []
    columns = 0
    #loading the board
    if os.path.exists("board.txt"):
        loadboard = open("board.txt", "r")
        for line in loadboard:
            tempp = []                    #list for per row on board
            line = line[:-2]
            data = line.split(",")
            columns = len(data)             
            for i in range(len(data)):
                temp = []               #enclosing the element to a list  
                temp.append(data[i][:len(data[i])])
                tempp.append(temp)
            boardd.append(tempp)
        if columns == 7:
            rows = 6
        elif columns == 8:
            rows = 7
        loadboard.close()
        #loading the player moves
        loadmoves = open("moves.txt")
        movess = []
        for linee in loadmoves:
            linee=linee[:-1]
            movess.append(linee)
        if movess != []:
            prevmoves1 = int(movess[0])
            prevmoves2 = int(movess[1])
        loadmoves.close()
        if boardd == [] and movess == []:
            print("      There's no previous game saved. Try playing a new game.")
            return False
        elif load_no_win(boardd,columns,rows,prevmoves1,prevmoves2): 
            playtime(boardd,columns,rows,prevmoves1,prevmoves2)     #if loaded game has no winner, continue playing the game
            return True
        else:
            return True
    else:
        print("      There's no previous game saved. Try playing a new game.")
        return False
#checking if the game loaded has no winner
def load_no_win(board_name,columns,rows,moves_1,moves_2):
    load_board = []
    clear()
    for element in board_name:
        load_board.append(element)
    if board_full(load_board,columns):
        print_afterturn(load_board,columns,moves_1,moves_2)
        game_over()
    elif columns==7:      #checking for winners in 7x6 board
        if winning_move1(load_board,["(_X_)"]):
            print_afterturn(load_board,columns,moves_1,moves_2)
            winplayer(columns,load_board,["(_X_)"],1)
        elif winning_move1(load_board,["(_O_)"]):
            print_afterturn(load_board,columns,moves_1,moves_2)
            winplayer(columns,load_board,["(_O_)"],2)
        else:
            return True    #indicates no winner
    elif columns==8:    #checking for winners in 8x7 board
        if winning_move2(load_board,["(_X_)"]):
            print_afterturn(load_board,columns,moves_1,moves_2)
            winplayer(columns,load_board,["(_X_)"],1)
        elif winning_move2(load_board,["(_O_)"]):
            print_afterturn(load_board,columns,moves_1,moves_2)
            winplayer(columns,load_board,["(_O_)"],2)
        else:
            return True     #indicates no winner
    
    end_of_match()

#function for saving the game
def savegame():
    saveboard = open("board.txt", "w")
    for ele in board:
        for elem in ele:
            for eleme in elem:
                eleme = str(eleme)
                saveboard.write(eleme + ",")
        saveboard.write("\n")
    saveboard.close()
    savemoves = open("moves.txt", "w") 
    savemoves.write(str(moves[0]) + "\n")
    savemoves.write(str(moves[1]) + "\n")
    savemoves.close()

#from https://onlineasciitools.com/convert-text-to-ascii-art
def player_1_won():
    print("      _____ __    _____ __ __ _____ _____    ___      _ _ _ _____ _____  __")
    print("     |  _  |  |  |  _  |  |  |   __| __  |  |_  |    | | | |     |   | ||  |")
    print("     |   __|  |__|     |_   _|   __|    -|   _| |_   | | | |  |  | | | ||__|")
    print("     |__|  |_____|__|__| |_| |_____|__|__|  |_____|  |_____|_____|_|___||__|")
#from https://onlineasciitools.com/convert-text-to-ascii-art
def player_2_won():
    print("      _____ __    _____ __ __ _____ _____    ____    _ _ _ _____ _____  __")
    print("     |  _  |  |  |  _  |  |  |   __| __  |  |_   |  | | | |     |   | ||  |")
    print("     |   __|  |__|     |_   _|   __|    -|  |  __|  | | | |  |  | | | ||__|")
    print("     |__|  |_____|__|__| |_| |_____|__|__|  |____|  |_____|_____|_|___||__|")

#function for checking winning patterns for all players and for all board sizes
def winplayer(columns,board,piece,player_number):
    if columns == 7:  #for 7x6 board
        if winning_move1(board,piece):
            if player_number == 1:  #for player 1     
                player_1_won()
                return True
            else:   #for player 2 
                player_2_won()
                return True
    else:    #for 8x7 board
        if winning_move2(board,piece):                                                       
            if player_number == 1:   #for player 1     
                player_1_won()
                return True
            else:   #for player 2
                player_2_won()
                return True
    return False    #no winning patterns

#function for player's turn
def player_turn(board,rows,columns,piece):
    player_turn = True
    while player_turn == True:
        col = input("     Enter column: ")   #entering desired column
        if col.isdigit():           #checking if the input is a digit
            col = int(col)
            if col != 0:
                if col <= columns and col > 0:  #checking if the input is a valid column 
                    if (iscolumnfree(board,col)): #checking if the column chosen is free or not full
                        player_turn = False
                        row = next_openrow(board,rows,col)
                        drop_piece(board,row,col,piece)
                        return True 
                    else:
                        print("     Oops. That column is already full. Go choose other column")
                else:
                    print("     Column chosen is out of range. Please choose from 1 to", columns ,"only.")
            elif col == 0:
                newgame()
                break
                return False
        else:
            print("     Please enter a number(from 1 to", columns ,"only).")

#function for playing the game
def playtime(board_name,columns,rows,moves_1,moves_2):
    board.clear()
    clear()
    for element in board_name:
        board.append(element)
    print_afterturn(board_name,columns,moves_1,moves_2)
    if moves_1 == moves_2:
        turn = 0     #means it is player 1's turn
    else:
        turn = 1    #means it is player 2's turn
    gameover = False
    while not gameover:
        #player 1 input
        if turn == 0:
            print("     Enter 0 to go back to Main Menu")
            print("     PLAYER 1 (X)")
            if player_turn(board,rows,columns,["(_X_)"]):
                moves_1 += 1
                moves[0] = moves_1
                clear()
                print_afterturn(board,columns,moves_1,moves_2)
                savegame()
                if winplayer(columns,board,["(_X_)"],1):
                    gameover = True
                if board_full(board,columns):
                    game_over()
                    gameover = True
            else:
                break
        #player 2 input
        else:
            print("     Enter 0 to go back to Main Menu")
            print("     PLAYER 2 (O)")
            if player_turn(board,rows,columns,["(_O_)"]):
                moves_2 += 1
                moves[1] = moves_2
                clear()
                print_afterturn(board,columns,moves_1,moves_2)
                savegame()
                if winplayer(columns,board,["(_O_)"],2):
                    gameover = True
                if board_full(board,columns):
                    game_over()
                    gameover = True
            else:
                break
        #changing of turns
        turn += 1      
        turn = turn % 2
    if gameover:
        end_of_match()

#function for playing a new game
def newgame():
    clear()   
    try_counter = 0   #counter of the user's number of tries
    title()
    menu()              #showing the choices
    game = True
    while game:
        x = input("      Enter choice: ")
        if not x.isdigit():  #checking if the user choice is a digit
            x = x.lower()
            if x == 'a':    #play 7x6 board
                playtime(board1(),7,6,0,0)
                game = False
            elif x == 'b':    #play 8x7 board
                playtime(board2(),8,7,0,0)
                game = False
            elif x == 'c':    #load the previous match
                if loadgame():
                    game = False
                try_counter+=1
            elif x == 'd':    #exit game
                exit()
                game = False
            else:           #for invalid choices
                print("      Please choose from A to D only.")
                try_counter+=1
        else:           #if the user entered any other character(not digit)
            print("      Please enter a letter(A to D).")
            try_counter+=1
        if try_counter == 3:  #checking if the user reaches 3 tries
            try_counter = 0   #reset counter
            clear()            #just clears the screen when the user reaches 3 tries/input error
            title()
            menu()              #showing the menu again after clearing everythng

#function for exiting the game
#from https://onlineasciitools.com/convert-text-to-ascii-art
def exit():
    print("        _____  _____  _____  ____   _____  __ __  _____  __")
    print("       |   __||     ||     ||    \ | __  ||  |  ||   __||  |")
    print("       |  |  ||  |  ||  |  ||  |  || __ -||_   _||   __||__|")
    print("       |_____||_____||_____||____/ |_____|  |_|  |_____||__|")                                       


board = []     #list for the board
moves = [0,0]  #list for the player moves
newgame()       #function call to start the game


