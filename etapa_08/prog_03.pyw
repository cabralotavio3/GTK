#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Componente Image

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da aplicação """

    def __init__(self):
        """ __init__() -> instancia de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_border_width(10)

        caminho = "imagens_b/figura_01.jpg"

        jnl.set_title(caminho)

        img = Gtk.Image()
        img.set_from_file(caminho)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=10)

        cxh_botoes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             homogeneous=False, spacing=10)

        img_voltar = Gtk.Image(file="icones/go-previous.svg")
        bt_voltar = Gtk.Button(label="_Voltar", use_underline=True,
                               image=img_voltar)

        img_avancar = Gtk.Image(file="icones/go-next.svg")
        bt_avancar = Gtk.Button(label="_Avançar", use_underline=True,
                                image=img_avancar)

        cxh_botoes.pack_start(bt_voltar, False, False, 0)
        cxh_botoes.pack_end(bt_avancar, False, False, 0)

        cxv.add(img)
        cxv.add(cxh_botoes)
        jnl.add(cxv)
        jnl.show_all()


    # Tratadores de eventos ou sinais:
    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação"""
        Gtk.main_quit()


if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()
