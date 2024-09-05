#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# No meio do caminho tinha um botão

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
        bt.connect("clicked", self.imprimir_saudacoes)
        bt.set_label("Ok pessoal :-)")

        jnl.add(bt)
        bt.show()
        jnl.show()


    def imprimir_saudacoes(self, componente=None, dados=None):
        """ Imprime uma saudação """
        print("Ok pessoal ;-)")


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")
        raise SystemExit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()








