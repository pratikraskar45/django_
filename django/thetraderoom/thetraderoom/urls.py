"""
URL configuration for thetraderoom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from thetraderoom import views

# for uplode image in admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),  
    
    # bcz i have only one html page no reqired for url for all
    path('about/',views.about),
    path('services/',views.services,name="services"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('contact/',views.contact,name="contact"),
    # ----------------------------------------------------
    # form
    path('userform',views.userForm),
    
    # redirect
    path('formoutput/',views.formOutput),
    
    # for action method   submitform
    path('submitform/',views.submitform,name="submitform"),



   

    path('about-us/',views.aboutUs),
    path('course/',views.course),
    path('course/<int:courseid>',views.courseDetails),
    # path for even odd
    # url also for manual form validation
    path('saveevenodd',views.saveevenodd,name="Saveevenodd"),
    # marksheet
    path('marksheet',views.marksheet),

    # for newadetails
    path('newsdetails/<slug>',views.newsDetails),#newsid or slug
    # for save data in admin
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),

]
# for uplode image in admin
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
else:
    pass