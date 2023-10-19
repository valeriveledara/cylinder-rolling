import unittest
from tkinter import Tk
from app.app import CylinderRollingApp


class TestCylinderRollingApp(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = CylinderRollingApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_start_animation(self):
        # Проверяем, что анимация запускается без ошибок
        self.app.angle_entry.insert(0, "45")
        self.app.position_entry.insert(0, "100 100")
        self.app.start_animation()

    def test_about(self):
        # Проверяем, что окно "О программе" отображается без ошибок
        self.app._CylinderRollingApp__about()

    def test_help(self):
        # Проверяем, что окно справки отображается без ошибок
        self.app._CylinderRollingApp__help()

    def test_version(self):
        # Проверяем, что окно с информацией о версии отображается без ошибок
        self.app._CylinderRollingApp__version()


if __name__ == '__main__':
    unittest.main()
