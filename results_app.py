import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # Agrega esta línea al inicio del archivo


# Configuración para caché de datos
@st.cache_data
def cargar_datos():
    # Cargar archivo Excel
    file_path = "./concatenated_results.xlsx"
    df = pd.read_excel(file_path)

    # Reordenar las columnas del DataFrame
    new_order = [31, 0, 1, 2, 3, 6, 7, 8, 9, 10, 4, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 21, 24, 25, 26, 27, 28, 29, 30]
    df = df.iloc[:, new_order]

    # Renombrar columnas
    column_rename_map = {
        "CICLO": "Ciclo",
        "nombre_micro": "Nombre programa",
        "FORMADOR": "Formador",
        "GRUPO": "Grupo",
        "GRUPO 1": "Tipo",
        "PARTICIPANTES": "Participantes",
        "promedio_temas": "Los temas tratados en la formación fueron presentados claramente para facilitar la comprensión.",
        "promedio_material": "El material del curso fue coherente, actualizado y útil para lograr el aprendizaje.",
        "promedio_mercado": "Lo aprendido durante la formación corresponde a los requerimientos del mercado laboral actual.",
        "promedio_carrera": "El aprendizaje alcanzado se puede aplicar directamente al trabajo o la carrera.",
        "promedio_respuestas": "El formador respondió y aclaró todas tus preguntas, teniendo en cuenta lo que necesitabas.",
        "promedio_explicacion": "La capacidad del formador para explicar los temas facilitó el aprendizaje durante las sesiones.",
        "promedio_acompanamiento": "El equipo de acompañamiento brindó apoyo y atención oportuna durante el proceso de formación.",
        "promedio_experiencia": "La experiencia general con la formación fue satisfactoria y se cumplieron las expectativas iniciales.",
        "promedio_instalaciones": "Las instalaciones (espacio físico o virtual) donde se llevaron a cabo los encuentros tenían condiciones adecuadas para el desarrollo de las actividades.",
        "promedio_personal": "El personal de apoyo mostró disposición y actitud de servicio durante toda la formación.",
        "promedio_duracion": "La duración del proceso fue adecuada para cubrir los temas previstos sin sobrecargar el tiempo de los participantes.",
        "promedio_horarios": "Los horarios de las sesiones fueron convenientes y permitieron una participación efectiva.",
        "promedio_plataforma": "La plataforma tecnológica utilizada fue intuitiva y permitió un fácil acceso a los contenidos del curso.",
        "promedio_encuentros": "Los encuentros sincrónicos fueron fluidos y sin problemas técnicos significativos.",
        "promedio_actualizaciones": "Las instrucciones y actualizaciones enviadas por correo electrónico fueron claras y oportunas, facilitando el seguimiento del programa de formación.",
        "promedio_canales": "Los canales de comunicación establecidos permitieron desarrollar de manera eficiente el proceso del programa.",
        "promedio_calidad_final": "Calidad",
        "promedio_pertinencia_final": "Pertinencia",
        "promedio_desempeño_final": "Desempeño",
        "promedio_satisfaccion_final": "Satisfacción",
        "promedio_servicio_final": "Servicio",
        "promedio_tiempos_final": "Tiempos",
        "promedio_acceso_final": "Acceso",
        "promedio_comunicacion_final": "Comunicación",
        "comentarios_grupo": "Comentarios",
        "resumen": "Resumen"
    }
    df.rename(columns=column_rename_map, inplace=True)

    # Normalizar nombres de programas y formadores
    programa_mapping = {
        "Herramientas para la visualización de datos financieros ": "Herramientas para la visualización de datos financieros",
        "Inteligencia Artifical en Modelos de costos para la formulación de proyectos ": "Inteligencia Artifical en Modelos de costos para la formulación de proyectos",
        "Inteligencia de negocios aplicada a organizaciones ": "Inteligencia de negocios aplicada a organizaciones",
        "Simulación financiera avanzada-estrategias de inversión y toma de decisiones": "Simulación financiera avanzada: estrategias de inversión y toma de decisiones"
    }
    formador_mapping = {
    " Diego Suárez": "Diego Suárez",  # Eliminar espacio inicial
    "Andres Montanez": "Andrés Montañez",
    "Andres Montañez": "Andrés Montañez",
    "Andrés Montañez": "Andrés Montañez",  # Unificación completa
    "David Gonzalez": "David González",
    "Diana Yesmid Suarez": "Diana Yesmid Suárez Rodríguez",
    "Diana Yesmid Suarez Rodriguez": "Diana Yesmid Suárez Rodríguez",
    "Diana Yesmid Suárez Rodriguez ": "Diana Yesmid Suárez Rodríguez",
    "Diana Yesmid Suárez Rodriguez": "Diana Yesmid Suárez Rodríguez",  # Asegurando consistencia
    "Juna Carlos Noriega": "Juan Carlos Noriega",
    "Juan Pablo Hernandez": "Juan Pablo Hernández",
    "Nydia Carrisoza": "Nydia Carrizosa",
    "Nydia Teresa Carrisoza Moscoso": "Nydia Carrizosa",
    "Paúl Medina": "Paul Medina",
    "Sebastian Moreno": "Sebastián Moreno"
    }

    

    df["Nombre programa"] = df["Nombre programa"].str.strip().replace(programa_mapping)
    df["Formador"] = df["Formador"].str.strip().str.title().replace(formador_mapping)

    # Crear DataFrames
    df_resultados = df[[
        "Ciclo", "Nombre programa", "Formador", "Grupo", "Tipo", "Calidad", "Pertinencia", "Desempeño", "Satisfacción", "Servicio", "Tiempos", "Acceso", "Comunicación"
    ]]

    # Paso 3: Limpiar posibles duplicados adicionales en "Formador" y "Nombre programa"
    df["Formador"] = df["Formador"].replace({
        "Diana Yesmid Suárez Rodriguez": "Diana Yesmid Suárez Rodríguez",  # Ajuste final
        "Andres Montañez": "Andrés Montañez"
    })

    df_items = df[[
        "Ciclo", "Nombre programa", "Formador", "Grupo", "Tipo", "Participantes",
        "Los temas tratados en la formación fueron presentados claramente para facilitar la comprensión.",
        "El material del curso fue coherente, actualizado y útil para lograr el aprendizaje.",
        "Lo aprendido durante la formación corresponde a los requerimientos del mercado laboral actual.",
        "El aprendizaje alcanzado se puede aplicar directamente al trabajo o la carrera.",
        "El formador respondió y aclaró todas tus preguntas, teniendo en cuenta lo que necesitabas.",
        "La capacidad del formador para explicar los temas facilitó el aprendizaje durante las sesiones.",
        "El equipo de acompañamiento brindó apoyo y atención oportuna durante el proceso de formación.",
        "La experiencia general con la formación fue satisfactoria y se cumplieron las expectativas iniciales.",
        "Las instalaciones (espacio físico o virtual) donde se llevaron a cabo los encuentros tenían condiciones adecuadas para el desarrollo de las actividades.",
        "El personal de apoyo mostró disposición y actitud de servicio durante toda la formación.",
        "La duración del proceso fue adecuada para cubrir los temas previstos sin sobrecargar el tiempo de los participantes.",
        "Los horarios de las sesiones fueron convenientes y permitieron una participación efectiva.",
        "La plataforma tecnológica utilizada fue intuitiva y permitió un fácil acceso a los contenidos del curso.",
        "Los encuentros sincrónicos fueron fluidos y sin problemas técnicos significativos.",
        "Las instrucciones y actualizaciones enviadas por correo electrónico fueron claras y oportunas, facilitando el seguimiento del programa de formación.",
        "Los canales de comunicación establecidos permitieron desarrollar de manera eficiente el proceso del programa."
    ]]

    df_formadores = df[[
        "Ciclo", "Nombre programa", "Formador", "Grupo", "Tipo", "El formador respondió y aclaró todas tus preguntas, teniendo en cuenta lo que necesitabas.",
        "La capacidad del formador para explicar los temas facilitó el aprendizaje durante las sesiones.", "Desempeño"
    ]]

    return df, df_resultados, df_items, df_formadores

