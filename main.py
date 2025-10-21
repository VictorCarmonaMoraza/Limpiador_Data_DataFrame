import pandas as pd  # Importamos la librería pandas para manejo de datos en forma de DataFrame


# -------------------------------
# Función para cargar el dataset
# -------------------------------
def load_data(file_path):
    """
    Carga un archivo CSV y lo convierte en un DataFrame de pandas.
    :param file_path: ruta del archivo CSV
    :return: DataFrame cargado o None si hay error
    """
    try:
        df = pd.read_csv(file_path)  # Intentamos leer el archivo CSV
        return df
    except Exception as e:
        # Si ocurre un error (por ejemplo, archivo no encontrado o formato incorrecto), lo mostramos
        print(f"Error loading data: {e}")
        return None


# -------------------------------
# Función para limpiar el dataset
# -------------------------------
def clean_data(df):
    """
    Limpia el DataFrame eliminando valores faltantes y duplicados.
    :param df: DataFrame original
    :return: DataFrame limpio
    """
    print("\n--- Limpiando Datos ---")
    print("Forma inicial del DataFrame:", df.shape)  # Muestra la cantidad de filas y columnas iniciales

    # 1️⃣ Eliminar valores faltantes (NaN)
    print("\nEliminando valores faltantes...")
    df.dropna(inplace=True)  # Elimina cualquier fila que tenga al menos un valor NaN
    print("Forma después de eliminar valores faltantes:", df.shape)

    # 2️⃣ Eliminar duplicados
    print("\nEliminando duplicados...")
    df.drop_duplicates(inplace=True)  # Elimina filas duplicadas completas

    # Devuelve el DataFrame limpio
    return df


# -------------------------------
# Función para guardar el dataset
# -------------------------------
def save_data(df, output_path):
    """
    Guarda el DataFrame limpio en un nuevo archivo CSV.
    :param df: DataFrame limpio
    :param output_path: ruta y nombre del archivo de salida
    """
    try:
        df.to_csv(output_path, index=False)  # Guardamos el DataFrame sin el índice
        print(f"Datos guardados en {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")  # Mostramos el error si no se puede guardar


# -------------------------------
# Función principal
# -------------------------------
def main():
    """
    Función principal que coordina la carga, limpieza y guardado del dataset.
    """
    # Solicitamos al usuario la ruta del archivo original
    input_file = input("Dame la ruta de tu dataset: ")
    df = load_data(input_file)  # Cargamos los datos
    if df is None:
        # Si hubo error en la carga, salimos del programa
        return

    # Mostramos las primeras filas del DataFrame para inspeccionar los datos iniciales
    print("\n--- Data inicial ---")
    print(df.head())

    # Llamamos a la función de limpieza
    df = clean_data(df)

    # Solicitamos al usuario la ruta donde guardar el dataset limpio (con nombre del archivo)
    output_file = input("\n¿Dónde quieres guardar tu dataset limpio? ")
    save_data(df, output_file)  # Guardamos el archivo limpio


# -------------------------------
# Punto de entrada del programa
# -------------------------------
if __name__ == "__main__":
    main()  # Ejecutamos la función principal solo si el archivo se ejecuta directamente
