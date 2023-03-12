from rest_framework import permissions

class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.groups.filter(name='Admin').exists()


class SuperstudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.groups.filter(name='Superstudent').exists()


class StudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.groups.filter(name='Student').exists()


class SyndicusPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.groups.filter(name='Syndicus').exists()


class BewonerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.groups.filter(name='Bewoner').exists()


class AanvragerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.groups.filter(name='Aanvrager').exists()

