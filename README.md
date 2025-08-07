# User Guide
This project remixes Library of Congress information into a carousel based on a search term input. The project uses Python to construct a [Flask](https://flask.palletsprojects.com/en/stable/) Application that is then formatted  into classes with [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/). 

# User
- Library workers or Archivists who develop discovery tools for their institution's digital collections.
- Code that can be used with the API systems of shared archival and digital collections to retrieve information in an alternative view. 

 # API use
 This project was developed on a [Library of Congress API]([url](https://www.loc.gov/apis/json-and-yaml/)) that can be used without a key. 

 # User Steps
## Create the Requests for the Library of Congress API
- Import requests
- Define Search Parameters
  - Image can be a tricky filter for the LOC collection, since the initial search includes non-digitized items, and copies of reports in addition to photographs and drawings.
  - Playing with the filters could help prevent these types of results. 
- Make the Request
- Check the Response and add in additional information.

## Create a a Flask App
- Import Flask 
- List the Default page and description that search will replace
- Create a function that uses the API to search and retrieve images and captions.
- Use @app.route('/', methods=['GET']) and an index function to access the global image urls and text


## Use Bootstrap 5 to Format the Flask App
- Code for both a search box and the display of the images. 
    


[Example Results](http://127.0.0.1:5000/?search=dog) "LOC Carousel")

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1a7df3b2-51db-443d-98e6-3d189f1f2e6d" />




