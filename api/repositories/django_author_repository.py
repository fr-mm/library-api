from api.models import AuthorModel
from domain.entities.author.author import Author
from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO
from domain.repositories.author_repository import AuthorRepository


# TODO: make integration test with bank

class DjangoAuthorRepository(AuthorRepository):
    def save(self, author: Author) -> None:
        author_dto = AuthorOutputDTO.from_entity(author)
        author_model = AuthorModel.from_dto(author_dto)
        author_model.save()
