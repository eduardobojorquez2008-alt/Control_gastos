import pandas as pd
import os

ARCHIVO = "gastos.csv"
COLUMNAS = ["Nombre", "Categoria", "Monto", "Fecha"]

def inicializar_archivo() -> None:
    if not os.path.exists(ARCHIVO):
        pd.DataFrame(columns=COLUMNAS).to_csv(ARCHIVO, index=False, encoding='utf-8')

def guardar_gasto(nombre: str, categoria: str, monto: float, fecha) -> None:
    nuevo = pd.DataFrame([[nombre, categoria, monto, fecha]], columns=COLUMNAS)
    escribir_header = not os.path.exists(ARCHIVO) or os.path.getsize(ARCHIVO) == 0
    nuevo.to_csv(ARCHIVO, mode="a", header=escribir_header, index=False, encoding='utf-8')

def leer_gastos() -> pd.DataFrame:
    try:
        if os.path.exists(ARCHIVO):
            df = pd.read_csv(ARCHIVO)
            return df if not df.empty else pd.DataFrame(columns=COLUMNAS)
        return pd.DataFrame(columns=COLUMNAS)
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=COLUMNAS) 
    

def eliminar_gasto(indice: int) -> None:
    df = leer_gastos()
    df = df.drop(index=indice).reset_index(drop=True)
    df.to_csv(ARCHIVO, index=False, encoding='utf-8')