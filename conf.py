# Импортируем стандартные библиотеки Sphinx и устанавливаем путь до документации
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Настраиваем базовые параметры документации
project = 'CultureNet'
author = 'А.М. Синюхина, У.И. Загуменнов'
release = '0.1'
language = 'ru'

# Указываем расширения Sphinx, которые будут использоваться
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

# Указываем исходные файлы документации
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Указываем тему оформления
html_theme = 'alabaster'