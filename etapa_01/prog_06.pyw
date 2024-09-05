#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Nome de componentes com .:: prefixos ::.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """Define a Interface da aplicação. """

    def __init__(self):
        """__init()  ->  instância de Aplicação """
        jnl = Gtk.Window()
        jnl.set_title("Python e GTK") # Define o título da janela.
        jnl.set_border_width(10)

        rtl = Gtk.Label() # Nome de classes -> notação camelo!!!
        rtl.set_label("Ok Pessoal ;-)")
        rtl.set_angle(45)

        jnl.add(rtl)
        rtl.show()
        jnl.show()


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()






