#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Orientação a Objetos

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """Define a Interface da aplicação. """

    def __init__(self):
        """__init()  ->  instância de Aplicação """
        janela = Gtk.Window()         # Instanciando um objeto do tipo Janela
        janela.show()                 # Pedindo para a janela se mostrar


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()



