import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from app_name import model


class Category(SQLAlchemyObjectType):
    class Meta:
        model = model.Category
        interfaces = (relay.Node,)


class Product(SQLAlchemyObjectType):
    class Meta:
        model = model.Product
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_categories = SQLAlchemyConnectionField(Category.connection)
    # Disable sorting over this field
    all_products = SQLAlchemyConnectionField(Product.connection)


schema = graphene.Schema(query=Query, types=[Category, Product])
