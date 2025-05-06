import tkinter as tk
from tkinter import ttk, messagebox
import random


class ArrayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Обработка массивов")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Фрейм для ввода данных
        input_frame = ttk.LabelFrame(self.root, text="Ввод параметров", padding=10)
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        ttk.Label(input_frame, text="Размер массива:").grid(row=0, column=0, padx=5, pady=5)
        self.size_entry = ttk.Entry(input_frame)
        self.size_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Диапазон значений:").grid(row=1, column=0, padx=5, pady=5)
        self.min_entry = ttk.Entry(input_frame, width=8)
        self.min_entry.grid(row=1, column=1, padx=5, pady=5)
        self.min_entry.insert(0, "-5")

        ttk.Label(input_frame, text="до").grid(row=1, column=2, padx=5, pady=5)
        self.max_entry = ttk.Entry(input_frame, width=8)
        self.max_entry.grid(row=1, column=3, padx=5, pady=5)
        self.max_entry.insert(0, "5")

        # Кнопки заданий
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.task1_btn = ttk.Button(btn_frame, text="Задание 1", command=self.run_task1)
        self.task1_btn.pack(side=tk.LEFT, padx=5)

        self.task2_btn = ttk.Button(btn_frame, text="Задание 2", command=self.run_task2)
        self.task2_btn.pack(side=tk.LEFT, padx=5)

        self.generate_btn = ttk.Button(btn_frame, text="Сгенерировать массив", command=self.generate_array)
        self.generate_btn.pack(side=tk.LEFT, padx=5)

        # Вывод массива
        self.array_label = ttk.Label(self.root, text="Массив не сгенерирован", font=('Arial', 10))
        self.array_label.pack(pady=5)

        # Фрейм для результатов
        self.result_frame = ttk.LabelFrame(self.root, text="Результаты", padding=10)
        self.result_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(self.result_frame, height=15, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # Инициализация массива
        self.array = []

    def generate_array(self):
        try:
            size = int(self.size_entry.get())
            min_val = float(self.min_entry.get())
            max_val = float(self.max_entry.get())

            if size <= 0:
                messagebox.showerror("Ошибка", "Размер массива должен быть положительным числом")
                return

            self.array = [round(random.uniform(min_val, max_val), 2) for _ in range(size)]
            self.array_label.config(text=f"Массив: {self.array}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Массив сгенерирован. Выберите задание для обработки.")

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def run_task1(self):
        if not self.array:
            messagebox.showwarning("Предупреждение", "Сначала сгенерируйте массив")
            return

        self.result_text.delete(1.0, tk.END)
        result = "=== Результаты задания 1 ===\n"

        # 1. Сумма элементов с нечетными номерами
        sum_odd = sum(self.array[i] for i in range(0, len(self.array), 2))
        result += f"1. Сумма элементов с нечетными номерами: {sum_odd:.2f}\n"

        # 2. Сумма между первым и последним отрицательными элементами
        first_neg = next((i for i, x in enumerate(self.array) if x < 0), None)
        last_neg = next((i for i, x in enumerate(reversed(self.array)) if x < 0), None)

        if first_neg is not None and last_neg is not None:
            last_neg = len(self.array) - 1 - last_neg
            if first_neg < last_neg:
                sum_between = sum(self.array[first_neg + 1:last_neg])
                result += f"2. Сумма между первым и последним отрицательными: {sum_between:.2f}\n"
            else:
                result += "2. Нет элементов между первым и последним отрицательными\n"
        else:
            result += "2. В массиве нет отрицательных элементов\n"

        # 3. Сжать массив
        compressed = [x for x in self.array if abs(x) > 1]
        zeros = [0] * (len(self.array) - len(compressed))
        compressed += zeros
        result += f"3. Сжатый массив: {[round(x, 2) for x in compressed]}\n"

        self.result_text.insert(tk.END, result)

    def run_task2(self):
        if not self.array:
            messagebox.showwarning("Предупреждение", "Сначала сгенерируйте массив")
            return

        self.result_text.delete(1.0, tk.END)
        result = "=== Результаты задания 2 ===\n"

        # 1. Количество нулевых элементов
        zero_count = sum(1 for x in self.array if x == 0)
        result += f"1. Количество нулевых элементов: {zero_count}\n"

        # 2. Сумма после минимального элемента
        min_index = self.array.index(min(self.array))
        if min_index < len(self.array) - 1:
            sum_after_min = sum(self.array[min_index + 1:])
            result += f"2. Сумма после минимального элемента: {sum_after_min:.2f}\n"
        else:
            result += "2. Минимальный элемент последний, сумма после него: 0\n"

        # 3. Сортировка по возрастанию модулей
        sorted_arr = sorted(self.array, key=lambda x: abs(x))
        result += f"3. Массив, отсортированный по модулям: {[round(x, 2) for x in sorted_arr]}\n"

        self.result_text.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayApp(root)
    root.mainloop()