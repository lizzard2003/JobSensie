# this app is made to as user questions about themselves to choose a careerpath
# we are using flask

#hello
from traitify import Traitify
secret_key= "API_KEY"
traitify= Traitify(secret_key)

decks= traitify.get_decks()

#set deck id
traitify.deck_id = decks[0].id

#create assessment
assessment= traitify.create_assessment()

#get assesment
assessment = traitify.get_assessment(assessment.id)

# Get an assessment's slides
slides = traitify.get_slides(assessment.id)

# Upate a slide
slide = slides[0]
slide.response = True
slide.time_taken = 200
slide = traitify.update_slide(assessment.id, slide)

# Bulk update slides
for slide in slides:
  slide.response = True
  slide.time_taken = 200
slides = traitify.update_slides(assessment.id, slides)

# Get an assessment's results (personality types)
personality_types = traitify.get_personality_types(assessment.id)

# Get an assessment's results (personality type traits)
personality_type = personality_types["personality_types"][0].personality_type

personality_traits = traitify.get_personality_type_traits(assessment.id, personality_type.id)

# Get an assessment's results (personality traits)
personality_traits = traitify.get_personality_traits(assessment.id)

# Get an assessment's results (personality traits raw, no dichotomy returned)
personality_traits_raw = traitify.get_personality_traits_raw(assessment.id)

# Get an assessment's career matches, only applicable to the `career-deck` deck
careers = traitify.career_matches(assessment.id)

# Get multiple types of results from an assessment
results = traitify.results(assessment.id, ["types", "traits", "blend"])