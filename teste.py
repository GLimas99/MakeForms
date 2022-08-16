import sys
from novo.menu import *
from novo.obra import *
from novo.client import *
from novo.make_doc import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
import sqlite3
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from datetime import date
from num2words import num2words
from pathlib import Path


import os

Path(
                        '//ROGER2/Users/ROCHA/Documents/PROCESSO DE CLIENTES').mkdir(
                        parents=True, exist_ok=True)


