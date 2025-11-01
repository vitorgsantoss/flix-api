from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        model_codename = self.__get_model_codename(request.method, view)

        if model_codename:
            return request.user.has_perm(model_codename)
        return False

    def __get_model_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_suffix(method)
            return f'{app_label}.{action}_{model_name}'

        except AttributeError:
            return None

    def __get_action_suffix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'DELETE': 'delete',
            'PUT': 'change',
            'PATCH': 'change',
            'HEAD': 'view',
            'OPTIONS': 'view',
        }
        return method_actions[method]
