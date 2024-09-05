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
        jnl.set_title("Python e GTK") # Define o título da janela.
        jnl.set_border_width(10)

        bt = Gtk.Button()
        bt.connect("clicked", self.amor_odio)
        bt.set_label("Amor")

        jnl.add(bt)
        bt.show()
        jnl.show()

    def amor_odio(self, componente=None, dados=None):
        """Muda de amor para odio e vice versa"""
        msg = componente.get_label()
        if msg == "Amor":
            componente.set_label("Ódio")
        else:
            componente.set_label("Amor")

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")
        raise SystemExit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()









