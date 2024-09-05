#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Alterando rtl na janela

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """Define a Interface da aplicação. """

    def __init__(self):
        """__init()  ->  instância de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("tenha mais...") # Define o título da janela.
        jnl.set_border_width(10)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 30, homogeneous = True)

        cxh = Gtk.Box(spacing = 30, homogeneous = True)
        #cxh = Gtk.Box()
        #cxh.set_spacing(30)
        #cxh.set_homogeneous(True)
        #cxh.set_Orientation(Gtk.Orientation.HORIZONTAL)

        rtl_msg = Gtk.Label()
        rtl_msg.set_label("----X----")

        mensagens = ["Coragem", "Fé", "Bebidas", "Rock"]
        for msg in mensagens:
            bt = Gtk.Button()
            bt.connect("clicked", self.imprimir_mensagem, rtl_msg)
            bt.set_label(msg)
            cxh.add(bt)

        cxv.add(cxh)
        cxv.add(rtl_msg)
        jnl.add(cxv)
        jnl.show_all()

    def imprimir_mensagem(self, componente=None, dados=None):
        """ Exibe uma mensagem no rótulo"""
        msg = componente.get_label()
        msg = msg.lower()
        msg = "Você precisa de mais {}".format(msg)
        dados.set_label(msg)

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Dormiu")
        raise SystemExit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
