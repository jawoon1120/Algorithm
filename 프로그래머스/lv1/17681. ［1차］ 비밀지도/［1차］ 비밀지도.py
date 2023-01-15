def solution(n, arr1, arr2):
    result = []
    for i, e in enumerate(arr1):
        result.append('{0:b}'.format(arr1[i] | arr2[i]))
    
    money_map = [('0'*(n - len(m_m)) + m_m).replace('0', ' ').replace('1', '#') for m_m in result]

    return money_map