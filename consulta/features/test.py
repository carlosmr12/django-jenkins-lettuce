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

@step(u'E preencho todos os campos do formulário')
def e_preencho_todos_os_campos_do_formulario(step):
    if not world.browser.find_by_id('inputSuccess2'):
        assert False

    world.browser.find_by_id('inputSuccess2').fill('firstInput')

    if not world.browser.find_by_id('inputWarning2'):
        assert False

    world.browser.find_by_id('inputWarning2').fill('secondInput')

    if not world.browser.find_by_id('inputError2'):
        assert False

    world.browser.find_by_id('inputError2').fill('thirdInput')
    assert True

@step(u'Então eu clico no botão "([^"]*)"')
def entao_eu_clico_no_botao_group1(step, group1):
    if not world.browser.find_link_by_text(group1):
        assert False
    world.browser.find_link_by_text(group1).click()
    assert True

@step(u'E me certifico de que estou na página do buscador Google')
def e_me_certifico_de_que_estou_na_pagina_do_buscador_google(step):
    if not world.browser.find_by_id('gbqfsa'):
        assert False
    if not world.browser.find_by_id('gbqfq'):
        assert False
    assert True

@step(u'E me certifico de que estou na página da Globo')
def e_me_certico_de_que_estou_na_pagina_da_globo(step):
    if not world.browser.find_by_css('.logo-topo'):
        assert False
    if not world.browser.find_by_id('home-menu'):
        assert False
    assert True
