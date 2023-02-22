from usuarios.models import Empleado

def sesion(request):
    usuario_actual= request.user
    image_user=r"../media/images/usuarios/default.png"
    if request.user.is_authenticated:
        if Empleado.objects.filter(user_id=usuario_actual.id):
            image_user=Empleado.objects.get(user_id=usuario_actual.id).perfil.url
    context={
        'usuario_actual':usuario_actual,
        'image_user': image_user
    }
    return context