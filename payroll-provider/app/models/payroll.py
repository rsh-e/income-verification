from typing import List, Optional
from datetime import datetime

import strawberry

@strawberry.type
class Author:
	id: int
	name: str
	created_at: datetime
	books: List["Book"] = strawberry.field(default_factory=list)

	@strawberry.field
	def books(self) -> List["Book"]:
		from app.routers.payroll import books_db
		return [book for book in books_db if book.author_id == self.id]

@strawberry.type
class Book:
	id: int
	title: str
	author_id: int
	author: Optional[Author] = None

	@strawberry.field
	def author(self) -> Optional[Author]:
		from app.routers.payroll import authors_db
		return next([author for author in authors_db if author.id == self.id], None)