import requests
# API Key: open trivia database.
api_key = 'https://opentdb.com/api.php?amount=10'
# Generating a request.
request = requests.get(api_key)
# Exception handling:
request.raise_for_status()
# Json.
data = request.json()
# Getting result, which are question answers:
data = data['results']
