from django.test import TestCase 
from django.contrib.auth import get_user_model 

class AuthTest(TestCase) : 
    
    def setUp(self) -> None : 
        print("start testting ...") 

    def test_jwt_authentication(self) : 
        print("test jwt")
    
    def tearDown(self) -> None : 
        print("end testting ...")