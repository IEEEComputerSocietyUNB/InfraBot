# InfraBot

[![English (WIP)](https://img.shields.io/badge/language-en--us-blue.svg)](README.md)
[![Portuguese (WIP)](https://img.shields.io/badge/language-pt--br-green.svg)](README-pt-br.md)

Bot to access and manage IEEE Computer Society UnB repositories running on a Raspberry Pi

## How it works

The InfraBot is a Telegram bot that runs on a Raspberry Pi and deals with the
IEEE CS UnB infrastructure. It's possible to send commands to the bot to add, update or
delete a repo, receive information from such repos and check the Rasp's status.

The intention is that the final version can be used to any organization to add any Python
repo. There is no intention to make it work for any other language, however,
if any good soul wants to do it and make a Pull Request (with tests, please), we'll
be happy to review the code and approve the PR if all's well.

## Available commands

1. `add {repository_name}` - Add new Github repository
2. `remove {repository_name}` - Remove Github repository
3. `update {repository_name}` - Update Github repository
4. `run {repository_name}` - Run main executable from repository
5. `download {repository_name}` - Download generated files from repository (if available)
6. `help` - List all commands
7. `info` - Show more information about the bot

## Structuring your project to work with InfraBot

For now, only Python projects are accepted.
You need to have a `requirements.txt` file and a `tasks.py` invoke file

# Further improvements

Things to do to consider the development done:

- [ ] Make it work
    - [X] Help
    - [X] Info
    - [X] Add
    - [ ] Remove
    - [ ] Run
    - [ ] Download
- [ ] Make it work for any CS repo 
- [ ] Make it work for any repo as long as there is access 