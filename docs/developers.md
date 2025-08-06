# Information for Developers
This project remixes Library of Congress information into a carousel based on a search term input. The project uses Python to construct a Flask Application that is then formatted  into classes with Bootstrap 5. 

# User
- Library workers or Archivists who develop discovery tools for their institution's digital collections.
- Code that can be used with the API systems of shared archival and digital collections to retrieve information in an alternative view. 
 
# Install 
Use pip to install third party packages [Flask](https://flask.palletsprojects.com/en/stable/url) and [Requests](https://pypi.org/project/requests/)

# Code for Reuse
The block of code that does most of the work requesting from the API is:

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

The code for the Carousel in Bootstrap 5 is :
``` <!-- Carousel -->
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            {% for image, caption in slides %}
            <div class="carousel-item {% if loop.first %}active{% endif %}">
                <img src="{{ image }}" class="d-block mx-auto carousel-img" alt="{{ caption }}">
                <div class="carousel-caption d-none d-md-block">
                    <h5>{{ caption }}</h5>
                </div>
            </div>
            {% endfor %}
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
        </button>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

# User Flow
•	Known Issues: You should mention any issues you know about (or suspect)

# Future Work
- Using this carousel with other API content
- Spacing the captions beneath the images for more clear reading.
- Linking the images back to the original catalog record for more information
- Applying a secondary filter or more clear display pattern for the results. 
