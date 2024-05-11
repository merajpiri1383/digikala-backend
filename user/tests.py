from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class TestUser(TestCase) : 
    
    # check is exception occur when two user have the same email
    def test_unique_email(self): 
        get_user_model().objects.create(email="test@gmail.com")
        with self.assertRaises(IntegrityError) : 
            get_user_model().objects.create(email="test@gmail.com")