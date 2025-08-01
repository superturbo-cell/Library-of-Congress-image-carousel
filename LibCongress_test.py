import requests

# Define search parameters
params = {
    'q': 'Minnesota', # replace with search term from user!
    #'fa': ['subject:Rosa Parks' ],  # Note filter by date or by location never works b/c that data is not stored with the image!
    'fo': 'json',
    'c': 25  # number of results per page
}

# API endpoint
url = 'https://www.loc.gov/pictures/search/'

# Make the request
response = requests.get(url, params=params)


image_urls = []
text_list = []

# Check response
if response.status_code == 200:
    data = response.json()
    for item in data.get('results', []):
        title = item.get('title')
        image_dict = item.get('image', 'No image available')
        image_url = image_dict["full"]
        image_urls.append(image_url)
        text_list.append(title)

        # Print the title and image URL
        print(f"Title: {title}\nImage URL: {image_url}\n")
        subjects = item.get('subjects', [])
        subject_list = ', '.join(subjects) if subjects else 'No subjects available'
        print(f"Title: {title}\nSubjects: {subject_list}\nImage URL: {image_url}\n")
else:
    print(f"Error: {response.status_code}")
print(image_urls, text_list)

'''
'source_created': str = '2010-06-23T00:00:00Z'
'index': int = 1
'medium': str = '1 photograph : digital, TIFF file, color.'
'reproduction_number': str = 'LC-DIG-highsm-05808 (original digital file)'
'links': dict = {'item': 'https://www.loc.gov/pictures/item/2010637645/', 'resource': 'https://www.loc.gov/pictures/item/2010637645/resource/'}
'title': str = 'Exact spot on Dexter Avenue in Montgomery, Alabama, where Rosa Parks waited for the bus on that fateful day that turned the Civil Rights Movement into a raging human rights war'
'image': dict = {'alt': 'digitized item thumbnail', 'full': 'https://tile.loc.gov/storage-services/service/pnp/highsm/05800/05808r.jpg', 'square': 'https://tile.loc.gov/storage-services/service/pnp/highsm/05800/05808_75x75px.jpg', 'thumb': 'https://tile.loc.gov/storage-services/service/pnp/highsm/05800/05808_150px.jpg'}
'created': str = '2017-06-27T00:00:00Z'
'modified': str = '2017-06-27T00:00:00Z'
'collection': list = ['diof', 'highsm', 'minload', 'pp']
'creator': str = 'Highsmith, Carol M., 1946-'
'call_number': str = 'LC-DIG-highsm- 05808 (ONLINE) [P&P]'
'medium_brief': str = '1 photograph :'
'source_modified': str = '2017-06-22T00:00:00Z'
'pk': str = '2010637645'
'created_published_date': str = '2010 March 12.'
'subjects': list = ['United States--Alabama--Montgomery.', 'Rosa Parks', 'civil rights', 'Black History', 'America', 'Digital photographs--Color--2000-2010.']
''' 
