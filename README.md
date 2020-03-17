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
