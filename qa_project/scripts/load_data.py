import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_project.settings')
application = get_wsgi_application()

from qa_app.models import QA

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            question, answer = line.strip().split('|')
            QA.objects.create(question=question.strip(), answer=answer.strip())

if __name__ == '__main__':
    file_path = 'C:\\Users\\Success\\Desktop\\custom-huggingface-model-main\\custom-huggingface-model-main\\boyQA.txt'
    load_data(file_path)
