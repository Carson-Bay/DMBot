# Architecture
This document outlines the architecture of the bot.

## Files
### [args.py](../args.py)
This contains the argument parser and a test function. Generally should not be used by command implementations,
 as parsed arguments will already be passed.

### [commands.py](../commands.py)
All top-level commands (i.e. echo, character, changeprefix, etc.). Sub-commands (e.g. character ...) should be
 placed in their own dedicated file.

### [embeds.py](../embeds.py)
An embed creation utility.

### [main.py](../main.py)
The main entry point of the program. This initializes the bot and state, then handles incoming messages and other
 bot events.

Also contains all top-level commands.

### [state.py](../state.py)
Manages bot state.

## Folders
### [commands](../commands/)
Contains all command-related files.
