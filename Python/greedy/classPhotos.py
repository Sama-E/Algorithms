# It's photo day at the local school, and you're the photographer assigned
# to take class photos. The class that you'll be photogaphing has an number 
# of students, and all these students are wearing red or blue shirts. In 
# fact, exactly half of the class is wearing red shirts, and the other half 
# is wearing blue shirts. You're responsible for arranging the students in 
# two rows before taking the photo. Each row should contain the same number
# of the students and should adhere to the following guidelines:

# - All students wearing red shirts must be in the same row 
# - All students wearing blue shirts must be in the same row
# - Each student in the back row must be strictly taller than the student directly
# in front of them in the front row.

# You're given 2 inputs arrays: one containing heights of all the students
# with red shirts and another one containing the heights of all the students
# with blue shirts. These arrays will always have the same length, and each 
# height will be a positive integer. Write a function that returns whether or 
# not a class photo that follows the stated guidelines can be taken.

# Note: you can assume that each class has at least 2 students.


redShirtHeights = [5,8,1,3,4]
blueShirtHeights = [6,9,2,4,5]
output = True 


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    colorInFrontRow = "Red" if redShirtHeights[0] < blueShirtHeights[0] else "Blue"
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if colorInFrontRow == "Red":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False


    return True


print(classPhotos(redShirtHeights, blueShirtHeights))