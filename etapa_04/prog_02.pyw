#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pythom e Gtk
# Prof. Douglas Machado Tavares

# Componente Caixa de Entrada

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da Aplicação """

    def __init__(self):
        """ __init__() -> instância de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("Invertendo ;-)")
        jnl.set_border_width(10)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=40)

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=False, spacing=0)

        rtl = Gtk.Label()
        cxe = Gtk.Entry()

        bt = Gtk.Button()
        bt.connect("clicked", self.inverter, [cxe, rtl])
        bt.set_label("Inverter")

        cxh.pack_end(bt, expand=False, fill=False, padding=10)
        cxh.pack_end(cxe, expand=False, fill=False, padding=10)
        cxv.pack_start(cxh, expand=False, fill=False, padding=10)
        cxv.pack_start(rtl, expand=False, fill=False, padding=10)

        jnl.add(cxv)
        jnl.show_all()


    def inverter(self, componente=None, dados=None):
        """ Inverter mensagem """
        cxe = dados[0]
        rtl = dados[1]
        str_entrada = cxe.get_text()
        str_saida = rtl.get_label()

        str_saida = '{}\n{}'.format(str_entrada[::-1], str_saida)


        rtl.set_label(str_saida)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
