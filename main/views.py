from main.models import Author,AuthorSchema
from flask import request,jsonify,make_response
from main import app,db
from bson import ObjectId

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
            {"authors":authors,
             "Success":True}
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
            "author":author,
            "Success":True}
        ),201
    )

    author=author_schema.dump(new_author)


####################################
######Get an Author with an id######
####################################

@app.route('/author/<id>',methods=['GET'])
def get_author_by_id(id):
    #fetch a user with an id
    get_author=Author.objects.get_or_404(id=ObjectId(id))

    author_schema=AuthorSchema(only=['id','name','specialization'])

    author=author_schema.dump(get_author)

    return make_response(jsonify(
        {
            "author":author,
            "success":True,
        }
    ))

@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({
            "message":"Not Found"
        })
    )

@app.errorhandler(500)
def internal_server_error(error):
    return make_response(
        jsonify(
            {
                "message":"Internal Server Error"
            }
        )
    )

@app.shell_context_processor
def make_shell_context():
    return {
        "db":db,
        "Author":Author,
        "app",app
    }