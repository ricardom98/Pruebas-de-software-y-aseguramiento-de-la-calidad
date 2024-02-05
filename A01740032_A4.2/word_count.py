"Archivo para contar el número de palabras a partir de un archivo .txt"

import sys
import time

def count_words(filename):
    "Cuenta la frecuencia de cada palabra en el archivo."
    word_count = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word.isalpha():  # Verificar si la palabra contiene solo letras
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
                else:
                    print(f"Invalid data: {word}")
    return word_count

def main(filename):
    "Crear archivo e imputar valores"
    start_time = time.time()
    counts = count_words(filename)

    with open('WordCountResults.txt', 'w', encoding='utf-8') as outfile:
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            result = f"{word}: {count}\n"
            print(result.strip())
            outfile.write(result)

        end_time = time.time()
        duration = end_time - start_time
        time_result = f"Total execution time: {duration} seconds.\n"
        print(time_result.strip())
        outfile.write(time_result)  # Asegúrate de que esta línea esté dentro del bloque `with`

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)
    input_filename = sys.argv[1]
    main(input_filename)
