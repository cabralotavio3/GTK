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
        jnl.set_size_request(400, -1)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                     homogeneous=False, spacing=10)

        msg = ("<span color='#15155C' font='Bold 14'>"
                 "F  =  m  *  a"
               "</span>")
        rtl_formula = Gtk.Label(label=msg, use_markup=True)
        cxv.add(rtl_formula)

        cxh_massa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                           homogeneous=False, spacing=10)
        rtl_massa = Gtk.Label(label="<b>m (kg):</b>")
        rtl_massa.set_use_markup(True)
        cxe_massa = Gtk.Entry()
        cxe_massa.set_width_chars(16)
        cxh_massa.pack_end(cxe_massa, False, False, 5)
        cxh_massa.pack_end(rtl_massa, False, False, 5)
        cxv.add(cxh_massa)

        cxh_aceleracao = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                homogeneous=False, spacing=10)
        rtl_aceleracao = Gtk.Label(label="<b>a (m/s²):</b>",
                                  use_markup=True)
        cxe_aceleracao = Gtk.Entry()
        cxe_aceleracao.set_width_chars(16)
        cxh_aceleracao.pack_end(cxe_aceleracao, False, False, 5)
        cxh_aceleracao.pack_end(rtl_aceleracao, False, False, 5)
        cxv.add(cxh_aceleracao)

        msg = "<span color='#A4A4A4' font='Bold 14'> ... </span>"
        rtl_resposta = Gtk.Label(label=msg, use_markup=True)
        cxv.add(rtl_resposta)

        cxh_botoes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             homogeneous=False, spacing=10)

        bt_calcular = Gtk.Button(label="_Calcular", use_underline=True)
        bt_limpar = Gtk.Button(label="_Limpar", use_underline=True)
        bt_sair = Gtk.Button(label="Sai_r", use_underline=True)

        bt_calcular.connect("clicked", self.calcular, [cxe_massa,
                           cxe_aceleracao, rtl_resposta, bt_limpar])
        bt_limpar.connect("clicked", self.limpar,
                         [cxe_massa, cxe_aceleracao, rtl_resposta])
        bt_sair.connect("clicked", self.sair)

        bt_calcular.set_tooltip_text("Calcula a força em newtons")
        bt_limpar.set_tooltip_text("Limpa os campos")
        bt_sair.set_tooltip_text("Sai do aplicativo")

        cxe_massa.connect("activate", self.trocar_foco, cxe_aceleracao)
        cxe_aceleracao.connect("activate", self.trocar_foco, bt_calcular)

        cxh_botoes.pack_start(bt_calcular, False, False, 5)
        cxh_botoes.pack_start(bt_limpar, False, False, 5)
        cxh_botoes.pack_end(bt_sair, False, False, 5)
        cxv.pack_end(cxh_botoes, False, False, 0)

        jnl.add(cxv)
        jnl.show_all()


    def trocar_foco(self, componente=None, dados=None):
        """ Muda o foco para o componente recebido em dados """
        dados.grab_focus()


    def limpar(self, componente=None, dados=None):
        """ Limpa os campos """
        cxe_massa = dados[0]
        cxe_aceleracao = dados[1]
        rtl_resposta = dados[2]

        cxe_massa.set_text("")
        cxe_aceleracao.set_text("")
        msg = "<span color='#A4A4A4' font='Bold 14'> ... </span>"
        rtl_resposta.set_markup(msg)
        cxe_massa.grab_focus()


    def calcular(self, componente=None, dados=None):
        """ Calcula a forca em N """
        cxe_massa = dados[0]
        cxe_aceleracao = dados[1]
        rtl_resposta = dados[2]
        bt_limpar = dados[3]

        excecao = False
        try:
            a = float(cxe_aceleracao.get_text())
        except:
            excecao = True
            cxe_aceleracao.set_text("")
            cxe_aceleracao.grab_focus()
        try:
            m = float(cxe_massa.get_text())
        except:
            excecao = True
            cxe_massa.set_text("")
            cxe_massa.grab_focus()

        if not excecao:
            f = m * a
            msg = ("<span color='#15155C' font='14'>"
                      "<b>F</b> = {0:.4f} N"
                   "</span>")
            rtl_resposta.set_markup(msg.format(f))
            bt_limpar.grab_focus()
        else:
            msg = ("<span color='#AE4848' font='Bold 14'>"
                      "Entre com um número real"
                   "</span>")
            rtl_resposta.set_markup(msg)


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
