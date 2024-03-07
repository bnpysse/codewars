def chessBishopDream(boardSize, initPosition, initDirection, k):
    [x, y] = boardSize
    orginitPosition = list(initPosition)
    initinitDirection = list(initDirection)
    for n in range(x * y * 4):
        orginitDirection = list(initDirection)

        if initPosition[0] + initDirection[0] < 0:
            initDirection[0] = 1
        elif initPosition[0] + initDirection[0] >= x:
            initDirection[0] = -1
        if initPosition[1] + initDirection[1] < 0:
            initDirection[1] = 1
        elif initPosition[1] + initDirection[1] >= y:
            initDirection[1] = -1
        print
        initPosition, initDirection
        temp = [(i + j) / 2 for (i, j) in zip(orginitDirection, initDirection)]
        initPosition = [i + j for (i, j) in zip(initPosition, temp)]
        if n == (k - 1):
            break
        if initPosition == orginitPosition and initDirection == initinitDirection:
            print
            n
            break

    if n != (k - 1):
        for m in range(k % (n + 1)):
            orginitDirection = list(initDirection)

            if initPosition[0] + initDirection[0] < 0:
                initDirection[0] = 1
            elif initPosition[0] + initDirection[0] >= x:
                initDirection[0] = -1
            if initPosition[1] + initDirection[1] < 0:
                initDirection[1] = 1
            elif initPosition[1] + initDirection[1] >= y:
                initDirection[1] = -1
            print
            initPosition, initDirection
            temp = [(i + j) / 2 for (i, j) in zip(orginitDirection, initDirection)]
            initPosition = [i + j for (i, j) in zip(initPosition, temp)]

    return initPosition