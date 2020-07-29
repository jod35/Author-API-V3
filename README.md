# Author API V3

This is a third version of the AuthorApi I created. It has some added functionality like JSON serialization and deserialization with Marshmallow and data storage with NoSQL (MongoDB).

## Built With
- Flask
- Flask Marshmallow
- Flask MongoEngine
- MongoDb


## The API Endpoints
 ENDPOINT  |METHOD | FUNCTION|
 ----------|-------|---------|
 /authors/ | GET   |Get all authors|
 /authors/ | POST  |Create an author|
 /author/id| GET   | Get an author with an id|
 /author/id| PUT   | Update an author with an id|
 /author/id| DELETE   | Delete an author with an id|




## To get running
1. Clone the project
`git clone https://github.com/jod35/AuthorAPI-V2`

2. Install project Dependencies
` pip3 install -r requirements.txt `

3. To run the API,
- Start your MongoDB server ` sudo mongod `

- Enter the command in your termainal ` export FLASK_APP=wsgi.py`

- Finally run the appliaction with ` flask run `

## Author
[Ssali Jonathan (Jod35)](https://github.com/jod35)
