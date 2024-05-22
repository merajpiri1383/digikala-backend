from authentication.tests import TestBase

class TestActivate(TestBase) : 
    
    def test_if_not_pass_email(self) -> None : 
        response = self.client.post(self.activate_url)
        self.assertEqual(response.data["detail"] , "required-email")
        self.assertEqual(response.status_code,400)
    
    def test_if_not_pass_otp(self) -> None : 
        response = self.client.post(self.activate_url,data={"email":self.user.email})
        self.assertEqual(response.data["detail"] ,"required-otp")
        self.assertEqual(response.status_code,400)
    
    def test_if_pass_not_registerd_email(self) -> None : 
        response = self.client.post(self.activate_url,data={"email":'test_1@gmail.com',
        "otp" : "123456"})
        self.assertEqual(response.data["detail"] , "wrong-email-otp")
        self.assertEqual(response.status_code,400)
    
    def test_if_pass_wrong_otp(self) -> None :
        response = self.client.post(self.activate_url,{'email':self.user,'otp':"12345"})
        self.assertEqual(response.data["detail"] ,"wrong-email-otp")
        self.assertEqual(response.status_code,400)