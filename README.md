Sticks
======

Nov 7, 2013

There's a game I really like to play called Sticks. Mostly because I (almost) always win, but it's also a fast simple game that only requires a pencil and paper.

How to play
-----------

To play sticks, you start with a board of 3, 5, and 7 sticks:
<pre>
  3     | | |
  5   | | | | | 
  7 | | | | | | |
</pre>

Each player goes back and forth crossing off as many sticks as they would like in a row. The player who crosses off the last stick (stick number 15) loses the game.

Example game:

Player 1 (crosses off 7 sticks): 
<pre>
  3   | | |
  5 | | | | |
  0 
</pre>

Player 2 (crosses off 3 sticks):
<pre>
  0 
  5 | | | | |
  0
</pre>

Player 1 (crosses off 4 sticks);
<pre>
  0
  1 |
  0
</pre>

Since player two then has to cross of the last stick, he/she loses the game. What a newb...

Game Solution
-------------

The other day I got beat by a first timer. No names will be mentioned (cough cough Alyssa), but it was embarassing. Because of this I decided to figure out the solution to the game, meaning if both people played perfect games, who will win?

Well it turns out the first person wins every time, if they play a perfect game. Here are the results:

<img src="/img/sticksSolution.png"> </img>

I represent each state of the game as a tuple. The example game above can be represented as (3,5,7) -> (3,5,0) -> (0,5,0) -> (0,1,0). The colors tell you if you will win or not. The states (0,0,1), (0,1,0), (1,0,0) are red, because if you are at that state, you will lose the game. Whereas state (0, 1, 7) is green, because you can take the 7 sticks on the bottom and win the game.

The key to winning is recognizing the states which insures the other player's loss. The losing states are:

<pre>
  0 0 0 0 0 1 1 1 2 | 2 3 3  
  1 2 3 4 5 1 2 4 4 | 5 4 5 
  1 2 3 4 5 1 3 5 6 | 7 7 6
</pre>

There are more, but (1,1,0), (1,0,1), and (0,1,1) are essential the same state.

So if you're going first, right off the back go to one of the states on the right (but taking one from any row). From there, every move you make should put the other player into one of the states on the left. Continue doing this till the end of the game.

Game Solution Code
------------------

The algorithm used to calculate the game map is moderately simple. The two keys points to remember when building the map are:

> The current state is a win IF there is at least one path to a losing state

> The current state is a lose IF there are zero paths to a losing state

So I started at the bottom. Each of the three first states (0,0,1), (0,1,0), (1,0,0) are losing states. I define length as number of sticks in the state. I then go to length 2 states, (1,0,1), (0,2,0), etc. I check if all of the children are true, this way I know if it's a losing state or not. Since there is a path to a losing state from each of the length 2 states I know it' ssha winning state. This makes sense, since it's pretty to win if you have (0,2,0).

I work my way up through length 15 (3, 5, 7), calculating each possible state along the way. The end result shows that state (3,5,7) is a win state, meaning there is at least one path from (3,5,7) to ensure the loss of the other player.

Well that's all folks!

_c0nrad_