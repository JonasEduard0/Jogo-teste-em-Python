import time
import random
from pygame import mixer
import socket

mixer.init() 
mixer.music.load("I:\Jogo\onceupon.mp3")
mixer.music.play()
mixer.music.set_volume(1.0) 


def creditos():
    print('''    \033[1;31;41mCréditos\033[m

Desenvolvedor : Jonas
Roteirista : Roger 
Músicas : Marcos

Utilizando PYTHON por meio do Visual Studio Code

Inspirado no anime Higurashi no Naku Koro ni

Trilha sonora : Undertale SoundTrack

Reinicie o código para iniciar um novo jogo''')
    mixer.music.stop()
    time.sleep(15)
    print('\n')

def sair():
    print('Fim de Jogo! Reinicie para iniciar um novo jogo')
    mixer.music.stop()
    time.sleep(15)
    print('\n')

def nop():
    print('Não há essa opção, escolha uma válida. Reinicie para iniciar um novo jogo')
    mixer.music.stop()
    print('\n')

def salvo():
    print('Não há jogo salvo, crie um novo jogo. Reinicie para iniciar um novo jogo')
    mixer.music.stop()
    time.sleep(15)
    print('\n')

def cap():
    print('\nIniciando capítulo 2...\n')

vida = 100
dano = 5
armadura = 0
dinheiro = 0

print('\n'*4)
print('''-=-=-=-=-=-=-=-=-=-=-= \033[4;30;41mHinamizawa Village\033[m -=-=-=-=-=-=-=-=-=-=-=
    1 - \033[4;32mIniciar Novo Jogo\033[m
    2 - \033[4;32mIniciar Cap. 2\033[m
    3 - \033[4;30mContinuar\033[m
    4 - \033[4;32mCréditos\033[m
    5 - \033[4;31mSair\033[m
''')

faz = float(input('O quê deseja fazer : '))
print('\n')
if faz == 3 :
    salvo()
elif faz == 4 :
    creditos()
elif faz == 5:
    sair()
elif faz < 1 or faz > 5:
    nop()
elif faz == 2:
    cap()
elif faz == 1:
    print('\n')
    print(f'\033[0;31;40mTome suas decisões com cuidado, os personagens se lembrarão de suas ações...\033[m')
    time.sleep(3)
    print('\n'*40)
    mixer.music.stop()
    mixer.music.load("I:\Jogo\oruins.mp3")
    mixer.music.play()
    print('''Você acaba de se mudar para uma vila remota com sua mãe e pai, chamada Hinamizawa
Seus pais sairam para fazer compras e você está organizando seu quarto
De repente, sua campainha toca
''')

    atende = input('Você atende a porta? (Atender / Ignorar) : ')
    if atende in 'atenderAtender atender AtenderATENDER':
        print('Você caminha em direção a porta e abre')
    if atende in 'ignorarIgnorarIGNORAR ':
        print('Você por algum motivo decide ignorar a batida, mas se lembra que seus não levaram a chave e pode ser eles, então abre')
    print('\n')
    time.sleep(3)
    print('''Para sua surpresa, um cara de cabelo amarelo aparece, ele parece atlético

    -\033[4;33m Olá! Eu sou Keiichi, moro aqui perto e fiquei sabendo que gente nova se mudaria pra cá\033[m''')
    nome = input('    - \033[4;33mQual seu nome?\033[m : ')
    print('\n')
    print('    - {}...'.format(nome))
    print('\n')
    time.sleep(3)
    print('Ele fica quieto por um instante com um olhar assustado mas logo se recupera e diz : \n')
    print(f'    - \033[4;33m{nome}, que coincidência... Passei aqui pra te perguntar se você irá no festival amanhã\033[m')
    festival = input('    - \033[4;33mVocê irá?\033[m (claro / que festival? / acho que nao) : ')
    print('\n')
    if festival in 'claroClaro claro Claro':
        print('    - \033[4;33mQue bom, então até amanhã!\033[m')
        print('\n')
        print('Você está cansado e não pretende esticar a conversa, então só fala "Claro" para terminar logo ')
    elif festival in 'acho que naoAcho que naoacho que não':
        print('    -\033[4;33m Que pena, então até outro dia!\033[m \n')
        print('Você está cansado e não pretende esticar a conversa, então só fala "Acho que não" para terminar logo')
    elif festival in 'que festival?que festivalQue festivalQue festival?':
        print('    -\033[4;33m Ah foi mal esqueci de falar, ele acontece todo dia 4 de abril e tem comida, música, essas coisas, e como diz a lenda, talvez amanhã... esquece, até amanhã!\033[m')
        print('\n')
    print('Ele se despede de você e caminha em direção à algumas casas no leste rapidamente')
    time.sleep(3)
    print('\n')
    print('Seus pais chegam, vocês conversam sobre suas novas vidas na vila e deitam esperando por um dia menos cansativo, mas você se pergunta o porquê da ação suspeita de Choji')
    time.sleep(3)
    print('\n'*7)
    print('É um novo dia, você acorda e se prepara ir ao seu primeiro dia de aula na nova escola. No caminho, você ouve dois idosos conversando')
    conv = input('O quê você faz? (Ouvir / Continuar) : ')
    if conv in 'continuarContinuarCONTINUAR':
        print('Não é certo espiar conversas alheias, você continua caminhando para a escola')
        print('\n')
    if conv in 'ouvirOuvirOUVIR':
        print('''
    - Você acha que vai se repetir esse ano?
    - Acho que sim, desde que o governo tentou profanar essas terras e alguns moradores apoiaram, a maldição se repetiu todos os anos, o último chamava {}, né?
    - Sim, uma parte do corpo ainda não foi encontrada.

Você se assusta com a conversa e decide voltar para o caminho pensando que não passa de uma brincadeira
        '''.format(nome))
    time.sleep(4)
    print('Você finalmente chega à escola e é abordado por um conhecido \n')
    print(f'    -\033[4;33m {nome}, finalmente! Como essa é a única escola, sabia que você apareceria aqui. Deixa eu te apresentar pra nossa turma\033[m \n')
    time.sleep(4)
    print('Uma garota de cabelo verde aparece, parece ter uma personalidade calma e inteligente \n')
    print('    - \033[4;32mE aí, eu sou a Mitsuki.\033[m\n')    
    print(f'    - Prazer, {nome}. \n')
    time.sleep(4)
    print('''Em seguida, uma outra garota de cabelo roxo se apresenta, você quase nem percebe que ela estava lá

    -\033[4;35m Rika\033[m

    - Quê?

    -\033[4;33m Ela não é de falar muito, deu pra perceber\033[m
    ''')
    time.sleep(3)
    print('Terminada as apresentações, vocês sentam perto um dos outros e conversam sobre coisas triviais até a professora chegar')
    print('\n')
    time.sleep(3)
    if conv in 'ouvirOuvirOUVIR':
        print('Você acaba de lembrar da conversa estranha que ouviu dos idosos mais cedo e a curiosidade toma conta')
        ido = input('Você questiona sobre a conversa? (Questionar / Não questionar) : ')
        print('\n')
        if ido in 'QuestionarquestionarQUESTIONAR questionar Questionar QUESTIONAR':
            print('''   - Então, tinha um cara com o mesmo nome que eu que morava aqui e foi... morto por uma maldição?''')
            mixer.music.stop()
            time.sleep(3)
            print('...')
            time.sleep(5)
            print('...')
            time.sleep(5)
            print('Um silêncio estranho toma conta do grupo, olhares de pavor te cercam... \n')
            time.sleep(5)
            print('''   -\033[4;33m Esqueça isso, eventualmente você saberá, mas não agora\033[m 
            
    - Entendi...\n''')
            mixer.music.load("I:\Jogo\sotemperated.mp3")
            mixer.music.play()
            time.sleep(3)
        elif ido in 'naoquestionar nao questionarNaoquestionarNão questionarnão questionar':
            print('Um sentimento de alívio toma conta, você sente que se perguntasse, algo ruim aconteceria \n')
            mixer.music.stop()
            mixer.music.load("I:\Jogo\sotemperated.mp3")
            mixer.music.play()
    elif conv in 'continuarContinuarCONTINUAR':
        time.sleep(3)
    if festival in 'acho que naoAcho que naoacho que não':
        print(f'''   -\033[4;33m Mudando de assunto, {nome} disse que não quer se juntar a nós no Wataganashi, mas acho que seria bom se ele fosse para conhecer mais da vila\033[m \n''')
    elif festival in 'claroClaro claro Claroque festival?que festivalQue festivalQue festival?':
        print(f'''  - \033[4;33mMudando de assunto, {nome} tem interesse em se juntar a nós no festival de Watanagashi!\033[m \n''')
    print('''   - \033[4;32mMas como ele não conhece a vila muito bem, ele deveria ir com alguém daqui, menos a Rika, já que ela ajuda na organização do festival\033[m

Todos olham para você''')

    ir = input('''    - \033[4;33mCom que você irá?\033[m (Mitsuki / Keiichi) : ''') 
    print('\n')
    if ir in 'Mitsukimitsuki MITSUKI mitsukiMITSUKI':
        print('''    - Acho que quero ir com Mitsuki, não gostaria de sair com o Keiichi do jeito que ele é''')
        time.sleep(3) 
        print('''   - \033[4;33mSério isso?\033[m
    - \033[4;32mDe qualquer forma,vou te passar meu número e te passarei o local\033[m
    - \033[4;35mMas de qualquer jeito, todos devem se encontrar lá, não costuma ir muita gente\033[m''')
        time.sleep(3)
        print('''
    A professora chega, você se apresenta formalmente para a turma. Terminando a aula, você volta para casa e está ansioso para ir ao tão aclamado Wataganashi''')
        print('\n')
        time.sleep(5)
        print('''Resultados do dia:
        Keiichi não gostou de não ter sido escolhido
        Mitsuki ficou feliz em ser escolhida
        \033[0;31;40mE amanhã você morre\033[m''')
        print('\n')
        time.sleep(5)
    elif ir in 'KeiichikeichikeiichiKEIICHIKEICHI keichi Keichi KEIICHI':
        print('''   - Acho que vou com Keiichi, conheço ele melhor
    - \033[4;32mTudo bem\033[m
    - \033[4;33mDe qualquer forma,vou te passar meu número e te passarei o local\033[m
    - \033[4;35mMas de qualquer jeito, devemos nos encontrar lá, não costuma ir muita gente\033[m''')
        time.sleep(3)
        print('''
    A professora chega, você se apresenta formalmente para a turma. Terminando a aula, você volta para casa e está ansioso para ir ao tão aclamado Wataganashi''')
        time.sleep(5)
        print('''Resultados do dia:
        Keiichi ficou feliz de ter sido escolhido
        Mitsuki não gostou de não ser a escolhida
        \033[0;31;40mE amanhã você morre\033[m''')
    time.sleep(3)
    print('Jogo salvo')
    print('Você terminou o capítulo 1 - "O começo do fim." \n')
    time.sleep(10)
    mixer.music.stop()

