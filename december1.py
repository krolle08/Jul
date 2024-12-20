import pandas as pd
import requests
import modulo as mo


def url():
#URL
    url = "https://adventofcode.com/2024/day/1/input"

    cookies = {
        'ga': 'GA1.2.696993009.1734523402',
        '_gid': 'GA1.2.1810354960.1734523402',
        'session': '53616c7465645f5f18e563f0c5f83e7eeef153c3d69fe83d767f98f1ad56a19010f3eb44e011c4ef31cb1ea04e360f7ac74bb6133af0136a9420f84ea4cf145d',
        '_ga_MHSNPJKWC7': 'GS1.2.1734523401.1.1.1734523432.0.0.0'
    }

    response = requests.get(url, cookies = cookies )
    data = response.content

    lines = data.split()

    column1 = []
    column2 = []
    column3 = []

    add_to_list2 = 0

    for line in lines:
        number = line.split()
        number = int(line.decode())
        if add_to_list2 % 2 == 1:
            column2.append(int(number))
            add_to_list2 += 1
        else:
            column1.append(int(number))
            add_to_list2 = 1
    column3.append(column1)
    column3.append(column2)
    return column3

def calculate_difference():

    column = url()
    column1 = column[0]
    column2 = column[1]


    column1.sort()
    column2.sort()
    sumOfDifference = 0

    for i in range(len(column1)):
        diff = abs(column1[i] - column2[i])
        sumOfDifference += diff

    return sumOfDifference


def calculate_similarity():

    column = url()
    column1 = column[0]
    column2 = column[1]

    sum_Of_Similarity = 0

    for x in column1:
        for i in range(len(column2)):
            if x == column2[i]:
                sum_Of_Similarity += x
    return sum_Of_Similarity



