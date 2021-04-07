from django.urls import path
from .views import ( IndexView,
                     BeepView,
                     RFIDView,
                     EMKView,
                     DLPView,
                     SmartDocsView,
                     )   


app_name='dev_com'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('beep/', BeepView.as_view(), name='beep'),
    path('rfid/', RFIDView.as_view(), name='rfid'),
    path('emk/', EMKView.as_view(), name='emk'),
    path('dlp/', DLPView.as_view(), name='dlp'),
    path('smart_docs/', SmartDocsView.as_view(), name='smart_docs'),
]