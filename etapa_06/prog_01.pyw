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
        # jnl.set_resizable(False)

        qdr = Gtk.Frame(label="Características da Personagem:")

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)

        cxv_botoes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        cxv_botoes.set_border_width(10)

        rtl = Gtk.Label()

        caracteristicas = ["Força", "Inteligância", "Vigor", "Presença", "Agilidade"]


        bte_energia = Gtk.RadioButton(group=None,label="Vigor")
        bte_energia.connect("toggled", self.exibir_marcado, rtl)
        cxv_botoes.pack_start(bte_energia, False, False, 0)

        bte_forca = Gtk.RadioButton(group=bte_energia,label="Força")
        bte_forca.connect("toggled", self.exibir_marcado, rtl)
        cxv_botoes.pack_start(bte_forca, False, False, 0)

        bte_agilidade = Gtk.RadioButton(group=bte_forca,label="Agilidade")
        bte_agilidade.connect("toggled", self.exibir_marcado, rtl)
        cxv_botoes.pack_start(bte_agilidade, False, False, 0)

        qdr.add(cxv_botoes)
        cxv.add(qdr)
        cxv.add(rtl)

        jnl.add(cxv)
        jnl.show_all()


    def exibir_marcado(self, componente=None, dados=None):
        """ Exibe a característica marcada """
        rtl = dados

        caracteristica = componente.get_label()
        estado = componente.get_active()
        msg = "<b>{}:</b> {}".format(caracteristica, estado)
        rtl.set_markup(msg)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()
