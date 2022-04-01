def solution(array, commands):
    answer = []

    cmd_length = len(commands)

    for i in range(cmd_length):
        arr_list = array[commands[i][0] - 1:commands[i][1]]

        arr_list.sort()

        answer.append(arr_list[commands[i][2] - 1])

    return answer


def solution2(clothes):
    clothesTypeMap = {}

    for clothe, clothesType in clothes:
        print(clothe)
        print("clothesType : ", clothesType)

        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

        print(clothesTypeMap)

        answer = 1
        for clothesType in clothesTypeMap:
            answer *= (clothesTypeMap[clothesType] + 1)

    return answer - 1










#� �C�o�d�i�n�g�t�e�s�t�
�
�#� �C�o�d�i�n�g�t�e�s�t�
�
�
