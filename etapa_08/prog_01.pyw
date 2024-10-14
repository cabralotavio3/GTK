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
        jnl.set_title("Imagens :-)")

        img_1 = Gtk.Image()
        img_1.set_from_file("imagens_c/flor_amarela.jpg")

        img_2 = Gtk.Image(file="imagens_c/flor_laranja.jpg")
        #img_2 = Gtk.Image()
        #img_2.set_from_file("imagens_c/flor_laranja.jpg")

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=False, spacing=10)

        cxh.pack_start(img_1, False, False, 0)
        cxh.pack_end(img_2, False, False, 0)
        jnl.add(cxh)

        jnl.show_all()


    # Tratadores de eventos ou sinais:
    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()


if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()
