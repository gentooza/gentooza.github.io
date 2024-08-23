# This file is part of Gentooza's web page
#
# Copyright 2021-2024 Joaquín Cuéllar <joa.cuellar (at) riseup (dot) net>
#
# Gentooza's web page is free software:
# you can redistribute it and/or modify it under the terms of
# the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gentooza's web page is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Gentooza's web page.
# If not, see <https://www.gnu.org/licenses/>.

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

CATEGORIES = (
    ('research', 'Investigación'),
    ('industrial', 'Industriales, SCADA, control...'),
    ('social', 'Movimientos sociales'),
    ('guides', 'Docencia, Talleres, manuales ...'),
    ('tools', 'Utilidades y otros'),
    ('robotics', 'Aplicaciones sobre robótica'),
    ('hybrid', 'Aplicaciones híbridas para móvil'),
    ('videogames', 'Videojuegos!'),
)

class project:
    def __init__(self):
        self.github = ''
        self.savannah = ''
        self.bitbucket = ''
        self.gitlab = ''

        self.title = ''
        self.description = ''

        self.doc = ''
        self.category = ''

projects = []

piresiduos = project()
piresiduos.title = "piResiduos"
piresiduos.description = "<strong> PROYECTO ACTIVO! </strong> En <strong>C++</strong>, usando como framework <a target=\"_blank\" href=\"https://pvbrowser.de\">pvbrowser</a>, es un programa de gestión local de entrada y salida de material de estaciones de tratamiento o transferencia de Residuos. Conecta con varios dispositivos locales como básculas y cámaras de detección de matrículas, y se sincroniza con un servidor central de administración mediante un túnel SSH.<br/>Bajo licencia libre GPLv3+."
piresiduos.github = "https://github.com/gentooza/piResiduos"
piresiduos.category = "industrial"
projects.append(piresiduos)

picomm = project()
picomm.title = "Pixelada Comms Translator"
picomm.description = "En <strong>C++</strong>, usando como framework <a target=\"_blank\" href=\"https://pvbrowser.de\">pvbrowser</a>, es un software que pretende hacer de OPC o capa traductora intermedia, entre comunicaciones industriales modernas y sistemas de supervisión que no los acepten, pero si acepten conexiones a base de datos remotas o de windows tipo ODBC. Mi proyecto final de grado, <strong> matrícula de honor!</strong><br/>Bajo licencia libre GPLv3+."
picomm.github = "https://github.com/Pixelada-S-Coop-And/Pixelada-Comms-Translator"
picomm.category = "industrial"
projects.append(picomm)

rb1000 = project()
rb1000.title = "SCADA Plastic Rolling Machine"
rb1000.description = "Programa en <strong>C++</strong> basado en <a target=\"_blank\" href=\"https://pvbrowser.de\">pvbrowser</a>, configurado en una pantalla táctil con Debian 7 Wheezy y comunicaciones MODBUS TCP/IP y MODBUS RTU de supervisión de una máquina industrial bobinadora de plástico.<br/>Bajo licencia libre GPLv3+."
rb1000.savannah = "https://savannah.nongnu.org/projects/rb1000"
rb1000.github = "https://github.com/gentooza/rbMIL"
rb1000.category = "industrial"
projects.append(rb1000)

gstools = project()
gstools.title = "gStools (Gentooza’s SCADA tools)"
gstools.description = "Es una <strong>librería en C</strong> de utilidades de uso común en cualquier desarrollo industrial, desde conversión de datos WORD, DINT, REAL… tratamiento de fechas (fecha Juliana), etc.<br/>Bajo licencia libre GPLv2+."
gstools.github = "https://github.com/gentooza/gStools"
gstools.category = "industrial"
projects.append(gstools)

conil = project()
conil.title = "Portal Conilhospeda"
conil.description = "<strong> Busco mantenedora/or para este proyecto!!</strong> Usando <strong>Python y Django</strong> Es el <a target=\"_blank\" href=\"https://conilhospeda.com\"> portal web de reservas de la Cooperativa Conilhospeda.</a> Es un proyecto muy bonito que proviene de la <a target=\"_blank\" href=\"https://enreda.coop\">Cooperativa Enreda </a>, paso a manos de <a target=\"_blank\" href=\"https://pixelada.org\">Pixelada</a> y finalmente se mantiene dentro <a target=\"_blank\" href=\"https://elalambre.org\">del Alambre.</a> Se está cobrando un mantenimiento mensual por los trabajos!<br/>Es software privativo (pero tenemos planes de abrirlo!)."
conil.category = "social"
projects.append(socias)

