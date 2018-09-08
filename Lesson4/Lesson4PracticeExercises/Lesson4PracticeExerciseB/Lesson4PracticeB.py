# Reads through Scores.txt and print each team name, followed by the maximum number of goals that team scored in a game.

import csv

def addScoretoScoresDict(teamName, numberOfGoals, scoresDict):
    if teamName in scoresDict:
        # team is already in the dictionary
        if numberOfGoals > scoresDict[teamName]:
            # update the score if needed
            scoresDict[teamName] = numberOfGoals
    else:
        # no entry for the team exists, so add new entry
        scoresDict[teamName] = numberOfGoals

scoresFile = open("C:\\Geog485\\Lesson4\\Lesson4PracticeExercises\\Lesson4PracticeExerciseB\\Scores.txt", "r")
csvReader = csv.reader(scoresFile, delimiter=" ")
header = csvReader.next()

scoresDict = {}

try:
    for row in csvReader:
        winner = row[0]
        winnerGoals = row[1]
        loser = row[2]
        loserGoals = row[3]
        addScoretoScoresDict(winner, winnerGoals, scoresDict)
        addScoretoScoresDict(loser, loserGoals, scoresDict)
    for k in scoresDict:
        print k + ": " + str(scoresDict[k])

except:
    print "There was an error processing the data."
