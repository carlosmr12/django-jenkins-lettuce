#language: pt-br

Funcionalidade: Funcionalidade Teste

    Cenário: Cenário de Teste
        Dado que eu abri o navegador
        Então eu visito o endereço "http://localhost:8000/consulta/"
        E preencho todos os campos do formulário
        Então eu clico no botão "Go google"
        E me certifico de que estou na página do buscador Google
        Então eu visito o endereço "http://localhost:8000/consulta/"
        E preencho todos os campos do formulário
        Então eu clico no botão "Go globo"
        E me certifico de que estou na página da Globo
        E fecho o navegador
