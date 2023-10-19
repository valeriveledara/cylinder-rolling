from storage.storage import Storage
from app.app import CylinderRollingApp


class MainController:
    """Класс MainController предоставляет методы для создания и запуска приложения.

    Methods:
        create(root): Создает экземпляр приложения CylinderRollingApp.
        start_app(root): Запускает главный цикл приложения.
    """

    @staticmethod
    def create(root):
        """Создает экземпляр приложения CylinderRollingApp.

        Args:
            root: Экземпляр корневого окна Tkinter.

        Returns:
            CylinderRollingApp: Экземпляр приложения для анимации скатывания цилиндра.
        """
        storage = Storage()
        main_about = storage.get_about()
        main_version = storage.get_version()
        main_help = storage.get_help()

        return CylinderRollingApp(root, 1000, 400, main_about, main_version, main_help)

    @staticmethod
    def start_app(root):
        """Запускает главный цикл приложения.

        Args:
            root: Экземпляр корневого окна Tkinter.
        """
        root.mainloop()
