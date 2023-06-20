array = [3, 5, -4, 8, 11, 1, -1, 6];
targetSum = 10;

array2 = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47];
targetSum2 = 164;

array3 = [];
targetSum3 = 0;

//O(n^2) time | O(1) space
// function twoNumberSum(array, targetSum) {
//   var hashN = new Map([]);
//   var length = array.length;
//   // Write your code here.
//   if (length > 0) {
//     //Loop through array, grab one number (x)
//     for (let i = 0; i < length; i++){
//       //Loop second time through array, grab another number (y) add to (x)
//       for (let j = 0; j < length; j++){
//         if (array[i] !== array[j]){
//           if (array[i] + array[j] === targetSum){
//             hashN.set(array[i], array[j]);
//             return hashN;
//           }
//         }
//       }
//     }
//   }
// }

//O(n) time | O(n) space
// function twoNumberSum(array, targetSum) {
//   var hashN = new Map([]);
//   var length = array.length;
//   // Write your code here.
//   if (length > 0) {
//     //Loop through array, grab one number (x)
//     for (let i = 0; i < length; i++){
//       //Loop second time through array, grab another number (y) add to (x)
//       for (let j = 0; j < length; j++){
//         if (array[i] !== array[j]){
//           if (targetSum - array[j] === array[i]){
//             hashN.set(array[i], array[j]);
//             return hashN;
//           }
//         }
//       }
//     }
//   }
// }

//Same As above with HashTable 
// function twoNumberSum(array, targetSum) {
//   const inArray = new Set();

//   for(let firstNum of array){
//     const secondNum = targetSum - firstNum;
//     if (inArray.has(secondNum)) {
//       return [firstNum, secondNum]
//     }
//     inArray.add(firstNum);
//   }
// }
  //Edge case: find other possibilities


//First sort
//Traverse both sides of array
//While left is less than right
//Add left to right = Sum
//Does Sum === targetSum
//O(nlog(n) | O(1))
function twoNumberSum(array, targetSum) {
  //Help Sort Function(compare a,b)
  var array = array.sort(function(a, b){return a - b});
  console.log(array);
  var left = 0;
  var right = array.length - 1;

  while (left < right){
    currentSum = array[left] + array[right]
    if (currentSum === targetSum){
      return [array[left], array[right]];
    } else if (currentSum < targetSum){
      left++;
    } else {
      right--;
    }
  }
  return [];
}

console.log(twoNumberSum(array, targetSum));
console.log(twoNumberSum(array2, targetSum2));
console.log(twoNumberSum(array3, targetSum3));
