// Counting Positives Number in an Array

var countPositives = 0;
var numbers = [3, 4, -2, 7, 16, -8, 0];
    
for (i = 0; i < numbers.length; i++) {
//for loop start at 0
//if array length is less tahn i
//i+1
    if (numbers[i] > 0){
    //if array[i] is greater than 0
    //add 1 to the countPositives
        countPositives++;
    }
}

console.log("there are " + countPositives + " positive values");