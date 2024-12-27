from django.urls import path
import myapp.views as vw

urlpatterns = [
    path('', vw.inicio, name="inicio"),

    path('logueo/', vw.vista_logueo, name="logueo"),
    path('deslogueo/', vw.vista_deslogueo, name="deslogueo"),
    path('registro/', vw.vista_registro, name="registro"),
    path('perfil-usuario/', vw.vista_perfil_usuario, name="perfil-usuario"),
    path('editar-perfil/', vw.vista_editar_perfil, name="editar-perfil"),
    path('cambiar-clave-usuario/', vw.cambiar_clave_usuario, name="cambiar-clave-usuario"),

    #    path('componentes/', vw.componentes, name="componentes"),
    path('componentes/', vw.ComponenteListView.as_view(), name="componentes"),
    path('colaboradores/', vw.ColaboradorListView.as_view(), name="colaboradores"),
    path('sedes/', vw.SedeListView.as_view(), name="sedes"),

    #path('componente-formulario/', vw.formulario_componentes_api, name="componentes-formulario"),
    path('componente-formulario/', vw.ComponenteCreateView.as_view(), name="componente-formulario"),
    path('sede-formulario/', vw.SedeCreateView.as_view(), name="sede-formulario"),
    path('colaborador-formulario/', vw.ColaboradorCreateView.as_view(), name="colaborador-formulario"),

    path('componente-eliminar/<int:pk>', vw.ComponenteDeleteView.as_view(), name="componente-eliminar"),
    path('sede-eliminar/<int:pk>', vw.SedeDeleteView.as_view(), name="sede-eliminar"),
    path('colaborador-eliminar/<int:pk>', vw.ColaboradorDeleteView.as_view(), name="colaborador-eliminar"),

    path('componente-editar/<int:pk>', vw.ComponenteUpdateView.as_view(), name="componente-editar"),
    path('sede-editar/<int:pk>', vw.SedeUpdateView.as_view(), name="sede-editar"),
    path('colaborador-editar/<int:pk>', vw.ColaboradorUpdateView.as_view(), name="colaborador-editar"),

    path('componente-detalle/<int:pk>', vw.ComponenteDetailView.as_view(), name="componente-detalle"),
    path('colaborador-detalle/<int:pk>', vw.ColaboradorDetailView.as_view(), name="colaborador-detalle"),
    path('sede-detalle/<int:pk>', vw.SedeDetailView.as_view(), name="sede-detalle"),

    path('acerca_de_nosotros/', vw.acerca_de_nosotros, name="acerca_de_nosotros"),

]