from rest_framework import permissions
from users.models import Users




class IsAdminOrSeller(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return(
            request.user 
            and request.user.is_authenticated 
            and request.user.role in [Users.Role.ADMIN, Users.Role.SELLERS]
        )
    

class IsSeller(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return(
            request.user 
            and request.user.is_authenticated 
            and request.user.role in [Users.Role.SELLERS,] 
        )