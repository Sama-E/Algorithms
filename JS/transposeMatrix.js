matrix0 = [[1,2]],
output = [
  [1],
  [2]
],

matrix1 = [
  [1,2],
  [3,4],
  [5,6]
],
output = [
  [1,3,5],
  [2,4,6]
],
matrix2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
output = [
  [1,4,7],
  [2,5,8],
  [3,6,9]
]
//when indexed array is complete start new array
//matrix1[i][j] = output[j][i]
//matrix1[0][0] = output[0][0]
//matrix1[0][1] = output[1][0]
//matrix1[1][0] = output[0][1]
//matrix1[1][1] = output[1][1]
//matrix1[2][0] = output[0][2]
//matrix1[2][1] = output[1][2]

//Start with output and place columns of output into an
//array.  

//O(w*h) - time
//O(w*h) - space

function transposeMatrix(matrix){
  //Set newMatrix
  var newMatrix = [];
  //For: Iterate through idx i  
  for(let i=0; i<matrix.length; i++){
    //For: Iterate through idx j to the length of matrix[i]
    for(let j=0; j<matrix[i].length; j++){
      //If the newMatrix[j] is undefined
      //Push new array in newMatrix
      if (newMatrix[j] === undefined) newMatrix.push([]);
      //Push matrix[i][j] to newMatrix[j]
      newMatrix[j].push(matrix[i][j]);
    }
  }
  return newMatrix;
}

console.log(transposeMatrix(matrix0));
console.log(transposeMatrix(matrix1));
console.log(transposeMatrix(matrix2));

// Do not edit the line below.
// exports.transposeMatrix = transposeMatrix;