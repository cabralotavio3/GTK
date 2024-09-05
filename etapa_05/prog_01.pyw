#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Interface amiga do usuario

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da aplicacao """

    def __init__(self):
        """ __init__() -> instancia de Aplicacao """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_border_width(10)
        jnl.set_title("Física")

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=10)

        rtl_formula = Gtk.Label()
        rtl_formula.set_label("F  =  m  *  a")
        cxv.add(rtl_formula)

        cxh_massa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=False, spacing=10)
        rtl_massa = Gtk.Label(label="m (kg):")
        cxe_massa = Gtk.Entry()
        cxh_massa.add(rtl_massa)
        cxh_massa.add(cxe_massa)
        cxv.add(cxh_massa)

        cxh_aceleracao = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=False, spacing=10)
        rtl_aceleracao = Gtk.Label(label="a (m/s²):")
        cxe_aceleracao = Gtk.Entry()
        cxh_aceleracao.add(rtl_aceleracao)
        cxh_aceleracao.add(cxe_aceleracao)
        cxv.add(cxh_aceleracao)

        rtl_resposta = Gtk.Label()
        cxv.add(rtl_resposta)

        cxh_botoes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             homogeneous=False, spacing=10)

        bt_calcular = Gtk.Button(label="_Calcular", use_underline=True)
        bt_sair = Gtk.Button(label="Sai_r", use_underline=True)
        cxh_botoes.add(bt_calcular)
        cxh_botoes.add(bt_sair)
        cxv.add(cxh_botoes)

        jnl.add(cxv)
        jnl.show_all()


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()
        print("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
