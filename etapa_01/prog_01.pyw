#!/usr/bin/env python
# -*- coding: utf - 8 -*-

# Python e GTK
# Prof. Douglas Machado Tavares

# Uma Janela Vazia

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

janela = Gtk.Window()         # Instanciando um objeto do tipo Janela
janela.show()                 # Pedindo para a janela se mostrar
Gtk.main()                    # Loop principal Gtk (Vovó Fofoqueira)


