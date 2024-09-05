#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Uma outra maneira de fazer as coisas

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """Define a Interface da aplicação. """

    def __init__(self):
        """__init()  ->  instância de Aplicação """
        janela = Gtk.Window(title = "Python e GTK")
        rotulo = Gtk.Label(label = "Ok Pessoal ;-)")

        janela.add(rotulo)
        rotulo.show()
        janela.show()


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()





