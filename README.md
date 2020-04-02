# ProjetoMestrado
Aplicação Django para Classificação Biomédica, usando técnicas de evolução computacional

Link Documentação: https://1drv.ms/f/s!AgOJzz54YksKgpZ978MIk4pHmeZbFw

Info e Links Datasets Gene Expression e Imagens, estão no fundo do doc Cifar_10

Cifar-10:
  - Apliquei o GA na Cloud e descrevi os resultados --> Conclui que a função de custo não estava coerente. Então reformulei a função de custo e apliquei (para ser mais rápido) no problema do microArray Breast Cancer, mais concretamente na rede CONV-2D. Os resultados obtidos e descrição encontram-se devidamente descritos;
  -Tal, como o professor sugeriu efetuei uma análise mais profunda entre resultados e complexidade das redes. Destaquei essa abordagem também na rede VGGNet. Resultados e conclusões descritas.
  - PSO na Cloud --> o algoritmo estava a demorar bastante, e terminei a sua execução. Para além disso, quando o executei não tinha a função de custo atualizada. Vou depois testar o PSO neste novo dataset, visto que está diretamente relacionado com o projeto, e como já investi muito tempo no Cifar, gostaria depois de perder esse tempo, num dataset que possa utilizar no projeto.
  
Breast Histopathology Images:
  Escolhi este dataset --> https://www.kaggle.com/paultimothymooney/breast-histopathology-images
  Estou atualmente a criar um script em Jupyter como análise exploratória dos dados e dataset, dps forneço acesso aos dados e documentos.
  Escolhi este dataset, porque do que fui lendo é um dataset complexo e binário.
  Eventualmente, poderei demorar um pouco mais a preparar este dataset, devido ao facto de ter de reforçar as miinhas bases nas bibliotecas pandas e os.

## Atualização 17/03:
  - Já efetuei toda a análise exploratória e já documentei os dados (para além do jupyter notebook criado);
  - Criar uma arquitetura bem mais robusta para responder ao problema: recorri a fábricas de objetos, estratégia, template, etc. De modo a aumentar a flexibilidade do código, sendo que à partida a arquitetura desenvolvida adapta-se a qualquer tipo de problema. **Ainda estou a retificar últimos ajustes**.
  - Depois de terminar este último ponto. Em príncipio começo já hoje, a documentar e a explicar o diagrama de classes utilizado. E ainda a explicar as técnicas de pré-processamento utilizadas.
  - A execução dos modelos e análises dos resultados, pode ser efetuada logo, dado que o código já está todo funcional. 
  - Os dados são muitos, e as classes não são balanceadas, criei várias estratégias (padrão) para dar resposta a este problema: Undersampling, OverSampling e Data Augmentation. O nº de dados a trabalhar terá de ser bem analisado ainda.
  - Preparado código para dar resposta a vários otimizadores, com facilidade. Neste momento estou me a concentrar apenas no PSO.
  - **Assim que terminar a escrita sobre a explicação da arquitetura e das técnicas de pré-processamento, disponibilizo o documento, no repositório. Para que depois me possa concentrar na análise de resultados**.

## Atualização 20/03:
  - A documentação relativa à análise exploratória, pré-processamento dos dados e arquitetura já foi desenvolvida;
  - Já inseri doc pdf no repositório, com o nome: **breast_histopathology_dataset**;
  - Neste momento vou começar a analisar os resultados:
    - Considerando diferentes tipos de rede (AlexNet, VGGNet, e eventual outra como ResNet);
    - Considerando volumes de dados distintos e complexidade da rede;
    - Diferentes estratégias de treino: undersampling, oversampling e data augmentation;
    - Utilização de otimizador, neste caso foco no PSO;
  - **Como esta análise vai já ser incluída (claro que resumida e devidamente bem fundamentada) no relatório, vou procurar a obtenção de bons resultados, e ainda de proceder uma análise mais cuidada. Vou tentar analisar várias métricas: Matriz confusão e AUC**;
  - Caso esteja a demorar um pouco mais nesta análise, vou atualizando o ficheiro;
 
 ## Atualização 25/03:
  - Documentação atualizada;
  - Documento pdf, permanece com o nome: **breast_histopathology_dataset**;
  - Toda a análise até à utilização do PSO fundamentada, ilustrada e explicada (AlexNet);
  - **O PSO provavelmente vai demorar bastante**;
  - GA lógica desenvolvida (caso haja necessidade, depois aplico);
  - A análise com VGGNet, vai ser mais resumida cingindo-me aos melhores resultados, porque no AlexNet contei uma história descritiva, de melhoria gradual do modelo;
  - Análises recorrendo a Matriz confusão, com foco no recall e precision da class menos balanceada (com Invasive Ductal Carcinoma) - maior foco no recall;
  - O dataset é complexo, mais concretamente na classificação desta classe, do que tenho lido, os resultados parecem-me bem ajustados;
  - Utilizei diversas abordagens para mellhorar resultados, como: Undersampling, Data Augmentation, class_weights, callbacks, etc;

## Atualização 28/03:
  - Documentação Atualizada;
  - Análise do VGGNet concluída (faltando parte otimização);
  - Fiz mais testes em AlexNet e consegui melhores resultados;
  - Maior exaustão na identificação de bons resultados (no VGGNet consegui também resultados interiores, e acima dos do artigo original);
  - Faltando assim apenas a aplicação do PSO;

## Atualização 02/04:
  - Compreensão do âmbito do problema do dataset Skin Mnist já documentada;
  - Análise exploratória do Skin Mnist já realizada (a documentar neste momento);
  - Criação de um projeto "aparte" com a arquitetura default a aplicar a qualquer tipo de problema relacionado com imagens (Skin Mnist, já é um git pull repo, deste repositório);
  - Preparação dos dados do problema já completa, faltando apenas implementar os modelos (apenas construção, que toda a arquitetura já está definida);
  - Neste momento estou a tentar resolver problemas na Cloud;
    - A minha conta já não é free, mas ainda assim o Google não me deixa aumentar cotas, tou a tentar encontrar abordagens para mitigar este problema;
    - Depois, tive problemas com o acesso remoto à Cloud, tive de reverter a instalação de ambiente gráfico, e utilizar outra ferramenta de acesso remoto;
