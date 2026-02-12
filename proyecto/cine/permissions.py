from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedForWrite(BasePermission):
    """
    Permite lectura a cualquiera (GET, HEAD, OPTIONS).
    Requiere autenticación para escritura (POST, PUT, PATCH, DELETE).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated