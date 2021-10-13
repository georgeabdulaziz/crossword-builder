# George Abdulaziz
# 500947969

def crossword(L):
    # Mainlist = L
    blanck = ' '
    board = [[blanck] * 20 for i in range(20)]

    def printboard(board):  # Main
        k = 0
        print('  0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9')
        print('', '___ ' * 20)
        # Matrix = [[0 for i in range(w)] for y in range(h)]
        # print(Matrix)
        for i in range(len(board)):
            #print('', end='')
            for j in range(len(board[i])):
                print('| ', end='')
                print(board[i][j], end=' ')
            print('|', k)
            #print('', '---' * 20)
            k += 1
        print('', '___ ' * 20)
        print('  0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9')

    def firstword(board, word):  # First
        boardLength = len(board)
        wordLength = len(word)
        # check first if the word is too long
        if wordLength > boardLength:
            return False
        # Put the word in to the board in the centre
        for letterPos in range(wordLength):
            column = boardLength // 2 - wordLength // 2 + letterPos
            board[boardLength // 2][column] = word[letterPos]
        return True

    def checkAndAddVertical(board, word, letterPos, letterPositionsInBoard):  # Second
        LB = len(board)
        LW = len(word)
        blank = ' '
        afterMatchIndex = 0
        beforeMatchIndex = 0
        for letterPositionInBoard in letterPositionsInBoard:
            passing = True
            (row, col) = letterPositionInBoard

            startOfWordIndexInBoard = row - letterPos    # beforeWordStart = row - beforeMatchIndex
            lengthOfWordAfterLetter = (LW-letterPos)   # the 1 for exclusion
            endOfWordIndexInBoard = row + lengthOfWordAfterLetter

            numOfRowsNeededBeforeLetterInBoard = letterPos
            numOfRowsNeededAfterLetterInBoard = LW-letterPos

            numOfAvailableRowsBeforeLetter = row - 1
            numOfAvailableRowsAfterLetter = LB - row

            #print(f'startOfWordIndexInBoard {startOfWordIndexInBoard} \n lengthOfWordAfterLetter {lengthOfWordAfterLetter} \n endOfWordIndexInBoard {endOfWordIndexInBoard}')

            if (numOfRowsNeededBeforeLetterInBoard > numOfAvailableRowsBeforeLetter) or (numOfRowsNeededAfterLetterInBoard > numOfAvailableRowsAfterLetter):
                # print('Length before main letter is short')
                continue

            if (startOfWordIndexInBoard > 0) and (board[startOfWordIndexInBoard-1][col] != blank and board[startOfWordIndexInBoard-1][col] != word[0]):  # the square above the start of the word on the board
                continue

            if (endOfWordIndexInBoard < LB-1) and (board[endOfWordIndexInBoard+1][col] != blank and board[endOfWordIndexInBoard+1][col] != word[LW-1]):  # the square under the end of the word on the board
                continue

            for i in range(startOfWordIndexInBoard, endOfWordIndexInBoard):  #  checking the squares on left and right of index in board and on index if they are empty
                if i != row:
                    if board[i][col - 1] != blank or board[i][col + 1] != blank:
                        passing = False
                        break
                    else:
                        # print('False Before main letter')
                        wordIndex = (endOfWordIndexInBoard-1) - i
                        if (board[i][col] != word[wordIndex]) and board[i][col] != blank:  # The best and correct
                            passing = False
                            break

            if passing:  # placing the word in the boards
                for i in range(startOfWordIndexInBoard, endOfWordIndexInBoard):
                    if i != row:
                        wordIndex = endOfWordIndexInBoard - (startOfWordIndexInBoard + (endOfWordIndexInBoard - i))
                        #print(i,wordIndex)
                        board[i][col] = word[wordIndex]
                return True
        return False





    def findLetters(board, word):     # Third
        listOfRowsAndCols = {}
        boardLength = len(board)
        for letterPos, letter in enumerate(word):
            for row in range(boardLength):
                for column in range(boardLength):
                    if board[row][column] == letter:
                        if letterPos in listOfRowsAndCols:
                            listOfRowsAndCols[letterPos].append((row, column))
                        else:
                            listOfRowsAndCols[letterPos] = [(row, column)]
        #print(f'word {word} letters {listOfRowsAndCols}')
        return listOfRowsAndCols

    def checkAndAddHorizontal(board, word, letterPos, letterPositionsInBoard):  # Second
        LB = len(board)
        LW = len(word)
        blank = ' '
        afterMatchIndex = 0
        beforeMatchIndex = 0
        for letterPositionInBoard in letterPositionsInBoard:
            passing = True
            (row, col) = letterPositionInBoard

            startOfWordIndexInBoard = col - letterPos  # beforeWordStart = row - beforeMatchIndex
            lengthOfWordAfterLetter = (LW - letterPos)  # the 1 for exclusion
            endOfWordIndexInBoard = col + lengthOfWordAfterLetter

            numOfRowsNeededBeforeLetterInBoard = letterPos
            numOfRowsNeededAfterLetterInBoard = LW - letterPos

            numOfAvailableRowsBeforeLetter = col - 1
            numOfAvailableRowsAfterLetter = LB - col

            # print(f'startOfWordIndexInBoard {startOfWordIndexInBoard} \n lengthOfWordAfterLetter {lengthOfWordAfterLetter} \n endOfWordIndexInBoard {endOfWordIndexInBoard}')

            if (numOfRowsNeededBeforeLetterInBoard > numOfAvailableRowsBeforeLetter) or (
                    numOfRowsNeededAfterLetterInBoard > numOfAvailableRowsAfterLetter):
                # print('Length before main letter is short')
                continue

            if (startOfWordIndexInBoard > 0) and (
                    board[row][startOfWordIndexInBoard - 1]!= blank and board[row][startOfWordIndexInBoard - 1] != word[0]):  # the square above the start of the word on the board
                continue

            if (endOfWordIndexInBoard < LB - 1) and (
                    board[row][endOfWordIndexInBoard + 1] != blank and board[row][endOfWordIndexInBoard + 1] != word[LW - 1]):  # the square under the end of the word on the board
                continue

            for i in range(startOfWordIndexInBoard,
                           endOfWordIndexInBoard):  # checking the squares on left and right of index in board and on index if they are empty
                if i != col:
                    if board[row - 1][i] != blank or board[row + 1][i] != blank:
                        passing = False
                        break
                    else:
                        # print('False Before main letter')
                        wordIndex = (endOfWordIndexInBoard - 1) - i
                        if (board[row][i] != word[wordIndex]) and board[row][i]!= blank:  # The best and correct
                            passing = False
                            break

            if passing:  # placing the word in the boards
                for i in range(startOfWordIndexInBoard, endOfWordIndexInBoard):
                    if i != col:
                        wordIndex = endOfWordIndexInBoard - (startOfWordIndexInBoard + (endOfWordIndexInBoard - i))
                        #print(i, wordIndex)
                        board[row][i] = word[wordIndex]
                return True
        return False

    def addWords(board, Mainlist):
        firstword(board, Mainlist[0])
        for i in range(1, len(Mainlist)):
            word = Mainlist[i]
            boardWordMatchingLetters = findLetters(board, word)  #  this is a hash map or a dictionary of <letter, [(),()] the list of matching indexes in the map>
            if i % 2 == 1:  # placing the word vertically
                for letter in boardWordMatchingLetters:
                    letterPositions = boardWordMatchingLetters[letter]  # this is a list of tuples of all the matching positions of a letter in the boart
                    if checkAndAddVertical(board, word, letter, letterPositions):
                        break  # word is placed
            else:
                for letter in boardWordMatchingLetters:
                    letterPositions = boardWordMatchingLetters[letter]
                    if checkAndAddHorizontal(board, word, letter, letterPositions):
                        break

        printboard(board)

    addWords(board, L)


crossword(['hippopotamus', 'horse', 'loon', 'snake', 'cat', 'rattlesnake','dinosaur', 'pineapple', 'eggs', 'panini', 'porcelain', 'wifi'])
