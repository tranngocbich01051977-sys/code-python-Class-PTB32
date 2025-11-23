# Bài tập thực hành: 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt6 import uic #Sử dụng để tải giao diện
from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl # Lấy đường dẫn
from PyQt6.QtGui import QDesktopServices # Mở trang web
import sys # Mở Terminal

class Lorem:
    def __init__(self):
         super().__init__()
        uic.loadUi("./check/ui/NotebookMenu.ui", self)
    