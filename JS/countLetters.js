//Count the number of the same letter in a String

function countLetters(str) {
    //Create a new object (letterCounter)
    var letterCounter = {};
    //For loop: Iterate through the string
    for (var i = 0; i < str.length; i++) {
        //Create a variable (currentLetter) to contain the element of the index
        var currentLetter = str[i];
        //If the element in the object is does not exist
        if (letterCounter[currentLetter] === undefined) {
            //Push the element and add a count of 1
            letterCounter[currentLetter] = 1;
        } else {
            //Else: Add 1 to the existing element in the object
            letterCounter[currentLetter]++;
        }
        console.log(letterCounter);
    }
    console.log(letterCounter);
    //Create new variable
    var outputString = "";
    //For each key in the object
    for (key in letterCounter) {
        //Print key(letter) and the value(the count of the letter)
        outputString += key + letterCounter[key];
    }
    return outputString;
}

str1 = "aaaabbcddd";
console.log(countLetters(str1));

str2 = "fdasfdasfdsafdsa";
console.log(countLetters(str2));