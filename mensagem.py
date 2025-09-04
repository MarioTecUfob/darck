def mensagem_agradecimento(destinatarios):
    # ASCII art do Darth Vader
    vader = r"""
                 .-.
                |_:_|
               /(_Y_)\
      .       ( \/M\/ )
       '.   _.'-/'-'\-'._
         : /   /   \   \ :
         '.   '--'--'   .'
           :     __     :
            '.  (  )  .'
              '.(__).'
               '.__.'
                |  |
                |  |
                |  |
               (____)
    """
    linha = "-" * 50
    print(vader)
    print(linha)
    print("Mensagem Especial ".center(50, "-"))
    print(linha)

    mensagem = f"""
    Prezados {destinatarios},

    Imagina aqui um texto grande cheio de agradecimentos e palavras bonitas.

    Muito obrigado pelas felicitações de aniversário,
    que a força esteja com você!
    """
    print(mensagem.strip())
    print(linha)
mensagem_agradecimento("colegas, alunos, clientes, parentes e amigos")
