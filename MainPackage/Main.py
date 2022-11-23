'''
Name: Mark Johnson, Puiki Lau
email: johns8mk@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Collaborating using APIs
'''
# API key is already included 
import json
import requests

response = requests.get('https://api.epa.gov/FACT/1.0/emissions/metadata?api_key=KverrnKmDgtreqzbOt6XsQkVukoanJiaUBA5bAoj')
json_string = response.content
    
parsed_data = json.loads(json_string) 

print(parsed_data['data']['categories'])

for category in parsed_data['data']:
    print (category)

for p in parsed_data:
    print('column names:', p)