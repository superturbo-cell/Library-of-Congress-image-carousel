# Information for Developers
This project remixes Library of Congress information into a carousel based on a search term input. The project uses Python to construct a Flask Application that is then formatted  into classes with Bootstrap 5. 

# User
- Library workers or Archivists who develop discovery tools for their institution's digital collections.
- Code that can be used with the API systems of shared archival and digital collections to retrieve information in an alternative view. 
 
# Install 
Use pip to install third party packages [Flask](https://flask.palletsprojects.com/en/stable/url) and [Requests](https://pypi.org/project/requests/)

# Search Code for the API
```  # Make the request
    response = requests.get(url, params=params)

    # Check response
    if response.status_code == 200:
        data = response.json()
        for item in data.get('results', []):
            title = item.get('title')
            image_dict = item.get('image', 'No image available')
            image_url = image_dict["full"]
            image_urls.append(image_url)
            text_list.append(title)

    else:
        print(f"Error: {response.status_code}")
```
# User Flow
•	Known Issues: You should mention any issues you know about (or suspect)

# Future Work
- Using this carousel with other API content
- Spacing the captions beneath the images for more clear reading.
- Linking the images back to the original catalog record for more information
- Applying a secondary filter or more clear display pattern for the results. 
