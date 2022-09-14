# ================================================ A função print() ===================================================

# A palavra print que se pode ver aqui é um nome de função. Isso não significa que, onde quer que a palavra apareça,
# é sempre um nome de função. O significado da palavra vem do contexto em que a palavra foi usada.
# print("Hello, World!") Apesar do número de argumentos necessários/fornecidos, as funções Python exigem fortemente a
# presença de um par de parêntesis - de abertura e de fecho, respetivamente. Se quiser entregar um ou mais argumentos a
# uma função, coloque-os dentro dos parêntesis. Se for utilizar uma função que não aceita qualquer argumento, ainda
# assim tem de ter os parêntesis.

# O que acontece quando o Python encontra uma invocação como esta abaixo?

# function_name(argument)

# ==>Primeiro, o Python verifica se o nome especificado é legal (navega nos seus dados internos a fim de encontrar
#       uma função existente com o mesmo nome; se esta pesquisa falhar, o Python aborta o código);
# ==>segundo, o Python verifica se os requisitos da função para o número de argumentos lhe permitem invocar a função
#       desta forma (por exemplo, se uma função específica exigir exatamente dois argumentos, qualquer invocação que
#       apresente apenas um argumento será considerada errada, e abortará a execução do código);
# ==>terceiro, o Python deixa o seu código por um momento e salta para a função que pretende invocar; claro, também leva
#       o(s) seu(s) argumento(s) e passa-o(s) para a função;
# ==>quarto, a função executa o seu código, causa o efeito desejado (se houver um), avalia o(s) resultado(s) desejado(s)
#       (se existir(em)) e termina a sua tarefa;
# ==>finalmente, o Python regressa ao seu código (ao local imediatamente após a invocação) e retoma a sua execução.

# Como pode ver, a invocação vazia print() não é tão vazia como se poderia esperar - produz uma linha vazia, ou
# (esta interpretação também é correta) o seu output é apenas uma newline.

# Esta não é a única forma de produzir uma newline na consola de output. Vamos agora mostrar-lhe outra forma.

# Há duas mudanças muito subtis - inserimos um estranho par de carateres dentro da rima. Têm este aspeto: \n.

# Curiosamente, enquanto se pode ver dois carateres, o Python vê um.
# A barra invertida (\) tem um significado muito especial quando usado dentro de strings - a isto chama-se o caratere de escape.

# A palavra escape deve ser entendida especificamente - significa que a série de carateres na string escapa por
# um momento (um momento muito curto) para introduzir uma inclusão especial.

# Por outras palavras, a barra invertida não significa nada em si, mas é apenas uma espécie de anúncio de que o
# próximo caratere após a barra invertida também tem um significado diferente.

# A letra n colocada após a barra invertida vem da palavra newline (nova linha).

# Tanto a barra invertida como o n formam um símbolo especial chamado um caratere de newline, que incita a consola a
# iniciar uma nova linha de output.