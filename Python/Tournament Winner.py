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
# React beats SpringBoot, Flask beats SpringBoot, Flask beats React
# React - 0 points
# SpringBoot - 3 points
# Flask - 6 points


def tournamentWinner(competitions, results):

    return ""