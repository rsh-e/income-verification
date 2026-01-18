import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    @strawberry.field
    async def hello(self) -> str:
        return "Hello World Again 2.0. abcsc beep again so"

    @strawberry.field
    async def bye(self) -> str:
        return "Goodbye so"

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
