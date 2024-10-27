from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv

# Parsing date string to check if it matches YYYY-MM-DD format or not
def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The date format is incorrect. Please use yyyy-mm-dd format.")

while True:
  matches_date = input('Enter matches day in the following format: YYYY-MM-DD\t')
  # Checking if the date format is correct
  try:
    validate_date_format(matches_date)
    print('The date format is correct.')
    break
  except ValueError as e:
    print(e)

# Parsing page content
page_url = f'https://www.filgoal.com/matches/?date={matches_date}'
response = requests.get(page_url)
page_content = response.text
soup = BeautifulSoup(page_content, 'html.parser')
all_matches_details = []

# Getting each match details
def get_championship_matches_details(championship):
  championship_name = championship.find('span').text.strip()
  all_matches = championship.find_all('div', {'class': 'cin_cntnr'})
  for match in all_matches:
    match_date = matches_date
    match_details = {}

    left_team = match.find('div', {'class': 'f'})
    right_team = match.find('div', {'class': 's'})
    match_status = match.find('div', {'class': 'm'}).text.strip()

    left_team_name = left_team.find('strong').text.strip()
    right_team_name = right_team.find('strong').text.strip()

    left_team_score = left_team.find('b').text.strip()
    right_team_score = right_team.find('b').text.strip()

    # Inserting match details into all_matches_details list
    match_details['البطولة'] = championship_name
    match_details['تاريخ المباراة'] = match_date
    match_details['الفريق الأول'] = left_team_name
    match_details['الفريق الثاني'] = right_team_name
    match_details['نتيجة المباراة'] = f'{right_team_score} - {left_team_score}'
    match_details['حالة المباراة'] = match_status

    all_matches_details.append(match_details)

# Getting the details of each championship separately
championships = soup.find('div', {'id': 'match-list-viewer'}).find_all('div', {'class': 'mc-block'})
for championship in championships:
  get_championship_matches_details(championship)

# Saving our work in a csv file
storing_location = input('Enter location where you wanna save the file: ')
if not storing_location.endswith('/'):
  storing_location += '/'
with open(f'{storing_location}{matches_date}_matches.csv', 'w') as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=list(all_matches_details[0].keys())[::-1])
  writer.writeheader()
  writer.writerows(all_matches_details)

