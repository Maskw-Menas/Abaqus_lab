import  matplotlib.pyplot  as  plt
import numpy as np
import pandas as pd
import math as mm

# Открываем файл для чтения
with open('logs/path1_x_s11.rpt', 'r') as file:
    # Пропускаем первые две строки (заголовки)
    next(file)
    next(file)
    next(file)
    # Инициализируем пустые списки для хранения данных
    x = []
    p1_s11 = []
    # Читаем файл построчно
    for line in file:
        # Убираем лишние пробелы в начале и конце строки
        line = line.strip()
        # Пропускаем пустые строки
        if not line:
            continue
        # Разделяем строку на два значения
        values = line.split()
        # Проверяем, что в строке ровно два значения
        if len(values) == 2:
            try:
                # Преобразуем значения в числа и добавляем в списки
                x.append(float(values[0]))
                p1_s11.append(float(values[1]))
            except ValueError:
                # Если преобразование в число не удалось, пропускаем строку
                print(f"Ошибка в строке: {line}. Невозможно преобразовать в число.")
        else:
            # Если в строке не два значения, пропускаем её
            print(f"Пропущена строка: {line}. Ожидалось 2 значения, получено {len(values)}.")

with open('logs/path2_x_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p2_s11 = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p2_s11.append(float(values[1]))

with open('logs/path3_x_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p3_s11 = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p3_s11.append(float(values[1]))

with open('logs/path4_x_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p4_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p4_s11.append(float(values[1]))

with open('logs/path5_x_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p5_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p5_s11.append(float(values[1]))

xy = np.linspace(0, 2*np.pi, 63)

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(xy, p1_s11, label='Кривая 1 (p1_s11)', color='red', marker='o')
plt.plot(xy, p2_s11, label='Кривая 2 (p2_s11)', color='blue', marker='s')
plt.plot(xy, p3_s11, label='Кривая 3 (p3_s11)', color='green', marker='^')
plt.plot(xy, p4_s11, label='Кривая 4 (p4_s11)', color='purple', marker='d')
plt.plot(xy, p5_s11, label='Кривая 5 (p5_s11)', color='orange', marker='x')

plt.xlabel('Ось X распределение от 0 до 2pi')
plt.ylabel('Ось значения для каждого пути по S11')
plt.title('График зависимости S11 от Teta')
plt.grid(True)
plt.legend(loc='upper left')
#plt.show()


with open('logs/path1_x_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p1_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p1_s12.append(float(values[1]))

with open('logs/path2_x_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p2_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p2_s12.append(float(values[1]))

with open('logs/path3_x_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p3_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p3_s12.append(float(values[1]))

with open('logs/path4_x_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p4_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p4_s12.append(float(values[1]))

with open('logs/path5_x_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p5_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p5_s12.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(xy, p1_s12, label='p1_s12', color='red', marker='o')
plt.plot(xy, p2_s12, label='p2_s12', color='blue', marker='s')
plt.plot(xy, p3_s12, label='p3_s12', color='green', marker='^')
plt.plot(xy, p4_s12, label='p4_s12', color='purple', marker='d')
plt.plot(xy, p5_s12, label='p5_s12', color='orange', marker='x')

plt.xlabel('Ось X распределение от 0 до 2pi')
plt.ylabel('Ось значения для каждого пути по S12')
plt.title('График зависимости S12 от Teta')
plt.grid(True)
plt.legend(loc='upper left')
#plt.show()

with open('logs/path1_x_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p1_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p1_s22.append(float(values[1]))

with open('logs/path2_x_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p2_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p2_s22.append(float(values[1]))

with open('logs/path3_x_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p3_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p3_s22.append(float(values[1]))

with open('logs/path4_x_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p4_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p4_s22.append(float(values[1]))

with open('logs/path5_x_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p5_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p5_s22.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(xy, p1_s22, label='p1_s22', color='red', marker='o')
plt.plot(xy, p2_s22, label='p2_s22', color='blue', marker='s')
plt.plot(xy, p3_s22, label='p3_s22', color='green', marker='^')
plt.plot(xy, p4_s22, label='p4_s22', color='purple', marker='d')
plt.plot(xy, p5_s22, label='p5_s22', color='orange', marker='x')

plt.xlabel('Ось X распределение от 0 до 2pi')
plt.ylabel('Ось значения для каждого пути по S22')
plt.title('График зависимости S22 от Teta')
plt.grid(True)
plt.legend(loc='upper left')
#plt.show()

with open('logs/path1_x_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p1_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p1_e11.append(float(values[1]))

with open('logs/path2_x_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p2_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p2_e11.append(float(values[1]))

with open('logs/path3_x_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p3_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p3_e11.append(float(values[1]))

with open('logs/path4_x_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p4_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p4_e11.append(float(values[1]))

with open('logs/path5_x_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p5_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p5_e11.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(xy, p1_e11, label='p1_e11', color='red', marker='o')
plt.plot(xy, p2_e11, label='p2_e11', color='blue', marker='s')
plt.plot(xy, p3_e11, label='p3_e11', color='green', marker='^')
plt.plot(xy, p4_e11, label='p4_e11', color='purple', marker='d')
plt.plot(xy, p5_e11, label='p5_e11', color='orange', marker='x')

plt.xlabel('Ось X распределение от 0 до 2pi')
plt.ylabel('Ось значения для каждого пути по e11')
plt.title('График зависимости e11 от Teta')
plt.grid(True)
plt.legend(loc='upper left')
#plt.show()

with open('logs/path1_x_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p1_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p1_e12.append(float(values[1]))

with open('logs/path2_x_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p2_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p2_e12.append(float(values[1]))

with open('logs/path3_x_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p3_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p3_e12.append(float(values[1]))

with open('logs/path4_x_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p4_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p4_e12.append(float(values[1]))

with open('logs/path5_x_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p5_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p5_e12.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(xy, p1_e12, label='p1_e12', color='red', marker='o')
plt.plot(xy, p2_e12, label='p2_e12', color='blue', marker='s')
plt.plot(xy, p3_e12, label='p3_e12', color='green', marker='^')
plt.plot(xy, p4_e12, label='p4_e12', color='purple', marker='d')
plt.plot(xy, p5_e12, label='p5_e12', color='orange', marker='x')

plt.xlabel('Ось X распределение от 0 до 2pi')
plt.ylabel('Ось значения для каждого пути по e12')
plt.title('График зависимости e12 от Teta')
plt.grid(True)
plt.legend(loc='upper left')
#plt.show()

with open('logs/path1_x_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p1_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p1_e22.append(float(values[1]))

with open('logs/path2_x_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p2_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p2_e22.append(float(values[1]))

with open('logs/path3_x_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p3_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p3_e22.append(float(values[1]))

with open('logs/path4_x_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p4_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p4_e22.append(float(values[1]))

with open('logs/path5_x_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p5_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p5_e22.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(xy, p1_e22, label='p1_e22', color='red', marker='o')
plt.plot(xy, p2_e22, label='p2_e22', color='blue', marker='s')
plt.plot(xy, p3_e22, label='p3_e22', color='green', marker='^')
plt.plot(xy, p4_e22, label='p4_e22', color='purple', marker='d')
plt.plot(xy, p5_e22, label='p5_e22', color='orange', marker='x')

plt.xlabel('Ось X распределение от 0 до 2pi')
plt.ylabel('Ось значения для каждого пути по e22')
plt.title('График зависимости e22 от Teta')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()




# Import time frame
with open('timefraeme/path6_1_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_1_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_1_s11.append(float(values[1]))

with open('timefraeme/path6_10_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_10_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_10_s11.append(float(values[1]))

with open('timefraeme/path6_15_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_15_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_15_s11.append(float(values[1]))

with open('timefraeme/path6_20_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_20_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_20_s11.append(float(values[1]))

with open('timefraeme/path6_30_s11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_30_s11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_30_s11.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(x, p6_1_s11, label='p6_1_s11', color='red', marker='o')
plt.plot(x, p6_10_s11, label='p6_10_s11', color='blue', marker='s')
plt.plot(x, p6_15_s11, label='p6_15_s11', color='green', marker='^')
plt.plot(x, p6_20_s11, label='p6_20_s11', color='purple', marker='d')
plt.plot(x, p6_30_s11, label='p6_30_s11', color='orange', marker='x')

plt.xlabel('Ось X распределение от трещины')
plt.ylabel('Ось значения для времени по s11')
plt.title('График зависимости s11 от времени')
plt.grid(True)
plt.legend(loc='upper right')
#plt.show()

with open('timefraeme/path6_1_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_1_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_1_s12.append(float(values[1]))

with open('timefraeme/path6_10_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_10_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_10_s12.append(float(values[1]))

with open('timefraeme/path6_15_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_15_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_15_s12.append(float(values[1]))

with open('timefraeme/path6_20_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_20_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_20_s12.append(float(values[1]))

with open('timefraeme/path6_30_s12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_30_s12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_30_s12.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(x, p6_1_s12, label='p6_1_s12', color='red', marker='o')
plt.plot(x, p6_10_s12, label='p6_10_s12', color='blue', marker='s')
plt.plot(x, p6_15_s12, label='p6_15_s12', color='green', marker='^')
plt.plot(x, p6_20_s12, label='p6_20_s12', color='purple', marker='d')
plt.plot(x, p6_30_s12, label='p6_30_s12', color='orange', marker='x')

plt.xlabel('Ось X распределение от трещины')
plt.ylabel('Ось значения для времени по s12')
plt.title('График зависимости s12 от времени')
plt.grid(True)
plt.legend(loc='upper right')
#plt.show()

with open('timefraeme/path6_1_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_1_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_1_s22.append(float(values[1]))

with open('timefraeme/path6_10_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_10_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_10_s22.append(float(values[1]))

with open('timefraeme/path6_15_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_15_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_15_s22.append(float(values[1]))

with open('timefraeme/path6_20_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_20_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_20_s22.append(float(values[1]))

with open('timefraeme/path6_30_s22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_30_s22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_30_s22.append(float(values[1]))

plt.figure(figsize=(13, 8))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(np.log10(x), np.log10(p6_1_s22), label='p6_1_s22', color='red', marker='o')
plt.plot(np.log10(x), np.log10(p6_10_s22), label='p6_10_s22', color='blue', marker='s')
plt.plot(np.log10(x), np.log10(p6_15_s22), label='p6_15_s22', color='green', marker='^')
plt.plot(np.log10(x), np.log10(p6_20_s22), label='p6_20_s22', color='purple', marker='d')
plt.plot(np.log10(x), np.log10(p6_30_s22), label='p6_30_s22', color='orange', marker='x')

plt.xlabel('Ось X распределение от трещины')
plt.ylabel('Ось значения для времени по s22')
plt.title('График зависимости s22 от времени')
plt.grid(True, which='major', axis='both', linestyle="--", linewidth=0.5)
plt.minorticks_on()
plt.grid(which='minor', color = 'lightgray', linestyle = ':')
#plt.xticks(np.arange(-5, 1, 0.2))
plt.yticks(np.arange(0, 2.2, 0.2))
plt.legend(loc='upper right')
#plt.show()

with open('timefraeme/path6_1_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_1_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_1_e11.append(float(values[1]))

with open('timefraeme/path6_10_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_10_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_10_e11.append(float(values[1]))

with open('timefraeme/path6_15_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_15_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_15_e11.append(float(values[1]))

with open('timefraeme/path6_20_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_20_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_20_e11.append(float(values[1]))

with open('timefraeme/path6_30_e11.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_30_e11 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_30_e11.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(x, p6_1_e11, label='p6_1_e11', color='red', marker='o')
plt.plot(x, p6_10_e11, label='p6_10_e11', color='blue', marker='s')
plt.plot(x, p6_15_e11, label='p6_15_e11', color='green', marker='^')
plt.plot(x, p6_20_e11, label='p6_20_e11', color='purple', marker='d')
plt.plot(x, p6_30_e11, label='p6_30_e11', color='orange', marker='x')

plt.xlabel('Ось X распределение от трещины')
plt.ylabel('Ось значения для времени по e11')
plt.title('График зависимости e11 от времени')
plt.grid(True)
plt.legend(loc='upper right')
#plt.show()

with open('timefraeme/path6_1_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_1_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_1_e12.append(float(values[1]))

with open('timefraeme/path6_10_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_10_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_10_e12.append(float(values[1]))

with open('timefraeme/path6_15_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_15_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_15_e12.append(float(values[1]))

with open('timefraeme/path6_20_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_20_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_20_e12.append(float(values[1]))

with open('timefraeme/path6_30_e12.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_30_e12 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_30_e12.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(x, p6_1_e12, label='p6_1_e12', color='red', marker='o')
plt.plot(x, p6_10_e12, label='p6_10_e12', color='blue', marker='s')
plt.plot(x, p6_15_e12, label='p6_15_e12', color='green', marker='^')
plt.plot(x, p6_20_e12, label='p6_20_e12', color='purple', marker='d')
plt.plot(x, p6_30_e12, label='p6_30_e12', color='orange', marker='x')

plt.xlabel('Ось X распределение от трещины')
plt.ylabel('Ось значения для времени по e12')
plt.title('График зависимости e12 от времени')
plt.grid(True)
plt.legend(loc='upper right')
#plt.show()

with open('timefraeme/path6_1_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_1_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_1_e22.append(float(values[1]))

with open('timefraeme/path6_10_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_10_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_10_e22.append(float(values[1]))

with open('timefraeme/path6_15_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_15_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_15_e22.append(float(values[1]))

with open('timefraeme/path6_20_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_20_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_20_e22.append(float(values[1]))

with open('timefraeme/path6_30_e22.rpt', 'r') as file:
    next(file)
    next(file)
    next(file)
    x = []
    p6_30_e22 = []
    for line in file:
        line = line.strip()
        values = line.split()
        if len(values) == 2:
            x.append(float(values[0]))
            p6_30_e22.append(float(values[1]))

plt.figure(figsize=(10, 6))  # Задаем размер графика

# Рисуем графики для каждого массива
plt.plot(x, p6_1_e22, label='p6_1_e22', color='red', marker='o')
plt.plot(x, p6_10_e22, label='p6_10_e22', color='blue', marker='s')
plt.plot(x, p6_15_e22, label='p6_15_e22', color='green', marker='^')
plt.plot(x, p6_20_e22, label='p6_20_e22', color='purple', marker='d')
plt.plot(x, p6_30_e22, label='p6_30_e22', color='orange', marker='x')

plt.xlabel('Ось X распределение от трещины')
plt.ylabel('Ось значения для времени по e22')
plt.title('График зависимости e22 от времени')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()