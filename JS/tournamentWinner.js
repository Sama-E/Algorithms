competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
];
results = [0,0,1];
results1 = [0,1,0];
results2 = [1,0,0];

HOME_TEAM_WON = 1;

//O(n) - time
//O(k) - space k=keys
// function tournamentWinner(competitions, results) {
//   // Write your code here.

//   let highestScoreTeam = "";
//   const scores = {highestScoreTeam: 0};

//   for(i=0; i<competitions.length; i++){
//     //Competitions index = results index
//     let result = results[i];
//     let homeTeam = competitions[i][0];
//     let awayTeam = competitions[i][1];

    //Winning Team equals homeTeam if result == HOME_TEAM_WON
    //else awayTeam
//     if(result === HOME_TEAM_WON){
//       winningTeam = homeTeam;
//     } else {
//       winningTeam = awayTeam;
//     }

//     updateScores(winningTeam, 3, scores);
//     // console.log(winningTeam)
//     console.log(updateScores(winningTeam, 3, scores))

//     if (scores[winningTeam] > scores[highestScoreTeam]){
//       highestScoreTeam = winningTeam;
//     }
//   }  

//   return highestScoreTeam;
// }

// function updateScores(team, points, scores) {
//   if(!team in scores){
//     scores[team] = 0;
//   }
//   scores[team] +=points;

//   return scores;
// }

// function tournyWinner(competitions, results){
//   let currentBestTeam = "";
//   const scoreboard = {[currentBestTeam]: 0};

//   for(let i=0; i<competitions.length; i++){
//     const [homeTeam, awayTeam] = competitions[i];
    

//     let matchWinner = results[i] > 0 ? homeTeam : awayTeam;

//     scoreboard[matchWinner] ? scoreboard[matchWinner] += 3 :scoreboard;

    

//     if (scoreboard[matchWinner] > scoreboard[currentBestTeam]){
//       currentBestTeam = matchWinner;
      
//     }
//   }

//   return currentBestTeam;
// }

function tournamentWinner(competitions, results) {
  //Winner
  let winner = {score: 0, name: ''};
  //Keep score object
  const scoreMap = {};

  //For: Iterate through competitions to declare a winner
  for(let i = 0; i < competitions.length; i++){

    //Set homeTeam and awayTeam
    let homeTeam = competitions[i][0];
    let awayTeam = competitions[i][1];

    //Applying point to teams in scoreMap
    //If results 0 for team idx add 3 to team idx in scoreMap
    if(results[i] === 0){
      scoreMap[awayTeam] = (scoreMap[awayTeam] || 0) +3;
    } else {
      scoreMap[homeTeam] = (scoreMap[homeTeam] || 0) +3;
    }

    //Declare winner - Highest score 
    //if team idx in scoreMap score is highest
    //declare team idx the winner
    if (scoreMap[awayTeam] >= winner.score){
      winner = { score: scoreMap[awayTeam], name: awayTeam };
    } else if(scoreMap[homeTeam] >= winner.score){
      winner = { score: scoreMap[homeTeam], name: homeTeam }
    }
  }
  return winner.name;

}


console.log(tournamentWinner(competitions, results));
console.log(tournamentWinner(competitions, results1));
console.log(tournamentWinner(competitions, results2));

// console.log(tournyWinner(competitions, results));
// console.log(tournyWinner(competitions, results1));
// console.log(tournyWinner(competitions, results2));

// Do not edit the line below.
// exports.tournamentWinner = tournamentWinner;