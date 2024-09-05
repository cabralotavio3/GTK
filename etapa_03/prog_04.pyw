#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Empacotando com pack_start e pack_end

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da aplicacao """

    def __init__(self):
        """ __init__() -> instancia de Aplicacao """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("Clarice Lispector")
        jnl.set_border_width(20)

        poema = ("Sou como você me vê.\n"
                 "Posso ser leve como uma brisa ou "
                 "forte como uma ventania.\n"
                 "Depende de quando e como você me vê passar.")

        rtl_1 = Gtk.Label(label=poema)
        rtl_2 = Gtk.Label(label=poema)
        rtl_3 = Gtk.Label(label=poema)

        rtl_1.set_justify(Gtk.Justification.CENTER)
        rtl_2.set_justify(Gtk.Justification.LEFT)
        rtl_3.set_justify(Gtk.Justification.RIGHT)

        rtl_2.set_selectable(True)
        rtl_3.set_selectable(True)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=40)

        cxv.add(rtl_1)
        cxv.add(rtl_2)
        cxv.add(rtl_3)

        jnl.add(cxv)
        jnl.show_all()


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
