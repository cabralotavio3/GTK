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
        rtl_formula.set_markup("<big><b>F  =  m  *  a</b></big>")
        cxv.add(rtl_formula)

        cxh_massa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=False, spacing=10)
        rtl_massa = Gtk.Label(label="<b>m (kg):</b>")
        rtl_massa.set_markup("<b>m (kg):</b>")
        cxe_massa = Gtk.Entry()

        cxh_massa.pack_end(cxe_massa, False, False, 5)
        cxh_massa.pack_end(rtl_massa, False, False, 5)

        cxv.add(cxh_massa)

        cxh_aceleracao = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=False, spacing=10)
        rtl_aceleracao = Gtk.Label(label="a (m/s²):")
        rtl_aceleracao.set_markup("<b>a (m/s²)</b>")
        cxe_aceleracao = Gtk.Entry()
        cxh_aceleracao.pack_end(cxe_aceleracao, False, False, 5)
        cxh_aceleracao.pack_end(rtl_aceleracao, False, False, 5)
        cxv.add(cxh_aceleracao)

        rtl_resposta = Gtk.Label()
        cxv.add(rtl_resposta)

        cxh_botoes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             homogeneous=False, spacing=10)

        bt_calcular = Gtk.Button(label="_Calcular", use_underline=True)
        bt_calcular.connect("clicked", self.calcular, [cxe_massa, cxe_aceleracao, rtl_resposta])
        bt_limpar = Gtk.Button(label="_Limpar", use_underline=True)
        bt_limpar.connect("clicked", self.limpar, [cxe_massa, cxe_aceleracao, rtl_resposta])
        bt_sair = Gtk.Button(label="Sai_r", use_underline=True)
        bt_sair.connect("clicked", self.sair)
        cxh_botoes.add(bt_calcular)
        cxh_botoes.add(bt_limpar)
        cxh_botoes.pack_end(bt_sair, False, False, 5)
        cxv.add(cxh_botoes)

        jnl.add(cxv)
        jnl.show_all()

    def calcular(self, componente=None, dados=None):
        """calcula a força"""
        cxe_m = dados[0]
        cxe_a = dados[1]
        rtl = dados[2]

        m = float(cxe_m.get_text())
        a = float(cxe_a.get_text())

        rtl.set_markup("<b>F</b> = {:.2f}N".format(m * a))

    def limpar(self, componente=None, dados=None):
        """ Inverter mensagem """
        cxe = dados[0]
        cxe_a = dados[1]
        rtl = dados[2]

        str_saida = " "


        rtl.set_label(str_saida)
        cxe.set_text(str_saida)
        cxe_a.set_text(str_saida)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