# Cargar y procesar datos
df, df_resultados, df_items, df_formadores = cargar_datos()

# Configuración de la barra lateral
st.sidebar.title("Menú de Navegación")
selected_page = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Resultados Generales", "Resultados Ítems", "Resultados Formadores"]
)


# Función para aplicar filtros dinámicos
def aplicar_filtros_dinamicos(df):
    with st.sidebar:
        st.subheader("Filtros")

        # Paso 1: Filtro para ciclos (sin filtrar inicialmente)
        ciclos_disponibles = sorted(df["Ciclo"].unique())
        ciclo_seleccionado = st.multiselect("Ciclo", ciclos_disponibles, default=None)

        # Filtrar DataFrame por ciclos seleccionados
        df = df[df["Ciclo"].isin(ciclo_seleccionado)] if ciclo_seleccionado else df

        # Paso 2: Filtro para programas basado en ciclos seleccionados
        programas_disponibles = sorted(df["Nombre programa"].unique())
        programa_seleccionado = st.multiselect("Nombre programa", programas_disponibles, default=None)

        # Filtrar DataFrame por programas seleccionados
        df = df[df["Nombre programa"].isin(programa_seleccionado)] if programa_seleccionado else df

        # Paso 3: Filtro para formadores basado en programas seleccionados
        formadores_disponibles = sorted(df["Formador"].unique())
        formador_seleccionado = st.multiselect("Formador", formadores_disponibles, default=None)

        # Filtrar DataFrame por formadores seleccionados
        df = df[df["Formador"].isin(formador_seleccionado)] if formador_seleccionado else df

        # Paso 4: Filtro para grupos basado en formadores seleccionados
        grupos_disponibles = sorted(df["Grupo"].unique())
        grupo_seleccionado = st.multiselect("Grupo", grupos_disponibles, default=None)

        # Filtrar DataFrame por grupos seleccionados
        df = df[df["Grupo"].isin(grupo_seleccionado)] if grupo_seleccionado else df

        # Paso 5: Filtro para tipo basado en grupos seleccionados
        tipos_disponibles = sorted(df["Tipo"].unique())
        tipo_seleccionado = st.multiselect("Tipo (Abierto/Cerrado)", tipos_disponibles, default=None)

        # Filtrar DataFrame por tipo seleccionado
        df = df[df["Tipo"].isin(tipo_seleccionado)] if tipo_seleccionado else df

    # Retornar DataFrame filtrado
    return df

