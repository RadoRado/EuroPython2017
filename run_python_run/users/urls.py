from django.conf.urls import url

from .views import LoginView, RegisterView, LogoutView


urlpatterns = [
    url(regex='^login/$',
        view=LoginView.as_view(),
        name='login'
    ),
    url(regex='^register/$',
        view=RegisterView.as_view(),
        name='register'
    ),
    url(regex='^logout/$',
        view=LogoutView.as_view(),
        name='logout'
    )
]
