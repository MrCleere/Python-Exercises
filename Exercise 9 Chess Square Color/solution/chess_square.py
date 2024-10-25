def getChessSquareColor(column, row):

    # If the column and row are out of bounds, return a blank string:
    if column < 1 or column > 8 or row < 1 or row > 8:
        return ''

    # If the even/oddness of the column and row match, return 'white':
    if column % 2 == row % 2:
        return 'white'
    
    # If they don't match, then return 'black':
    else:
        return 'black'
