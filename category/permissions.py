from rest_framework.permissions import BasePermission

class IsStaffOrReadOnly(BasePermission) :
    def has_permission(self,request,view):
        if request.user.is_authenticated : 
            return request.user.is_staff