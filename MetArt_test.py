import requests

# Search for object IDs with a query term
search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
search_params = {
    "q": "Battle of Borodino", # replace with search term from user!
    "hasImages": "true"
}


search_response = requests.get(search_url, params=search_params)
object_ids = search_response.json().get("objectIDs", [])[:20]  # Limit to first 20 results


# Fetch object details and filter by date
object_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
for obj_id in object_ids:
    obj_response = requests.get(f"{object_url}{obj_id}")
    if obj_response.status_code == 200:
        obj_data = obj_response.json()
        year = obj_data.get("objectBeginDate", "")
        try:
            title = obj_data.get("title")
            image = obj_data.get("primaryImage")
            print(f"Title: {title}\nYear: {year}\nImage URL: {image}\n")
        except KeyError as e:
            continue  # Skip if some data is missing



'''
# All fields in the object data

'objectID': int = 437422
'isHighlight': bool = False
'accessionNumber': str = '1974.348'
'accessionYear': str = '1974'
'isPublicDomain': bool = True
'primaryImage': str = 'https://images.metmuseum.org/CRDImages/ep/original/DT10776.jpg'
'primaryImageSmall': str = 'https://images.metmuseum.org/CRDImages/ep/web-large/DT10776.jpg'
'additionalImages': list = ['https://images.metmuseum.org/CRDImages/ep/original/LC-1974_348-2.jpg', 'https://images.metmuseum.org/CRDImages/ep/original/LC-1974_348-3.jpg']
special variables
function variables
0: str = 'https://images.metmuseum.org/CRDImages/ep/original/LC-1974_348-2.jpg'
1: str = 'https://images.metmuseum.org/CRDImages/ep/original/LC-1974_348-3.jpg'
len(): int = 2
'constituents': list = [{'constituentID': 162301, 'role': 'Artist', 'name': 'Guido Reni', 'constituentULAN_URL': 'http://vocab.getty.edu/page/ulan/500030334', 'constituentWikidata_URL': 'https://www.wikidata.org/wiki/Q109061', 'gender': ''}]
'department': str = 'European Paintings'
'objectName': str = 'Painting'
'title': str = 'Charity'
'culture': str = ''
'period': str = ''
'dynasty': str = ''
'reign': str = ''
'portfolio': str = ''
'artistRole': str = 'Artist'
'artistPrefix': str = ''
'artistDisplayName': str = 'Guido Reni'
'artistDisplayBio': str = 'Italian, Bologna 1575–1642 Bologna'
'artistSuffix': str = ''
'artistAlphaSort': str = 'Reni, Guido'
'artistNationality': str = 'Italian'
'artistBeginDate': str = '1575'
'artistEndDate': str = '1642'
'artistGender': str = ''
'artistWikidata_URL': str = 'https://www.wikidata.org/wiki/Q109061'
'artistULAN_URL': str = 'http://vocab.getty.edu/page/ulan/500030334'
'objectDate': str = 'ca. 1630'
'objectBeginDate': int = 1625
'objectEndDate': int = 1635
'medium': str = 'Oil on canvas'
'dimensions': str = '54 x 41 3/4 in. (137.2 x 106 cm)'
'measurements': list = [{'elementName': 'Overall', 'elementDescription': None, 'elementMeasurements': {...}}]
'creditLine': str = 'Gift of Mr. and Mrs. Charles Wrightsman, 1974'
'geographyType': str = ''
'city': str = ''
'state': str = ''
'county': str = ''
'country': str = ''
'region': str = ''
'subregion': str = ''
'locale': str = ''
'locus': str = ''
'excavation': str = ''
'river': str = ''
'classification': str = 'Paintings'
'rightsAndReproduction': str = ''
'linkResource': str = ''
'metadataDate': str = '2025-06-27T04:50:31.807Z'
'repository': str = 'Metropolitan Museum of Art, New York, NY'
'objectURL': str = 'https://www.metmuseum.org/art/collection/search/437422'
'tags': list = [{'term': 'Children', 'AAT_URL': 'http://vocab.getty.edu/page/aat/300025945', 'Wikidata_URL': 'https://www.wikidata.org/wiki/Q7569'}, {'term': 'Women', 'AAT_URL': 'http://vocab.getty.edu/page/aat/300025943', 'Wikidata_URL': 'https://www.wikidata.org/wiki/Q467'}, {'term': 'Allegory', 'AAT_URL': 'http://vocab.getty.edu/page/aat/300055866', 'Wikidata_URL': 'https://www.wikidata.org/wiki/Q18535'}, {'term': 'Nursing', 'AAT_URL': 'http://vocab.getty.edu/page/aat/300379905', 'Wikidata_URL': 'https://www.wikidata.org/wiki/Q174876'}]
'objectWikidata_URL': str = 'https://www.wikidata.org/wiki/Q19911778'
'isTimelineWork': bool = True
'GalleryNumber': str = '620'
'''
