from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Regular Expressions
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'emailjoin.views.index', name='index.html'),
    url(r'^post/$','post.views.post', name = 'post.html'),
    url(r'^foo(?P<ref_id>.*)$', 'emailjoin.views.home', name='home.html'),
    #url(r'^(?P<post_id>.*)$', 'post.views.post', name= 'post'),
    # url(r'^blog/', include('blog.urls')),
    #admin/ tells us that we can navigte to 127.0.0.1:8000/admin
   
)