# Función para graficar promedios por columna
def plot_column_means(df, title, exclude_columns=None, numbered_columns=False):
    """
    Genera un gráfico de líneas y puntos para los promedios de columnas numéricas en un DataFrame.

    :param df: DataFrame con las columnas numéricas a analizar.
    :param title: Título del gráfico.
    :param exclude_columns: Lista de columnas a excluir del análisis.
    :param numbered_columns: Si es True, reemplaza los nombres de las columnas en el eje x por números.
    """
    # Excluir columnas si se especifican
    if exclude_columns:
        df = df.drop(columns=exclude_columns, errors="ignore")

    # Filtrar solo las columnas numéricas
    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns

    # Calcular promedios por columna
    column_means = df[numeric_columns].mean()

    # Reemplazar nombres por números si se especifica
    if numbered_columns:
        column_mapping = {i + 1: col for i, col in enumerate(column_means.index)}
        x_labels = list(column_mapping.keys())
    else:
        x_labels = column_means.index

    # Crear el gráfico
    fig = plt.figure(figsize=(12, 8))
    plt.plot(x_labels, column_means.values, marker="o", linestyle="-", label="Promedio", color="#e65a07")
    plt.xticks(ticks=x_labels, labels=x_labels if not numbered_columns else list(column_mapping.keys()), rotation=45, ha="right")
    plt.xlabel("Columnas" if not numbered_columns else "Indicadores")
    plt.ylabel("Promedio")
    plt.title(title)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Aumentar el tamaño de la fuente en las leyendas
    plt.legend(fontsize=12)  # Aumentar tamaño de letra un 50%

    # Agregar leyenda con nombres originales si se usaron números
    if numbered_columns:
        legend_text = "\n".join([f"{k}: {v} : {column_means[v]:.2f}" for k, v in column_mapping.items()])
        plt.gcf().text(
            0.02, -0.03, legend_text, fontsize=15,  # Aumentar tamaño de letra un 50%
            ha="left", va="top",
            bbox=dict(facecolor="white", alpha=0.5)
        )

    plt.tight_layout()
    return fig


# Resultados Generales
if selected_page == "Resultados Generales":
    st.title("Resultados Generales")
    
    # Aplicar filtros dinámicos
    df_resultados_filtrado = aplicar_filtros_dinamicos(df_resultados)

    # Gráfico de resultados generales
    st.subheader("Promedios Generales")
    fig = plot_column_means(df_resultados_filtrado, "Resultados Generales", exclude_columns=["Participantes"])
    st.pyplot(fig)

# Resultados Ítems
elif selected_page == "Resultados Ítems":
    st.title("Resultados Ítems")
    
    # Aplicar filtros dinámicos
    df_items_filtrado = aplicar_filtros_dinamicos(df_items)

    # Gráfico de resultados ítems
    st.subheader("Promedios de Ítems")
    fig = plot_column_means(df_items_filtrado, "Resultados Items", exclude_columns=["Participantes"], numbered_columns=True)
    st.pyplot(fig)

# Resultados Formadores
elif selected_page == "Resultados Formadores":
    st.title("Resultados Formadores")
    
    # Aplicar filtros dinámicos
    df_formadores_filtrado = aplicar_filtros_dinamicos(df_formadores)

    # Gráfico de resultados formadores
    st.subheader("Promedios de Formadores")
    fig = plot_column_means(df_formadores_filtrado, "Resultados Formadores", exclude_columns=["Participantes"], numbered_columns=True)
    st.pyplot(fig)
