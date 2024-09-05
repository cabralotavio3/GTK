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
        jnl.set_title("Empacotamento :-)")
        jnl.set_border_width(10)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=True, spacing=40)

        cxh_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=True, spacing=10)

        cxh_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=False, spacing=10)

        cxh_1.set_border_width(10)
        cxh_2.set_border_width(10)

        qdr_1 = Gtk.Frame(label="cxh  ->  homeneous=True:")
        qdr_2 = Gtk.Frame(label="cxh  ->  homogeneous=False:")

        bt_1 = Gtk.Button(label="Io")
        bt_2 = Gtk.Button(label="Europa")
        bt_3 = Gtk.Button(label="Ganímedes")
        bt_4 = Gtk.Button(label="Calisto")

        bt_5 = Gtk.Button(label="Io")
        bt_6 = Gtk.Button(label="Europa")
        bt_7 = Gtk.Button(label="Ganímedes")
        bt_8 = Gtk.Button(label="Calisto")

        bt_1.connect('clicked', self.aumentar_largura, jnl)
        bt_2.connect('clicked', self.aumentar_largura, jnl)
        bt_3.connect('clicked', self.aumentar_largura, jnl)
        bt_4.connect('clicked', self.aumentar_largura, jnl)
        bt_5.connect('clicked', self.aumentar_largura, jnl)
        bt_6.connect('clicked', self.aumentar_largura, jnl)
        bt_7.connect('clicked', self.aumentar_largura, jnl)
        bt_8.connect('clicked', self.aumentar_largura, jnl)

        cxh_1.add(bt_1)
        cxh_1.add(bt_2)
        cxh_1.add(bt_3)
        cxh_1.add(bt_4)

        cxh_2.add(bt_5)
        cxh_2.add(bt_6)
        cxh_2.add(bt_7)
        cxh_2.add(bt_8)

        qdr_1.add(cxh_1)
        qdr_2.add(cxh_2)

        cxv.add(qdr_1)
        cxv.add(qdr_2)

        jnl.add(cxv)
        jnl.show_all()

        self.largura, self.altura = jnl.get_size()


    def aumentar_largura(self, componente=None, dados=None):
        """ Aumenta a largura da janela """
        self.largura += 50
        dados.resize(self.largura, self.altura)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
