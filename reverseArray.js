//Reverse order of string elements in an array  

function reverse(arr){
    var rev = [];
    //Empty array
    for(let i=arr.length-1; i >= 0; i--){
    //i = array index
    //let i = length of array -1, start at the end of the array
    //when i is greater than 0
    //next i = i-1
        rev.push(arr[i]);
        //push element(arr[i]) to new array
    }
    console.log(rev);
}

reverse(["a", "b", "c", "d", "e"]);