def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["Avatar"] = avatar[cantidadDeAvatares-1].imagen.url 
    
    #return HttpResponse("Esto es una prueba del inicio")

    return render(request,'AppMedica/inicio.html')



def inicio(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    
    return render(request, 'AppMedica/inicio.html',{"url":avatares[0].imagen.url})