from django.contrib.auth.models import BaseUserManager 

class UserManager(BaseUserManager) : 
    
    def create_user(self,email,password=None,**extra_fields) : 
        if not email : raise ValueError("email field is required .")
        if not password : raise ValueError("password field is required .")
        
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        return user.save()
    
    def create_superuser(self,email,password=None,**extra_fields) : 
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_manager",True)
        extra_fields.setdefault("is_superuser",True)
        
        if not extra_fields.get("is_active") : raise ValueError("is_active must be True .")
        if not extra_fields.get("is_staff") : raise ValueError("is_staff must be True .")
        if not extra_fields.get("is_superuser") : raise ValueError("is_superuser must be True .")
        if not extra_fields.get("is_manager") : raise ValueError("is_manager must be True .")
        return self.create_user(email,password,**extra_fields)