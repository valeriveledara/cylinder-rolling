from tkinter import Label, Button, Canvas, Menu, Entry, messagebox
import math
import time


class CylinderRollingApp:
    """Приложение для анимации скатывания цилиндра.

        Attributes:
            width (int): Ширина окна приложения.
            height (int): Высота окна приложения.
            root (tkinter.Tk): Корневое окно приложения.
            canvas (tkinter.Canvas): Область для рисования анимации.
            angle_label (tkinter.Label): Метка для ввода угла наклона.
            angle_entry (tkinter.Entry): Поле ввода угла наклона.
            position_label (tkinter.Label): Метка для ввода начального положения.
            position_entry (tkinter.Entry): Поле ввода начального положения.
            start_button (tkinter.Button): Кнопка для запуска анимации.
            cylinder (int): Объект, представляющий цилиндр на холсте.
            triangle (int): Объект, представляющий треугольник на холсте.
            __about_message (str): Информация о приложении для раздела "О программе".
            __version_message (str): Информация о версии приложения для раздела "Версия".
            __help_message (str): Информация о использовании приложения для раздела "Справка".
            __main_menu (tkinter.Menu): Главное меню приложения.

        Methods:
            __about: Отображает информационное окно о приложении.
            __help: Отображает окно с информацией о использовании приложения.
            __version: Отображает окно с информацией о версии приложения.
            start_animation: Запускает анимацию скатывания цилиндра.
        """

    def __init__(self, init_root, width=400, height=400, main_about="", main_version="", main_help=""):
        """Инициализация приложения.

        Args:
            init_root (tkinter.Tk): Корневое окно приложения.
            width (int, optional): Ширина окна приложения. По умолчанию 400.
            height (int, optional): Высота окна приложения. По умолчанию 400.
            main_about (str, optional): Информация "О программе". По умолчанию "".
            main_version (str, optional): Информация о версии приложения. По умолчанию "".
            main_help (str, optional): Информация о использовании приложения. По умолчанию "".
        """

        self.width = width
        self.height = height

        self.root = init_root
        self.root.title("Скатывание цилиндра")

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.angle_label = Label(self.root, text="Угол наклона (градусы):")
        self.angle_label.pack()

        self.angle_entry = Entry(self.root)
        self.angle_entry.pack()

        self.position_label = Label(self.root, text="Начальное положение (x, y):")
        self.position_label.pack()

        self.position_entry = Entry(self.root)
        self.position_entry.pack()

        self.start_button = Button(self.root, text="Старт", command=self.start_animation)
        self.start_button.pack()

        self.cylinder = None
        self.triangle = None

        # меню
        self.__about_message = main_about
        self.__version_message = main_version
        self.__help_message = main_help
        self.__main_menu = Menu(self.root)
        self.__main_menu.add_command(label="About", command=self.__about)
        self.__main_menu.add_command(label="Help", command=self.__help)
        self.__main_menu.add_command(label="Version", command=self.__version)

        self.root.config(menu=self.__main_menu)

    def __about(self):
        """Отображает информационное окно "О программе"."""

        messagebox.showinfo("About", self.__about_message)

    def __help(self):
        """Отображает окно с информацией о использовании приложения."""

        messagebox.showinfo("Help", self.__help_message)

    def __version(self):
        """Отображает окно с информацией о версии приложения."""

        messagebox.showinfo("Version", self.__version_message)

    def start_animation(self):
        """Запускает анимацию скатывания цилиндра."""

        self.canvas.delete("all")

        angle = float(self.angle_entry.get())
        x, y = map(int, self.position_entry.get().split())

        rad = 40

        self.cylinder = self.canvas.create_oval(x, y, x + rad, y + rad, fill="blue")

        # Определяем координаты вершин треугольника
        x1, y1 = x + rad / 4, y + rad
        x2, y2 = x1, self.width

        x3, y3 = (x1 + (y2 - y1) * math.tan(math.radians(90 - angle)), self.width)

        # Рисуем треугольник
        self.triangle = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="green")

        while y < self.height - rad:
            self.root.update()
            time.sleep(0.01)
            self.canvas.move(self.cylinder, math.cos(math.radians(angle)), math.sin(math.radians(angle)))
            x, y, _, _ = self.canvas.coords(self.cylinder)
            if x < 0 or x > self.width - rad:
                break

