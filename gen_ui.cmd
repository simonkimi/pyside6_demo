set pa=%cd%
path=%path%;%pa%\venv\Scripts
cd ui/xml

pyside6-uic main_window.ui -o ../../gen/main_window.py