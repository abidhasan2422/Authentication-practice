from rest_framework.permissions import BasePermission
from django.utils import timezone
from .models import Post
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
    
# User Can Create Only 5 Posts Per Day

# class DailyPostLimit(BasePermission):

#     def has_permission(self, request, view):

#         if request.method == "POST":

#             today = timezone.now().date()

#             count = Post.objects.filter(
#                 user=request.user,
#                 created_at__date=today
#             ).count()

#             return count < 5

#         return True