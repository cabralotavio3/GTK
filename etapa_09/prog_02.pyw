#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Componente Paned

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicação:
    """ Define a interface da aplicação """

    def __init__(self):
        """ __init__() -> instancia de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("Painel :-)")
        jnl.set_border_width(10)
        jnl.resize(800, 500)

        img_1 = Gtk.Image(file="imagens_c/flor_amarela.jpg")
        img_2 = Gtk.Image(file="imagens_c/flor_laranja.jpg")

        pnv = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL) # horizontal ou vertical
        pnv.set_wide_handle(True) #colocar a marca de onde vai mexer
        pnv.set_position(400) #onde vai iniciar

        pnv.pack1(img_1, True, True)
        pnv.pack2(img_2, False, False)
        jnl.add(pnv)

        jnl.show_all()


    # Tratadores de eventos ou sinais:
    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()


if __name__ == '__main__':
    prog = Aplicação()
    Gtk.main()
