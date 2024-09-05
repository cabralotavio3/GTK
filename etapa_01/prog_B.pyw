#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Tinha um botão no meio do caminho

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """Define a Interface da aplicação. """

    def __init__(self):
        """__init()  ->  instância de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("Multiplos de 3") # Define o título da janela.
        jnl.set_border_width(10)

        bt = Gtk.Button()
        bt.connect("clicked", self.multiplos)
        bt.set_label("0")

        jnl.add(bt)
        bt.show()
        jnl.show()

    def multiplos(self, componente=None, dados=None):
        """Muda de amor para odio e vice versa"""
        msg = componente.get_label()
        componente.set_label(str(int(msg) + 3))

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")
        raise SystemExit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()


