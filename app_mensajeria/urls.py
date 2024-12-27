from django.urls import path
import app_mensajeria.views as vw

urlpatterns = [
    path('enviar-mensaje', vw.enviar_mensaje, name="enviar-mensaje"),
    path('mostrar-mensajes', vw.mostrar_mensajes, name="mostrar-mensajes"),

]