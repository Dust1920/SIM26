# Sistema de Indicadores Municipales.

A través del Sistema Nacional de Información Estadística y Geográfica (SNIEG), el Instituto Nacional de Estadística y Geografía (INEGI), pone a disposición de los gobiernos estatal y municipales de Sonora el Sistema de Indicadores Municipales (SIM), que contiene datos estadísticos y geográficos que permiten elaborar diagnósticos situacionales y favorecen el seguimiento a los Planes Estatales y Municipales de Desarrollo, documentos rectores de las acciones y políticas públicas que llevarán a cabo las autoridades en el periodo de gestión.

El objetivo de esta herramienta es que los usuarios interesados accedan a información actualizada y oportuna de acuerdo con la Norma Técnica de Datos Abiertos. La información proviene de fuentes de datos oficiales obtenidos a través de censos, encuestas y registros administrativos. 

La temática abordada gira en torno a: composición territorial, ubicación geográfica, dinámica poblacional, estructura de la población, grupos vulnerables, hechos vitales, salud, educación, medio ambiente, hogares y viviendas, entorno urbano, vehículos de motor registrados en circulación, accidentes de tránsito, seguridad, infraestructura, economía y finanzas municipales. Por la parte geográfica se incluyen Shapes relacionados con: climas, temperatura, precipitación, áreas naturales protegidas, orografía, fisiografía, geología, hidrología, vegetación, reforestación, uso potencial agrícola y pecuario, y demás.

Adicionalmente, se incluyen los principales resultados por Área Geoestadística Básica (AGEB) y manzana urbana, así como accesos directos para la descarga de QGIS y el Mapa Digital de México; así, los usuarios interesados disponen de los elementos necesarios para realizar el procesamiento y visualización de los datos geográficos.

(Información extraida de la presentación del SIM)

## Próposito
Se pretende, a partir del SIM, crear una base de datos referente a los indicadores mencionados de cada municipio para ser utilizada a futuro según sea conveniente. 

## Descarga de Datos
El tablero esta sobre Power BI. Lo que dificultó su descarga de forma programática, por lo que, por el momento, se descargaron de forma manual. Se espera más adelante anexar la forma prográmatica. 

(1) Tablero de Datos SIM: https://app.powerbi.com/view?r=eyJrIjoiOTczYWE5N2UtM2Q1MS00OGU4LWEwZjItOTI4Y2YwNDkzOWQzIiwidCI6ImNhOGYwOWY1LTMzNWUtNGZjNS04MDQxLWY1YjQ3MmEwMmVlZiIsImMiOjR9

(2) SCEINE 2010, Sonora : https://www.inegi.org.mx/app/descarga/?ti=13&ag=00

(3) Marco Geoestadistico : https://www.inegi.org.mx/temas/mg/#descargas
## Base de Datos

Una vez tenemos los datos en sus tablas tidy. Vamos a agruparlos de el tipo de dato. Según los indicadores tenemos dos:
* Absoluto: Valor Medido. 
* Porcentual: Valor Medido con respecto al total. 

Entonces crearemos dos bases de datos, una por cada tipo. 





