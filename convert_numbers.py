"Archivo para convertir números a binarios y hexadecimales a partir de un archivo .txt"

import sys
import time

def convert_to_binary(number):
    "Convierte un número a binario"
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary or '0'

def convert_to_hexadecimal(number):
    "Convierte un número a hexadecimal"
    hexadecimal = ''
    digits = '0123456789ABCDEF'
    while number > 0:
        hexadecimal = digits[number % 16] + hexadecimal
        number = number // 16
    return hexadecimal or '0'

def main(filename):
    "Crear archivo e imputar valores"
    start_time = time.time()
    with open(filename, 'r', encoding='utf-8') as file, \
        open('ConversionResults.txt', 'w', encoding='utf-8') as outfile:
        for line in file:
            line = line.strip()
            if line.isdigit():
                number = int(line)
                binary = convert_to_binary(number)
                hexadecimal = convert_to_hexadecimal(number)
                result = f"{number}: Binary = {binary}, Hexadecimal = {hexadecimal}\n"
                print(result.strip())
                outfile.write(result)
            else:
                print(f"Invalid data: {line}")


        end_time = time.time()
        duration = end_time - start_time
        time_result = f"Total execution time: {duration} seconds.\n"
        print(time_result.strip())
        outfile.write(time_result)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    input_filename = sys.argv[1]
    main(input_filename)
