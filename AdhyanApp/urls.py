from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('otp/',views.otp,name='otp'),
    path('logout/',views.logout,name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('change-password/',views.change_password,name='change-password'),
    path('about/',views.about,name='about'),
    path('admission/',views.admission,name='admission'),
    path('all-courses/',views.all_courses,name='all-courses'),
    path('course-details/<int:pk>',views.course_details,name='course-details'),
    path('payment/<int:pk>',views.payment,name='payment'),
    path('cart/',views.cart,name='cart'),
    path('review/<int:pk>',views.review,name='review'),
    path('view-course/<int:pk>',views.view_course,name='view-course'),
    path('views/<int:pk>',views.views,name='views'),

    path('awards/',views.awards,name='awards'),
    path('contact-us/',views.contact_us,name='contact-us'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('db-courses/',views.db_courses,name='db-courses'),
    path('wish-list/',views.wish_list,name='wish-list'),
    path('wish-list-delete/<int:pk>',views.wish_list_delete,name='wish-list-delete'),
    path('db-profile/',views.db_profile,name='db-profile'),
    # path('db-time-line/',views.db_time_line,name='db-time-line'),
    path('departments',views.departments,name='departments'),
    path('event-details',views.event_details,name='event-details'),
    path('event-register/',views.event_register,name='event-register'),
    path('events/',views.events,name='events'),
    path('facilities',views.facilities,name='facilities'),
    path('gallery-photo/',views.gallery_photo,name='gallery-photo'),
    path('research/',views.research,name='research'),
    path('seminar/',views.seminar,name='seminar'),
    path('forpass/',views.forpass,name='forpass'),
    path('payment/paymenthandler/<int:pk>', views.paymenthandler, name='paymenthandler'),
    
    
    path('game1/',views.game1,name='game1'),
    path('game2/',views.game2,name='game2'),
    path('game3/',views.game3,name='game3'),
    path('game4/',views.game4,name='game4'),
    path('game5/',views.game5,name='game5'),
    path('notification/',views.notification,name='notification'),
    
    



]