# There's an algorithms tournament taking place in which teams of 
# programmers compete against each other to solve algorithmic problems
# as fast possible. Teams compete in a round robin, where each
# team faces off against all other teams. Only two teams compete against
# each other at a time, and for each competition, one team is designed
# the home team, while the other team is the away team. In each 
# competition there's always one winner and one loser; there are no ties.
# A winner is the team receives the most amount of points.

# Given an array of pairs representing the teams that have competed against
# each other and an array containing the results of each competition,
# write a function that returns the winner of the tournament. The input
# arrays are named competitions and results, respectively. The competitions
# array has elements in the form of [homeTeam, awayTeam], where each team
# is a string of at most 30 characters representing the name of the team.
# The results array contains information about the winner of wach corresponding
# competition in the competitions array. Specifically, results[i]
# denotes the winner of competitions[i], where 1 in the results array means that
# the home team in the corresponding compeititon won and a 0 mean that the
# away team won.
 
# It's guarenteed that exactly one team will the tournament and that each team
# will compete against all other teams exactly once. It's also guaranteed
# that the tournament will always have at least two teams.

competitions = [
    ["React", "SpringBoot"],
    ["SpringBoot", "Flask"],
    ["Flask", "React"]
]

results = [0,0,1]
output = "Flask"

results0 = [1,0,0]
output0 = "React"

results1 = [0,1,0]
output1 = "SpringBoot"

# React beats SpringBoot, Flask beats SpringBoot, Flask beats React
# React - 0 points
# SpringBoot - 1 points
# Flask - 2 points

# [homeTeam, awayTeam] // 1 = homeTeam win, 0 = awayTeam win
#  points = win(1) or lose(0)

# Declare:
# HOME_TEAM_WON: if result = 1, homeTeam wins 
# HOME_TEAM_WON = 1
# winner = ""
# To keep score is an object with winner: points 
# keepScore = {winner:0}


# Loop through results identify winner 
# [React, SpringBoot] ex.[0]
# [SpringBoot, Flask] ex.[0]
# [Flask, React] ex.[1]

# Loop through competition: identify team that won 
# [React, SpringBoot] ex.[SpringBoot]
# [SpringBoot, Flask] ex.[Flask]
# [Flask, React] ex.[Flask]

# Loop through keepScore: 
# if team does not exist, add team to keepScore 
# else team exists update/add point 
# [[SpringBoot, 1]]
# [[SpringBoot, 1], [Flask, 1]]
# [[SpringBoot, 1], [Flask, 2]]

# Identify winner = which team in keepScore has most points = return winner
# [Flask, 2] = Flask

# if homeTeam wins = 1

# O(n) Time O(k) // n = number of competitions, k = number of teams
def tournamentWinner(competitions, results):
    HOME_TEAM_WON = 1 
    winner = ""
    keepScores = {winner: 0}

    # The enumerate() method adds a counter to an iterable and returns it in the 
    # form of an enumerating object. This enumerated object can then be used 
    # directly for loops or converted into a list of tuples using the list() function.
    # Traverse i(index), competition in counted competitions
    for i, competition in enumerate(competitions):
        
        # Get result and competition
        result = results[i]
        homeTeam, awayTeam = competition

        # Determine winningTeam
        # winningTeam = if result = 1 (homeTeam wins) else 0 (awayTeam wins)
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        # updateScore function takes winningTeam, 1 point, and current keepScores
        # updateScore function updates keepScore object with teams and points
        updateScores(winningTeam, 1, keepScores)

        # If winningTeam points in keepScores > than keepScores[winner] 
        if keepScores[winningTeam] > keepScores[winner]:
            # Winner = winningTeam
            winner = winningTeam

    # Return winner
    return winner

# update keepScores
def updateScores(team, points, keepScores):
    # If winningTeam is not in keepScores, add team with result 0
    if team not in keepScores:
        keepScores[team] = 0
    # Else find team in keepScores and add points
    keepScores[team] += points


print(tournamentWinner(competitions, results))
print(tournamentWinner(competitions, results0))
print(tournamentWinner(competitions, results1))