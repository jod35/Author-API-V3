from main.models import Author,AuthorSchema
from flask import request,jsonify,make_response
from main import app,db

##########################################
######### Get all authors ################
##########################################

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


#######################################
######## Create an author #############
#######################################

@app.route('/authors',methods=['POST'])
def create_new_author():
    
    data=request.get_json()

    new_author=Author(name=data['name'],specialization=data['specialization'])

    new_author.save()

    author_schema=AuthorSchema(only=['name','specialization'])

    author=author_schema.dump(new_author)

    return make_response(
        jsonify(
            {"message":"Author Created Successfully",
            "author":author}
        ),201
    )

    author=author_schema.dump(new_author)


