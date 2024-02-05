"Archivo para calcular estadísticas descriptivas a partir de un archivo .txt"

import time

start_time = time.time()

nombres_archivos = [
    "TC1.txt", "TC2.txt", "TC3.txt", "TC4.txt", "TC5.txt", "TC6.txt", "TC7.txt"
]
resultados = []

for nombre_archivo in nombres_archivos:
    BASE_PATH = "C:\\Users\\RicardoMoralesBustil\\OneDrive\\05. Educación\\02. MNA\\"
    BASE_PATH += "6° Trimestre\\Calidad de Software\\S4\\4.2.P1\\P1\\"
    FILE_PATH = BASE_PATH + nombre_archivo

    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        numeros = []
        TOTAL_LINEAS = 0
        TOTAL_NUMEROS = 0
        SUMA_NUMEROS = 0.0

        for linea in file:
            try:
                NUMERO = float(linea.strip())
                if NUMERO.is_integer():
                    NUMERO = int(NUMERO)

                TOTAL_NUMEROS += 1
                SUMA_NUMEROS += NUMERO
                numeros.append(NUMERO)
            except ValueError:
                continue

    MEDIA = SUMA_NUMEROS / TOTAL_NUMEROS

    def calculo_mediana(valores):
        """Calcula la mediana de una lista de valores."""
        numeros_ordenados = sorted(valores)
        n = len(valores)
        mitad = n // 2

        if n % 2:
            return numeros_ordenados[mitad]
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2

    MEDIANA = calculo_mediana(numeros)

    def calculo_moda(valores):
        """Calcula la moda de una lista de valores."""
        frecuencias = {}
        for num in valores:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1

        max_frecuencia = max(frecuencias.values())
        if max_frecuencia == 1:
            return "NA"

        modas = [num for num, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
        return modas

    MODA = calculo_moda(numeros)

    def calculo_varianza(valores, media):
        """Calcula la varianza de una lista de valores."""
        suma_cuadrados = sum((num - media) ** 2 for num in valores)
        return suma_cuadrados / len(valores)

    VARIANZA = calculo_varianza(numeros, MEDIA)

    DESV_ESTANDAR = VARIANZA ** 0.5

    resultados.append({
        'Archivo': nombre_archivo,
        'Total de líneas': TOTAL_LINEAS,
        'Números encontrados': TOTAL_NUMEROS,
        'Media': MEDIA,
        'Mediana': MEDIANA,
        'Moda': MODA,
        'Varianza': VARIANZA,
        'Desviación Estándar': DESV_ESTANDAR
    })

print(
    f"{'Archivo':<10} {'Total Líneas':<15} {'Total Números':<15} "
    f"{'Media':<10} {'Mediana':<10} {'Moda':<10} {'Varianza':<10} {'Desv. Est.':<15}"
)
for resultado in resultados:
    MODA_TEXTO = (
        ', '.join(map(str, resultado['Moda']))
        if isinstance(resultado['Moda'], list) else str(resultado['Moda'])
)

    print(
        f"{resultado['Archivo']:<10} "
        f"{resultado['Números encontrados']:<15} "
        f"{resultado['Media']:<10.2f} "
        f"{resultado['Mediana']:<10} "
        f"{MODA_TEXTO:<10} "
        f"{resultado['Varianza']:<10.2f} "
        f"{resultado['Desviación Estándar']:<15.2f}"
    )

end_time = time.time()

duration = end_time - start_time
print (f"Total time: {duration} segundos")

with open('StatisticsResults.txt', 'w') as file:
    for resultado in resultados:
        MODA_TEXTO = (
            ', '.join(map(str, resultado['Moda']))
            if isinstance(resultado['Moda'], list) else str(resultado['Moda'])
)

        file.write(
            f"{resultado['Archivo']:<10} "
            f"{resultado['Números encontrados']:<15} "
            f"{resultado['Media']:<10.2f} "
            f"{resultado['Mediana']:<10} "
            f"{MODA_TEXTO:<10} "
            f"{resultado['Varianza']:<10.2f} "
            f"{resultado['Desviación Estándar']:<15.2f}\n"
        )

    # Detiene el cronómetro justo antes de finalizar
    end_time = time.time()

    # Calcula la duración y escribe el tiempo total en el archivo
    duration = end_time - start_time
    file.write(f"Total time: {duration} segundos")