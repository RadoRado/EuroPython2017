from django.conf.urls import url

from .views import (
    ReplIndexView,
    ReplCodeRunView,
    ReplCodeRunResultView
)


urlpatterns = [
    url(regex='^$',
        view=ReplIndexView.as_view(),
        name='index'
    ),
    url(regex='^run/$',
        view=ReplCodeRunView.as_view(),
        name='code-run'
    ),
    url(regex='^code-run/(?P<code_run_id>[0-9]+)/$',
        view=ReplCodeRunResultView.as_view(),
        name='code-run-detail'
    )
]
