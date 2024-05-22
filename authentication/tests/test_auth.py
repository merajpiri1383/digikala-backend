from authentication.tests import TestBase

class AuthTest(TestBase) : 
    
    def test_registerd_user(self) :
        response = self.client.post(self.auth_url,data={"email":self.user.email})
        self.assertFalse(response.data["created"])
        self.assertEqual(response.status_code,200)
    
    def test_not_registed_user(self) : 
        response = self.client.post(self.auth_url,data={'email':'test_2@gmail.com'})
        self.assertTrue(response.data["created"])
        self.assertEqual(response.status_code,200)
    
    def test_if_not_pass_email(self) : 
        response = self.client.post(self.auth_url)
        self.assertEqual(response.data["detail"] , "required-email")
        self.assertEqual(response.status_code,400)
        