# ==================================== Linguagens naturais vs. linguagens de programação ===============================

# Uma linguagem é um meio (e uma ferramenta) para expressar e registar pensamentos. Há muitas linguagens ao nosso redor.
# Algumas delas não requerem nem a fala nem a escrita, como a linguagem corporal; é possível expressar os seus
# sentimentos mais profundos com muita precisão sem dizer uma palavra.
#
# Outra linguagem que usa diariamente é a sua língua materna, que usa para manifestar a sua vontade e para pensar
# na realidade. Os computadores também têm a sua própria linguagem, chamada === (linguagem de máquina)== , que é muito
# rudimentar.
#
# Um computador, mesmo o mais sofisticado tecnicamente, é desprovido até mesmo de um vestígio de inteligência.
# Pode-se dizer que é como um cão bem treinado - responde apenas a um conjunto pré-determinado de comandos conhecidos.
#
# Os comandos que reconhece são muito simples. Podemos imaginar que o computador responde a ordens como
# "pega nesse número, divide-o por outro e guarda o resultado".
#
# Um conjunto completo de comandos conhecidos é chamado de === (lista de instruções) === , por vezes abreviado para IL
# (do inglês, Instruction List). Os diferentes tipos de computadores podem variar em função do tamanho das suas
# IL, e as instruções podem ser completamente diferentes em diferentes modelos.
#
# Nota: as linguagens de máquina são desenvolvidas por humanos.
# São criadas novas palavras todos os dias e as palavras antigas desaparecem. Estas línguas são chamadas linguagens naturais.

# Um programa escrito numa linguagem de programação de alto nível é chamado source code
# (em contraste com o machine code executado por computadores). Da mesma forma, o ficheiro que contém o source code
# chama-se source file.

# =================================================== Compilação vs. interpretação =====================================

# Há duas formas diferentes de transformar um programa de uma linguagem de programação de alto nível em linguagem de máquina:

# ==== COMPILAÇÃO ===
#    - o source program é traduzido uma vez
#    (no entanto, este ato deve ser repetido sempre que modificar o source code) obtendo um ficheiro
#    (por exemplo, um ficheiro .exe se o código se destinar a ser executado no MS Windows) contendo o machine code; agora
#    pode distribuir o ficheiro por todo o mundo; o programa que executa esta tradução chama-se compilador ou tradutor;
#
# ==== INTERPRETAÇÃO ===
#    - você (ou qualquer utilizador do código) pode traduzir o source program cada vez que este tem de ser executado;
#    o programa que executa este tipo de transformação chama-se intérprete, pois interpreta o código cada vez que se
#    pretende executá-lo; também significa que não pode simplesmente distribuir o source code tal como está, porque o
#    utilizador final também precisa do intérprete para o executar.

# COMPILAÇÃO
#      === VANTAGENS ===
#           a execução do código traduzido é geralmente mais rápida;
#           apenas o utilizador tem de ter o compilador - o end-user (utilizador final) pode usar o código sem ele;
#           o código traduzido é armazenado utilizando linguagem de máquina - como é muito difícil de entender,
#           as suas próprias invenções e truques de programação provavelmente permanecerão segredo.

#      === DESVANTAGENS ===
#           a compilação em si pode ser um processo muito demorado - pode não ser capaz de executar o seu código
#           imediatamente após qualquer alteração;
#           tem de ter tantos compiladores quanto plataformas de hardware em que queira que o seu código seja executado.

# INTERPRETAÇÃO
#      === VANTAGENS ===
#           pode executar o código assim que o concluir - não há fases adicionais de tradução;
#           o código é armazenado usando linguagem de programação, não de máquina - isto significa que pode ser executado em
#           computadores utilizando diferentes linguagens de máquina; não se compila o código separadamente para cada
#           arquitetura diferente.

#      === DESVANTAGENS ===
#           não espere que a interpretação aumente o seu código para alta velocidade - o seu código irá partilhar o
#           poder do computador com o intérprete, pelo que não pode ser realmente rápido;
#           tanto você como o end-user têm de ter o intérprete para executar o seu código.

