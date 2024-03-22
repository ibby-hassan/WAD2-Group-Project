import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insQuire_Project.settings')
import django
django.setup()

from random import randint
from insQuire.models import Category, Question, Answer, UserProfile
from django.contrib.auth.models import User

def populate():

    users = [
        {'username': 'user1', 'password': 'password1', 'email': 'email1@example.com'},
        {'username': 'user2', 'password': 'password2', 'email': 'email2@example.com'},
        {'username': 'user3', 'password': 'password3', 'email': 'email3@example.com'},
        {'username': 'user4', 'password': 'password4', 'email': 'email4@example.com'},
        {'username': 'user5', 'password': 'password5', 'email': 'email5@example.com'},
    ]

    answerCooking1 = [
        {'content': 'I usually use 3 eggs for my omelet. I find that it is the perfect amount for me.', 'votes': 0},
    ]
    answerCooking2 = [
        {'content': 'I usually cook my steak on a grill. I find that it is the best way to cook a steak.', 'votes': 0},
    ]
    answerCooking3 = [
        {'content': 'I love using carrots in my cooking. They add a nice sweet taste to my dishes.', 'votes': 0},
    ]
    cookingQuestions = [
        {'title': 'How many eggs in your omelet?', 'content': 'Hi guys. I was curious, how many eggs should I be adding to my omelet?', 'answers':answerCooking1, 'votes': 0},
        {'title': 'What is the best way to cook a steak?', 'content': 'I have been trying to cook a steak for a while now, but I can never get it right. What is the best way to cook a steak?', 'answers':answerCooking2, 'votes': 0},
        {'title': 'Favourite vegetables?', 'content': 'What are your favourite vegetables to cook with?', 'answers':answerCooking3, 'votes': 0}
    ]

    answerSport1 = [
        {'content': 'I find that practicing my shooting and dribbling has helped me improve my basketball skills.', 'votes': 0},
    ]
    answerSport2 = [
        {'content': 'I find that running long distances has helped me improve my marathon times.', 'votes': 0},
    ]
    answerSport3 = [
        {'content': 'I love playing basketball. It is my favourite sport to play.', 'votes': 0},
    ]
    sportsQuestions = [
        {'title': 'How do I get better at basketball?', 'content': 'I have been playing basketball for a while now, but I am not improving. What can I do to get better?', 'answers':answerSport1, 'votes': 0},
        {'title': 'What is the best way to train for a marathon?', 'content': 'I have been training for a marathon for a while now, but I am not improving. What can I do to get better?', 'answers':answerSport2, 'votes': 0},
        {'title': 'Favourite sports?', 'content': 'What are your favourite sports to play?', 'answers':answerSport3, 'votes': 0}
    ]

    categories = {
        'Sports': {'description': 'Questions relating to all things sports! Discuss your teams, how to play sports, etc.', 'questions': sportsQuestions},
        'Cooking': {'description': 'Questions about all things that pique your culinary interest! Ask for recipes, advice, or discuss shows!', 'questions': cookingQuestions}
    }

    profile_list = []
    for user_details in users:
        user = addUser(user_details['username'], user_details['password'], user_details['email'])
        user_profile = addUserProfile(user)
        profile_list.append(user_profile)

    for category, category_data in categories.items():
        c = addCategory(category, category_data['description'])
        for q in category_data['questions']:
            author = profile_list[randint(0, len(profile_list) - 1)]
            q_instance = addQuestion(c, q['title'], q['content'], author, q['votes'])
            for a in q['answers']:
                author = profile_list[randint(0, len(profile_list) - 1)]
                addAnswer(q_instance, a['content'], author, a['votes'])

def addUser(username, password, email):
    u = User.objects.get_or_create(username=username, email=email)[0]
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        user.set_password(password)
        user.save()
    return u

def addUserProfile(user):
    u = UserProfile.objects.get_or_create(user=user)[0]
    u.save()
    return uP

def addCategory(name, description):
    c = Category.objects.get_or_create(name=name, description=description)[0]
    c.save()
    return c

def addQuestion(category, title, content, author, votes):
    q = Question.objects.get_or_create(category=category, title=title, content=content, author=author, votes=votes)[0]
    q.save()
    return q

def addAnswer(question, content, author, votes):
    a = Answer.objects.get_or_create(question=question, content=content, author=author, votes=votes)[0]
    a.save()
    return a

if __name__ == '__main__':
    print('Starting insQuire population script...')
    populate()
    print('insQuire population script complete.')