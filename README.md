Bato-yo-slaget (Battleship)
==========

A Python implementation of the classic battleship game.

## History

Basic logic adopted from **@JBKahn** [code](https://github.com/JBKahn/Battleship).

Features I liked:

- board size is a variable
- amount of players defined at runtime
- user ships can be placed on the board randomly
- simple console output

Important things added:

- ships can not intersect
- unlimited amount of players (strange feature of course)
- split the monolith code onto small classes (one class - one file)
- game logic in separate python modules


From **@tmac-balla** I've taken [the engine](https://github.com/tmac-balla/battleship-game) that uses PyGame library and 

* extended logic classes with sprites and fonts
* linked game classes to the engine


## Current state of development

![Last screenshot](last_screen.png "I have won!")

- game ends when the game ends (just restart the app)
- not stable (auto ship positioning going wild)
- and maybe more...

## Run

Requires [Pygame](http://www.pygame.org/download.shtml)

```
pip install pygame
```

Play
```
cd src/py
python run-pygame.py
```
 
**Controls**: arrow keys; Enter to select, fire or place a ship; Space to rotate ships.
