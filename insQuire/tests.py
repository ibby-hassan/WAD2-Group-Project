from django.test import TestCase
from insQuire.models import UserProfile, Question, User, Category

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.userprofile = UserProfile.objects.create(user=self.user)

    def test_user_profile_creation(self):
        self.assertEqual(self.user.username, 'testuser')

class QuestionModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Test Category')
        self.question = Question.objects.create(title='Test Question', content='This is a test question', category=category)

    def test_question_creation(self):
        self.assertEqual(self.question.title, 'Test Question')
        self.assertEqual(self.question.content, 'This is a test question')
        self.assertEqual(self.question.category.name, 'Test Category')