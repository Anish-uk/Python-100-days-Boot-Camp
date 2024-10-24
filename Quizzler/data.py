#question_data
import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&type=boolean")
response.raise_for_status()
question_data = response.json()["results"]