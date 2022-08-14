from django.urls import path

from .views import MolliePaymentView

urlpatterns = [
    path("mollie-payment", MolliePaymentView.as_view(), name="mollie_payment")
]
