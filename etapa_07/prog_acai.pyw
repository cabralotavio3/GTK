#OTÁVIO CABRAL E MIGUEL COSTA 


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
        jnl.set_title("Açaí é tudo de bom :-)")

        cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        
        msg = "<span color='#950391'><b>.:: Açaí Super 10 ::.</b></span>"
        rtl_acai = Gtk.Label(label=msg, use_markup=True)

        cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=True, spacing=10)
        
        cxv_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        

        cxv_tamanho = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        
        cxv_recipiente = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        
        qdr_tamanho = Gtk.Frame(label="Tamanho:")
        
        tamanho = ["300ml", "400ml", "500ml", "600ml", "700ml"]
        bte = None
        for c in tamanho:
            bte = Gtk.RadioButton(group =bte,label=c)
          #  bte.connect('toggled', self.limpar, rtl)
            cxv_tamanho.pack_start(bte, False, False, 0)
        qdr_tamanho.add(cxv_tamanho)

        qdr_recipiente = Gtk.Frame(label="Recipiente:")

        recipiente = ["Copo", "Tijela"]
        bte = None
        for c in recipiente:
            bte = Gtk.RadioButton(group =bte,label=c)
          #  bte.connect('toggled', self.limpar, rtl)
            cxv_recipiente.pack_start(bte, False, False, 0)
        qdr_recipiente.add(cxv_recipiente)

        cxv_1.pack_start(qdr_tamanho, False, False, 0)
        cxv_1.pack_start(qdr_recipiente, False, False, 0)

        cxv_2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)
        
        cxv_adicionais = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        homogeneous=False, spacing=10)

        qdr_adicionais = Gtk.Frame(label="Adicionais:")
        
        adicionais = ["Banana", "Passoca", "Chocolate", "Bis", "Morango", "Granola", "Leite em pó"]
        bte = None
        for c in adicionais:
            bte = Gtk.CheckButton(label=c)
          #  bte.connect('toggled', self.limpar, rtl)
            cxv_adicionais.pack_start(bte, False, False, 0)
        qdr_adicionais.add(cxv_adicionais)

        bt_enviar = Gtk.Button(label='_Enviar', use_underline=True)
        bt_enviar.connect('clicked', self.fechar_pedido, [cxv_tamanho, cxv_recipiente, cxv_adicionais])


        cxv_2.pack_start(qdr_adicionais, False, False, 0)
        cxv_2.pack_end(bt_enviar, False, False, 0)
        

        cxh.add(cxv_1)
        cxh.add(cxv_2)

        cxv.add(rtl_acai)
        cxv.pack_end(cxh, True, True, 0)

        jnl.add(cxv)
        jnl.show_all()

    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")

    def fechar_pedido(self, componente=None, dados=None):
        """Fecha o pedido do cliente e imprime um comprovante"""
        cxv_tamanho = dados[0]
        cxv_recipiente = dados[1]
        cxv_adicionais = dados[2]
        print("-" * 80)

        for botao in cxv_tamanho.get_children():
            tamanho = botao.get_label()
            estado = botao.get_active()
            if estado == True:
                tamanho = botao.get_label()
                print(f"Tamanho: {tamanho}")

        for botao in cxv_recipiente.get_children():
            recipiente = botao.get_label()
            estado = botao.get_active()
            if estado == True:
                recipiente = botao.get_label()
                print(f"Recipiente: {recipiente}")

        adic = "Adicionais: " 
        for botao in cxv_adicionais.get_children():
            adicional = botao.get_label()
            estado = botao.get_active()
            
            if estado == True:
                adicional = botao.get_label()
                adic += f" {adicional},"                
        adic = adic[:-1] + "."
        print(adic)



if __name__ == "__main__":
    prog = Aplicacao()
    Gtk.main()