mixer.music.load("I:\Jogo\onceupon.mp3")
mixer.music.play()
print(''' 
-=-=-=-=-=-=-=-=-=-=-= \033[4;30;41mHinamizawa Village Capítulo 2\033[m -=-=-=-=-=-=-=-=-=-=-=
    1 - \033[4;32mIniciar Jogo\033[m
        * 1.1 - \033[4;32mIniciar Cap. 2\033[m
    2 - \033[4;32mContinuar\033[m
    3 - \033[4;32mCréditos\033[m
    4 - \033[4;31mSair\033[m \n''')
menu2 = float(input('O quê deseja fazer : '))
print('\n')

if menu2 == 3:
    creditos()
elif menu2 == 4:
    sair()
elif menu2 < 1 or menu2 > 4:
    nop()
elif menu2 == 1 or menu2 == 1.1 or menu2 == 2:
    print('Carregando capítulo 2 ...')
    time.sleep(3)
    print('\n')
    print('''Hinamizawa Village Capítulo 2 - "Descobertas"
\033[0;31;40mTome suas decisões com cuidado, os personagens se lembrarão de suas ações...\033[m''')
    time.sleep(3)
    print('\n'*10)

    mixer.music.load("I:\Jogo\sotemperated.mp3")
    mixer.music.play()
    print('''É uma terça-feira, 4/4, são 21:30, não há aulas pois uma festa cultural da vila que acontece uma vez por ano está acontecendo
Você deveria se encontrar com Mitsuki e Keiichi e depois ser apresentado ao festival pela pessoa que você escolheu ontem''')
    time.sleep(3)
    print('''Você aguarda perto de uma barraca de cachorro-quente como combinado
Mitsuki aparece, mas nada de Keiichi''')
    time.sleep(5)
    print('\n')

    print('''    - \033[4;32mE aí, o Keiichi está com você?\033[m

    - Não, inclusive você mesma está atrasada

    - \033[4;32mQue estranho, ele nunca é de perder esse tipo de coisa. Vamos só eu e você, quero te apresentar à algumas pessoas importantes, depois nós vamos fazer algo\033[m \n''')
    time.sleep(6)
    print('''Vocês começam a se afastar da multidão. Você se aproxima de uma espécie de galpão e há duas pessoas em frente a ele, uma mulher de aproximadamente 20 anos e um cara grande com calça camuflada de militar de 25 á 30 anos \n''')
    time.sleep(3)
    print('''    - \033[4;34mEstávamos te esperando, Mitsuki\033[m''')
    nome = input('    - \033[4;34mE qual seria seu nome, garoto\033[m? :')
    print('\n')
    print(f'''  -\033[4;32m Ele é um amigo da escola que se mudou esse ano, não se preocupe Miyo e Irie, ele é confiável\033[m \n
    - \033[4;36mPrazer {nome}. Sou o médico local e Miyo a enfermeira, nós criamos a clínica de enfermagem da vila recentemente. Nós vamos entrar nesse galpão, enquanto isso Miyo vai te explicar o motivo de estarmos aqui\033[m \n''')
    time.sleep(5)
    mixer.music.stop()
    mixer.music.load("I:\Jogo\premonition.mp3")
    mixer.music.play()
    print('''    - \033[4;32mBom, existem duas famílias fundadoras da vila, a minha que é responsável por políticas públicas, e a da Ruri, era responsável pela parte religiosa de Hinamizawa. Seus pais eram sacerdotes\033[m \n''')
    time.sleep(3)
    print(f'''    - Eram? \n
    - \033[4;32mBem... eles morreram por apoiarem a construção de uma represa que inundaria a Hinamizawa e sofreram da 'maldição de Oyashiro', nosso deus protetor da vila. O pai de Ruri se chamava {nome}\033[m
    - \033[4;32mUma represa chegou aqui falando que queriam nossas terras, em troca ofereceriam grande quantia de dinheiro para cada morador da vila se mudar daqui e irem para outra cidade, mas poucos aceitaram, e esses poucos coincidentemente morreram dessa maldição\033[m
    - \033[4;32mKeiichi também sofreu com essa tal maldição, seus pais tentaram sair da cidade e morar na cidade vizinha, mas Keiichi simplesmente enlouqueceu e seus pais acharam que isso era um castigo de Oyashiro por saírem da vila, quando eles voltaram Keiichi voltou ao normal. Deste então a família dele se tournou fanática religiosa por Oyashiro\033[m
    - \033[4;32mSuspeito que não existe tal maldição nem Oyashiro, acho que minha família quer ter controle total da vila controlando seus moradores pelo medo\033[m
    - \033[4;32mTambém dizem que um dia no ano, hoje, uma pessoa é capturada por demônios comandados pelo Oyashiro para servir de alimento e acalmar sua ira\033[m
    - \033[4;32mE esse galpão é muito suspeito por estar no meio do nada e ter esse cadeado. Poucas pessoas da minha família tem acesso a ele\033[m \n
    - \033[4;36mE agora iremos descobrir o que tem dentro\033[m \n ''')
    time.sleep(7)
    
    print('Irie tenta quebrar o cadeado com um alicate fazendo muita força')
    print('Ele consegue, mas no instante que o cadeado cai e a porta abre, um morcego maior que o normal voa em sua direção')
    print('\n')
    time.sleep(3)
    
    tutcom = input('O tutorial de combate será iniciado, deseja ve-lô? (Ver / Pular) : ')
    time.sleep(3)
    print('\n')
    if tutcom in 'verVerVER ver VER Ver':
        print('''Sempre que fazer uma ação de combate, um dado no algoritmo será rodado e um número aleatório será sorteado, seu inimigo também roda o dado e tirará um valor
Se seu valor for maior que o do inimigo, você executará a ação que escolheu

Sua armadura é 0, podendo ser aumentada ao conseguir roupas mais robustas ou até mesmo colete a prova de balas
Com dinheiro, você pode comprar itens, atualmente possui R$0,00
Você possui 100 pontos de vida(PV), se chegar a 0...
Seu personagem dá 5 de dano atualmente, pode ser aumentado equipando armas

    Existem 4 ações que podem ser feitas em um combate : 
Fugir : caso escolha esta opção, você poderá fugir de algumas lutas contra oponentes fracos
Atacar : ataca o oponente com sua arma equipada no momento.
Esquivar : você esquiva do ataque sem tomar dano.
 ''')
    else:
        print('Você pulou o tutorial \n')

    time.sleep(5)
    mixer.music.stop()
    mixer.music.load("I:\Jogo\heartache.mp3")
    mixer.music.play()
    porta = input('O morcego te ataca, oquê você faz? (Fugir / Atacar / Esquivar): ')
    if porta in 'atacarATACARAtacar atacar Atacar ATACAR':
        print('Girando dado D20...')
        time.sleep(5)
        portaataque = random.randint(0,20)
        print(f'''Você tirou {portaataque} no dado''')
        if portaataque <= 9:
            print('''O morcego desvia do ataque
Ele te ataca com suas garras, você perde PV (100 -> 95) \n''')
            vida = vida - 5
        else:
            print('''Você consegue atacar o morcego que perde PV (10 -> 5)
Ele te ataca com suas garras, você perde PV (100 -> 95) \n''')
            vida = vida - 5
    if porta in 'FugirFUGIRfugir fugir FUGIR Fugir' or porta in 'esquivarESQUIVAREsquivar esquivar Esquivar ESQUIVAR':
        print('Girando dado D20...')
        time.sleep(5)
        portaataque = random.randint(0,20)
        print(f'''Você tirou {portaataque} no dado''')
        if portaataque <= 9:
            print('''Você não consegue esquivar ou fugir
Ele te ataca com suas garras, você perde PV (100 -> 95) \n''')
            vida = vida - 5
        else:
            print('''Você consegue esquivar do ataque surpresa, mas não foge
Ele te ataca com suas garras
Você perde PV (100 -> 95)''')
            vida = vida - 5

    time.sleep(3)
    print('''   - \033[4;36mGaroto, você está bem?\033[m \n
Irie se junta a você
Ele ataca o morcego com um soco
O morcego morre \n''')
    time.sleep(7)
    if vida < 100:
        print('''   - \033[4;34mDeixe-me ver suas feridas\033[m \n
Miyo retira um curativo e começa um tratamento
Você recupera PV(95 -> 100) \n''')
        vida = 100

    print('''Irie vai até um encanamento e arranca um cano \n
    - \033[4;36mTome, vamos precisar\033[m \n
Dano aumentado (5 -> 10)''')
    dano = dano + 5
    mixer.music.stop()
    mixer.music.load("I:\Jogo\waterfall.mp3")
    mixer.music.play()
    print('''O grupo se prepara para entrar no galpão, e a visão é assustadora
Vocês veem ferramentas de tortura antigas, como grilhões, facões, etc \n''')
    print('''    
    -\033[4;34m Uau...\033[m

    - Então realmente tem algo de estranho nessa vila

    - \033[4;32mPorque minha família teria isso?\033[m \n''')
    time.sleep(7)
    
    print('''Você entra mais fundo e vê uma enorme estatúa de cor dourada que impõe uma presença muito forte

    - \033[4;36mSe não me engano, é assim que Oyashiro se parace para os habitantes\033[m
    
Mitsuki se aproxima e toca na estátua
No mesmo instante a cabeça de Oyashiro cai, quase acertando Mitsuki e fazendo um barulho enorme \n

    - \033[4;34mCuidado Mitsuki!\033[m

    - \033[4;36mVamos embora, alguém deve ter ouvido!\033[m
    \n
Vocês segue o grupo para um lugar distante correndo muito rápido
Quando você olha para trás, consegue ver um vulto... Ele tinha a mesma silhueta de Keiichi...''')
    time.sleep(7)

    print('''
Vocês chegam a um lugar mais movimentado

    - \033[4;36mBom, acho melhor nós aproveitarmos o festival e criar um álibi dizendo que estávamos no festival para que ninguém suspeite de termos invadido uma propriedade\033[m

    - \033[4;34mDivirtam-se, e lembre de manter isso só entre nós\033[m

Irie e Miyo se despedem e você fica a sós com Mitsuki

    - \033[4;32mAcho melhor eu voltar para casa, tenho que pensar sobre os incidentes recentes, até algum dia\033[m \n''')
    print('''Triste, ela se despede de você e segue para casa. Você não vê sentido em continuar sozinho logo volta para casa''')
    time.sleep(5)

    print('''Em casa você faz sua rotina noturna e joga o pedaço de cano que tinha pego de Irie fora
Você lembra de seu taco de baseball feito de metal que usava para jogar quando criança, deve machucar... Há também uma grande jaqueta de couro e um resto da sua mesada \n''')
    dano -= 5
    taco = input('''Pegar? (Sim / Não) : ''')
    if taco in 'simSimSIM sim Sim SIM':
        dano += 10
        armadura += 10
        dinheiro += 20
        print('\nDano aumentado(5 -> 15), armadura aumentada(0 -> 10), dinheiro aumentado(0 -> 20)')

    print('''Você deita e dorme
Jogo salvo''')
    time.sleep(10)
    print('\n'*40)
    time.sleep(10)
    mixer.music.stop()
    mixer.music.load("I:\Jogo\oruins.mp3")
    mixer.music.play()

    print(f'''É um novo dia, sexta-feira, você acorda atrasado e tem que ir para a escola às pressas
Chegando lá você encontra as pessoas de sempre, Ruri, Mitsuki, mas Keiichi não
No início do intervalo, Mitsuki te chama para um lugar isolado da sala
Ela parece preocupada com algo

    - Então, para que você me chamou?

    - \033[4;32m{nome}, algo aconteceu...\033[m

Ela começa a tremer \n''')
    time.sleep(10)
    print('''   - \033[4;32mEu descobri muitas coisas sobre a 'maldição'. Primeiramente, ela não é algo criado pela minha família para controlar a vila, como sou a herdeira e futura líder, perguntei á minha mãe e ela negou qualquer participação nisso, e ela mesma se sente confusa, não sabe se é real ou não.\033[m
    \033[4;32mE... sobre o que fizemos ontem...\033[m
    \033[4;32mLembra que todo ano alguém morre e alguém desaparece? Seria normal se nós fossemos alvos da maldição, já que invadimos um lugar com uma estátua de Oyashiro, né?\033[m
    \033[4;32mSobre Irie... ele sumiu da vila, era para ele estar na clínica dele atendendo pessoas, mas nem na casa dele ele chegou ontem depois do festival, foi o que os vizinhos disseram\033[m \n''')
    time.sleep(10)
    
    print(f'''    - Isso... não passa de uma coincidência, ele desapareceu, mas ninguém morreu, né?
    
    - \033[4;32mNa verdade, a --\033[m

    - {nome}! Favor comparecer na sala dos professores, tem alguém querendo te ver
    
A professora chega do nada no meio do intervalo e diz isso

    - Me espere aqui, vou lá ver oque é
    
Você chega na sala e lá está apenas um homem gordo, velho e cabelo cinza

    - \033[7;30mSente-se garoto, tenho algumas perguntas para você\033[m''')
    mixer.music.stop()
    mixer.music.load("I:\Jogo\sotemperated.mp3")
    mixer.music.play()
    time.sleep(10)
    print('''    - \033[7;30mMe chamo Oishi, sou da polícia local. Deve ter ficado sabendo do desaparecimento de Irie e da morte de Miyo\033[m
    
Você começa a suar frio

    - \033[7;30mParece que ficou sabendo só agora, que pena. Você foi visto com eles no festival de ontem, sabe de algo anormal que pode ter acontecido?\033[m \n''')

    vdd = input('Dizer a verdade à Oishi? (Sim / Não) : ')
    if vdd in 'simSimSIM sim Sim SIM':
        print(f'''\nVocê conta tudo para ele, desde a invasão ao galpão quanto à ter visto uma sihueta les observando. Também conta o que sabe sobre a maldição
Ele só aparenta ficar surpreso quando você termina a falar sobre a maldição

    - \033[7;30mEntendi... não se preocupe, você não será penalisado por invadir uma propriedade já que foi por influência\033[m
    - \033[7;30mSobre a maldição, garoto, esqueça isso\033[m
    
    - Como ela morreu?
    
    -\033[7;30m Ah?\033[m

    - A Miyo
        
    - \033[7;30mBem... foi suicídio, ela arranhou o próprio pescoço até perder muito sangue\033[m

Você segura o vômito

    - \033[7;30mVocê é forte {nome}, e sabe de muita coisa... Tome meu cartão, caso tenha uma informação nova, me ligue\033[m

Você pega o cartão e põe no bolso
Oishi sai da sala, você segue em direção á enfermaria e retira um atestado para faltar as últimas aulas por não se sentir bem''')
    else:
        print('''\n   - Não sei de nada... só nos encontramos no festival e seguimos nosso rumo

Ele olha desconfiado

    - \033[7;30mTudo bem, por questão de segurança, tome meu cartão\033[m
    
Você pega o cartão e põe no bolso \n''')

    time.sleep(7)
    print(f'''Você chega em casa e é recebido pelos seus pais
Você vai direto pro quarto e liga para Mitsuki para terminarem a conversa
Você conta a ela tudo o que aconteceu hoje e sobre Keiichi

    - ... \033[4;32mEntão você acha que Keichi nos viu e achou apropriado sequestrar Irie e armar a morte de Miyo?\033[m

    - Sim, não acho que ela se mataria assim, e como Keichi já ficou insano uma vez, ele pode estar de novo agora

    - \033[4;32mVou pensar no que fazer de agora em diante e contar isso para Ruri, ela tem que saber. E não conte para seus pais, eles podem achar que não passa de uma brincadeira. Tchau\033[m

Ela desliga
Você desce para o jantar
Sua mãe começa uma conversa e você responde com simples 'sim', 'não', 'talvez'.
Até que seu pai diz algo interesante

    - Parece que você já fez amigos, {nome}. Inclusive, um deles veio aqui te procurando, mas você estava com a cabeça nas nuvens e foi direto pro quarto sem ver ele na cozinha. O que vocês conversaram que o fez sair com tanta pressa?
    
    - Mas... ele não veio no meu quarto... Qual era o nome dele?
    
    - Se não me engano era... \033[0;31;40mKeiichi\033[m
    
Você imediatamente pensa que ele ouviu sua conversa com Mitsui no telefone por trás da porta

    - Ah! Quase me esqueci, amanhã é nosso aniversário de casamento, passaremos o dia de amanhã no restaurante famoso da cidade vizinha, você ficará bem sozinho?
    
Você nem escuta o resto da conversa direito e vai direto para a cama
Você está exausto, confuso e não sabe o que fazer
Sentado na cama, você tenta acreditar que tudo não passa de um pesadelo
Sem perceber, você pega no sono''')
    time.sleep(30)
    mixer.music.stop()
    print('\n'*10)

    print('''É um novo dia, sábado, 7/4, 11:00
Você não acorda pelo despertador, mas sim pelo som da tempestade que está acontecendo lá fora
Você levanta, vai ao banheiro e percebe que ouve uma queda de luz, está escuro. Seus pais também não estão em casa, aí você lembra que é aniversário do casal e devem ter ido em viagem para sua cidade natal e pego um ônibus
Sua campainha toca, você não está esperando visitas...''')

    time.sleep(10)

    print(f'''Você olha pelo olho-mágico
...    
... 
...    
É o Keiichi    
    
    - \033[4;33m{nome}! Abre ae, quero só conversar\033[m \n''')

    abri = input('Você abre a porta? (Abrir / Não abrir) : ')
    if abri in 'abrirABRIRAbrir ABRIR Abrir abrir':
        print(''' \n ...
Acho que não ficou claro''')
        abriclaro = input('Você abre a porta para KEIICHI? (abrir / não abrir) : ')
        if abriclaro in 'abrirABRIRAbrir ABRIR Abrir abrir':
            print('''...
Seu corpo paralisa, você não consegue abrir a porta \n''')
        else:
            print('''Você obviamente não abre a porta para Keiichi
Ele começa a bater na porta mais forte enquanto grita \n''')
    else:
        print('''Você obviamente não abre a porta para Keiichi
Ele começa a bater na porta mais forte enquanto grita \n''')

    print('''   - \033[4;33mEU SÓ QUERO CONVERSAR\033[m
    
A tranca da porta se quebra com as pancadas e ela abre \n''')
    mixer.music.load("I:\Jogo\megalovania.mp3")
    mixer.music.play()
    time.sleep(10)
    print('''   - ...
   - O quê você quer?
   
   -\033[4;33m Você invadiu um local sagrado, isso pode trazer a maldição para todos da vila\033[m
   
Ele corre em cima de você e te ataca \n''')

