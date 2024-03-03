import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insQuire_Project.settings')
import django
django.setup()

from insQuire.models import Category, Question

def populate():
    pythonQuestions = [
        {'title': 'What is Python?', 'content': 'Python is a high-level, interpreted, interactive and object-oriented scripting language.', 'votes': 0},
        {'title': 'What are the key features of Python?', 'content': 'Python is an interpreted language, it is interactive, it is object-oriented, it is high-level, it is extensible in C++ and C.', 'votes': 0},
        {'title': 'What are the benefits of using Python?', 'content': 'Python is easy to learn, easy to read, easy to maintain, easy to extend, easy to deploy.', 'votes': 0},
        {'title': 'What are the drawbacks of using Python?', 'content': 'Python is slow, it is not memory efficient, it is not good for mobile development, it is not good for game development.', 'votes': 0},
        {'title': 'What is the Python Software Foundation?', 'content': 'The Python Software Foundation is a non-profit organization entirely supported by its sponsor members.', 'votes': 0}
    ]

    djangoQuestions = [
        {'title': 'What is Django?', 'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.', 'votes': 0},
        {'title': 'What are the key features of Django?', 'content': 'Django is fast, it is secure, it is scalable, it is versatile, it is maintainable.', 'votes': 0},
        {'title': 'What are the benefits of using Django?', 'content': 'Django is fast, it is secure, it is scalable, it is versatile, it is maintainable.', 'votes': 0},
        {'title': 'What are the drawbacks of using Django?', 'content': 'Django is monolithic, it is not good for small projects, it is not good for mobile development, it is not good for game development.', 'votes': 0},
        {'title': 'What is the Django Software Foundation?', 'content': 'The Django Software Foundation is a non-profit organization that maintains Django.', 'votes': 0}
    ]

    categories = {
        'Python': {'description': 'Python is a high-level, interpreted, interactive and object-oriented scripting language.', 'questions': pythonQuestions},
        'Django': {'description': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.', 'questions': djangoQuestions}
    }

    for category, categoryData in categories.items():
        c = addCategory(category, categoryData['description'], len(categoryData['questions']))
        for question in categoryData['questions']:
            addQuestion(c, question['title'], question['content'], question['votes'])

    for c in Category.objects.all():
        for q in Question.objects.filter(category=c):
            print(f'- {c}: {q}')

def addCategory(name, description, questionsInCategory):
    c = Category.objects.get_or_create(name=name, description=description, questionsInCategory=questionsInCategory)[0]
    c.save()
    return c

def addQuestion(category, title, content, votes):
    q = Question.objects.get_or_create(category=category, title=title, content=content, votes=votes)[0]
    q.author 
    q.save()
    return q

if __name__ == '__main__':
    print('Starting insQuire population script...')
    populate()
    print('insQuire population script complete.')