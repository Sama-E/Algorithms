//Wikipedia - In mathematics, a subsequence of a given sequence is a sequence that can be derived 
//from the given sequence by deleting some or no elements without changing the order of the remaining elements. 

array = [5,1,22,25,6,-1,8,10];
sequence = [1,6,-1,10];

array2 = [5, 1, 22, 25, 6, -1, 8, 10];
sequence2 = [5, 1, 22, 6, -1, 8, 10];


//O(n) time - traverse the array once 
//O(1) space -  one set of variables
function isValidSubsequence(array, sequence) {
	arrIdx = 0;
	seqIdx = 0;

	//While traversing both arrays, 
	//while arrayIndex is less than array length and
	//while sequenceIndex is less than sequence length 
	while ((arrIdx < array.length) && (seqIdx < sequence.length)){
		//If element of arrayIndex equals element of sequenceIndex
		if(array[arrIdx] === sequence[seqIdx]){
			//Continue to next sequenceIndex
			seqIdx++;
		}
		//If arrayIndex does not equal sequenceIndex
		//Continue to next arrayIndex
		arrIdx++;
	}
	//Boolean sequenceIndex equals sequence length
	//Then array has satisfied the condition 
	//of all sequenceIndex exist in the array
	//by the end of the length of the sequence
	return seqIdx === sequence.length;
}

//O(n) time - traverse the array once 
//O(1) space -  one variable
function isValidSubsequence2(array, sequence) {
	seqIdx = 0;
	//For each element in the array
	for (element of array){
		//If sequenceIndex equals the length of sequence
		if (seqIdx === sequence.length){
			//exit for loop
			break;
		}
		//If element of sequenceIndex equals the element of array 
		if (sequence[seqIdx] === element){
			//Continue to next sequenceIndex
			seqIdx++;
		}
	}
	//Boolean sequenceIndex equals sequence length
	//Then elements of all sequenceIndex 
	//are found in array. 
	return seqIdx === sequence.length;
}

  console.log(isValidSubsequence(array, sequence));
  console.log(isValidSubsequence(array2, sequence2));

	console.log(isValidSubsequence2(array, sequence));
  console.log(isValidSubsequence2(array2, sequence2));
  
  // Do not edit the line below.
  exports.isValidSubsequence = isValidSubsequence;