socias = project()
socias.title = "SociasMercao"
socias.description = "En <strong>PHP</strong> como módulo de la aplicación ERP <a target=\"_blank\" href=\"https://www.dolibarr.org/\">Dolibarr</a>, módulo de gestión de socias, sus cuotas, crédito, y su aplicación en las compras en tienda. Trabajando dentro del <a target=\"_blank\" href=\"https://latejedora.org\">Mercao Social de Córdoba, La Tejedora.</a><br/>Bajo licencia libre AGPLv3+."
socias.savannah = "https://savannah.nongnu.org/projects/sociasmercao/"
socias.category = "social"
projects.append(socias)

maimo = project()
maimo.title = "MaimoNides"
maimo.description = "Mi proyecto final de Máster en Informática Industrial en la Universidad de Almería. Es un sistema de publicidad empotrado, <strong>en C</strong> para implementarse <strong>en un Raspberry PI</strong>.<br/>Bajo licencia libre GPLv3+."
maimo.savannah = "https://savannah.nongnu.org/projects/maimonides/"
maimo.doc = "http://repositorio.ual.es:8080/handle/10835/2823"
maimo.category = "tools"
projects.append(maimo)

lhs = project()
lhs.title = "License Header Script"
lhs.description = "Sencillo script en <strong>BASH</strong> para automatizar la inserción de la cabecera de licencia en un programa de software libre cualquiera.<br/>Bajo licencia libre GPLv3+."
lhs.savannah = "https://github.com/gentooza/license_header_script"
lhs.category = "tools"
projects.append(lhs)

quetalk = project()
quetalk.title = "QueTalk"
quetalk.description = "Desarrollado <strong>en C++, QXMPP, QT5</strong>.  programa descontinuado ya que estaba pensado para ser un cliente de Kontalk en el sistema para móviles de Ubuntu. Fork del programa <a target=\"_blank\" href=\"https://github.com/chloerei/qtalk\">QTalk desarrollado por REI.</a><br/>Bajo licencia libre GPLv3+."
quetalk.savannah = "https://github.com/gentooza/QueTalk"
quetalk.category = "tools"
projects.append(quetalk)

FFMM = project()
FFMM.title = "Freedom Fighters of Might and Magic"
FFMM.description = "Un día me puse a aprender <strong>Python y Pygame</strong> y dejé esto a medias :-e un clon apenas planteado del Heroes of Might And Magic II.<br/>Bajo licencia libre GPLv3+."
FFMM.savannah = "https://github.com/gentooza/Freedom-Fighters-of-Might-Magic"
FFMM.category = "videogames"
projects.append(FFMM)

gsresolver = project()
gsresolver.title = "GSResolver"
gsresolver.description = "Aprendiendo como programar <strong>C++</strong> usando plugins, me puse a desarrollar un resolutor de sudokus, es un programa de consola usando ncurses que implementa los algoritmos personalizados de resolución en forma de librerías .so independientes y dinámicamente cargadas en programa.<br/>Bajo licencia libre GPLv3+."
gsresolver.github = "https://github.com/gentooza/GSResolver"
gsresolver.category = "videogames"
projects.append(gsresolver)

dentaltea = project()
dentaltea.title = "DentalTEA"
dentaltea.description = "Usando <strong>Typescript, Ionic, y Cordova</strong>, aplicación híbrida para las citas al dentista de personas con trastorno autista, para la asociación Autismo Córdoba. <br/>Bajo licencia libre GPLv3+."
dentaltea.bitbucket = "https://bitbucket.org/pixelada/appautismocordoba/src/master/"
dentaltea.category = "hybrid"
projects.append(dentaltea)

