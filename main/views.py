from main.models import Author,AuthorSchema
from flask import request,jsonify,make_response
from main import app,db

@app.route('/authors',methods=['GET'])
def get_all_authors():
    all_authors=Author.objects.all()
    #getting all the authors 

    author_schema=AuthorSchema(many=True,only=['name','specialization'])

    authors=author_schema.dump(all_authors) #return users as JSON

    return make_response(
        jsonify(
            {"authors":authors}
        )
    )



