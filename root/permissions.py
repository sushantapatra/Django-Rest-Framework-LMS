from rest_framework.permissions import BasePermission, SAFE_METHODS


class isAdminUserOrReadonly(BasePermission):
    def has_permission(self, request, view):
        # if method is GET return true
        if request.method in SAFE_METHODS:
            return True
        # if user is admin return true

        if request.user.is_superuser:
            return True

        return False
        # else return false
