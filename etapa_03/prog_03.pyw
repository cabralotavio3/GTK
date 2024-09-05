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
        jnl.set_title("MATRIX")
        jnl.set_border_width(10)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=10)

        msg = ("<tt>"
               "<span font='20'><b>Morphel:</b></span>\n\n"
               " - Se tomar a pílula azul a história acaba e você"
               " acordará na sua cama acreditando\n"
               " no que quiser acreditar.\n\n"
               " - Se tomar a pílula vermelha ficará no País das"
               " Maravilhas e eu te mostrarei até\n"
               " onde vai a toca do coelho.\n\n"
               " - Lembre-se tudo o que ofereço é a verdade."
               " Nada mais.\n"
               "</tt>")
        rtl_msg = Gtk.Label(label=msg, use_markup=True)

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=False, spacing=10)

        vm = "<span color='red'><b>Vermelha</b></span>"
        rtl_vermelha = Gtk.Label(label=vm, use_markup=True)
        bt_vermelha = Gtk.Button()
        bt_vermelha.add(rtl_vermelha)
        bt_vermelha.connect('clicked', self.escolher_vermelha,
                            [rtl_msg, cxh])

        az = "<span color='blue'><b>Azul</b></span>"
        rtl_azul = Gtk.Label(label=az, use_markup=True)
        bt_azul = Gtk.Button()
        bt_azul.add(rtl_azul)
        bt_azul.connect('clicked', self.escolher_azul, [rtl_msg, cxh])

        bt_sair = Gtk.Button(label="Sai_r", use_underline=True)
        bt_sair.connect("clicked", self.sair)

        cxh.pack_start(bt_vermelha, False, False, 0)
        cxh.pack_start(bt_azul, False, False, 0)
        cxh.pack_end(bt_sair, False, False, 0)

        cxv.pack_start(rtl_msg, True, True, 0)
        cxv.pack_end(cxh, False, False, 0)

        jnl.add(cxv)
        jnl.show_all()


    def escolher_azul(self, componente=None, dados=None):
        """ Escolher pilula azul """
        rtl_msg, cxh = dados
        msg = "<span font='16'>Você acordou com uma dor de cabeça.</span>"
        rtl_msg.set_markup(msg)
        cxh.hide()


    def escolher_vermelha(self, componente=None, dados=None):
        """ Escolher pilula vermelha """
        rtl_msg, cxh = dados
        msg = ("<span font='16'>"
               "Você foi conduzido para uma outra sala.\n"
               "A aventura começou."
               "</span>")
        rtl_msg.set_markup(msg)
        cxh.hide()


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
