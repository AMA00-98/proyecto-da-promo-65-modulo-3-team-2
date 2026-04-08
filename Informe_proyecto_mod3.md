# Módulo 3: Proyecto ABC Corporation 
**Equipo:** Core Consulting 

**Integrantes:** Ana Marín, Janira Sánchez, Laura Mulero, Lorena Serra y Valeria Mora.

**Materia:** Data Analytics


# Introducción
Los datos analizados en el presente proyecto provienen de un archivo en formato CSV proporcionado por la empresa ABC Corporation. 

Esta base de datos contiene información detallada sobre el capital humano de la organización, incluyendo variables relacionadas con la retención de empleados.

# Objetivo General
El objetivo de este informe es analizar de manera integral la rotación de personal mediante la transformación y validación de un dataset de Recursos Humanos, evolucionando desde datos con ruido e inconsistencias hacia una fuente confiable de información.

A partir de este proceso, se busca identificar los principales factores que impactan la deserción y generar insights estratégicos que permitan a la organización mejorar la retención del talento, optimizar la toma de decisiones y fortalecer la sostenibilidad del capital humano.


# Glosario de columnas

**Age (Edad)** – Edad del empleado en años.

**Attrition (Deserción)** – Indica si el empleado ha dejado la empresa. Valores posibles: Sí, No.

**Business Travel (Viajes de negocios)** – Frecuencia de viajes por trabajo. Valores posibles: Nunca, Poco, Frecuente.

**Department (Departamento)** – Área de trabajo del empleado. Valores posibles: Ventas, Tecnología de la información, Recursos humanos.

**Distance From Home (Distancia desde casa)** – Distancia en millas entre la residencia del empleado y la empresa.

**Education (Educación)** – Nivel educativo del empleado. Valores posibles: 1: Educación básica, 2: Educación secundaria, 3: Licenciatura, 4: Maestría, 5: Doctorado.
**Education Field (Campo de educación)** – Especialidad educativa del empleado. Valores posibles: Ciencias de la vida, Marketing, Finanzas, Recursos humanos, Ingeniería, Médica, Otro.

**Employee Number (Número de empleado)** – Identificador único de cada empleado dentro de la empresa.

**Environment Satisfaction (Satisfacción con el entorno)** – Nivel de satisfacción con el ambiente laboral. Valores posibles: 1: Bajo, 2: Medio, 3: Alto, 4: Muy alto.
**Gender (Género)** – Género del empleado. Valores posibles: Masculino, Femenino.

**Job Involvement (Involucramiento en el trabajo)** – Nivel de compromiso con las responsabilidades laborales. Valores posibles: 1: Bajo, 2: Medio, 3: Alto, 4: Muy alto.

**Job Level (Nivel de puesto)** – Jerarquía o rango del puesto dentro de la empresa. Valores posibles: 1, 2, 3, 4, 5.

**Job Role (Rol laboral)** – Puesto específico del empleado dentro de la empresa. Valores posibles: Representante de ventas, Gerente de ventas, Ingeniero de software, Analista de datos, Especialista en recursos humanos, Investigador científico, Gerente de proyecto, Otro.

**Job Satisfaction (Satisfacción en el trabajo)** – Nivel de satisfacción del empleado con su puesto. Valores posibles: 1: Bajo, 2: Medio, 3: Alto, 4: Muy alto.
**Marital Status (Estado civil)** – Estado civil del empleado. Valores posibles: Soltero, Casado, Divorciado.

**Monthly Income (Ingresos mensuales)** – Salario mensual del empleado en la moneda de la empresa.

**Num Companies Worked (Número de empresas en las que trabajó)** – Cantidad de empresas anteriores en las que el empleado ha trabajado.

**Over Time (Horas extra)** – Indica si el empleado realiza horas extra regularmente. Valores posibles: Sí, No.

**Percent Salary Hike (Porcentaje de aumento salarial)** – Incremento porcentual en el salario en el último ajuste.
**Performance Rating (Calificación de desempeño)** – Evaluación del desempeño del empleado. Valores posibles: 1: Bajo, 2: Bueno, 3: Excelente, 4: Superior.

**Relationship Satisfaction (Satisfacción en las relaciones)** – Nivel de satisfacción del empleado con sus relaciones laborales. Valores posibles: 1: Bajo, 2: Medio, 3: Alto, 4: Muy alto.

**Stock Option Level (Nivel de opciones de acciones)** – Nivel de participación del empleado en planes de opciones de acciones. Valores posibles: 0, 1, 2, 3.

**Total Working Years (Total de años trabajados)** – Experiencia laboral total del empleado en años.

**Training Times Last Year (Capacitaciones el año pasado)** – Número de cursos, entrenamientos o talleres realizados en el último año.

**Work Life Balance (Equilibrio vida-trabajo)** – Nivel de balance entre la vida personal y laboral del empleado. Valores posibles: 1: Bajo, 2: Bueno, 3: Mejor, 4: Excelente.

**Years At Company (Años en la compañía)**– Cantidad de años que el empleado lleva trabajando en la empresa actual.

**Years In Current Role (Años en el puesto actual)** – Cantidad de años que el empleado lleva desempeñando su rol actual.

