/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  const str1 = "a x a";
  const expected1 = true;
  
  const str2 = "racecar";
  const expected2 = true;
  
  const str3 = "Dud"; 
  const expected3 = false;
  
  const str4 = "oho!";
  const expected4 = false;
  
  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */

function isPalindrome(str) {
    //Empty var temp to hold str after looped through
    var temp = "";
    //Set index to 0
    var index = 0;
    //For loop: Iterate through string
    for (var i = 0; i < str.length; i++){
        //Index = string length - 1 - i(for loop index)
        index = (str.length - 1) - i;
        //Add to var temp element (each letter) of string as it passes through for loop
        temp += str[index];
    }
    //If temp = string
    if (temp == str){
        //Print str is a palidrome
        console.log(str + " Is a Palidrome!");
    }else{
        //Print str is a not palidrome
        console.log(str + " Is NOT a Palidrome!");
    }
}

isPalindrome(str1);
isPalindrome(str4); 