fa = input('O que você faz? (Atacar / Fugir / Esquivar) : ')
if fa in 'esquivarESQUIVAREsquivar Esquivar esquivar ESQUIVAR':
    print('''\nRodando dado d20...
Você falhou, ele é muito rápido e parece que é inútil tentar esquivar. Ele contra-ataca...
Crítico! Você perde PV (100 -> 65)''') 
    vida = 65
    fa2 = input('\nO que você faz?(Atacar / Fugir ) : ')
    if fa2 in 'AtacaratacarATACAR ATACAR Atacar atacar':
        print('''\nRodando dado d20...
Você tenta atacá-lo com seu taco, mas ele segura rapidamente e contra-ataca
Ele te soca com uma força sobre-humana, dói muito. Você perde PV (65 -> 30)
Parece que atacar ele é inútil, sua única opção é fugir''')
        vida = 30
        print('''Ele abre uma brecha e você consegue escapar''')
elif fa in 'atacarATACARAtacar ATACAR atacar Atacar':
    print('''\nRodando dado d20...
Você tenta atacá-lo com seu taco, mas ele segura rapidamente e contra-ataca
Ele te soca com uma força sobre-humana, dói muito. Crítico! Você perde PV (100 -> 65)
Parece que atacar ele é inútil''')
    vida = 65
    fa3 = input('\nO que você faz?(Esquivar / Fugir ) : ')
    if fa3 in 'EsquivaresquivarESQUIVAR esquivar Esquivar ESQUIVAR':
        print('''Rodando dado d20...
Você falhou, ele é muito rápido e parece que é inútil tentar esquivar. Ele contra-ataca...
Crítico! Você perde PV (65 -> 30)''')
        vida = 30
