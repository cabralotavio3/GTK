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

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=True, spacing=10)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=10)

        emoji = ["_Feliz", "_Triste", "_Rindo", "_Surpreso", "_Desapontado", "_Indiferente"]
        for msg in emoji:
            bt = Gtk.Button()
            bt.connect("clicked", self.exibir_mensagem)
            bt.set_label(msg)
            bt.set_use_underline(True)
            cxv.add(bt)


        qdr = Gtk.Frame(label="emojis: ")

        cxh.set_border_width(10)

        self.rtl_mensagem = Gtk.Label()
        self.rtl_mensagem.set_label('---X---')

        cxh.add(qdr)
        qdr.add(self.rtl_mensagem)
        cxh.add(cxv)

        jnl.add(cxh)
        jnl.show_all()


    def exibir_mensagem(self, componente=None, dados=None):
        """ Exibe uma mensagem no rótulo """
        label = componente.get_label()
        if label == "_Feliz":
            msg = "<span font='bold 16'>:-)</span>"
        elif label == "_Triste":
            msg = "<span font='bold 16'>:-(</span>"
        elif label == "_Rindo":
            msg = "<span font='bold 16'>:-D</span>"
        elif label == "_Surpreso":
            msg = "<span font='bold 16'>:-o</span>"
        elif label == "_Desapontado":
            msg = "<span font='bold 16'>:-/</span>"
        elif label == "_Indiferente":
            msg = "<span font='bold 16'>:-|</span>"
        self.rtl_mensagem.set_markup(msg)
        self.rtl_mensagem.set_angle(-90)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
