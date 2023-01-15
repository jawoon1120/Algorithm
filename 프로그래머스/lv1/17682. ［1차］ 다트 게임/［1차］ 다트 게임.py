def solution(dartResult):
    
    point = []
    for i, turn in enumerate(list(dartResult)):
        if turn == '1' and dartResult[i+1] == '0':
            continue
        if turn == '0' and dartResult[i-1] == '1':
            point.append(10)    
        elif turn.isdigit():
            point.append(int(turn))
        elif turn == 'D':
            point.append(point.pop() ** 2)
        elif turn == 'T':
            point.append(point.pop() ** 3)
        elif turn == '*':
            first = point.pop()
            if len(point):
                point.append(point.pop() * 2)
            point.append(first * 2)
        elif turn == '#':
            point.append(point.pop() * -1)
        print(point)
            
    return sum(point)