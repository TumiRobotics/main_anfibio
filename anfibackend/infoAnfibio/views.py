from django.shortcuts import render
from django.http import JsonResponse
from .models import usuariosAnfibio,botesAnfibio, fotosAnfibio, inspecctionInfo
import datetime

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
    if usrContra == usuario_acceso.contra and usuario_acceso.nombre == 'admin':
        print('Se envia la respuesta del admin')
        return JsonResponse({
            'resp':'300'
        })
    elif usrContra == usuario_acceso.contra:
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

def infoFotos(request):
    fotos_totales = fotosAnfibio.objects.all()
    fotos_enviar = []
    for foto in fotos_totales:
        arreglo_fotos = [foto.id,foto.codigoFoto,foto.urlFoto]
        fotos_enviar.append(arreglo_fotos)
    return JsonResponse({
        'fotos':fotos_enviar,
    })

def consultarEstadisticas(request):
    inspecciones_totales = inspecctionInfo.objects.all()
    hora_total = 0.00
    distancia_total = 0.00
    recorridos_totales = 0
    recorridos_totales = len(inspecciones_totales)
    for inspeccion in inspecciones_totales:
        hora_total = hora_total + round(float(inspeccion.duracion),2)
    
    for inspeccion in inspecciones_totales:
        distancia_total = distancia_total + round(float(inspeccion.distancia),2)
    
    return JsonResponse({
        'horas':str(hora_total),
        'distancia':str(distancia_total),
        'recorridos':str(recorridos_totales)
    })

def infoInspecciones(request):
    inspTotal = inspecctionInfo.objects.all().order_by('-id')
    arreglo_enviar = []
    for inspeccion in inspTotal:
        arreglo_insp = [inspeccion.fechaInspeccion,inspeccion.distancia,inspeccion.duracion,inspeccion.codigoBote]
        arreglo_enviar.append(arreglo_insp)
    return JsonResponse({
        'inspecciones':arreglo_enviar
    })

def registrarTrabajo(request):
    duracionTrabajo = request.GET.get('duracion')
    distanciaTrabajo = request.GET.get('distancia')
    fechaRegistro = datetime.datetime.now().strftime('%d-%m-%Y')
    print(duracionTrabajo)
    duracionTrabajo = duracionTrabajo.split(':')
    print(duracionTrabajo)
    duracion = str(round(float(duracionTrabajo[0]) + round(float(duracionTrabajo[1])/60,2),2))
    codigoBote = 'BOT-0001'
    inspecctionInfo(fechaInspeccion=fechaRegistro,distancia=distanciaTrabajo,duracion=duracion,codigoBote=codigoBote).save()
    return JsonResponse({
        'resp':'ok'
    })

#Colocar icono por inspeccion para poder revisar videos y fotos de inspeccion
#Roles de usuario
#Admin
#Adociar videos a inspeccion con botonos y tmb fotos
#Rol de usuario admin, operario
#Acceso de usuario Admin
# --Cerrador
#Iconos de monitoreo (saber si estan prendidos o aplicar funcion
#Guardar los datos finales e iniciales
#Lista de pruebas - App - Integracion con el robot
#Informe Final del software - 18 de Diciembre
#Puntos complementarios Agregar, pantallas, funcionalidades y variables
#Finales
#Tomar Foto - Operador - Tomar FOTO FUNCION

def foto(request,ind):
    fotoVer = fotosAnfibio.objects.get(id=ind)
    return render(request,'infoAnfibio/foto.html',{
        'fotoAnfibio':fotoVer.urlFoto,
    })

#Grabar pocision final e inicial
#Grabar la distancia total recorrida 
#Hacer las pruebas con arduino programado