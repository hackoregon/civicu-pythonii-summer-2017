import requests

# Initialize our yearly count dictionary
yearly_count = dict()

# Request data for the years 2008 - 2017
for year in range(2008, 2018):
    # Generate the url
    url = ('http://service.civicpdx.org/homeless/ethnicity/' +
           f'?format=json&page=1&year={year}')
    # Submit our request to the API
    response = requests.get(url)
    # If we have any non-200s
    if response.status_code != 200:
        print(f'Unexpected response code {response.status_code} for year ' 
              f'{year}')
    # Initialize our count for this year (resets each loop)
    this_year_count = 0
    # Loop over the response json and pull the count value (pull 0 by default)
    for d in response.json():
        this_year_count += d.get('count',0)
    # Store the count for this year in our yearly count dictionary
    yearly_count[year] = this_year_count

# Print out the yearly count in a slightly more readable format
for year in yearly_count:
    print(f'{year}: {yearly_count[year]}')


        