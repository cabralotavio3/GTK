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
                      homogeneous=False, spacing=10)
        # cxv = Gtk.Box()
        # cxv.set_orientation(Gtk.Orientation.VERTICAL)
        # cxv.set_homogeneous(True)
        # cxv.set_spacing(10)

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=True, spacing=10)
        cxh.set_border_width(10)

        qdr = Gtk.Frame()
        qdr.set_label("Sistema de cores")
        qdr.set_shadow_type(Gtk.ShadowType.IN) #OUT/NONE


        self.rtl_mensagem = Gtk.Label()
        self.rtl_mensagem.set_label('---X---')

        bt_aditivo = Gtk.Button()
        bt_aditivo.connect("clicked", self.exibir_mensagem_aditivo)
        bt_aditivo.set_label("_Aditivo")
        bt_aditivo.set_use_underline(True)
        cxh.add(bt_aditivo)

        bt_subtrativo = Gtk.Button()
        bt_subtrativo.connect("clicked", self.exibir_mensagem_subtrativo)
        bt_subtrativo.set_label("_Subtrativo")
        bt_subtrativo.set_use_underline(True)
        cxh.add(bt_subtrativo)

        qdr.add(cxh)
        cxv.add(qdr)
        cxv.add(self.rtl_mensagem)

        jnl.add(cxv)
        jnl.show_all()


    def exibir_mensagem_aditivo(self, componente=None, dados=None):
        """ Exibe uma mensagem no rótulo """

        msg = ("<big><b><i>Sistema aditivo️</i></b></big>: \n      \n"
                "Formado pelas <u>cores primárias</u>: \n"
                "<tt><b>"
                "Vermelho - <span color='#FF0000'>Red</span>\n"
                "Verde    - <span color='#00FF00'>Green</span>\n"
                "Azul     - <span color='#0000FF'>Blue</span>\n"
                "</b></tt>")
        self.rtl_mensagem.set_markup(msg)

    def exibir_mensagem_subtrativo(self, componente=None, dados=None):
        """ Exibe uma mensagem no rótulo """
        msg = ("<big><b><i>Sistema subtrativo</i></b></big>: \n      \n"
                "Formado pelas <u>cores primárias</u>: \n"
                "<tt><b>"
                "Ciano    - <span color='#00FFFF'>Cyan</span>\n"
                "Magenta  - <span color='#FF00FF'>Magenta</span>\n"
                "Amarelo  - <span color='#FFFF00'>Yellow</span>\n"
                "</b></tt>")
        self.rtl_mensagem.set_markup(msg)
# u = underline/ b = bold/ tt = fonte/ i = itálico

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
