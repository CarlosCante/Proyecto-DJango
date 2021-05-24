from django.shortcuts import render_to_response

def login(request):
    return render_to_response("index.html")

def Pagina_Principal(request):
    return render_to_response("Principal.html")

def Registro_Usuario(request):
    return render_to_response("Registro.html")

