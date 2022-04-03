import os
import time
import cProfile
from memory_profiler import profile


@profile
def Lena_the_best():
    k = 0  # счетчик длины числа
    array_len = []  # массив для вывода результата
    array_qv = []
    buffer_len = 1  # размер буфера чтения
    dot_flag = False
    position = 1
    try:
        with open("text.txt", "r") as file:  # открываем файл
            buffer = file.read(buffer_len)  # читаем первый блок

            while buffer:  # пока файл не пустой
                while (buffer < '0' or buffer > '9') and buffer != '.' and buffer:  # ищем цифры
                    buffer = file.read(buffer_len)  # читаем очередной блок
                    position += 1

                while (buffer >= '0' and buffer <= '9') or buffer == '.' and buffer:  # обрабатываем цифры
                    if buffer == '.':
                        dot_flag = True
                    elif buffer >= '0' and buffer <= '9':
                        k += 1
                    buffer = file.read(buffer_len)
                    position += 1
                    if buffer == '.' and buffer and dot_flag:
                        print("встретилось число с несколькими символами .")
                        break
                        # если символ не является цифрой, то
                if k > 0:
                    if k in array_len:
                        ind = array_len.index(k)
                        array_qv[ind] += 1
                    else:
                        array_len.append(k)
                        array_qv.append(1)  # выводим значение длин чисел

                    # print(array_len)  # возвращаем счетчику исходное значение для нового числа
                    # print(array_qv)
                    k = 0  # ищем максимальную длину числа для дальнейшего вывода
                    dot_flag = False

            if len(array_len) > 0:
                for i in range(len(array_len)):
                    print("Чисел длиной", array_len[i], ":", array_qv[i], "шт", "\n")
            else:
                print('В файле нет чисел')

    except FileNotFoundError:
        print(
            "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

    print("Время работы программы:  ", time.process_time(), "seconds")


def main():
    Lena_the_best()


if __name__ == '__main__':
    cProfile.run('main()')
    Lena_the_best()
