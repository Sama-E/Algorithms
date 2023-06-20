//Given an array of positive integers representing the values
//of coins in your possession, write a function that reurns 
//the minimum amount of change( min sum of money ) that 
//you cannot create. The given coins can have any positive 
//integer value and aren't neccessarily unique.

coins = [5, 7, 1, 1, 2, 3, 22];
coins1 = [];
coins2 = [5, 6, 1, 1, 2, 3, 4, 9];
coins3 = [22];

output = 20;

//O(n log(n)) - Time
//O(1) - Space
//Ask to sort the array in place to use to sort()
//If not allowed create a new array
function nonConstructibleChange(coins) {
  //Sort array
  var array = coins.sort(function(a, b){return a - b});
  if(array.length == 0){
    return 1;
  } else {
    let runningSum = 0;
    for (let i=0; i < array.length; i++){
      if(array[i] > (runningSum+1)){
        return (runningSum+1);
      } else {
        runningSum += array[i];
      }
    lowestSum = runningSum + 1;
    }
    return lowestSum;
  }
}

function nonConstructibleChange1(coins) {
  //Sort array
  var array = coins.sort(function(a, b){return a - b});

  if(array.length === 0){
    return 1;
  } else {
    let runningSum = 0;
    for (i in array){
      if(array[i] > (runningSum+1)){
        return (runningSum+1);
      } else {
        runningSum += array[i];
      }
    lowestSum = runningSum;
    }
    return lowestSum;
  }
}

console.log(nonConstructibleChange(coins));
console.log(nonConstructibleChange(coins1));
console.log(nonConstructibleChange(coins2));
console.log(nonConstructibleChange(coins3));

console.log(nonConstructibleChange1(coins));
console.log(nonConstructibleChange1(coins1));
console.log(nonConstructibleChange1(coins2));
console.log(nonConstructibleChange1(coins3));

// Do not edit the line below.
// exports.nonConstructibleChange = nonConstructibleChange;