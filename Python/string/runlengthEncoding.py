# Run-length encoding is a form of lessless data compression in which
# runs of data are stored as a simgle data value and count, rather 
# than as the original run. For this problem, a run of data is any 
# sequence of consecutive, identical characters. So the run "AAA"
# would be run-length-encoded as "3A".

# To make things more complicated, however, the input string can 
# contain all sorts of special characters, including numbers. And
# since encoded data must be decodable, this means that we can't 
# naively run-length-encode runs. For example, the run "AAAAAAAAAAA"
# (11A) can't naively be encoded as "10A", since this string can be 
# decoded as either "AAAAAAAAAAA" or "1A". Thus, long runs (runs of
# 10 or more characters) should be encoded in a split fashion; the 
# aforementioned runs should be encoded as "9A1A".

string = "AAAAAAAAAABBCCCDD"
output = "9A1A2BC3D2"

string1 = ""
output1 = ""


# 1. Set counter = 1 for check on nonempty string
# 2. Initialize newArray = []
# 3. Iterate through string start at index 1
# 4. Set currLetter, prevLetter, lastLetter
# 5. If currLetter not equal to prevLetter or counter == 9
# 6. Append newArray with string.value of str(counter)
# 7. Append newArray with prevLetter
# 8. Counter = 9 or currLetter does not equal prevLetter: Set counter to 0 
# to restart counter with next Letter
# 9. Counter < 9: Set counter +1
# 10. Print last Counter and letter 

def runLengthEncoding(string):
    if len(string) != 0:
        counter = 1
        newArray = []
        lastLetter = string[(len(string)) - 1]
        for element in range(1, len(string)):
            currLetter = string[element]
            prevLetter = string[element-1]
            if currLetter != prevLetter or counter == 9:
                newArray.append(str(counter))
                newArray.append(prevLetter)
                counter = 0
            counter += 1

        newArray.append(str(counter))
        newArray.append(lastLetter)

        
        return "".join(newArray)


print(runLengthEncoding(string))
print(runLengthEncoding(string1))