from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# List of default image URLs and texts
# These will be replaced with the results from the API call
# after the user enters a search term.
image_urls = ["https://www.loc.gov/static/research-centers/main/images/banners/banner-placeholder.jpg"
   
]
text_list = ["Welcome to the Image Carousel! Enter a search term find a carousel of images categorized with that term in the Library of Congress digital collections."
  
]

def fetch_images_and_text(search_term):
    # This function would fetch images and text based on the search term using the API.
    
    # start with empty lists, otherwise the old images and text will still be displayed
    image_urls = []
    text_list = []

    import requests

    # Define search parameters
    params = {
        'q': search_term, # replace with search term from user!
        #'fa': ['subject:Rosa Parks' ],  # Note filter by date or by location never works b/c that data is not stored with the image!
        'fo': 'json',
        'c': 25  # number of results per page
    }

    # API endpoint
    url = 'https://www.loc.gov/pictures/search/'

    # Make the request
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

        

    return image_urls, text_list


@app.route('/', methods=['GET'])
def index():
    # get access to global image_urls and text_list
    # (this is a bit of hack but works for this simple app)
    global image_urls, text_list

    search_term = request.args.get('search')
    if search_term:
        print(f"Search term entered: {search_term}")
        image_urls, text_list = fetch_images_and_text(search_term)

    # zip IMAGE_URLS and TEXT_LIST to create pairs for display
    slides = zip(image_urls, text_list)

    return render_template('index.html', slides=slides)


if __name__ == '__main__':
    app.run(debug=True)