if fa in 'fugirFugirFUGIR Fugir fugir FUGIR':
    print('''\nRodando dado d20...''')

print(f'''Você consegue fugir para seu quarto e ele te persegue mas escorrega em um degrau
Imediatamente você lembra do número de telefone de Oishi e liga ás pressas com seu celular

    - \033[7;30mAlô? Detetive Oishi na escuta\033[m
    
    - VOCÊ TEM QUE ME AJUDAR, TÔ SENDO ATACADO
    
    - \033[7;30m{nome}? Se acalme e me diga se vo--\033[m
    
A porta é arrombada

    - \033[4;33mVOCÊ NÃO TEM IDEIA DO QUE PODE ACONTECER QUANDO VOCÊ PROFANA UM LUGAR SAGRADO\033[m
    - \033[4;33mHá muito tempo, uma represa queria nossas terras e nos mandou ir embora para a cidade grande, TODOS ELES FORAM MORTOS POR OYASHIRO\033[m
    - \033[4;33mEu e minha família achamos que seria mais seguro nos mudarmos, assim que nos mudamos, Oyashiro falou comigo e nós voltamos\033[m
    
Enquanto fala essas coisas, Keiichi está coçando muito forte seu pescoço, está começando a sangrar

    - \033[4;33mComo coça! Isso é um sintoma da maldição que estou sofrendo por SUA CAUSA\033[m
    
Ele avança até você, a única saída parece ser pular da janela de seu quarto do 2 andar ou morrer para ele
Você pula''')
vida = vida - 10
time.sleep(10)
print(f'''Você não sente seu braço esquerdo
Você perde 10 PV e sobra {vida} de PV
Desesperado, você corre para o celeiro de seu pai em busaca de sua arma de caça profissional
Enquanto isso, Keiichi desce as escadas correndo e te procura pelo rastro de sangue
Você acha uma pistola .45 no baú do celeiro, mas tambem acha umas bandagens, você estanca o que consegue das suas feridas
Keiichi te localiza e corre em sua direção
Você tem uma chance para atirar e acertar Keiichi, se não sua morte é certa. \n''')

