# qa_search/management/commands/populate_qa_data.py

from django.core.management.base import BaseCommand
from qa_search.models import QADataset

class Command(BaseCommand):
    help = 'Populate QA data from a text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the text file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    question, answer = line.strip().split('|')
                    QADataset.objects.create(question=question, answer=answer)
            self.stdout.write(self.style.SUCCESS('Successfully populated QA data.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File '{file_path}' not found."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
