
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('events1/',views.events1,name='events1'),
      path('events/',views.events,name='events'),
       path('booking/',views.booking,name='booking'),
       path('booking/thanks/', views.thanks_view, name='thanks'),
        path('contact/',views.contact,name='contact'),
       path('my-events/', views.my_events, name='my_events'),
       path('booking_confirmation_email',views.booking_confirmation_email,name='booking_confirmation_email'),
       path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
       path('update-booking/<int:booking_id>/', views.update_booking, name='update_booking'),
       path('event/<int:event_id>/', views.event_detail, name='event_detail'),
       path('feedback/', views.feedback, name='feedback'),
       path('feedback/<int:pk>/delete/', views.delete_feedback, name='delete_feedback'),
       path('feedback1/', views.feedback1, name='feedback1'),
]