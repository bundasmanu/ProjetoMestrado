# ProjetoMestrado
Aplicação Django para Classificação Biomédica, usando técnicas de evolução computacional

Link Documentação: https://1drv.ms/f/s!AgOJzz54YksKgpZ978MIk4pHmeZbFw

Info e Links Datasets Gene Expression e Imagens, estão no fundo do doc Cifar_10

Cifar-10:
  - Apliquei o GA na Cloud e descrevi os resultados --> Conclui que a função de custo não estava coerente. Então reformulei a função de custo e apliquei (para ser mais rápido) no problema do microArray CONV-2D. Os resultados obtidos e descrição encontram-se devidamente descritos;
  -Tal, como o professor sugeriu efetuei uma análise mais profunda entre resultados e complexidade das redes. Destaquei essa abordagem também na rede VGGNet. Resultados e conclusões descritas.
  - PSO na Cloud --> o algoritmo estava a demorar bastante, e terminei a sua execução. Para além disso, quando o executei não tinha a função de custo atualizada. Vou depois testar o PSO neste novo dataset, visto que está diretamente relacionado com o projeto, e como já investi muito tempo no Cifar, gostaria depois de perder esse tempo, num dataset que possa utilizar no projeto.
  
Breast Histopathology Images:
  Escolhi este dataset --> https://www.kaggle.com/paultimothymooney/breast-histopathology-images
  Estou atualmente a criar um script em Jupyter como análise exploratória dos dados e dataset, dps forneço acesso aos dados e documentos.
  Escolhi este dataset, porque do que fui lendo é um dataset complexo e binário.
  Eventualmente, poderei demorar um pouco mais a preparar este dataset, devido ao facto de ter de reforçar as miinhas bases nas bibliotecas pandas e os.
