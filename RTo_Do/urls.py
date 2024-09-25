from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("login/",views.login,name="login"),
    path("signin/",views.signin,name="signin"),
    path("addtask/",views.addtask,name="addtask"),
    path("edittask/",views.edittask,name="edittask"),
    path("resettask/",views.resettask,name="resettask"),
    path("logresettask/",views.logresettask,name="resettask"),
    path("email-verification-code/",views.email_verification,name="email_verification")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)