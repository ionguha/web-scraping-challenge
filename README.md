![Mars Image](https://d28rv7itqgss13.cloudfront.net/assets/img/blogsix/martian_deviant-1600_large_2x.jpg)
**_The Martian by Rhads_**
# web-scraping-challenge
## Scraping websites for data related to the Mission to Mars
In this assignment, I have built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page
### Step 1 - Scraping
Web Scraping performed using **Jupyter Notebook, BeautifulSoup, Pandas,** and **Requests/Splinter**.
* A Jupyter Notebook file called `mission_to_mars.ipynb` contains all the scraping and analysis tasks. Here are the items scraped.
#### NASA Mars News
* (https://mars.nasa.gov/news/) was scraped to collect the latest News Title and Paragraph Text. 
#### JPL Mars Space Images - Featured Image
* (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) was navigates using splinter and the image url for the current Featured Mars Image was scraped.
#### Mars Weather
* (https://twitter.com/marswxreport?lang=en) was scraped for the latest Mars weather tweet
#### Mars Facts
* (https://space-facts.com/mars/) was scraped to collect a table containing facts about the planet including Diameter, Mass, etc.
### Mars Hemispheres
* (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) page was scraped to get the urls to obtain high resolution images for each of Mar's hemispheres. Each url was visited and scraped for the url and title for the full resolution hemisphere image
### Step 2 - MongoDB and Flask Application
Using **_MongoDB_** with **_Flask_** templating I created a new HTML page that displays all of the information that was scraped from the URLs above.
* The Jupyter notebook was converted into a Python script called **`scrape_mars.py`** with a function called **`mars_scraper`** that executes all the scraping code from above and return one Python dictionary containing all of the scraped data.
* A route called **`/scrape`** was created that imports **`scrape_mars.py`** script and calls **`mars_scraper`** function which updates (rather upserts) a **_MongoDB database_**.
* The root route **`/`** queries the **_MongoDB_** database and pass the mars data into a **_HTML template_** to display the data.
* A template HTML file called **`index.html`** takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 
### Additional Details
* The directory **_Screenshots_** stores all the images scraped from the Jupyter Notebook
* **_Mission_To_Mars.pdf_** contains screenshots of the HTML page illustrating different elements
* Recent versions of the following libraries are needed for executing the Python scripts and Jupyter Notebook **_(a) splinter (b) beautifulsoup4 (c) requests (d) cssutils (d) flask (e) flask_pymongo_** and **_(f) pandas_**
