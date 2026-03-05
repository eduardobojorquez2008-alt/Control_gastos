import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st

SHEET_ID = "15pDT5c1dVxTiFVN3F49qzUCPcVm9fX2UFRnUuO7i100"
COLUMNAS = ["Nombre", "Categoria", "Monto", "Fecha"]
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def conectar():
    credenciales = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credenciales, SCOPE)
    cliente = gspread.authorize(creds)
    return cliente.open_by_key(SHEET_ID).sheet1

def inicializar_archivo():
    pass  

def guardar_gasto(nombre: str, categoria: str, monto: float, fecha) -> None:
    hoja = conectar()
    hoja.append_row([nombre, categoria, float(monto), str(fecha)])

def leer_gastos() -> pd.DataFrame:
    try:
        hoja = conectar()
        datos = hoja.get_all_records()
        if datos:
            return pd.DataFrame(datos, columns=COLUMNAS)
        return pd.DataFrame(columns=COLUMNAS)
    except Exception:
        return pd.DataFrame(columns=COLUMNAS)

def eliminar_gasto(indice: int) -> None:
    hoja = conectar()
    hoja.delete_rows(indice + 2)  

