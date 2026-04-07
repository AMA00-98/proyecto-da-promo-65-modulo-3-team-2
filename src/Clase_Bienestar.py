import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


class TalentSatisfactionAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    # --- 1. PATRÓN HORAS EXTRAS VS ROTACIÓN --- (Barras Apiladas)
    def graficar_horas_extra(self):
        
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x="OverTime", hue="Attrition")
        plt.title("IMPACTO DE LAS HORAS EXTRA EN LA ROTACIÓN")
        plt.xlabel("¿Hace Horas Extra?")
        plt.ylabel("Cantidad de Empleados")
        plt.show()

        
        reporte_horas_extras = self.df.groupby("OverTime")["Attrition"].value_counts(normalize=True) * 100
        print("---REPORTE HORAS EXTRA VS ROTACIÓN ---")
        for (h_extra, rotacion), porcentaje in reporte_horas_extras.items():
            if rotacion == "yes": 
               print(f"Personal con Horas Extra ({h_extra}): {porcentaje:.1f}% de fuga")



    # --- 2. PATRÓN DISTANCIA VS ROTACIÓN --- (diagrama de caja y bigotes)
    def graficar_distancia(self):
        
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=self.df, x="Attrition", y="DistanceFromHome")
        plt.title("IMPACTO DE LA DISTANCIA EN LA ROTACIÓN")
        plt.xlabel("¿Se fue de la empresa?")
        plt.ylabel("Distancia (Millas)")
        plt.show()

        
        reporte_distancia = self.df.groupby("Attrition")["DistanceFromHome"].median()
        
        nombres = {"yes": "Grupo que renunció", "no": "Grupo que permanece"}

        print("--- REPORTE DE DISTANCIA CASA-TRABAJO ---")
        for rotacion, promedio in reporte_distancia.items():
            print(f"{nombres[rotacion]}: {promedio:.1f} millas")



    # --- 3. PATRÓN BIENESTAR ---  (Pie Chart)
    def Balance_vida_laboral(self):
        suma_puntos = self.df["JobSatisfaction"] + self.df["WorkLifeBalance"]
    
        self.df["Nivel_Bienestar"] = pd.cut(suma_puntos, 
                                       bins=[0, 3, 5, 8], 
                                       labels=["Baja", "Media", "Alta"])
    
        data = self.df["Nivel_Bienestar"].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
        plt.title("DISTRIBUCIÓN DE BIENESTAR (BALANCE VIDA LABORAL)")
        plt.show()


        porcentajes = self.df["Nivel_Bienestar"].value_counts(normalize=True) * 100
        print("--- REPORTE DE BIENESTAR ---")
        for nivel, valor in porcentajes.items():
            print(f"Nivel {nivel}: {valor:.1f}% ({data[nivel]} empleados)")

        

    # --- 4. PATRÓN ESTANCAMIENTO  --- (Barras Apiladas)
    def graficar_estancamiento_por_depto(self):
        self.df["Estancado"] = (self.df["YearsSinceLastPromotion"] >= 3)+(self.df["YearsInCurrentRole"] >= 5)+(self.df["YearsAtCompany"] >= 5)

        plt.figure(figsize=(10, 6))
        
        sns.countplot(data=self.df, x="Department", hue="Estancado", palette="viridis")
        
        plt.title("EMPLEADOS ESTANCADOS POR DEPARTAMENTO (>3 AÑOS SIN PROMOCIÓN)")
        plt.xlabel("Departamento")
        plt.ylabel("Cantidad de Empleados")
        plt.legend(title="¿Está Estancado?", labels=["No", "Sí"])
        
        plt.show()

        conteo_total = self.df.groupby("Department")["Estancado"].count()
        conteo_estancados = self.df.groupby("Department")["Estancado"].sum()
        porcentajes = (conteo_estancados / conteo_total) * 100

        antiguedad_media = self.df.groupby("Department")["YearsAtCompany"].median()
        tiempo_rol_medio = self.df.groupby("Department")["YearsInCurrentRole"].median()

        print("--- REPORTE DE ESTANCAMIENTO POR DEPARTAMENTO ---")
        print(f"{'DEPARTAMENTO':25} | {'ESTANCADOS':18} | {'ANTIGUEDAD':12} | {'EN EL ROL'}")

        
        for depto in conteo_total.index:
            numero_estancados = int(conteo_estancados[depto])
            total = int(conteo_total[depto])
            porcentaje_total = porcentajes[depto]
            años_empresa = antiguedad_media[depto]
            años_rol = tiempo_rol_medio[depto]
            
           
            print(f"{depto.upper():25} | {numero_estancados:>3} de {total:>3} ({porcentaje_total:>4.1f}%) | "f"{años_empresa:>5.1f} años  | {años_rol:>5.1f} años")


    # --- 5. PATRÓN SEMAFORO SATISFACCIÓN  --- (Barras Apiladas)
    def analizar_satisfaccion_entorno(self):
        self.df["Entorno_satisfacción"] = (self.df["JobInvolvement"] + self.df["EnvironmentSatisfaction"] + self.df["RelationshipSatisfaction"])

        self.df["Nivel_Entorno"] = pd.cut(self.df["Entorno_satisfacción"], 
                                          bins=[2, 6, 9, 12], 
                                          labels=["Baja", "Media", "Alta"])

        sns.countplot(data=self.df, x="Nivel_Entorno", palette=["#E63946", "#FFB703", "#2A9D8F"])
        plt.title("NIVEL DE SATISFACCIÓN DEL ENTORNO LABORAL")
        plt.xlabel("Nivel de Entorno")
        plt.ylabel("Cantidad de Empleados")
        plt.show()
        
        reporte = self.df.groupby("Nivel_Entorno")["Entorno_satisfacción"].median()
        conteo = self.df["Nivel_Entorno"].value_counts()

        print("--- REPORTE DE SATISFACCIÓN DE ENTORNO ---")
        for nivel, mediana in reporte.items():
            cantidad = conteo[nivel]
            print(f"Nivel {nivel}: {cantidad} empleados (Puntaje medio: {mediana})")

    
    



           
 