tiro = int(input('''Qual a ordem você deve seguir para conseguir atirar? 
1 - Girar tambor, travar a arma, mirar e atirar 
2 - Destravar a arma, mirar e atirar
3 - Girar tambor, destravar, mirar e atirar 
Qual? : '''))
if tiro == 1:
    print('...')
    time.sleep(3)
    print('Errado, você deve destravar a arma para atirar')
    mixer.music.stop()
elif tiro == 2:
    print('...')
    time.sleep(3)
    print('Errado, você deve girar o tambor primeiro')
    mixer.music.stop()
elif tiro == 3:
    print('...')
    time.sleep(3)
    print('Correto! Você verifica o tambor e ... não há munição')
    mixer.music.stop()
print('Sedento por sua morte Keiichi corre em sua direção e te esfaqueia no braço, você já não tem mais forças para reagir')
viv = vida - 3
vida = vida - viv
print(f'Você perde {viv} PV e sobra {vida} de PV')
print(''' \n Ele ri enquanto seus olhos quase se fecham e prepara o golpe final

    - \033[4;33mAdeus\033[m
    
Você está caido no chão, e ele acima de você levanta uma faca que tinha pego na cozinha''')
time.sleep(5)
print('...')
time.sleep(5)
print('Ele está demorando... você abre o olho para ver o porquê da demora. Ele está morto, há um buraco de bala na testa dele, mas não foi você...')
print('\n'*40)
time.sleep(3)

print('Jogo salvo')
print('Você terminou o capítulo 2 - "Descobertas" \n')
time.sleep(5)


mixer.music.load("I:\Jogo\onceupon.mp3")
mixer.music.play()
print(''' 
-=-=-=-=-=-=-=-=-=-=-= \033[4;30;41mHinamizawa Village\033[m -=-=-=-=-=-=-=-=-=-=-=
    1 - \033[4;32mIniciar Jogo\033[m
        1.1 - \033[4;30mIniciar Cap. 2\033[m
        1.2 - \033[4;32mIniciar Cap. 3\033[m
    2 - \033[4;32mContinuar\033[m
    3 - \033[4;30mCréditos\033[m
    4 - \033[4;30mSair\033[m 
 ''')
menu3 = float(input('Selecione 1, 2 ou 1.2 para iniciar a parte final de seu tormento : '))
print('\n')

if menu3 == 3:
    print(f'Não se distraia de seu caminho,',nome )
elif menu3 == 4:
    print(f'Você não pode mais escapar, ',nome )
    print('\n')
elif menu3 < 1 or menu3 > 4:
    print(f'Não tente escapar digitando um número que não tem, ',nome )
    print('\n')
elif menu3 == 1.1:
    print(f'Você já passou por esse tormento, ',nome )

print('Carregando capítulo 3 ...')
time.sleep(3)
print('\n')
print('''Hinamizawa Village Capítulo 3 - "A maldição"
\033[0;31;40mTome suas decisões com cuidado, os personagens se lembrarão de suas ações...\033[m''')
time.sleep(5)
print('\n'*40)
mixer.music.load("I:\Jogo\sotemperated.mp3")
mixer.music.play()
time.sleep(5)

print(f'''   - \033[7;30mJá faz tempo, {nome}. 3 dias talvez?\033[m
    
Uma voz familiar conversa com você

    - Quem é?
    
    - \033[7;30mFinalmente. Sou eu, Oishi. Te encontrei à beira da morte em seu celeiro\033[m
    
    - O que aconteceu?

    - \033[7;30mVocê ficou desacordado por um bom tempo, levou facadas no braço e teve uma costela quebrada. Keiichi está com o corpo na necrópsia para análise\033[m''')
time.sleep(8)

