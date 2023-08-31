#Calculo posición si existe un elemento en una lista:

texto=["Brett","Kavanaugh","se","encuentra","a","un","paso","del","Tribunal","Supremo.","Tras","una","batalla","monumental","por","la","nominación","del","juez","conservador,","a","raíz","de","varias","acusaciones","de","abusos","sexuales,","el","Senado","votó","este","viernes","a","favor","de","llevar","su","confirmación","al","voto","final","del","pleno.","Dos","de","los","tres","senadores","republicanos","menos","convencidos,","como","Jeff","Flake","y","Susan","Collins,","dieron","su","sí,","al","igual","de","un","demócrata","de","West","Virginia,","Joe","Manchin.","En","el","día","en","que","se","cumple","un","año","del","nacimiento","del","movimiento","#Metoo","contra","el","acoso,","Estados","Unidos","impulsa","como","nuevo","miembro","vitalicio","de","su","más","alta","instancia","judicial","a","un","hombre","irremediablemente","manchado","por","las","dudas","y","el","partidismo."]
contador=0
cantidad=0
palabra= input("Inserte una palabra a buscar:\n")
for x in texto:
   
    if x == palabra:
         # break
        cantidad=cantidad+1
        print("'"+palabra+"' esta en la posicion "+ str(contador))
    contador=contador+1
#Cuantas veces esta un elemento en un lista

for x in texto:
    if x == palabra:
        contador=contador+1
print("'"+palabra+"' esta "+ str(cantidad)+ " veces en la lista")
