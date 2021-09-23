import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, title, body, **kwargs):
        post = Post()
        post.title = title
        post.body = body
        post.save()

        return PostCreate(post=post)

class PostUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
        body = graphene.String(required=True)
    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, id, title, body, **kwargs):
        post = Post.objects.get(pk=id)
        post.title = title
        post.body = body
        post.save()

        return PostUpdate(post=post)


class Query(graphene.ObjectType):
    posts = DjangoListField(PostType)

    def resolve_posts(root, info, **kwargs):
        return Post.objects.all()

class Mutation(graphene.ObjectType):
    create_post = PostCreate.Field()
    update_post = PostUpdate.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)