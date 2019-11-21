# Bot.py
It contains the main logic with which our bot gets its functionality. Three commands are supported by the bot i.e. 'hi' from a user, 
'!google <query>' and '!recent <keyword>'. '!google' can perform google search and will return top 5 links. '!recent' will fetch you 
those previous search queries which contains your provided keyword.

#connections.py
File takes care of interaction with the storage system. We are using RDS as our database host and postgres as our database.
