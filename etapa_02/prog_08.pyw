#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pythom e Gtk
# Prof. Douglas Machado Tavares

# Caixa é igual ao coração de mãe, sempre cabe mais um :-D

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da Aplicação """

    def __init__(self):
        """ __init__() -> instância de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("Python e Gtk")
        jnl.set_border_width(10)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=True, spacing=10)
        # cxv = Gtk.Box()
        # cxv.set_orientation(Gtk.Orientation.VERTICAL)
        # cxv.set_homogeneous(True)
        # cxv.set_spacing(10)

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=True, spacing=10)
        cxh.set_border_width(10)

        # cxh = Gtk.Box()
        # cxh.set_orientation(Gtk.Orientation.HORIZONTAL)
        # cxh.set_homogeneous(True)
        # cxh.set_spacing(10)


        self.rtl_mensagem = Gtk.Label()
        self.rtl_mensagem.set_label('---X---')

        bt_ok = Gtk.Button()
        bt_ok.connect("clicked", self.exibir_mensagem)
        bt_ok.set_label("_Ok")
        bt_ok.set_use_underline(True)
        cxh.add(bt_ok)

        bt_cancelar = Gtk.Button()
        bt_cancelar.connect("clicked", self.exibir_mensagem)
        bt_cancelar.set_label("_Cancelar")
        bt_cancelar.set_use_underline(True)
        cxh.add(bt_cancelar)

        cxv.add(cxh)
        cxv.add(self.rtl_mensagem)

        jnl.add(cxv)
        jnl.show_all()


    def exibir_mensagem(self, componente=None, dados=None):
        """ Exibe uma mensagem no rótulo """
        msg = componente.get_label()
        msg = msg.replace("_", "")
        msg = "<b>Rótulo:</b> {}".format(msg)
        self.rtl_mensagem.set_markup(msg)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
