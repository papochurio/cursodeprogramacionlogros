introduccion = input("nos encontramos en el 2012, un mundo post apocliptico donde la viruela del mono a acabado con la mayoria de supervivientes, te encuentras en la zona mas alta de un edificio( el techo ) de 4 pisos ¿Quieres bajar o no bajar? . ")
a = "bajar"
b = "no bajar"
if introduccion == a:
    continuar = input("Bajas al cuarto piso y tienes la posibilidad de obtener un objeto, cual escoges: bate o barra de acero")
c = "bate"
d = "barra de acero"
if introduccion == b:
    continuar = print("se te acabaron los recursos y moriste d hambre")

if continuar == c:
    continuar = input("¡Buena idea!, vuelves a bajar otro piso y debes romper un cristal. ¿Que haces: golpe o no?")
e = "golpe"
f = "no"
if continuar == d:
    continuar = input("¡Gran opcion!, vuelves a bajar pero te tropiezas y te cortas con la barra, deberas buscar una cura ya que estaba oxidada, tienes 2 opciones: dejar la barra o seguir")
g = "dejar la barra"
h = "seguir"
if  continuar == e:
    continuar = input("Logras romper el cristal y te encuentras con supervivientes. ¿Que haces: saludar o esconder?")
i = "esconder"
j = "saludar"
if continuar == f:
    continuar = input("Buscaste otra salida, pero al final rompiste el cristal, tienes 2 opciones: saludar o esconder")
i = "esconder"
j = "saludar"
if continuar == i:
    terminal = print("te escondes hasta que se fueron y sobreviviste")
if continuar == j:
    terminal = print("te ignoran y sigues caminando, hasta que se te tiran encima y mueres")
g = "dejar la barra"
h = "seguir"
if continuar == g:
    continuar = print("al no tener la barra no pudiste romper el cristal, y al regresar por ella era muy tarde, falleces por el veneno del oxido")
if continuar == h:
    continuar = input("Logras romper el cristal y te encuentras con supervivientes. ¿Que haces: saludar o esconder?")
if continuar == i:
    continuaar = print("al esconderte el veneno hizo efecto y moriste antes de darte cuenta")
if continuar == j:
    continuar = print("te ignoran y sigues caminando, hasta que se te tiran encima logras acabarlos y encuentras un botiquin, ¡¡congratulacion!!")
    
else:
    final = print("juego terminado")
    
