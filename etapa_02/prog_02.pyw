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
        jnl.set_title("Boa...") # Define o título da janela.
        jnl.set_border_width(10)

        bt_dia = Gtk.Button()
        bt_dia.connect("clicked", self.imprimir_saudacoes)
        bt_dia.set_label("Bom dia")

        bt_tarde = Gtk.Button()
        bt_tarde.connect("clicked", self.imprimir_saudacoes)
        bt_tarde.set_label("Boa tarde")

        bt_noite = Gtk.Button()
        bt_noite.connect("clicked", self.imprimir_saudacoes)
        bt_noite.set_label("Boa noite")

        cxh = Gtk.Box()
        cxh.add(bt_dia)
        cxh.add(bt_tarde)
        cxh.add(bt_noite)
        jnl.add(cxh)

        jnl.show_all()

    def imprimir_saudacoes(self, componente=None, dados=None):
        """ mostrar saudacao"""
        saudacao = componente.get_label()
        saudacao = saudacao.capitalize()
        print("Ola! {} pessoal".format(saudacao))

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Dormiu")
        raise SystemExit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()


