from authentication.tests import TestBase 

class TestSendOTP(TestBase) : 
    
    def test_not_pass_email(self) -> None : 
        response = self.client.post(self.send_otp_url)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data["detail"],"required-email")
    
    def test_email_not_exist(self) -> None : 
        response = self.client.post(self.send_otp_url,{"email":"test_email@gmail.com"})
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data["detail"],"invalid-email")
    
    def test_email_exist(self) -> None : 
        response = self.client.post(self.send_otp_url,{"email":self.user.email})
        self.assertEqual(response.status_code,200)