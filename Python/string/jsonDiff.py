json1 = {"hacker": "rank", "input": "output"}
json2 = {"hacker": "ranks", "input": "input"}

json3 = {"hacker": "rank", "input": "output"}
json4 = {"hacker": "rank", "input": "output"}

def getJSONDiff(json1, json2):
    diffValues = []
    for i in json1:
        for j in json2:
            if i == j and json1[i] != json2[j]:
                diffValues.append(i)
    return diffValues
            
                


print(getJSONDiff(json1, json2))
print(getJSONDiff(json3, json4))