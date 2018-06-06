# Python-sc2 Ladder Bot Example
This is a StarCraft 2 example bot coded using [python-sc2](https://github.com/Dentosal/python-sc2) that has the ability to integrate with the [LadderManager](https://github.com/Cryptyc/Sc2LadderServer) so that it can run against other bots on the [SC2 AI Ladder](http://sc2ai.net).

This bot can be run either locally against a computer opponent, or through the [LadderManager](https://github.com/Cryptyc/Sc2LadderServer). The file "run.py" is used for both variants, which loads ExampleBot from example_bot.py, and starts the appropriate game type.

## Requirements
* [Python 3.6+](https://www.python.org/downloads/)
* [python-sc2](https://github.com/Dentosal/python-sc2)

## Usage

### Run a basic game 
```
python run.py
```
You can modify run.py to load your own bot or change the computer opponent.

### Run a LadderManager game
If you want to run LadderManager yourself to test the bot against other ladder bots, you must first download and compile [LadderManager](https://github.com/Cryptyc/Sc2LadderServer). Then, within the LadderManager directory, extract the files from this repo into Bots/python-sc2-ladderbot/ and add the following to Bots/LadderBots.json:
```
"MyBot": {
    "Race": "Random",
    "Type": "Python",
    "RootPath": "C:/Ladder/Bots/python-sc2-ladderbot/",
    "FileName": "run.py"
}
```
Modify RootPath if you placed LadderManager in another directory than C:/Ladder/. You should now be able to configure LadderManager to start a game with "MyBot" as one of the opponents (by modifying the "matchupList" file).

## Bot coding
See [python-sc2](https://github.com/Dentosal/python-sc2) for more example bots and documentation.
