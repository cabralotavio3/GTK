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
        jnl.set_title("tenha") # Define o título da janela.
        jnl.set_border_width(10)

        # cxh = Gtk.Box(spacing = 30, homogeneous = True)
        cxh = Gtk.Box()
        cxh.set_spacing(30)
        cxh.set_homogeneous(True)

        bt_paz = Gtk.Button()
        bt_paz.connect("clicked", self.imprimir, 1)
        bt_paz.set_label("paz")
        cxh.add(bt_paz)

        bt_fe = Gtk.Button()
        bt_fe.connect("clicked", self.imprimir, 2)
        bt_fe.set_label("fe")
        cxh.add(bt_fe)

        bt_coragem = Gtk.Button()
        bt_coragem.connect("clicked", self.imprimir, 3)
        bt_coragem.set_label("coragem")
        cxh.add(bt_coragem)

        jnl.add(cxh)
        jnl.show_all()

    def imprimir(self, componente=None, dados=None):
        """ mostrar saudacao"""
        msg = componente.get_label()
        print(":) {} :)".format(msg * dados))

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Dormiu")
        raise SystemExit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()