# === (O Python é uma linguagem interpretada) ===. Isto significa que herda todas as vantagens e desvantagens descritas.
# Naturalmente, acrescenta algumas das suas características únicas a ambos os conjuntos.
# Se quiser programar em Python, precisará do === (intérprete Python) ===. Não será capaz de executar o seu código sem ele.
# Felizmente, o === (Python é gratuito) ===. Esta é uma das suas vantagens mais importantes.
# Devido a razões históricas, as linguagens concebidas para serem utilizadas na forma de interpretação são muitas
# vezes chamadas linguagens de scripting, enquanto os source programs codificados que as utilizam são chamados scripts.

# O Python é uma linguagem de programação de grande utilização, interpretada, orientada a objetos, e de alto nível com
# semântica dinâmica, utilizada para programação de uso geral.
#  ===>   uma linguagem fácil e intuitiva, tão poderosa como a dos principais concorrentes;
#  ===>   de open source, para que qualquer pessoa possa contribuir para o seu desenvolvimento;
#  ===>   código que seja tão compreensível como o inglês simples;
#  ===>   adequado para tarefas quotidianas, permitindo tempos de desenvolvimento curtos.

#  Há muitas razões - já enumerámos algumas delas, mas vamos enumerá-las novamente de uma forma mais prática:

#       ===> é fácil de aprender - o tempo necessário para aprender Python é menor do que para muitas outras linguagens;
#           isto significa que é possível iniciar a programação em si mais rapidamente;
#       ===> é fácil de ensinar - a carga de trabalho de ensino é menor do que a necessária para outras linguagens; isto
#           significa que o professor pode colocar mais ênfase em técnicas de programação gerais (independentes da linguagem),
#           não desperdiçando energia em truques exóticos, estranhas exceções e regras incompreensíveis;
#       ===> é fácil de usar para escrever novo software - é muitas vezes possível escrever código mais rapidamente quando
#           se usa Python;
#       ===> é fácil de compreender - é também frequentemente mais fácil e rápido de compreender o código de outra pessoa se
#           for escrito em Python;
#       ===> é fácil de obter, instalar e implementar - o Python é gratuito, aberto e multiplataforma; nem todas as
#           linguagens se podem gabar disso.

# É claro que o Python também tem os seus inconvenientes:

#   ===> não é um demónio da velocidade - o Python não oferece um desempenho excecional;
#   ===>em alguns casos pode ser resistente a algumas técnicas de teste mais simples - isto pode significar que depurar
#       o código Python pode ser mais difícil do que com outras linguagens; felizmente, cometer erros é sempre
#       mais difícil em Python.

#  === Cython ===

#  Cython pretende fazer - traduzir automaticamente o código Python (limpo e claro, mas não demasiado rápido)
#  em código "C" (complicado e falador, mas ágil).

# O Cython é uma das várias soluções possíveis para a mais dolorosa das características de Python - a falta de
# eficiência. Grandes e complexos cálculos matemáticos podem ser facilmente codificados em Python (muito mais
# facilmente do que em "C" ou qualquer outra linguagem tradicional), mas a execução do código resultante pode
# ser extremamente demorada.

# === Jython ===

# “J” é para “Java”. Imagine um Python escrito em Java em vez de C. Isto é útil, por exemplo, se desenvolver sistemas
# grandes e complexos escritos inteiramente em Java, e quiser acrescentar alguma flexibilidade Python a eles. O CPython tradicional pode ser difícil de integrar em tal ambiente, já que C e Java vivem em mundos completamente diferentes e não partilham muitas ideias comuns.

# Jython pode comunicar com a infra-estrutura Java existente de forma mais eficaz. É por isso que alguns projetos o
# consideram utilizável e necessário.

# Nota: a atual implementação do Jython segue as normas do Python 2. Até ao momento, não há Jython em conformidade com Python 3.