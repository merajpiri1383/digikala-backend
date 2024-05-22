from authentication.tests import TestBase

class LoginTest(TestBase) : 
    
    def test_email_not_pass(self) -> None : 
        response = self.client.post(self.login_url) 
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data["detail"],"required-email")
    
    def test_pass_not_registerd_email(self) -> None : 
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data["detail"],'required-email')
    
    def test_password_not_password(self) -> None : 
        response = self.client.post(self.login_url,{"email":self.user.email})
        self.assertEqual(response.data["detail"],"required-password")
        self.assertEqual(response.status_code,400)
    
    def test_invalid_password(self) -> None : 
        response = self.client.post(self.login_url,{"email":self.user.email,
            "password": "Passowrd"})
        self.assertEqual(response.data["detail"],'invalid-password')
        self.assertEqual(response.status_code,400)
    
    def test_correct_password(self) -> None : 
        response = self.client.post(self.login_url,{"email":self.user.email,
            "password": self.password})
        self.assertEqual(response.status_code,200)