from rest_framework.permissions import BasePermission

class OnlySpecificUsersDelete(BasePermission):

    def has_permission(self, request, view):
        # user must be authenticated
        if not request.user or not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            # return request.user.id in [1, 5] #user id not database id
            return obj.id in [3,5] # used in database id
        return True