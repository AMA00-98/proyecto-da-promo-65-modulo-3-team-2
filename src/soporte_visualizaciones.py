import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizaciones:
    def __init__(self, dataframe):

        """
        Inicializa la clase con un DataFrame.

        Parámetros
        ----------
        dataframe : pandas.DataFrame
        DataFrame sobre el que se harán las visualizaciones.
        """

        self.dataframe = dataframe # Con esto evitamos llamar al df cada vez que queramos hacer una visualización de esta clase
        sns.set_theme(style='white',palette="bright")
    
    # Histograma
    def histograma(self, variable, hue=None, bins=20, figsize=(8, 5), kde=True):

        """
        Representa un histograma de una variable numérica.

        Parámetros
        ----------
        variable : str
            Nombre de la columna numérica.
        hue : str, optional
            Variable categórica para segmentar el histograma.
        bins : int, default=20
            Número de barras.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        kde : bool, default=True
            Si se añade la curva de densidad.
        """

        plt.figure(figsize=figsize)
        sns.histplot(data=self.dataframe, x=variable, hue=hue, bins=bins, kde=kde)
        plt.title(f"Distribución de {variable}")
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()

    # Boxplot
    def boxplot(self, x=None, y=None, hue=None, figsize=(8, 5)):

        """
        Representa un boxplot.

        Parámetros
        ----------
        x : str, optional
            Variable categórica.
        y : str, optional
            Variable numérica.
        hue : str, optional
            Variable categórica para segmentar.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.        
            """
        
        plt.figure(figsize=figsize)
        sns.boxplot(data=self.dataframe, x=x, y=y, hue=hue)
        plt.title(f"Boxplot de {y} por {x}" if x and y else "Boxplot")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Barplot
    def barplot(self, x, y, hue=None, figsize=(8, 5)):

        """
        Representa un barplot.

        Parámetros
        ----------
        x : str
            Variable categórica.
        y : str
            Variable numérica.
        hue : str, optional
            Variable categórica para segmentar.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        """

        plt.figure(figsize=figsize)
        sns.barplot(data=self.dataframe, x=x, y=y, hue=hue,errorbar=None)
        plt.title(f"{y} por {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Countplot
    def countplot(self, variable, hue=None, figsize=(8, 5)):

        """
        Representa un countplot de una variable categórica.

        Parámetros
        ----------
        variable : str
            Nombre de la columna categórica.
        hue : str, optional
            Variable categórica para segmentar.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        """

        plt.figure(figsize=figsize)
        sns.countplot(data=self.dataframe, x=variable, hue=hue)
        plt.title(f"Frecuencia de {variable}")
        plt.xlabel(variable)
        plt.ylabel("Conteo")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Regplot
    def regplot (self, x, y, marker="o", figsize=(8, 5)):

        """
        Representa un regplot entre dos variables numéricas.

        Parámetros
        ----------
        x : str
            Variable numérica en eje X.
        y : str
            Variable numérica en eje Y.
        marker : str, default="o"
            Marcador de los puntos.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        """

        plt.figure(figsize=figsize)
        sns.regplot(data=self.dataframe, x=x, y=y, marker=marker)
        plt.title(f"Relación entre {x} y {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.tight_layout()
        plt.show()
    
    # Scatterplot
    def scatterplot (self, x, y, hue=None, figsize=(8, 5)):

        """
        Representa un scatterplot entre dos variables.

        Parámetros
        ----------
        x : str
            Variable en eje X.
        y : str
            Variable en eje Y.
        hue : str, optional
            Variable categórica para segmentar.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        """

        plt.figure(figsize=figsize)
        sns.scatterplot(data=self.dataframe, x=x, y=y, hue=hue)
        plt.title(f"Relación entre {x} y {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.tight_layout()
        plt.show()
    
    # Heatmap
    def heatmap (self, matriz, titulo="Heatmap", figsize=(8, 5), annot=True, cmap="coolwarm"):

        """
        Representa un heatmap.

        Parámetros
        ----------
        matriz : pandas.DataFrame o array-like
            Matriz a representar, por ejemplo una correlación.
        titulo : str, default="Heatmap"
            Título del gráfico.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        annot : bool, default=True
            Si muestra los valores dentro de las celdas.
        cmap : str, default="coolwarm"
            Paleta de colores.
        """

        plt.figure(figsize=figsize)
        sns.heatmap(matriz, annot=annot, cmap=cmap)
        plt.title(titulo)
        plt.tight_layout()
        plt.show()
    
    # Violinplot
    def violin(self, x, y, hue=None, figsize=(8, 5)):

        """
        Representa un violinplot.

        Parámetros
        ----------
        x : str
            Variable categórica.
        y : str
            Variable numérica.
        hue : str, optional
            Variable categórica para segmentar.
        figsize : tuple, default=(8, 5)
            Tamaño de la figura.
        """

        plt.figure(figsize=figsize)
        sns.violinplot(data=self.dataframe, x=x, y=y, hue=hue)
        plt.title(f"Distribución de {y} por {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Pieplot
    def pieplot (self, variable, figsize=(6, 6)):

        """
        Representa un gráfico de sectores de una variable categórica.

        Parámetros
        ----------
        variable : str
            Nombre de la columna categórica.
        figsize : tuple, default=(6, 6)
            Tamaño de la figura.
        """
        
        frecuencias = self.dataframe[variable].value_counts()

        plt.figure(figsize=figsize)
        plt.pie(
            frecuencias.values,
            labels=frecuencias.index,
            autopct="%1.1f%%",
            textprops={"fontsize": 8},
            startangle=90
        )
        plt.title(f"Distribución de {variable}")
        plt.tight_layout()
        plt.show()