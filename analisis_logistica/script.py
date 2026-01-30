import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# PROYECTO: Automatización de Análisis de Ventas y Logística
# OBJETIVO: Procesar datos brutos para generar KPIs y visualizaciones
# ==========================================================

def procesar_datos_ventas(input_file):
    print(f"--- Iniciando procesamiento de: {input_file} ---")
    
    # 1. CARGA DE DATOS
    # Cargamos el archivo original (asumiendo que viene separado por comas)
    df = pd.read_csv(input_file)
    
    # 2. LIMPIEZA Y TRANSFORMACIÓN (ETL)
    # Convertimos las columnas de fecha a formato datetime de Python
    # Esto es vital para poder hacer cálculos matemáticos con fechas
    df['FECHA_COMPRA'] = pd.to_datetime(df['FECHA_COMPRA'], dayfirst=True)
    df['FECHA_ENTREGA'] = pd.to_datetime(df['FECHA_ENTREGA'], dayfirst=True)
    
    # 3. INGENIERÍA DE DATOS (Creación de KPIs)
    # Calculamos el 'Lead Time' (Días que tarda en entregarse el producto)
    df['DIAS_ENTREGA'] = (df['FECHA_ENTREGA'] - df['FECHA_COMPRA']).dt.days
    
    # 4. GENERACIÓN DE INSIGHTS (Análisis rápido)
    promedio_entrega = df['DIAS_ENTREGA'].mean()
    top_sucursal = df.groupby('SUCURSAL')['CANTIDAD'].sum().idxmax()
    
    print(f"RESULTADOS:")
    print(f"- Promedio de días para entrega: {promedio_entrega:.2f} días")
    print(f"- Sucursal con mayor volumen: {top_sucursal}")
    
    # 5. EXPORTACIÓN PROFESIONAL
    # Guardamos con separador ';' para que Excel lo abra en columnas automáticamente
    output_name = 'Ventas_Final_Para_PowerBI.csv'
    df.to_csv(output_name, index=False, sep=';', encoding='utf-8-sig')
    print(f"--- Proceso completado. Archivo guardado como: {output_name} ---")
    
    # 6. VISUALIZACIÓN PREVIA (Opcional, para validar antes de Power BI)
    df.groupby('SUCURSAL')['DIAS_ENTREGA'].mean().sort_values().tail(10).plot(kind='barh', color='skyblue')
    plt.title('Top 10 Sucursales más lentas (Promedio de días)')
    plt.xlabel('Días')
    plt.tight_layout()
    plt.savefig('grafico_logistica.png')
    print("- Gráfico de control generado: grafico_logistica.png")

# Ejecutar la función con tu archivo
if __name__ == "__main__":
    archivo_usuario = 'Ventas.csv' # Asegúrate de que el archivo esté en la misma carpeta
    procesar_datos_ventas(archivo_usuario)