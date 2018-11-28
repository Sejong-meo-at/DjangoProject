from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    massage = "이 글 작성자입니다."
    my_safe_method = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method == self.my_safe_method:
            return True
        return False

    def has_objects_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True
        return obj.user == request.user
