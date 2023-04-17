# this app is made to as user questions about themselves to choose a careerpath
# we are using flask


from traitify import Traitify
secret_key= "API_KEY"
traitify= Traitify(secret_key)

decks= traitify.get_decks()

#set deck id
traitify.deck_id = decks[0].id

#create assessment
assessment= traitify.create_assessment()

#get assesment
