from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

from trench.views import MFAFirstStepMixin, MFASecondStepMixin, MFAStepMixin, User


class MFAJWTView(MFAStepMixin):
    def _successful_authentication_response(self, user: User) -> Response:
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        token = RefreshToken.for_user(user=user)
        return Response(data={"refresh": str(token), "access": str(token.access_token)})


class MFAFirstStepJWTView(MFAJWTView, MFAFirstStepMixin):
    pass


class MFASecondStepJWTView(MFAJWTView, MFASecondStepMixin):
    pass
