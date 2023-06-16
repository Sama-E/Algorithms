//Roll 6-sided dice. Experiment with math.random, math.floor.

function d6() {
    var roll = Math.random();
    roll = Math.floor(roll * 7);
    return roll;

}

var playerRoll = d6();
console.log("The player rolled: " + playerRoll);

//Magic 8 ball

var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

function ball() {
    var roll = Math.random();
    x = Math.floor(roll * (lifesAnswers.length));
    return lifesAnswers[x];

}
var answer = ball();
console.log(answer);
