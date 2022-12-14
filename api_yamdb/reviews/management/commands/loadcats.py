import os
from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Category


class Command(BaseCommand):
    """Загрузка в базу данных по модели Cats.
      Для загрузки данных нужно указать путь к файлу или
      загрузка выполнится автоматически из DEFAULT_FILE_PATH.
      """

    DEFAULT_FILE_PATH = os.path.join(
        os.path.join(os.path.abspath('static'), 'data'),
        'category.csv'
    )

    help = 'Загружает данные из csv-файла в таблицу Category.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, nargs='?', default=self.DEFAULT_FILE_PATH
        )

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, encoding='utf-8') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                _, created = Category.objects.get_or_create(
                    id=int(row['id']),
                    name=row['name'],
                    slug=row['slug'],
                )
        self.stdout.write(
            self.style.SUCCESS(
                f'Данные из {file_path} успешно загружены.'
            )
        )
