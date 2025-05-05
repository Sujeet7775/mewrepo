from rest_framework import permissions

class BookCRUDPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('myapp.can_read_book')
        elif request.method == 'POST':
            return request.user.has_perm('myapp.can_create_book')
        elif request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('myapp.can_update_book')
        elif request.method == 'DELETE':
            return request.user.has_perm('myapp.can_delete_book')
        return False

class ArticleCRUDPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('myapp.can_read_article')
        elif request.method == 'POST':
            return request.user.has_perm('myapp.can_create_article')
        elif request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('myapp.can_update_article')
        elif request.method == 'DELETE':
            return request.user.has_perm('myapp.can_delete_article')
        return False