import argparse

from django.core.management import BaseCommand, CommandParser

from api.repositories.django_author_repository import DjangoAuthorRepository
from domain.entities.authors_csv_file.authors_csv_file import AuthorsCSVFile
from domain.services.author.save_author_collection_service import SaveAuthorCollectionService


class Command(BaseCommand):
    __argument_name: str = 'csv_file'
    __save_author_collection_service: SaveAuthorCollectionService

    help = 'Import authors from a CSV file to database.'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        author_repository = DjangoAuthorRepository()
        self.__save_author_collection_service = SaveAuthorCollectionService(author_repository)

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            self.__argument_name,
            type=argparse.FileType('r')
        )

    def handle(self, *args, **options) -> None:
        raw_csv = options[self.__argument_name]
        authors_csv = AuthorsCSVFile(raw_csv)
        author_count = authors_csv.length

        author_creation_dtos = authors_csv.to_dto_collection()

        self.__save_author_collection_service.execute(author_creation_dtos)
        print(f'Added {author_count} author(s) to database')
