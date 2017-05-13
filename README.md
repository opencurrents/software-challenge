# Rock-Scissors-Paper Game

## Problem Statement
As part of the software challenge, you'll need to implement this popular game in 2-player mode. Each player should be presented a form where they can make a choice between the three available options. Once the player makes their choice, they should be directed to a game status page. For each player the status can be one of the following four:

1. Other player has not made their choice yet
2. You won the game (other player has made a choice of X)
3. You lost the game (other player has made a choice of Y)
4. The game resulted in a tie (other player has made the same choice as you)

## Implementation Details
You are free to implement the challenge in a programming language and/or web framework of your choice. Depending on your area of expertise you may choose to implement the front end component, the back end component or both. For example, if you are a full-stack generalist or backend developer with some basic HTML knowledge, you may choose to implement the entire functionality of the game. If you are only familiar with Frontend / UI, we'd expect to see something impressive for the user interface.

If you choose a fully-responsive framework like Meteor or ReactJS, it'd be nice if the status page would reflect the actual status of the game without the need for refreshing. For example, once the first player makes their choice, they would be directed to the status page with the outcome #1. Once the second player follows with their choice, the status page of player 1 will be automatically updated to one of #2 - #4.

## Submission Details
To start on your solution, please fork and clone this repository. Once you are finished, please submit your solution as a Pull Request to this repository from your fork. Do not merge the Pull Request.

## Bonus
To gain extra credit, consider implementing persistent game score. In other words, every time the two players play a game, the score is adjusted the same as in chess (1 point for a win, 0 points for a loss, 1/2 point for a draw). The score should be present at all times on both the choice selection page and the game status page.

Good luck!
