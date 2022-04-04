import graphene

# In all schemas we need to receive graphene.ObjectType as argument
class Query(graphene.ObjectType):
    # These are the fields for the root type query
    # {
    #     hello
    # }
    hello = graphene.String(default_value="Hi!")
    cloud_greetings = graphene.String(default_value="Woof woof")

schema = graphene.Schema(query=Query)