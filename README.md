Sticks
Nov 7, 2013

There's a game I really like to play called Sticks. Mostly because I (almost) always win, but it's also a fast simple game that only requires a pencil and paper.

How to play
-----------

To play you draw rows of 3, 5, and 7 lines:

3     | | |
5   | | | | | 
7 | | | | | | |

Each player goes back and forth crossing off as many sticks as they would like in a row. The player who crosses off the last stick (stick number 15) looses the game.

Example game:

Player 1 (crosses off 7 sticks): 
3   | | |
5 | | | | |
0 

Player 2 (crosses off 3 sticks):
0 
5 | | | | |
0

Player 1 (crosses off 4 sticks);
0
1 |
0

Since player two then has to cross of the last stick, he/she looses the game. What a newb...

Game Solution
-------------

The other day I got beat by a first timer. No names will be mentioned, but it was embarassing. Because of this I decided to figure out the solution to the game, meaning if both people played perfect games, who will win?

Well it turns out the first person wins every time, if they play a perfect game. I printed out the results.

<img src="/img/sticksSolution.png" width="300"> </img>

I represent each state of the game as a tuple. The example game above can be represented as (3,5,7) -> (3,5,0) -> (0,5,0) -> (0,1,0). The colors tell you if you will win or not. The states (0,0,1), (0,1,0), (1,0,0) are red, because if you are at that state, you will lose the game. Whereas state (0, 1, 7) is green, because you can take the 7 sticks on the bottom and win the game.

The key to winning is recognizing the states which insures the other players loss. The states are (I removed all duplicates, rows can be moved around but it's essentialy the same state):

0 0 0 0 0 1 1 1 2 | 2 3 3  
1 2 3 4 5 1 2 4 4 | 5 4 5 
1 2 3 4 5 1 3 5 6 | 7 7 6

So if you're going first, right off the back go to one of the states on the right, and from there, make sure every move you make puts the other player into one of the states on the left.

Game Solution Code
------------------

The algorithm used to calculate the game map is moderately simple. The two keys points to remember when building the map are:

1.) The current state is a win IF there is at least one path to a loosing state
2.) The current state is a loose IF there are no paths to a loosing state

So I started at the bottom. Each of the three first states (0,0,1), (0,1,0), (1,0,0) are losing states. I define length as number of sticks in the state. I then go to length 2 states, (1,0,1), (0,2,0), etc. I check if all of the children are true, this way I know if it's a losing state or not. Since there is a path to a losing state from each of the length 2 states I know it's a winning state. This makes sense, since it's pretty to win if you have (0,2,0).

I work my way up through length 15 (3, 5, 7), calculating each possible state along the way. The end result shows that state (3,5,7) is a win state, meaning there is at least one path from (3,5,7) to ensure the loss of the other player.