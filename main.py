from controller.main_controller import MainController
from tkinter import Tk

root = Tk()
controller = MainController()
controller.create(root)
controller.start_app(root)
