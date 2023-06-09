from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    # def has_permission(self, request, view):
    #     # Only allow POST (create) requests if the user is a superuser
    #     if request.method == 'POST':
    #         return request.user.is_superuser

    #     # For other request types, don't deny permission at this level
    #     return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return obj == request.user

        # Write permissions are only allowed to the superuser.
        return request.user.is_superuser