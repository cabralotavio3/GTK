#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Componente Image

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

def retornar_nomes(pasta):
    """Retorna o nome de todos os arquivos de imagem"""
    validas = ["jpg", "png", "jpeg"]
    lista_nomes = []
    for nome in os.listdir(pasta):
        extensao = nome.split("-")[-1]
        if extensao in validas:
            lista_nomes.append(nome)
    lista_nomes.sort()
    return lista_nomes

class Aplicacao:
    """ Define a interface da aplicação """

    def __init__(self):
        """ __init__() -> instancia de Aplicação """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_border_width(10)

        self.cursor = 0

        self.pasta = "imagens_a"

        self.lista_nomes =retornar_nomes(self.pasta)

        atual = self.lista_nomes[self.cursor]

        caminho = "{}/{}".format(self.pasta, atual)

        jnl.set_title(caminho)

        img = Gtk.Image()
        img.set_from_file(caminho)

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      homogeneous=False, spacing=10)

        cxh_botoes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             homogeneous=False, spacing=10)

        img_voltar = Gtk.Image(file="icones/go-previous.svg")
        bt_voltar = Gtk.Button(label="_Voltar", use_underline=True,
                               image=img_voltar)
        bt_voltar.connect("clicked", self.navegar, [jnl, img, -1])

        img_avancar = Gtk.Image(file="icones/go-next.svg")
        bt_avancar = Gtk.Button(label="_Avançar", use_underline=True,
                                image=img_avancar)
        
        bt_avancar.connect("clicked", self.navegar, [jnl, img, 1])

        cxh_botoes.pack_start(bt_voltar, False, False, 0)
        cxh_botoes.pack_end(bt_avancar, False, False, 0)

        cxv.pack_start(img, False, False, 0)
        cxv.pack_end(cxh_botoes, False, False, 0)
        jnl.add(cxv)
        jnl.show_all()


    # Tratadores de eventos ou sinais:
    def navegar(self, componente=None, dados=None):
        """ Navega pelas imagens"""
        jnl = dados[0] 
        img = dados[1]
        delta = dados[2]

        self.cursor += delta
        if self.cursor < 0:
            self.cursor = len(self.lista_nomes)

        if self.cursor > len(self.lista_nomes):
            self.cursor = self.minimo

        nome_arq = self.lista_nomes[self.cursor]
        caminho = "{}/{}".format(self.pasta, nome_arq)

        jnl.set_title(caminho)
        img.set_from_file(caminho)

    # Tratadores de eventos ou sinais:
    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação"""
        Gtk.main_quit()


if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()
