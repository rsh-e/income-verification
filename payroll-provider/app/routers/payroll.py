import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
from app.models.payroll import Author, Book
from datetime import datetime

# Demo Data
authors_db =[
	Author(
		id=1,
		name="rishi",
		created_at=datetime(2026, 1, 18),
	),
	Author(
		id=2,
		name="sugi",
		created_at=datetime(2025, 11, 11),
	),
	Author(
		id=3,
		name="sushi",
		created_at=datetime(2022, 8, 20),
	)
]


books_db = [
	Book(
		id=1,
		title="a fistful of dollars",
		author_id=1
	),
	Book(
		id=1,
		title="for a few dollars more",
		author_id=2
	),
	Book(
		id=1,
		title="the good, bad and the ugly",
		author_id=3		
	),
	Book(
		id=1,
		title="spaghetti western",
		author_id=1
	),
]

# Usage: 
# query {
#   author(id: 1) {
#     id
#     name
#     books {
#       title
#     }
#   }
# }

@strawberry.type
class Query:
	@strawberry.field
	async def hello(self) -> str:
		return "Hello World Again 2.0. abcsc beep again so"

	@strawberry.field
	async def bye(self) -> str:
		return "Goodbye so"
	
	@strawberry.field
	async def books(self) -> List[Book]:
		return books_db
	
	@strawberry.field
	async def book(self, id:int) -> Optional[Book]:
		return next((book for book in books_db if book.id == id), None)
	
	@strawberry.field
	async def authors(self) -> List[Author]:
		return authors_db

	@strawberry.field
	async def author(self, id:int) -> Optional[Author]:
		return next((author for author in authors_db if author.id ==id), None)

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
