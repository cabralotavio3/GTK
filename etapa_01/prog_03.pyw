#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Finalmente o epserado "Ok pessoal"

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """Define a Interface da aplicação. """

    def __init__(self):
        """__init()  ->  instância de Aplicação """
        janela = Gtk.Window()
        janela.set_title("Python e GTK") # Define o título da janela.

        rotulo = Gtk.Label() # Nome de classes -> notação camelo!!!
        rotulo.set_label("Ok Pessoal ;-)")

        janela.add(rotulo)
        rotulo.show()
        janela.show()


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()




