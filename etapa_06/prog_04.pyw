#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Componente Botão de Visto - CheckButton

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da Aplicação """

    def __init__(self):
        """ __init__() -> instância de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_border_width(10)
        jnl.set_title("RPG")

        qdr = Gtk.Frame(label="Características da Personagem:")

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)

        cxv_botoes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        cxv_botoes.set_border_width(10)

        rtl = Gtk.Label()

        bt_aplicar = Gtk.Button(label='Aplicar', use_underline=True)
        bt_aplicar.connect('clicked', self.exibir_marcados, [rtl, cxv_botoes])


        caracteristicas = ["Força", "Inteligância", "Vigor", "Presença", "Agilidade"]

        for c in caracteristicas:
            btv = Gtk.CheckButton(label=c)
            btv.connect('toggled', self.limpar, rtl)
            cxv_botoes.pack_start(btv, False, False, 0)


        qdr.add(cxv_botoes)
        cxv.add(qdr)
        cxv.pack_end(bt_aplicar, False, False, 0)
        cxv.add(rtl)

        jnl.add(cxv)
        jnl.show_all()


    def exibir_marcados(self, componente=None, dados=None):
        """ Exibe a característica marcada """
        rtl = dados[0]
        cxv_botoes = dados[1]

        dic = {}
        for botao in cxv_botoes.get_children():
            caracteristica = botao.get_label()
            estado = botao.get_active()
            if estado == True:
                dic[caracteristica] = estado
            rtl.set_markup('{}'.format(dic))

    def limpar(self, componente=None, dados=None):
        """limpa tudo"""
        rtl = dados
        rtl.set_label('')


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()
