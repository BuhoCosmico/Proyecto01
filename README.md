# <h1 align=center> **PROYECTO** </h1>

# <h1 align=center>**`Data Engineering`**</h1>


Bienvenidos a este primer proyecto (que subo a github) de  ***Data Engineer***. 

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

`Application Programming Interface`  es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## Rol a desarrollar

Elaborar las *transformaciones* requeridas y disponibilizar los datos mediante la *elaboración y ejecución de una API*.



## **Trabajo**

**`Transformaciones`**:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:  Para disponibilizar los datos utilizo el framework ***FastAPI***. Para realizar las siguientes consultas a los Datasets:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>


**`Deployment`**: Uso [Deta Cloud](https://www.deta.sh/?ref=fastapi) para realizar el deploy de la aplicacion.
<br/>

## **Tecnologias utilizadas para cada instancia**

+ Tratamiento/limpieza: En esta ocasion utilice una libreria de Python  llamada Pandas

+ Creacion de la API: Se utilizo Fastapi

+ Deployment: Deta Cloud

## **Fuente de datos**

+ Los archivos sin limpiar son aquellos cuyo formato es CSV y no presentan la palabra 'limpio' en su titulo, podran encontrarlos en este mismo repositorio.

+ En el archivo llamado proyecto.ipynb podran encontrar el tratamiento de estos datasets y los mismos con sus respectivas limpiezas presentan en su titulo la palabra 'limpio'

+ En el archivo main.py se encuentra el montaje de la API

<br/>

## **Documentacion para la elaboracion**

Imagen Docker con Uvicorn para aplicaciones web de alta performance:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 


FAST API Documentacion:

+ https://fastapi.tiangolo.com/tutorial/


DETA CLOUD Documentacion:

+ https://fastapi.tiangolo.com/deployment/deta/
+ https://docs.deta.sh/docs/home

## **Link del proyecto finalizado**

+  https://1atxu9.deta.dev/docs#/