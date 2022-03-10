# This file is part of Gentooza's web page
#
# Copyright 2021-2022, Joaquín Cuéllar <joa.cuellar (at) riseup (dot) net>
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
    ('guides', 'Talleres, manuales, guías...'),
    ('tools', 'Utilidades y otros'),
    ('videogames', 'Videojuegos!'),
)

class project:
    def __init__(self):
        self.github = ''
        self.savannah = ''
        self.bitbucket = ''

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

