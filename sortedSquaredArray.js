// Sorted Squared Array

// Write a function that takes in a non-empty array of integers
// that are sorted in ascending order and returns a new array of 
// the same length with the squares of the original integers also
// sorted in ascending order.

array =  [1,2,3,5,6,8,9];
array1 = [-1,26,-3,-52,65,88,91];
array2 = [0,12,83,54,67,80,"x"];
array3 = [-2,-1];
array4 = [-5,-4,-3,-2,-1];

//O(n) time, Sort algorithm add n log(n) = O(n log(n)) time
//O(n) space = new array
function sortedSquaredArray(array) {
  //Declare new Array
  const newArray = [];
  //Loop through array
  for (let i = 0; i < array.length; i++){
    //Square element of each index and push to new array
    newArray.push(Math.pow(array[i], 2))
  }
  console.log(newArray);
  //Sort new Array function compares two values, it sends the values  
  //to the compare function, and sorts the values according to the
  //returned (negative, zero, positive) value.
  newArray.sort(function(a, b){return a - b});
  //Return new array
  return newArray;
}

console.log(sortedSquaredArray(array));
console.log(sortedSquaredArray(array1));
console.log(sortedSquaredArray(array2));
console.log(sortedSquaredArray(array3));
console.log(sortedSquaredArray(array4));

//If array is already sorted algorithm can be solved in linear time O(n)
//Since its sorted, try comparing the absolute value of
//the first element and last element of the array
//O(n) time
//O(n) space
function sortedSquaredArray2(array) {
  //New array
  const newArray = [];
  //Add pointers to the start and end of array
  //Start pointer
  var smallerValueIdx = 0;
  //End pointer
  var largerValueIdx = array.length - 1;
  //Reverse for loop
  for(i=largerValueIdx; i >= 0; i--){
    //Set pointer in array
    smallerValue = array[smallerValueIdx];
    largerValue = array[largerValueIdx];
    //Compare elements of pointers
    if(Math.abs(smallerValue) > Math.abs(largerValue)){
      //Place smallerValue in current index from the for loop
      //Square smallerValue
      newArray[i] = smallerValue*smallerValue;
      //Move to the next value
      smallerValueIdx++;
    } else {
      //Place largerValue in current index from the for loop
      //Square largerValue
      newArray[i] = largerValue*largerValue;
      //Move to the previous value
      largerValueIdx--;
    }
  }
  return newArray;
}


console.log(sortedSquaredArray2(array));
console.log(sortedSquaredArray2(array1));
console.log(sortedSquaredArray2(array2));
console.log(sortedSquaredArray2(array3));
console.log(sortedSquaredArray2(array4));


