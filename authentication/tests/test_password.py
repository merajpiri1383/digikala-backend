from authentication.tests import TestBase

class PasswordTest(TestBase) : 
    
    def test_not_authenticated_user(self) -> None :
        response = self.client.put(self.update_password_url)
        self.assertEqual(response.status_code,401)
    
    def test_change_weak_password(self) -> None : 
        self.client.force_authenticate(self.user)
        response = self.client.put(self.update_password_url,data={"password":"12345"})
        self.assertEqual(response.status_code,400)
    
    def test_change_password(self) -> None : 
        self.client.force_authenticate(self.user) 
        response = self.client.put(self.update_password_url,data={"password":"Password@1"})
        self.assertEqual(response.status_code,200)