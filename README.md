## Setup

### The first thing to do is to clone the repository:

$ `git clone https://github.com/naiyoma/movie_api.git`
$ `cd movie`

### Create a virtual environment to install dependencies in and activate it:

$ `virtualenv2 --no-site-packages env`
$ `source env/bin/activate`

### Then install the dependencies:

(env)$ `pip install -r requirements.txt`

Start the server
(env)$ `python manage.py runserver`


#### And navigate to `http://127.0.0.1:8000/movie/`

##### To Create a Movie 

###### `POST` the sample data below 

`
{
        "type": "new",
        "title": "aave",
        "genre": "Action",
        "popularity": "low",
        "poster": "https://monamovieapi.herokuapp.com/photos/Uon_emblem.gif"
}
`

###### To LIST all movies Created 

###### And navigate to http://127.0.0.1:8000/movie/ and GET

###### Navigate to https://monamovieapi.herokuapp.com/movie/ to acess the deployed version of the `API`

`POST` the sample data above to the `movie` endpoint






