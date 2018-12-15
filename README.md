# InfraBot

English (WIP) | Portuguese (WIP)

Bot to access and manage IEEE Computer Society UnB repositories running on a Raspberry Pi

## How it works

The InfraBot is a Telegram bot that runs on a Raspberry Pi and deals with the IEEE CS UnB infrastructure. It's possible to send commands to the bot to add, update or delete a repo, receive information from such repos and check the Rasp's status.

## Available commands

1. `add {repository_url}` - Add new Github repository
2. `remove {repository}` - Remove Github repository
3. `update {repository}` - Update Github repository
4. `run {repository}` - Run main executable from repository
5. `download {repository}` - Download generated files from repository (if available)
6. `help` - List all commands
7. `info` - Show more information about the bot

## Structuring your project to work with InfraBot

FOr now, only Python projects are accepted.
