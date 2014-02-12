# -*- coding: utf-8 -*-
from lettuce import step, world
from splinter import Browser

@step(u'Dado que eu abri o navegador')
def dado_que_eu_abri_o_navegador(step):
    world.browser = Browser('firefox')
    assert True

@step(u'Então eu visito o endereço "([^"]*)"')
def entao_eu_visito_o_endereco_group1(step, group1):
    world.browser.visit(group1)
    assert True

@step(u'E fecho o navegador')
def e_fecho_o_navegador(step):
    world.browser.quit()
    assert True
