from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message

# Create your tests here.
class SnsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        usr = cls.create_user()
        cls.create_message(usr)

    @classmethod
    def create_user(cls):
        User(username="test", password="test", is_staff=True, is_active=True).save()
        usr = User.objects.filter(username="test").first()
        return (usr)

    @classmethod
    def create_message(cls, usr):
        Message(contents="this is test message.", owner_id=usr.id).save()
        Message(contents="test", owner_id=usr.id).save()
        Message(contents="ok", owner_id=usr.id).save()
        Message(contents="ng", owner_id=usr.id).save()
        Message(contents="finish", owner_id=usr.id).save()


    def test_check(self):
        usr = User.objects.first()
        self.assertIsNotNone(usr)
        msg = Message.objects.first()
        self.assertIsNotNone(msg)

        # x = True
        # self.assertTrue(x) # xはTrueか？

        # y = 100
        # self.assertGreater(y, 0) # どっちが大きいか？

        # arr = [10, 20, 30]
        # self.assertIn(20, arr) # 20が含まれているか？

        # nn = True
        # self.assertIsNone(nn) # nnはnoneか？