appsem = project()
appsem.title = "semApp"
appsem.description = "Usando <strong>Typescript, Ionic, y Cordova</strong>, aplicación híbrida de carnet virtual de los afiliados de un conocido sindicato andaluz.<br/>Bajo licencia libre GPLv3+."
appsem.github = "https://github.com/Pixelada-S-Coop-And/SEM-app"
appsem.category = "hybrid"
projects.append(appsem)

mpich = project()
mpich.title = "Entorno para pŕacticas con MPICH bajo docker"
mpich.description = "Basado en el trabajo de <a target=\"_blank\" href=\"https://github.com/NLKNguyen/alpine-mpich\"> N. Nguyen </a>, he actualizado y modificado una imagen y un clúster de Alpine GNU/Linux en docker, para poder realizar prácticas de Arquitecturas Paralelas, asignatura de 3º del Grado de Informática en su mención de <strong> Arquitectura de Computadores </strong>, Arquitecturas Paralelas, para poder emplear con mínimo esfuerzo, <strong> C y MPICH <strong> y realizar prácticas de programación distribuida pudiendo medir recursos y tiempo de cómputo con un hardware simulado pero limitado.<br/>Bajo licencia libre MIT."
mpich.github = "https://github.com/gentooza/alpine-mpich"
mpich.doc = "https://ieeexplore.ieee.org/document/7868429"
mpich.category = "guides"
projects.append(mpich)

soberania = project()
soberania.title = "Guía de alternativas tecnológicas"
soberania.description = "Basada en una guía originalmente de Pixelada, para el <a target=\"_blank\" href=\"https://reasmadrid.org/encuentro-internacional-cordoba/\"> Encuentro Internacional de Economías Transformadoras, en Córdoba 2018</a>, desarrollada actualmetne dentro del <a target=\"_blank\" href=\"https://latejedora.org\"> Mercao Social de Córdoba, La Tejedora</a> , una guía de criterio a colectivos e individuales, de adquisición de programas y hardware informático. Se ha empleado recientemente en el <a target=\"_blank\" href=\"https://cfp.us.es/cursos/mu/politicas-y-practicas-para-un-desarrollo-humano-sostenible\"> Máster de Políticas Y Prácticas para un Desarrollo Humano Sostenible 2024</a>.<br/>Bajo licencia libre CC-BY."
soberania.gitlab = "https://gitlab.com/la-tejedora/soberania-tecnologica"
soberania.category = "guides"
projects.append(soberania)

tallerlicenciado = project()
tallerlicenciado.title = "Taller de licenciado de software libre"
tallerlicenciado.description = "Guión del taller a impartir para el <a target=\"_blank\" href=\"https://www.uco.es/aulasoftwarelibre/\">Aula de Software Libre de la Universidad de Córdoba</a>, el <a target=\"_blank\" href=\"https://ideas.aulasoftwarelibre.uco.es/idea/taller-para-el-licenciado-de-software-libre\"> 15 Marzo de 2022.</a><br/>Bajo licencia libre GPLv3+."
tallerlicenciado.github = "https://github.com/gentooza/taller-licenciado-software"
tallerlicenciado.category = "guides"
projects.append(tallerlicenciado)

bitbloq = project()
bitbloq.title = "Bitbloq Offline Reborn"
bitbloq.description = "Aplicación para la programación local de los robots Zowie de BQ. Con la caída de la empresa y la divisón de su sección robótica ahora sólo ofrecen la versión online de la herramienta y bajo registro. ¡Yo quiero que mis hijos pueda programarlo en un entorno local y seguro!Bajo licencia libre GPLv3+."
bitbloq.github = "https://github.com/gentooza/bitbloq-offline-reborn"
bitbloq.category = "robotics"
projects.append(bitbloq)

tock = project()
tock.title = "Investigación en mi tésis doctoral"
tock.description = "No tengo nada bajo licencia libre, pero trabajo destripando <a target=\"_blank\" href=\"https://tockos.org/\">Tock OS</a>, un sistema desarrollado puramente en <strong> Rust </strong> para sistemas empotrados, me interesa medir tiempos de cómputo empleando diversos lenguajes de programación en la capa de aplicación, distintos algoritmos... Migrarlo a Risc-V para los esp32-C3 y esp32-c6... A ver a donde me lleva esto :-D"
tock.github = "https://github.com/tock/tock"
tock.category = "research"
projects.append(tock)
