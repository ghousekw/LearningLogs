/*
UseCase:
--------
Rock, Paper, or Scissors
Rock paper scissors is a classic two player game. Each player chooses either rock, paper, or scissors. The items are compared, and whichever player chooses the more powerful item wins.

The possible outcomes are:

Rock destroys scissors.
Scissors cut paper.
Paper covers rock.
If there’s a tie, then the game ends in a draw.
Our code will break the game into four parts:

Get the user’s choice.
Get the computer’s choice.
Compare the two choices and determine a winner.
Start the program and display the results.
*/
const getUserChoice = userInput => {
    userInput = userInput.toLowerCase();
    if (userInput === 'bomb' || userInput === 'rock' || userInput === 'paper' || userInput === 'scissors'){
      return userInput;
    }else{
      console.log('Error!');
    }
  }
  
  // console.log(getUserChoice('Paper'));
  
  // console.log(getUserChoice('fork'));
  
  const getComputerChoice = () => {
    randomNumber = Math.floor(Math.random()*3);
    switch (randomNumber) {
    case 0:
      return 'rock';
    case 1:
      return 'paper';
    case 2:
      return 'scissor';
    }
  }
  
  // console.log(getComputerChoice());
  
  const determineWinner = (getUserChoice, getComputerChoice) => {
    if (getUserChoice === getComputerChoice){
      return "Game was a tie.";
    }
    if(getUserChoice === 'rock'){
      if(getComputerChoice === 'paper'){
        return 'The Computer Won!';
      }else{
        return 'You Won!';
      }
    }
    if(getUserChoice === 'paper'){
      if(getComputerChoice === 'scissors'){
        return 'The Computer Won!';
      }else{
        return 'You Won!';
      }
    }
    if(getUserChoice === 'scissors'){
      if(getComputerChoice === 'paper'){
        return 'The Computer Won!';
      }else{
        return 'You Won!';
      }
    }
  }
  
  console.log(determineWinner('paper', 'scissors'));
  console.log(determineWinner('paper', 'paper'));
  console.log(determineWinner('paper', 'rock')); 
  
  const playGame = () => {
    const userChoice = getUserChoice('bomb');
    const computerChoice = getComputerChoice();
    console.log('You threw: ' + userChoice);
    console.log('The computer threw:' + computerChoice);
  }
  
  playGame();