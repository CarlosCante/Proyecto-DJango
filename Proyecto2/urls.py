from django.conf.urls import url
from Principal import views

urlpatterns = [
    url(r'^$',views.Pagina_Principal),
    url(r'^login/$',views.login),
    url(r'^registro/$',views.Registro_Usuario),
]