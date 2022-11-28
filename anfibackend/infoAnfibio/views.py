from django.shortcuts import render
from django.http import JsonResponse
from .models import usuariosAnfibio,botesAnfibio

# Create your views here.
def infoUsuarios(request):
    usuarios_totales = usuariosAnfibio.objects.all()
    usuarios_enviar = []
    for usuario in usuarios_totales:
        usr_datos = [usuario.nombre,usuario.apellido,usuario.codigoUsr,usuario.urlFoto,usuario.usuario]
        usuarios_enviar.append(usr_datos)
    return JsonResponse({
        'usuarios':usuarios_enviar,
    })

def datosUsuario(request):
    usuario_codigo = request.GET.get('codigo')
    print(usuario_codigo)
    usuario_info = usuariosAnfibio.objects.get(codigoUsr=usuario_codigo)
    informacio_usuario = [usuario_info.nombre,usuario_info.apellido,usuario_info.usuario,usuario_info.codigoUsr,usuario_info.urlFoto]
    return JsonResponse({
        'info':informacio_usuario
    })

def crearUsuario(request):
    nombreUsr = request.GET.get('nombre')
    apelllidoUsr = request.GET.get('apellido')
    celularUsr = request.GET.get('celular')
    emailUsr = request.GET.get('email')
    contraUsr = request.GET.get('contra')
    print(nombreUsr)
    print(apelllidoUsr)
    print(celularUsr)
    print(emailUsr)
    print(contraUsr)
    usuariosAnfibio(nombre=nombreUsr,apellido=apelllidoUsr,nroCelular=celularUsr,email=emailUsr,contra=contraUsr).save()
    usr_mod = usuariosAnfibio.objects.get(nombre=nombreUsr)
    usr_mod.usuario = usr_mod.nombre.lower()
    usr_mod.save()
    codUsr = str(usr_mod.id)
    while len(codUsr) < 4:
        codUsr = '0' + codUsr
    usr_mod.codigoUsr = 'OP-' + codUsr
    usr_mod.save()
    return JsonResponse({
        'respuesta':'Ok',
    })

def accederUsuario(request):
    usrCodigo = request.GET.get('codigo')
    usrContra = request.GET.get('contra')
    print(usrCodigo)
    print(usrContra)
    usuario_acceso = usuariosAnfibio.objects.get(codigoUsr=usrCodigo)
    print(usuario_acceso.contra)
    if usrContra == usuario_acceso.contra:
        return JsonResponse({
            'resp':'200'
        })
    else:
        return JsonResponse({
            'resp':'100'
        })
    
def infoBoats(request):
    botes_totales = botesAnfibio.objects.all()
    botes_enviar = []
    for bote in botes_totales:
        arreglo_bote = [bote.codigoBote,bote.urlBote]
        botes_enviar.append(arreglo_bote)
    return JsonResponse({
        'boats':botes_enviar,
    })