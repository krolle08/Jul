import pandas as pd
import requests

def url():
#URL
    url = "https://adventofcode.com/2024/day/2/input"

    cookies = {
        'ga': 'GA1.2.696993009.1734523402',
        '_gid': 'GA1.2.1810354960.1734523402',
        'session': '53616c7465645f5f18e563f0c5f83e7eeef153c3d69fe83d767f98f1ad56a19010f3eb44e011c4ef31cb1ea04e360f7ac74bb6133af0136a9420f84ea4cf145d',
        '_ga_MHSNPJKWC7': 'GS1.2.1734523401.1.1.1734523432.0.0.0'
    }

    response = requests.get(url, cookies = cookies )
    raw_data = response.content

    data = raw_data.decode("utf-8").strip().split('\n')
    formatted_data = []
    for i in data:
       formatted_data.append([int(ele) for ele in i.split()])

    return formatted_data

def sum_of_safe_reports():

    reportScores = url()
    maxScoreChange  = 3
    minScoreChange = 1
    totalSafeReports = 0

    for scores in reportScores:
        is_increasing = all(scores[i] < scores[i+1] for i in range(len(scores)-1))
        is_decreasing = all(scores[i] > scores[i+1] for i in range(len(scores)-1))

        is_difference_valid = all(minScoreChange <= abs(int(scores[i])- int(scores[i+1])) <= maxScoreChange for i in range(len(scores)-1))

        if(is_increasing or is_decreasing) & is_difference_valid:
            totalSafeReports += 1
    return totalSafeReports


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