if vdd in 'simSimSIM sim Sim SIM':
    print(f'''  - \033[7;30mGraças à você ter me contado mais sobre a maldição, ficou óbvio que ela era algo criado e não uma 'punição divina'\033[m
    - \033[7;30mJá que não foi algo criado pelos fundadores da vila, os únicos capazes de criar isso seriam os médicos locais, deve ser uma espécie de vírus\033[m
    -\033[7;30m Mas como Irie está desaparecido, vou invadir o hospital sem permissão. Estava indo agora mesmo, passei mais para ver como você está\033[m 
    - \033[7;30mInclusive, Miyo provavelmente foi infectada pelo vírus já que tambem arranhava o pescoço como o Keiichi e outros que sofreram da maldição nos anos anteriores\033[m 
    - \033[7;30mEntão é isso, até algum dia, {nome}. Seus pais foram comunicados que você foi trago no hospital da cidade vizinha já estão vindo te buscar aqui\033[m 
    
    - Até... \n''')
    time.sleep(8)
else:
    print('''   - \033[7;30mEu até te daria mais informações, mas você não quis me contar o quê sabia quando nos encontramos antes, só vou dizer que irei investigar o hospital e tenho que ir, até algum dia\033[m \n''')

print('''Obviamente, após tudo que aconteceu, você não ficará parado. Seu corpo já está bem e você se sente quase totalmente revigorado (90 de PV)''')
vida = 90

print('''Você rapidamente veste as roupas que estavam em uma escrivaninha, provavelmente lavadas pela Mitsuki ou Ruri, já que há uma carta delas em cima desejando que você melhore e sai do hospital onde você está
Oishi está conversando com um médico, uma chance perfeita para você entrar no banco de trás
Dado alguns minutos, ele entra e acelera em direção á Hinamizawa
30 minutos se passam e o carro para em algum lugar, Oishi sai do carro e fecha a porta. Antes de você ser trancado, você rapidamente abre a porta e sai, deixando ele surpreso''')
time.sleep(5)
print(f'''   
    - \033[7;30mO que VOCÊ está fazendo aqui, criança?\033[m
    
    - Eu vou com você!

    - \033[7;30mDe jeito nenhum, você acaba de fica quase uma hora em um carro quente e acaba de sair do hospital, se morrer a culpa é minha\033[m
    
    - Eu tambem quero descobrir a verdade tanto quanto você, não posso simplesmente ignorar tudo
    
Ele percebe que não vai conseguir te parar e conclui que é mais seguro com ele perto do que você sozinho

    - \033[7;30mEstá bem, você vem comigo. Mas antes vista um colete e toma uma arma, não sabemos oque tem aqui\033[m
    
Você veste um colete a prova de balas e recebe um cacetete policial
Dano aumentado ({dano} -> 30), armadura aumentada ({armadura} -> 30) \n

    - \033[7;30mPosso até te dar uma arma, mas isso custaria uma graninha se é que me entende...\033[m \n''')
time.sleep(8)
if taco in 'simSimSIM sim Sim SIM':
    print('Por sorte, você pegou um dinheiro em casa antes e tem R$20,00 \n')
    print('    - \033[7;30mÉ o suficiente... tome, acho que você sabe usar uma já que usou lá no celeiro\033[m \n')
    dano = 50
    print('Dano aumentado (30 -> 50) \n')
else:
    print('Infelizmente você recusou pegar dinheiro na sua casa antes, você não tem nada')
    print('''   - \033[7;30mTô brincando nunca te daria uma arma de fogo...\033[m

Você sente que em um universo paralelo ele te daria sim uma arma de fogo se tivesse dinheiro, que arrombado''')
mixer.music.stop()
mixer.music.load("I:\Jogo\waterfall.mp3")
mixer.music.play()
time.sleep(5)

print('''   - \033[7;30mEntão vamos entrando\033[m

Vocês entram e procuram por qualquer pista sobre o envolvimento dos médicos locais que chegaram do nada na criação de um suposto vírus que deixa pessoas loucas
Se passam 1 hora e nada
Até que vocês entram na sala onde fica o diretor do hospital

    - \033[7;30mBom, parece que estávamos enganados, não há nada aqui\033[m
    
    - Espera, algo nesta estante de livros está errado, este livro de filosofia não combina com o resto dos livros de anatomia
    
Assim que você puxa o livro, uma passagem secreta se abre na estante e uma escadaria é revelada

    - \033[7;30mQue clichê\033[m
    
Vocês descem as escadas e à frente há duas portas, a da esquerda está escrito : 'Arquivos' e na direita : 'Teste final' 
Vocês seguem para o Arquivos e é revelado várias estantes de documentos, mas um livro grosso chama mais a atenção
Você o pega e lê em voz alta \n''')
time.sleep(20)

print('''    - "Hoje, começa o grande dia. Eu e Miyo descobrimos esse potencial vírus específico de uma vila iremos analisá-lo"
    "Ela não possui um hospital, então chegaremos com o pretexto de querer ajudar a saúde local"
    "Descobrimos o vírus quando um paciente de nosso primeiro hospital foi diagnosticado com uma doença até então não descoberta por mais ninguém e ele era de Hinamizawa"
    "Chamamos a doença de \033[0;31;40mMaldição de Oyashiro\033[m, pois esse será a desculpa para as pessoas que espalharemos quando elas começarem a morrer ou enlouquecer, uma maldição do deus local" 
    
    Esse texto foi escrito alguns anos atrás, quando as pessoas começaram a enlouquecer e desaparecer da doença\n''')
time.sleep(8)
print('''O próximo que interessa foi escrito ano passado : 
    
    "Já estamos aqui há alguns anos, eis oquê descobrimos : o vírus se aloja no pescoço do infectado, causando grande coceira. As pessoas parecem acreditar na história da maldição. Aproveitamos uma briga interna da vila por conta de uma represa para causarmos mais vítimas e termos mais corpos para estudar e enfim vender o vírus como arma biológica ou criar super-soldados. Miyo parece estar se sensibilizando com as vítimas desde que matamos os pais de uma garotinha chamada \033[4;35mRika\033[m, filha dos sacerdotes locais, mas caso ela tente me trair, posso infectá-la e fazer parecer suicídio. Caso isso aconteça, terei que forjar meu desaparecimento e estudar mais intensamente escondido" \n''')
time.sleep(8)
print(f'''Esse próximo foi escrito a poucos dias

    - "Aquela puta me traiu, tentou comunicar um detetive chamado Oishi escondido de mim, não deve ter aguentado o fardo de termos criado aquela coisa na sala de 'Teste final'. E tem tambem essa criança chamada Keiichi, um fanático por Oyashiro que nos viu entrando no depósito, mas já cuidei dele...''')
    
print('\n')
print('''Isso é tudo \n''')
time.sleep(6)
print('''   - \033[7;30mNossa... tem mais coisa que eu pensei, vamos apenas ir na última sala e depois damos depoimento à minha delegacia de polícia, garoto\033[m
    
    - Ok...
    
Vocês seguem em silêncio e considerando se estão mesmo acreditando em tudo isso''')
mixer.music.stop()
time.sleep(5)
print('''Vocês estão em frente á porta de "Teste final" 

    - \033[7;30mVamos ver logo o quê tem aqui e depois saímos\033[m
    
    - Concordo
    
Vocês abrem a porta e está tudo escuro lá dentro, vocês entram mais a fundo
A porta atrás de vocês é fechada bruscamente em meio a risos

    - \033[4;36mSeus idiotas! Vocês não poderão mais sair daqui\033[m
    
    - \033[7;30mIrie! Recomendo destrancar a porta e se render se não posso usar de força policial para te impedir\033[m \n''')

