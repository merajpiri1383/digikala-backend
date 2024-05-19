from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsStaffOrNot(BasePermission) : 
    def has_permission(self,request,view) : 
        if request.user.is_authenticated : 
            return request.user.is_staff
        
class IsStaffOrReadOnly(BasePermission) :
    def has_permission(self,request,view): 
        if request.method in SAFE_METHODS : 
            return True 
        else : 
            return request.user.is_staff and request.user.is_authenticated