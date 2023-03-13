from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.role == 'AD'


class SuperstudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.role == 'SU'


class StudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.role == 'ST'


class SyndicusPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.role == 'SY'


class BewonerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.role == 'BE'


class AanvragerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return user.role == 'AA'

