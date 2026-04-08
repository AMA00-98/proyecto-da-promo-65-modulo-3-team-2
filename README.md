##  Proyecto Final Módulo 3 | Equipo CORE CONSULTING
📊 ABC CORPORATION

<img width="250" height="850" alt="logo_atomo" src="https://github.com/user-attachments/assets/efdb57ee-6275-45d5-9ec9-01aac565e7dc" />

## 👥 Nuestro Equipo
Core Consulting nace de la especialización y el análisis crítico de nuestras integrantes:

- **CO** - Colaboración estratégica: Ana Marín & Valeria Mora
- **RE** - Retención y Diagnóstico:  Janira Sánchez, Laura Mulero y Lorena Serra

##  Descripción del Proyecto
Este proyecto ha sido diseñado para transformar datos crudos de Recursos Humanos en una herramienta estratégica de toma de decisiones a través de la auditoría y limpieza de un dataset de 1,476 empleados, hemos identificado los patrones críticos que impulsan la rotación de personal en ABC Corporation, proponiendo un enfoque integral que equilibra la eficiencia operativa con el bienestar del capital humano.

##  Metodología de Datos (EDA)
El proyecto aborda el ciclo de vida del dato con un enfoque de calidad total:

1. Auditoría y Diagnóstico (EDA): Identificación de nulos y eliminación de duplicados para garantizar una base de estudio única y veraz.

2. Transformación y Limpieza: Eliminación de ruido estadístico (columnas constantes como Over18 o StandardHours).

3. Estandarización: Normalización de textos y corrección de errores tipográficos críticos.

4. Imputación Inteligente: Uso de mediana para variables numéricas (salarios, edad) y moda específica por puesto para variables operativas (BusinessTravel, OverTime).

##  Dimensiones de Análisis Estratégico
Hemos desarrollado tres ejes de visualización y consulta para resolver retos de negocio:

##  Estructura Salarial 
Análisis de la vulnerabilidad en perfiles Junior. Identificamos que la limitación salarial y la falta de incentivos ligados al desempeño son los principales motores de salida en las primeras etapas de la carrera.

![rotación_sueldo](https://github.com/user-attachments/assets/8ec46934-d530-4917-b003-fc8b7f54d374)         ![overtime_sueldo](https://github.com/user-attachments/assets/1bf9de9b-3521-4f76-8a83-7128ddca19ea)


##  Análisis de Bienestar
Detección de puntos de quiebre mediante el análisis de Horas Extra y Work-Life Balance. Los datos confirman que el agotamiento físico y la falta de flexibilidad incrementan significativamente la probabilidad de renuncia.

<img width="1247" height="510" alt="Sin título" src="https://github.com/user-attachments/assets/ab5b20ee-0402-427b-8c0e-3e0058f21817" />


##  Diagnóstico de falta de promoción
Un sistema de diagnóstico que cruza el estancamiento profesional (años sin promoción) con la satisfacción del entorno, permitiendo a la organización predecir fugas de talento clave.

<img width="854" height="553" alt="image" src="https://github.com/user-attachments/assets/7024f4f6-9dfa-4f32-84dc-7194137f0ef1" />

## Estructura del Repositorio
**Carpeta Files:**
- Hr.csv: CSV RR.HH original proporcionado por ABC Corporation.
- Hr_clean.csv: CSV tras la depuración.
  
**Carpeta SRC:**
 _pycache_:
- Clase_Bienestar.py : métodos para visualizaciones del foco satisfacción 
- Soporte_visualizaciones.py : métodos para visualizaciones del foco economico

**Externo: Fase 1 y 2_proyect_mod3.ipynb**
- Documentación del proceso de transformación, gestión de nulos y estandarización.
  
**Externo: Fase3.visualizaciones proyecto mod 3.ipynb**
- Gráficos y dashboards que representan la correlación entre satisfacción, salario y rotación.

**Externo: Reporte:**
- Informe ejecutivo detallando los hallazgos de las Fases 1, 2 y 3.

## Herramientas y Tecnologías
1. Excel / CSV – Formato de entrada de los datos de Recursos Humanos.
3. Python – Lenguaje principal para análisis y transformación de datos.
8. Jupyter Notebook – Documentación interactiva del análisis paso a paso.
5. Archivos .py – Definición de clases, estructuración del código y modularización del proyecto.
6. Pandas – Manipulación y limpieza de datasets.
7. NumPy – Cálculos estadísticos y manejo de datos numéricos.
8. Matplotlib / Seaborn – Visualización de datos y análisis exploratorio.
9. SQL – Consulta, extracción y gestión de datos desde bases de datos relacionales.
10. Git / GitHub – Control de versiones y repositorio del proyecto.
   
##  Conclusiones
El análisis de Core Consulting ha permitido transformar filas de datos en una hoja de ruta para la sostenibilidad organizacional:

Sinergia de Factores: La rotación no es una causa aislada; responde a una combinación de estancamiento en el rol y exceso de carga laboral.

Cultura de Datos: La etapa de "Auditoría de Salud de Datos" fue crucial. Aprendimos que sin una limpieza ética, las decisiones de RR.HH. se basarían en sesgos e información.

Visión Estratégica: Al alinear la eficiencia operativa con condiciones laborales sostenibles, ABC Corporation no solo reduce costes de contratación, sino que fortalece su compromiso a largo plazo.
