from typing import List

from domain.entities.author.dtos import AuthorDTO
from domain.services.author.base_author_service import BaseAuthorService


class ListAuthorsService(BaseAuthorService):
    def execute(self) -> List[AuthorDTO]:
        authors = self._author_repository.get_all()
        return [AuthorDTO.from_entity(author) for author in authors]
