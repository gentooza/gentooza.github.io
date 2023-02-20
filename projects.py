# This file is part of Gentooza's web page
#
# Copyright 2021-2023 Joaquín Cuéllar <joa.cuellar (at) riseup (dot) net>
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
    ('industrial', 'Industriales, SCADA, control...'),
    ('social', 'Movimientos sociales'),
    ('hybrid', 'Aplicaciones híbridas para móvil'),
    ('robotics', 'Aplicaciones sobre robótica'),
    ('guides', 'Talleres, manuales, guías...'),
    ('tools', 'Utilidades y otros'),
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

rb1000 = project()
rb1000.title = "SCADA Plastic Rolling Machine"
rb1000.description = "Programa  en C++ basado en <a target=\"_blank\" href=\"https://pvbrowser.de\">pvbrowser</a>, configurado en una pantalla táctil con Debian 7 Wheezy y comunicaciones MODBUS TCP/IP y MODBUS RTU de supervisión de una máquina industrial bobinadora de plástico."
rb1000.savannah = "https://savannah.nongnu.org/projects/rb1000"
rb1000.category = "industrial"
projects.append(rb1000)

gstools = project()
gstools.title = "gStools (Gentooza’s SCADA tools)"
gstools.description = "Es una librería en C de utilidades de uso común en cualquier desarrollo industrial, desde conversión de datos WORD, DINT, REAL… tratamiento de fechas (fecha Juliana), etc."
gstools.github = "https://github.com/gentooza/gStools"
gstools.category = "industrial"
projects.append(gstools)

piresiduos = project()
piresiduos.title = "piResiduos"
piresiduos.description = "En C++, usando como framework <a target=\"_blank\" href=\"https://pvbrowser.de\">pvbrowser</a>, es un programa de gestión local de entrada y salida de material de estaciones de tratamiento o transferencia de Residuos. Conecta con varios dispositivos locales como básculas y cámaras de detección de matrículas, y se sincroniza con un servidor central de administración mediante un túnel SSH."
piresiduos.github = "https://github.com/Pixelada-S-Coop-And/piResiduos2"
piresiduos.category = "industrial"
projects.append(piresiduos)

socias = project()
socias.title = "SociasMercao"
socias.description = "en PHP como módulo de la aplicación ERP <a target=\"_blank\" href=\"https://www.dolibarr.org/\">Dolibarr</a>, módulo de gestión de socias, sus cuotas, crédito, y su aplicación en las compras en tienda. Trabajando dentro del <a target=\"_blank\" href=\"https://latejedora.org\">Mercao Social de Córdoba, La Tejedora.</a>"
socias.savannah = "https://savannah.nongnu.org/projects/sociasmercao/"
socias.category = "social"
projects.append(socias)

maimo = project()
maimo.title = "MaimoNides"
maimo.description = "Mi proyecto final de Máster en Informática Industrial. Es un sistema de publicidad empotrado, en C para implementarse en un Raspberry PI."
maimo.savannah = "https://savannah.nongnu.org/projects/maimonides/"
maimo.doc = "http://repositorio.ual.es:8080/handle/10835/2823"
maimo.category = "tools"
projects.append(maimo)

lhs = project()
lhs.title = "License Header Script"
lhs.description = "Sencillo  script en BASH para automatizar la inserción de la cabecera de licencia en un programa de software libre cualquiera."
lhs.savannah = "https://github.com/gentooza/license_header_script"
lhs.category = "tools"
projects.append(lhs)

quetalk = project()
quetalk.title = "QueTalk"
quetalk.description = "Desarrollado en C++, QXMPP, QT5.  programa descontinuado ya que estaba pensado para ser un cliente de Kontalk en el sistema para móviles de Ubuntu. Fork del programa <a target=\"_blank\" href=\"https://github.com/chloerei/qtalk\">QTalk desarrollado por REI.</a>"
quetalk.savannah = "https://github.com/gentooza/QueTalk"
quetalk.category = "tools"
projects.append(quetalk)

FFMM = project()
FFMM.title = "Freedom Fighters of Might and Magic"
FFMM.description = "Un día me puse a aprender python y pygame y dejé esto a medias :-e un clon apenas planteado del Heroes of Might And Magic II."
FFMM.savannah = "https://github.com/gentooza/Freedom-Fighters-of-Might-Magic"
FFMM.category = "videogames"
projects.append(FFMM)

gsresolver = project()
gsresolver.title = "GSResolver"
gsresolver.description = "Aprendiendo como programar C++ usando plugins, me puse a desarrollar un resolutor de sudokus, es un programa de consola usando ncurses que implementa los algoritmos personalizados de resolución en forma de librerías .so independientes y dinámicamente cargadas en programa."
gsresolver.github = "https://github.com/gentooza/GSResolver"
gsresolver.category = "videogames"
projects.append(gsresolver)

dentaltea = project()
dentaltea.title = "DentalTEA"
dentaltea.description = "Usando typescript, Ionic, y Cordova, aplicación híbrida para las citas al dentista de personas con trastorno autista, para la asociación Autismo Córdoba."
dentaltea.bitbucket = "https://bitbucket.org/pixelada/appautismocordoba/src/master/"
dentaltea.category = "hybrid"
projects.append(dentaltea)

appsem = project()
appsem.title = "semApp"
appsem.description = "Usando typescript, Ionic, y Cordova, aplicación híbrida de carnet virtual de los afiliados de un conocido sindicato andaluz."
appsem.github = "https://github.com/Pixelada-S-Coop-And/SEM-app"
appsem.category = "hybrid"
projects.append(appsem)

soberania = project()
soberania.title = "Guía de alternativas tecnológicas"
soberania.description = "Basada en una guía originalmente de Pixelada, para el <a target=\"_blank\" href=\"https://reasmadrid.org/encuentro-internacional-cordoba/\"> Encuentro Internacional de Economías Transformadoras, en Córdoba 2018</a>, desarrollada actualmetne dentro del <a target=\"_blank\" href=\"https://latejedora.org\"> Mercao Social de Córdoba, La Tejedora</a> , una guía de criterio a colectivos e individuales, de adquisición de programas y hardware informático."
soberania.gitlab = "https://gitlab.com/la-tejedora/soberania-tecnologica"
soberania.category = "guides"
projects.append(soberania)

tallerlicenciado = project()
tallerlicenciado.title = "Taller de licenciado de software libre"
tallerlicenciado.description = "Guión del taller a impartir para el <a target=\"_blank\" href=\"https://www.uco.es/aulasoftwarelibre/\">Aula de Software Libre de la Universidad de Córdoba</a>, el <a target=\"_blank\" href=\"https://ideas.aulasoftwarelibre.uco.es/idea/taller-para-el-licenciado-de-software-libre\"> 15 Marzo de 2022.</a>"
tallerlicenciado.github = "https://github.com/gentooza/taller-licenciado-software"
tallerlicenciado.category = "guides"
projects.append(tallerlicenciado)

bitbloq = project()
bitbloq.title = "Bitbloq Offline Reborn"
bitbloq.description = "Aplicación para la programación local de los robots Zowie de BQ. Con la caída de la empresa y la divisón de su sección robótica ahora sólo ofrecen la versión online de la herramienta y bajo registro. ¡Yo quiero que mis hijos pueda programarlo en un entorno local y seguro!"
bitbloq.github = "https://github.com/gentooza/bitbloq-offline-reborn"
bitbloq.category = "robotics"
projects.append(bitbloq)
