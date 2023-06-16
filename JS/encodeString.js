/* 
    String Encode  
*/


/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 
    
    
    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
*/


const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a1";

const str4 = "bbcc";
const expected4 = "b2c2";

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */


function encodeStr(str) {
    //Create new string
    let new_string = "";
    //Count starts at 1
    let count = 1;
    //For Loop: Iterate through string
    for (let i = 0; i < str.length; i++) {
        //If element of string index equals string's next index's element
        if(str[i] == str[i+1]){
            //Add 1 to count
            count ++;
        }else{
        //Else push element of index to new string
        new_string += str[i];
        //And push count of element to new string 
        new_string += count;
        //Reset count to 1
        count = 1;
        }
    }
    return new_string;
}

console.log(encodeStr(str1))
console.log(encodeStr(str2))
console.log(encodeStr(str3))
console.log(encodeStr(str4))