time.sleep(10)
print('''    - \033[4;36mNUNCA! Trabalho nesse projeto a anos, e estou a ponto de criar um supersoldado utilizando o vírus\033[m
    - \033[4;36mCoincidentemente, precisava de cobaias vivas para testar o potencial do meu teste final...\033[m
    - \033[4;36mApareça Higurashi! \033[m \n''')
time.sleep(10)
cont = input('A partir deste ponto não há mais volta (Entendi) : ')
mixer.music.load("I:\Jogo\onightmare.mp3")
mixer.music.play()
time.sleep(15)
print('''No mesmo instante, um rugido terrível ecoa o lugar em que vocês estão trancados. Um mostro de 4 metros, veias pulsantes, e cobreto por sangue dele próprio aparece \n''')
time.sleep(5)
print('A batalha final começou, você tambem comandará as ações de Oishi ')
time.sleep(7)
print('\n'*40)


boss = input('O quê Oishi faz? (Atacar / Esquivar / \033[4;30mFugir\033[m / Clamar por piedade) : ')
danooishi = 60

if boss in 'atacarAtacarATACAR atacar Atacar ATACARatacar Atacar ATACAR ':
    a = random.randint(0,20)
    print(f'''Rodando D20...
Você tirou {a} no dado\n''')
    if a < 10:
        print('Oishi não faz nem cócegas no demônio\n')
        l = 0
    else:
        print('Oishi causa um pequeno dano na criatura\n')
        l = 0
elif boss in 'clamar por piedadeCLAMAR POR PIEDADEClamar por piedadeclamarporpiedadeCLAMARPORPIEDADE':
    print('?... É um monstro irracional, ele não te entende\n')
    l = 0
elif boss in 'esquivarEsquivarESQUIVAR esquivar Esquivar ESQUIVAR':
    print('Rodando D20...')
    a = random.randint(0,20)
    if a < 10:
        print('Oishi não consegue esquivar do próximo ataque \n')
        l = 0
    else:
        l = 1
        print('Oishi esquiva do próximo golpe \n')
else:
    print('Oishi não vai á lugar algum \n')
    l = 0

boss = input('O quê você faz? (Atacar / Esquivar / \033[4;30mFugir\033[m / Clamar por piedade) : ')
if boss in 'atacarAtacarATACAR atacar Atacar ATACARatacar Atacar ATACAR ':
    a = random.randint(0,20)
    print(f'''Rodando D20...
Você tirou {a} no dado\n''')
    if a < 10:
        print('Você não faz nem cócegas no demônio\n')
        l1 = 0
    else:
        l1 = 0
        print('Você causa um pequeno dano na criatura\n')
elif boss in 'clamar por piedadeCLAMAR POR PIEDADEClamar por piedadeclamarporpiedadeCLAMARPORPIEDADE':
    print('?... É um monstro irracional, ele não te entende\n')
    l1 = 0
elif boss in 'esquivarEsquivarESQUIVAR esquivar Esquivar ESQUIVAR':
    print('Rodando D20...')
    a = random.randint(0,20)
    if a < 10:
        print('Você não consegue esquivar do próximo ataque \n')
        l1 = 0
    else:
        l1 = 1
        print('Você esquiva do próximo golpe \n')
else:
    print('Você não vai á lugar algum \n')
    l1 = 0

print('O monstro, Higurashi, avança em vocês dois de uma vez')
if l == 1:
    print('Oishi consegue esquivar do avanço do monstro')
else:
    print('Oishi não esquivou e tomou um soco do ser humanóide. (100 -> 56)')
if l1 == 1:
    print('Você consegue esquivar do avanço do monstro')
else:
    print('Você não esquivou e tomou um soco do ser humanóide. (90 -> 76)')
    vida = 76

boss = input('O quê Oishi faz? (Atacar / Esquivar / \033[4;30mFugir\033[m / Clamar por piedade) : ')
if boss in 'atacarAtacarATACAR atacar Atacar ATACARatacar Atacar ATACAR ':
    a = random.randint(0,20)
    print(f'''Rodando D20...
Você tirou {a} no dado\n''')
    if a < 10:
        print('Oishi não faz nem cócegas no demônio\n')
        l = 0
    else:
        print('Oishi causa um pequeno dano na criatura\n')
        l = 0
elif boss in 'clamar por piedadeCLAMAR POR PIEDADEClamar por piedadeclamarporpiedadeCLAMARPORPIEDADE':
    print('?... É um monstro irracional, ele não te entende\n')
    l = 0
elif boss in 'esquivarEsquivarESQUIVAR esquivar Esquivar ESQUIVAR':
    print('Rodando D20...')
    a = random.randint(0,20)
    if a < 10:
        print('Oishi não consegue esquivar do próximo ataque \n')
        l = 0
    else:
        l = 1
        print('Oishi esquiva do próximo golpe \n')
else:
    print('Oishi não vai á lugar algum \n')
    l = 0

boss = input('O quê você faz? (Atacar / Esquivar / \033[4;30mFugir\033[m / Clamar por piedade) : ')
if boss in 'atacarAtacarATACAR atacar Atacar ATACARatacar Atacar ATACAR ':
    a = random.randint(0,20)
    print(f'''Rodando D20...
Você tirou {a} no dado\n''')
    if a < 10:
        print('Você não faz nem cócegas no demônio\n')
        l1 = 0
    else:
        l1 = 0
        print('Você causa um pequeno dano na criatura\n')
elif boss in 'clamar por piedadeCLAMAR POR PIEDADEClamar por piedadeclamarporpiedadeCLAMARPORPIEDADE':
    print('?... É um monstro irracional, ele não te entende\n')
    l1 = 0
elif boss in 'esquivarEsquivarESQUIVAR esquivar Esquivar ESQUIVAR':
    print('Rodando D20...')
    a = random.randint(0,20)
    if a < 10:
        print('Você não consegue esquivar do próximo ataque \n')
        l1 = 0
    else:
        l1 = 1
        print('Você esquiva do próximo golpe \n')
else:
    print('Você não vai á lugar algum \n')
    l1 = 0

print('Higurashi está furioso, avança em Oishi com soco muito rápido e após isso ele tenta chutar você')
if l == 1:
    print('Oishi consegue esquivar do monstro, mas está ficando traumatizado')
else:
    print('Oishi não esquivou e tomou um soco do ser humanóide. ')
    print('Oishi está agonizando e não consegue se mover, perdendo uma ação')
if l1 == 1:
    print('Você consegue esquivar do monstro, mas por pouco')
else:
    print(f'Você não esquivou e tomou um soco do ser humanóide. (76 -> 53)')
    vida = 53
    print('Você sente suas feridas da última batalha se abrindo ')
print('\n')
boss = input('O quê você faz? (Atacar / Esquivar / \033[4;30mFugir\033[m / Clamar por piedade) : ')
if boss in 'atacarAtacarATACAR atacar Atacar ATACARatacar Atacar ATACAR ':
    a = random.randint(0,20)
    print(f'''Rodando D20...
Você tirou {a} no dado\n''')
    if a < 10:
        print('Você não faz nem cócegas no demônio\n')
        l1 = 0
    else:
        l1 = 0
        print('Você causa um pequeno dano na criatura\n')
elif boss in 'clamar por piedadeCLAMAR POR PIEDADEClamar por piedadeclamarporpiedadeCLAMARPORPIEDADE':
    print('?... É um monstro irracional, ele não te entende\n')
    l1 = 0