**Years Since Last Promotion (Años desde la última promoción)** – Tiempo transcurrido desde que el empleado recibió su última promoción.

**Years With Curr Manager (Años con el gerente actual)** – Tiempo que el empleado ha trabajado bajo la supervisión del mismo gerente actual. 


# Desarrollo de las fases del proyecto

**Fase 1: Auditoría de Calidad y Diagnóstico (EDA)**
- El objetivo de esta etapa fue realizar un "escaneo" profundo del estado de la información, identificando la salud de los datos y extrayendo los primeros indicadores demográficos de la organización.
1. Diagnóstico de Salud de Datos 
Antes de analizar, evaluamos la fiabilidad de la fuente original:
Dimensiones: Se identificó un universo de 1,476 empleados y 35 variables de estudio.
Integridad (Nulos): Detectamos un 17.4% de ausencia de datos global, lo que marcó la hoja de ruta para la limpieza técnica.
Depuración de Duplicados: Localizamos y eliminamos registros redundantes (4 filas), asegurando que cada empleado sea único en el análisis.
2. Perfilamiento Demográfico 
Establecimos las bases sobre quiénes componen la fuerza laboral:
Género y Edad: Análisis de la distribución por sexo y estadísticas de edad para entender la madurez de la plantilla.
Estructura Organizacional: Identificación de la densidad de talento por departamento para detectar áreas críticas de gestión.
3. Indicadores Base de Bienestar y Riesgo
Calculamos las métricas "termómetro" que justifican la auditoría:
Índice de Deserción (Attrition): Medición del nivel general de salidas voluntarias.
Carga Laboral: Análisis preventivo sobre la incidencia de Horas Extra y la percepción de Work-Life Balance.

#
**Fase 2: Transformación de Datos**
- El objetivo de esta fase fue transformar el dataset de RR.HH. en una fuente de información fiable, eliminando ruido estadístico y garantizando la integridad de cada registro antes del análisis.

1. Depuración de Estructura

Se optimizó el dataset eliminando columnas que no aportan valor estratégico:
Redundante: Over18, EmployeeCount y StandardHours (valores constantes/sin varianza).
Irrelevantes: HourlyRate, MonthlyRate y DailyRate, priorizando MonthlyIncome como métrica salarial principal. 

2. Estandarización y Calidad

Se aplicó un proceso de normalización para asegurar la coherencia del texto:
Formato: Conversión de todo el contenido a minúsculas.
Corrección: Rectificación de errores tipográficos en variables críticas (ej. de "marreid" a "married").

3. Gestión Inteligente de Nulos

Se trataron las ausencias de datos utilizando criterios estadísticos y de negocio para evitar sesgos:
Imputación por Mediana: Aplicada a variables numéricas (Age, MonthlyIncome, YearsWithCurrManager, JobSatisfaction, TrainingTimesLastYear) por su robustez frente a valores atípicos (outliers).
Imputación por Moda: Utilizada en OverTime y BusinessTravel. En viajes, se calculó la moda específica por puesto de trabajo, asegurando coherencia operativa.

Etiquetado como "Desconocido": Aplicado a EducationField, MaritalStatus y Department. Esta decisión preserva la ética de los datos, evita inventar perfiles personales/académicos inexistentes y señala áreas de mejora en la recolección de datos original.

#

**Fase 3: Análisis Integral de Factores de Rotación**
- Enfoque Económico:

El análisis evidencia que la rotación se concentra principalmente en perfiles junior y en niveles salariales más bajos, lo que sugiere una vulnerabilidad estructural en las primeras etapas de la carrera. Sin embargo, también se observa deserción en niveles más altos, lo que indica que el salario, aunque relevante, no es un factor determinante por sí solo. La falta de incentivos ligados al desempeño, junto con estructuras de crecimiento limitadas, reduce la percepción de valor y permanencia en la organización. En este sentido, la eficiencia operativa y una estrategia de compensación alineada a resultados se vuelven clave para mejorar la retención.

- Enfoque de Satisfacción y Bienestar:

Desde la perspectiva del bienestar, el principal factor de riesgo identificado es el agotamiento derivado de las horas extra, el cual incrementa significativamente la probabilidad de renuncia. A esto se suma el estancamiento profesional, especialmente en áreas clave donde los colaboradores permanecen largos periodos sin cambios en su rol, generando desmotivación y falta de proyección. Adicionalmente, factores como la distancia al trabajo y niveles bajos de satisfacción del entorno laboral contribuyen a acelerar la rotación. En conjunto, estos elementos reflejan la necesidad de mejorar la experiencia del empleado de forma integral.

- Enfoque Integral:

La rotación de personal responde a una combinación de factores económicos y de bienestar, más que a una causa aislada. Por un lado, existen limitaciones en la estructura salarial y en las oportunidades de crecimiento, particularmente en perfiles junior. Por otro, el exceso de carga laboral, el estancamiento en los roles y un entorno laboral poco satisfactorio generan desgaste y pérdida de compromiso. Para abordar este problema de manera efectiva, la organización debe adoptar un enfoque integral que combine eficiencia operativa, desarrollo profesional continuo y condiciones laborales sostenibles. La alineación de estos elementos permitirá reducir la rotación y fortalecer la retención del talento a largo plazo.
