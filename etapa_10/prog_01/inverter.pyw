#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Componente Caixa de Entrada

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da Aplicação """

    def __init__(self):
        """ __init__() -> instância de Aplicação """
        self.gui = Gtk.Builder()
        self.gui.add_from_file('inverter.ui~')
        self.gui.connect_signals(self)

        jnl = self.gui.get_object('jnl')
        jnl.show_all()


    def inverter(self, componente=None, dados=None):
        """ Inverte a mensagem """
        rtl = self.gui.get_object('rtl')
        cxe = self.gui.get_object('cxe')

        msg_entrada = cxe.get_text()
        msg_saida = rtl.get_label()
        msg = "<b><span color='#FF00FF'>{}:</span></b> {}\n{}"
        msg = msg.format(msg_entrada, msg_entrada[::-1], msg_saida)
        rtl.set_markup(msg)
        cxe.set_text("")
        cxe.grab_focus()


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