elif boss in 'esquivarEsquivarESQUIVAR esquivar Esquivar ESQUIVAR':
    print('Rodando D20...')
    a = random.randint(0,20)
    if a < 10:
        print('Você não consegue esquivar do próximo ataque \n')
        l1 = 0
    else:
        l1 = 1
        print('Você esquiva do próximo golpe \n')
else:
    print('Você não vai á lugar algum \n')
    l1 = 0

mixer.music.stop()
mixer.music.load("I:\Jogo\onightmare.mp3")
mixer.music.play()

print('''Higurashi pula em cima de Oishi, com intenção de matar.
... \n ''')
time.sleep(5)
print('Oishi irá morrer, mas você pode salvá-lo se pegar pelo braço e arrastá-lo rapidamente. Mas se falhar no dado D20(10 ou menos), você morrerá no lugar dele. ')
salv = input('Você tenta salvar Oishi correndo risco de morrer se falhar no dado? ( Salvar / Olhar ele ser esmagado) : ')
final = 0
if salv in 'salvarSALVARSalvar salvar Salvar SALVAR':
    print('''\n Você corre em direção á Oishi e tenta salvá-lo
Rodando D20...''')
    a = random.randint(0,20)
    print(f'Você tirou {a} \n')
    if a < 10:
        final += 1
        ida = 0
        print(f'''Você consegue salvar Oishi, mas...
Como ele é pesado, você demora muito e o golpe te atinge, Higurashi cai em cima de você, te explodindo
Você Morreu
({vida} -> {ida}) \n''')
        vida = ida
        time.sleep(10)
    elif a > 9:
        print('Você consegue salvar Oishi e sair ileso')
        print('O pulo do monstro foi tão grande que ele fica preso no chão por um tempo\n')
        time.sleep(7)
        final += 2
else:
    print('''Você não vai salvá-lo e o vê sendo morto na sua frente
O monstro está distraído comendo o que sobrou de Oishi
Enquanto isso, homens começam a arrombar a porta e entrar, com a adrenalina abaixando, você desmaia \n''')
    final = 3

if final == 1 or vida == 0:
    print('''Oishi vê seu corpo sendo explodido e grita:

    - \033[7;30mGAROTO! NÃO!\033[m

Em um acesso de fúria e em meio a lágrimas, ele saca uma granada de chamas que não usou no início pois poderia carbonizar você, mas agora que você morreu, ele a usa
O mosntro solta um grito ensurdecedor enquanto é consumido pelas chamas. Oishi se senta e espera o fogo espalhar e atingí-lo já que não tem para onde fugir por conta da porta ter sido trancada...
Até que...Oishi perde a consciência''')
elif final == 2 :
    print('''   - \033[7;30mPorquê, garoto?...\033[m

Oishi perde aconsciência
Neste tempo, policias começam a arrombar a porta que vocês estavam trancados e te resgata enquanto incineram o monstro com lança-chamas
Você perde a consciência depois que a adrenalina abaixou''')

time.sleep(20)
mixer.music.stop()
mixer.music.load("I:\Jogo\oruins.mp3")
mixer.music.play()
if final == 3:
    print('''Você acorda em uma sala branca e tem um homem em sua frente. Você está traumatizado, obviamente, e não consegue falar
    
    - Não se preocupe, trabalhávamos com Oishii e ele nos chamou antes de entrar no laboratório. Você foi resgatado e está se recuperando
    - Nós incineramos aquele bixo e prendemos o responsável
    - Você recebeu muito dano psicológico e deve ficar aqui por mais tempo, seus pais e amigos virão te visitar, agora tente descansar \n''')

if final == 1 or vida == 0:
    print('''Oishi acorda em uma sala branca, cercado de pessoas. Você se se

    - Oishi, não levante, somos nós. Você nos comunicou no caminho para aquele laboratório e acabou lutando com o experimento e perdendo a consciência \n''')
    print('''   - \033[7;30mE o... garoto...?\033[m
    
    - Conseguimos recolher algum pedaços do corpo dele. Seria ótimo se pudéssemos recrutá-lo para nosso grupo de combatentes secretos de monstros resultados de experimentos ou paranormais, ele até que se saiu bem na luta. Ah, você será penalisado pelo chefe por levar um civil sem treinamento para uma batalha, enfim, descanse \n''')
elif final == 2:
    print('''Oishi acorda em uma sala branca, cercado de pessoas

    - Oishi, não levante, somos nós. Você nos comunicou no caminho para aquele laboratório e acabou lutando com o experimento e perdendo a consciência \n''')
    print('''   - \033[7;30mE o... garoto...?\033[m

    - Está se recuperando aqui na nossa base, mas teremos que explicar para ele que somos combatentes secretos de monstros resultados de experimentos ou paranormais, ele não vai mais cair nessa que somos só policiasis, vai ser um saco explicar

    - \033[7;30mPoderíamos... recrutar ele. Se saiu bem enfrentando esse monstro\033[m

    - Pode até ser, mas mais pra frente só. Enfim, descanse e melhora para você treinar ele e você mesmo recrutá-lo \n''')
time.sleep(20)

if final == 1 :
    print('Após isso, a vila foi notificada que não existe maldição e A Ordem, composta por investigadores paranormais, teve que inventar uma desculpa para o desaparecimento e mortes das pessoas, deixando a vila mais tranquila. Irie foi preso na base especial dos Agentes e devidamente penalisado.')
if final == 2:
    print('Após isso, a vila foi notificada que não existe maldição e A Ordem, composta por investigadores paranormais, teve que inventar uma desculpa para o desaparecimento e mortes das pessoas, deixando a vila mais tranquila. Irie foi preso na base especial dos Agentes e devidamente penalisado.')
if final == 3:
    print('Após isso, a vila foi notificada que não existe maldição e os detetives tiveram que inventar uma desculpa para o desaparecimento e mortes das pessoas, deixando a vila mais tranquila. Irie foi preso e devidamente penalisado.')
time.sleep(10)
if vida == 0 :
    print(f'Os pais e amigos de {nome} foram comunicados e estão lidando com sua morte.\n')
    print('''   FINAL 2 de 3 - Ruim
Jogues os outros finais para obter mais informações e descobrir coisas novas... \n''')
    time.sleep(5)
elif vida > 0 and final == 2: 
    print('Você recebe alta e volta para a vila e é obrigado a manter segredo dos detalhes para seus amigos e família. Posteriormente você é recrutado e treinado na Ordem\n')
    print('''   FINAL 1 de 3 - Bom
Jogues os outros finais para obter mais informações e descobrir coisas novas... \n''')
    time.sleep(5)
elif vida > 0 and final == 3:
    print('Você recebe alta e volta para a vila, seus amigos e família, mas sua consciência está pesada.\n')
    print('''   FINAL 3 de 3 - Neutro
Jogues os outros finais para obter mais informações e descobrir coisas novas... \n''')
    time.sleep(5)

mixer.music.stop()


mixer.music.load("I:\Jogo\last.mp3")
mixer.music.play()
print('''    \033[1;31;41mCréditos\033[m

Desenvolvedor : Jonas
Roteirista : Roger 
Músicas : Marcos''')

time.sleep(5)

print('''Utilizando PYTHON por meio do Visual Studio Code

Inspirado no anime Higurashi no Naku Koro ni

Trilha sonora : Undertale SoundTrack''')
time.sleep(5)
print('''Obrigado por jogar!
Fim!
Fim?...''')
time.sleep(40)
mixer.music.stop()