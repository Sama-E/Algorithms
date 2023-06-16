/* 
String: Reverse
Given a string,
return a new string that is the given string reversed
*/


const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */


function reverseString(str) {
    //Create new string
    var new_string = "";
    //For loop: iterate through all elements of the string backwards
    for (var i = str.length - 1; i >= 0; i--) {
        //Add element to new string
        new_string += str[i];
    }
    return new_string;

}
console.log(reverseString('hello'));
console.log(reverseString('peaches'));
console.log(reverseString('expectations'));