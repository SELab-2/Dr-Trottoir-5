from rest_framework import permissions
from planning.models import InfoPerBuilding, DagPlanning


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS and request.user and not request.user.is_anonymous


class StudentReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return request.method in permissions.SAFE_METHODS and user.role == 'ST'


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return user.role == 'AD'


class SuperstudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return user.role == 'SU'


class StudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return user.role == 'ST'


# TODO Fix Student that has building can place picture
class StudentPicturePermission(permissions.BasePermission):
    def has_permissions(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        try:
            info = InfoPerBuilding.objects.get(pk=request.data["infoPerBuilding"])
            dag = DagPlanning.objects.get(pk=info.dagPlanning)
            return False
        except InfoPerBuilding.DoesNotExist or DagPlanning.DoesNotExist:
            return False


class SyndicusPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return user.role == 'SY'


class BewonerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return user.role == 'BE'


class AanvragerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.is_anonymous:
            return False
        return user.role == 'AA'
