# **📦 Tic-Tac-Toe-project-morpion**

**MVP Status:** \[e.g., v1.0-Production]

**Group Members:** Alexandre W, Raphaël W, Anne, Axel, Mathis

 Team roles: 
- Alexandre : Team leader
- Mathis : Scribe
- Anne : Timekeeper
- Raphaël : Activator
- Axel : Secretary


**Problem to solve :** developp a tic-tac-toe program with multiple features like PVP or IA versus player with possibly different levels of difficulty

**Initial objectives (11/02/2026):**

 **- Rules Setting :**
 How to design the rules and features of this game (3 symboles in a raw , a three by three matrix)
 The easiest part of the project   
    
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]     (0: empty , 1:*player* 1, 2: *player 2 or IA in the IA mode*)

 **Victory conditions :** 

- *By each raw*: [1,1,1]
- *By each column*:
[[1,X,X],
[1,X,X],
[1,X,X]]
- *By diagonals*:
[[1,X,X],
[X,1,X],
[X,X,1]]
  
[[X,X,1],
[X,1,X],
[1,X,X]]

**- Developp a player vs player mode:**
How do you build a pvp mode where multiple people can interact between each other

*current status : done*

**- AI development (IA versus player):**
  How do you integrate an algorithm who can automatically play and interact with the player actions
  Possibly the most difficult part of the project: the group will have to reasearch more information about IA implementation: 

  Easy IA mode : 
  The bot choose at random the move after the player, win if it can win

  Medium IA mode:
  The bot calculates the odds of winning over 2 tree subdivision with highest score possible, win if it can win

  Hard difficulty: 
  
The bot calculates the odds of winning over 5 + tree subdivisions with highest score possible, win if it can win 
 


Easy and medium IA difficulties are made without recursion and MidMax usage

  
*current status : in development*




**Interface:** 
 How to developp a technical and intuitive interface to help the player choose his own play style and make him enjoy the game.

 Panel : 
- PVP
- IA
- IA difficulty mode to choose
 
*current status : in development*
