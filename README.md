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
If you want to run LadderManager yourself to test the bot against other ladder bots, you must first download and compile [LadderManager](https://github.com/Cryptyc/Sc2LadderServer). Then extract python-sc2-ladderbot into LadderManager/Bots/python-sc2-ladderbot and add the following to LadderManager/Bots/LadderBots.json:
```
"PythonSC2LadderBot": {
    "Race": "Random",
    "Type": "BinaryCpp",
    "Path": "python C:/Ladder/Bots/python-sc2-ladderbot/run.py"
},
```
You should now be able to configure LadderManager to start a game with "PythonSC2LadderBot" as one of the opponents (by modifying LadderManager/matchupList).

## Bot coding
See [python-sc2](https://github.com/Dentosal/python-sc2) for more example bots and documentation.
