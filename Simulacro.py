# Hacer un programa que sea un juego de preguntas y respuestas.
# Capitales del mundo.
# Tienes que mostrarnos de forma aleatoria 10 preguntas de 20 posibles almacenadas.
# El programa tiene que ser indiferente a insertarlo en mayúsculas o minúsculas.
# Al final nos tiene que mostrar la cantidad de respuestas correctas.
# Al inicio tenemos que insertar un nombre de usuario.
# Al final del juego nos tiene que guardar en un archivo, el nombre del usuario, 
# la fecha y hora que ha jugado y la puntuación obtenida, también las respuestas erróneas cometidas.

# LISTADO CON LOS PAÍSES Y CAPITALES DEL MUNDO (por orden alfabético)

paises["Afganistan","Albania","Alemania","Andorra","Angola","Antigua y Barbuda","Arabia Saudita","Argelia","Argentina","Armenia","Australia","Austria","Azerbaiyan","Bahamas","Banglades","Barbados","Barein","Belgica","Belice","Benin","Bielorrusia","Birmania","Bolivia","Bosnia y Herzegovina","Botsuana","Brasil","Brunei","Bulgaria","Burkina Faso","Burundi","Butan","Cabo Verde","Camboya","Camerun","Canada","Catar","Chad","Chile","China","Chipre","Ciudad Vaticano","Colombia","Comoras","Corea Norte","Corea Sur","Costa de Marfil","Costa Rica","Croacia","Cuba","Dinamarca","Dominica","Ecuador","Egipto","El Salvador","Emiratos Arabes Unidos","Eritrea","Eslovaquia","Eslovenia","España","Estados Unidos","Estonia","Etiopia","Filipinas","Finlandia","Fiyi","Francia","Gabon","Gambia","Georgia","Ghana","Granada","Grecia","Guatemala","Guyana","Guinea","Guinea-Bisau","Guinea Ecuatorial","Haiti","Honduras","Hungria","India","Indonesia","Irak","Iran","Irlanda","Islandia","Islas Marshall","Islas Salomon","Israel","Italia","Jamaica","Japon","Jordania","Kazajistan","Kenia","Kirguistan","Kiribati","Kuwait","Laos","Lesoto","Letonia","Libano","Liberia","Libia","Liechtenstein","Lituania","Luxemburgo","Madagascar","Malasia","Malaui","Maldivas","Mali","Malta","Marruecos","Mauricio","Mauritania","Mexico","Micronesia","Moldavia","Monaco","Mongolia","Montenegro","Mozambique","Namibia","Nauru","Nepal","Nicaragua","Niger","Nigeria","Noruega","Nueva Zelanda","Oman","Paises Bajos","Pakistan","Palaos","Panama","Papua Nueva Guinea","Paraguay","Peru","Polonia","Portugal","Reino Unido de Gran Bretaña e Irlanda de Norte","Republica Centroafricana","Republica Checa","Republica de Macedonia","Republica de Congo","Republica Democratica de Congo","Republica Dominicana","Republica Sudafricana","Ruanda","Rumania","Rusia","Samoa","San Cristobal y Nieves","San Marino","San Vicente y las Granadinas","Santa Lucia","Santo Tome y Principe","Senegal","Serbia","Seychelles","Sierra Leona","Singapur","Siria","Somalia","Sri Lanka","Suazilandia","Sudan","Sudan de Sur","Suecia","Suiza","Surinam","Tailandia","Tanzania","Tayikistan","Timor Oriental","Togo","Tonga","Trinidad y Tobago","Tunez","Turkmenistan","Turquia","Tuvalu","Ucrania","Uganda","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Yibuti","Zambia","Zimbabue"]
capitales["Kabul","Tirana","Berlin","Andorra la Vieja","Luanda","Saint Johns","Riad","Argel","Buenos Aires","Erevan","Camberra","Viena","Baku","Nasau","Daca","Bridgetown","Manama","Bruselas","Belmopan","Porto Novo y Cotonu","Minsk","Naipyido","Sucre","Sarajevo","Gaborone","Brasilia","Bandar Seri Begawan","Sofia","Uagadugu","Buyumbura","Timbu","Praia","Nom Pen","Yaunde","Ottawa","Doha","Yamena","Santiago de Chile","Pekin","Nicosia","Ciudad Vaticano","Bogota","Moroni","Pionyang","Seul","Yamusukro","San Jose","Zagreb","La Habana","Copenhague","Roseau","Quito","El Cairo","San Salvador","Abu Dabi","Asmara","Bratislava","Liubliana","Madrid","Washington DC","Tallin","Adis Abeba","Manila","Helsinki","Suva","Paris","Libreville","Banjul","Tiflis","Acra","Saint George","Atenas","Ciudad de Guatemala","Georgetown","Conakri","Bisau","Malabo","Puerto Principe","Tegucigalpa","Budapest","Nueva hi"," Yakarta","Bagdad","Teheran","Dublin","Reikiavik","Majuro","Honiara","Jerusalen","Roma","Kingston ","Tokio","Aman","Astana","Nairobi","iskek","Tarawa","Kuwait","Vientian","Maseru","Riga","Beirut","Monrovia","Tripoli","Vaduz","Vilna","Luxemburgo","Antananarivo","Kuala Lumpur","Lilongüe","Male","Bamako","La Valeta","Rabat","Port-Louis","Nuakchot","Ciudad de Mexico","Palikir","Chisinau","Monaco","Ulan Bator","Podgorica","Maputo","Windhoek","Yaren","Katmandu","Managua","Niamey","Abuya","Oslo","Wellington","Mascate","Amsterdam","Islamabad","Melekeok","Panama","Port Moresby","Asuncion","Lima","Varsovia","Lisboa","Londres","Bangui","Praga","Skopie","Brazzaville","Kinsasa","Santo Domingo","Bloemfontein, Ciudad de Cabo y Pretoria","Kigali","Bucarest","Moscu","Apia","Basseterre","San Marino","Kingstown","Castries","Santo Tome","akar","Belgrado"," Victoria","Freetown","Singapur","Damasco","Mogadiscio"," Sri Jayewardenepura (cap.admva) y Colombo (cap.comercial)","Babane y Lobamba","Jartum","Yuba","Estocolmo","Berna","Paramaribo","Bangkok","Dodoma","Dusambe","Dili","Lome","Nukualofa","Puerto España","Tunez","Asjabad","Ankara","Fongafale","Kiev","Kampala","Montevideo","Taskent","Port Vila","Caracas","Hanoi","Sana","Yibuti","Lusaka","Harare"]

import random
