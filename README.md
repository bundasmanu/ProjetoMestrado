# ProjetoMestrado


<!-- Aplicação Django para Classificação Biomédica, usando técnicas de evolução computacional -->

<!--Link Documentação: https://1drv.ms/f/s!AgOJzz54YksKgpZ978MIk4pHmeZbFw -->

<!--Info e Links Datasets Gene Expression e Imagens, estão no fundo do doc Cifar_10-->

<!--Cifar-10:
  - Apliquei o GA na Cloud e descrevi os resultados: Conclui que a função de custo não estava coerente. Então reformulei a função de custo e apliquei (para ser mais rápido) no problema do microArray Breast Cancer, mais concretamente na rede CONV-2D. Os resultados obtidos e descrição encontram-se devidamente descritos;
  -Tal, como o professor sugeriu efetuei uma análise mais profunda entre resultados e complexidade das redes. Destaquei essa abordagem também na rede VGGNet. Resultados e conclusões descritas.
  - PSO na Cloud: o algoritmo estava a demorar bastante, e terminei a sua execução. Para além disso, quando o executei não tinha a função de custo atualizada. Vou depois testar o PSO neste novo dataset, visto que está diretamente relacionado com o projeto, e como já investi muito tempo no Cifar, gostaria depois de perder esse tempo, num dataset que possa utilizar no projeto. -->
  
<!-- Breast Histopathology Images:
  Escolhi este dataset: https://www.kaggle.com/paultimothymooney/breast-histopathology-images
  Estou atualmente a criar um script em Jupyter como análise exploratória dos dados e dataset, dps forneço acesso aos dados e documentos.
  Escolhi este dataset, porque do que fui lendo é um dataset complexo e binário.
  Eventualmente, poderei demorar um pouco mais a preparar este dataset, devido ao facto de ter de reforçar as miinhas bases nas bibliotecas pandas e os. -->

<!--## Atualização 17/03:
  - Já efetuei toda a análise exploratória e já documentei os dados (para além do jupyter notebook criado);
  - Criar uma arquitetura bem mais robusta para responder ao problema: recorri a fábricas de objetos, estratégia, template, etc. De modo a aumentar a flexibilidade do código, sendo que à partida a arquitetura desenvolvida adapta-se a qualquer tipo de problema. **Ainda estou a retificar últimos ajustes**.
  - Depois de terminar este último ponto. Em príncipio começo já hoje, a documentar e a explicar o diagrama de classes utilizado. E ainda a explicar as técnicas de pré-processamento utilizadas.
  - A execução dos modelos e análises dos resultados, pode ser efetuada logo, dado que o código já está todo funcional. 
  - Os dados são muitos, e as classes não são balanceadas, criei várias estratégias (padrão) para dar resposta a este problema: Undersampling, OverSampling e Data Augmentation. O nº de dados a trabalhar terá de ser bem analisado ainda.
  - Preparado código para dar resposta a vários otimizadores, com facilidade. Neste momento estou me a concentrar apenas no PSO.
  - **Assim que terminar a escrita sobre a explicação da arquitetura e das técnicas de pré-processamento, disponibilizo o documento, no repositório. Para que depois me possa concentrar na análise de resultados**. -->

<!-- ## Atualização 20/03:
  - A documentação relativa à análise exploratória, pré-processamento dos dados e arquitetura já foi desenvolvida;
  - Já inseri doc pdf no repositório, com o nome: **breast_histopathology_dataset**;
  - Neste momento vou começar a analisar os resultados:
    - Considerando diferentes tipos de rede (AlexNet, VGGNet, e eventual outra como ResNet);
    - Considerando volumes de dados distintos e complexidade da rede;
    - Diferentes estratégias de treino: undersampling, oversampling e data augmentation;
    - Utilização de otimizador, neste caso foco no PSO;
  - **Como esta análise vai já ser incluída (claro que resumida e devidamente bem fundamentada) no relatório, vou procurar a obtenção de bons resultados, e ainda de proceder uma análise mais cuidada. Vou tentar analisar várias métricas: Matriz confusão e AUC**;
  - Caso esteja a demorar um pouco mais nesta análise, vou atualizando o ficheiro; -->
 
 <!--## Atualização 25/03:
  - Documentação atualizada;
  - Documento pdf, permanece com o nome: **breast_histopathology_dataset**;
  - Toda a análise até à utilização do PSO fundamentada, ilustrada e explicada (AlexNet);
  - **O PSO provavelmente vai demorar bastante**;
  - GA lógica desenvolvida (caso haja necessidade, depois aplico);
  - A análise com VGGNet, vai ser mais resumida cingindo-me aos melhores resultados, porque no AlexNet contei uma história descritiva, de melhoria gradual do modelo;
  - Análises recorrendo a Matriz confusão, com foco no recall e precision da class menos balanceada (com Invasive Ductal Carcinoma) - maior foco no recall;
  - O dataset é complexo, mais concretamente na classificação desta classe, do que tenho lido, os resultados parecem-me bem ajustados;
  - Utilizei diversas abordagens para mellhorar resultados, como: Undersampling, Data Augmentation, class_weights, callbacks, etc; -->

<!--## Atualização 28/03:
  - Documentação Atualizada;
  - Análise do VGGNet concluída (faltando parte otimização);
  - Fiz mais testes em AlexNet e consegui melhores resultados;
  - Maior exaustão na identificação de bons resultados (no VGGNet consegui também resultados interiores, e acima dos do artigo original);
  - Faltando assim apenas a aplicação do PSO;-->

<!--## Atualização 02/04:
  - Compreensão do âmbito do problema do dataset Skin Mnist já documentada;
  - Análise exploratória do Skin Mnist já realizada (a documentar neste momento) - Jupyter notebook criado;
  - Criado um projeto "aparte" com a arquitetura default a aplicar a qualquer tipo de problema relacionado com imagens (Skin Mnist, já é um git pull repo, deste repositório);
  - Preparação dos dados do problema já completa (leitura, obtenção dos datasets, transformação dos dados, etc) - esta parte também irá ser documentada de seguida, faltando apenas implementar os modelos (apenas construção, já que toda a arquitetura já está definida);
  - Neste momento estou a tentar resolver problemas na Cloud;
    - A minha conta já não é free, mas ainda assim o Google não me deixa aumentar cotas, tou a tentar encontrar abordagens para mitigar este problema;
    - Depois, tive problemas com o acesso remoto à Cloud, tive de reverter a instalação de ambiente gráfico, e utilizar outra ferramenta de acesso remoto;-->
    
<!--## Atualização 04/04:
  **Documentação (atual) inserida no repositório**
  - Adição de mais detalhes relativos ao âmbito do problema Skin Mnist (documentados);
  - Análise exploratória totalmente documentada, e alteração/adição de conteúdo no jupyter notebook;
  - Já foi também documentada a preparação dos dados, que foi necessária e aplicada;
  - Neste momento já me encontro a criar os modelos (AlexNet já criado e testado, com e sem estratégias de treino);
  - Estou a estudar também a aplicação da rede U-Net, que parece me uma boa opção para a resolução deste problema;
  - Relativamente à Cloud, não me deixam aumentar as quotas, de que necessito;
  - Já agendei uma reunião com um Especialista da Google, para resolver o problema, entretanto vou continuar a trabalhar neste dataset;-->

<!--## Atualização 09/04:
  - Modelo AlexNet implementado, testado e praticamente quase documentado (com análise bem definida);
  - Implementados modelos VGGNet e ResNet - já testados (documentação será mais breve);
  - Utilizei a rede U-Net com pesos obtidos do treino de um problema extenso Coco Dataset (ficheiro com os pesos da rede obtido na web);
  - Segmentei as imagen utilizando a rede U-Net (predict). Imagens já obtidas. Esta abordagem foi considerada de modo a tentar identificar as partes mais importantes de cada imagem (e classes), na tentativa de melhorar os resultados;
  - Definição de ensemble, recorrendo aos melhores modelos obtidos (AlexNet, VGGNet, ResNet);
  - Relativamente à Cloud, ainda estou com problemas com o Google Cloud. Já falei com os profissionais dele, mas eles dão mais importância a empresas. O meu pedido foi para análise novamente. Tou a estudar outras alternativas, como o uso do Gradient (mas terei de pagar mensalmente).
  - Neste momento, estou a documentar as análises, dado que a implementação está pronta.
  - Neste problema, considerei um maior nº de abordagens, porque o dataset é mais complexo que o anterior (bem mais). Espero que a utilização futura do PSO, permita a obtenção de melhores resultados;-->

<!--## Atualização 13/04:
  - Documentação atualizada "Skin_MNIST_Analise.pdf";
  - Toda a análise às três arquiteturas criadas já foi documentada (AlexNet, VGGNet e ResNet);
  - Redes mais capazes VGGNet e ResNet - comparando os resultados macro average, com os disponibilizados no Kaggle, os mesmos são melhores, sendo que foi considerando sempre um baixo nº de epochs, que influencia ligeiramente os resultados;
  - A aplicação de segmentação recorrendo à rede U-Net, não permite a obtenção de melhores resultados. Sendo assim, vou descartar esta opção. Mas vou analisar melhor.;
  - Tenciono aplicar o PSO, recorrendo a duas topologias - Global Best e Local Best;
  - Relativamente ao problema da Google, já resolvi em parte, mas penso que vou necessitar de recorrer a outras abordagens;-->

<!--## Atualização 16/04:
  - Documentação atualizada "Skin_MNIST_Analise.pdf";
  - Documentação atualizada "breast_histopathology_dataset.pdf";
  - Foi aplicado e documentado o conceito de Ensemble, em ambos os dataset's;
  - Corrigidos problemas de código, existentes em ambos os respositórios (dois dataset's);
  - Definida uma Função objetivo mais robusta, para o PSO;
  - Adição de mais conteúdo relevante e retificação de erros no repositório, que contêm a arquitetura base de todos os dataset's. Pode ser utilizado, no estudo de qualquer dataset de imagens. Ambos os dataset's em estudo são um git pull repo desse mesmo repositório. O seu Diagrama de Classes está inserido no documento: breast_histopathology_dataset.pdf;
  - Falta-me apenas aplicar o PSO: necessito de aprovação da minha ideia, por parte do professor;-->

<!--## Atualização 19/04:
  - Retificados problemas arquiteturais no código do otimizador (PSO);
  - Análise breve sobre quais os melhores valores a considerar para as constantes c1 e c2: abordagem prática e com efeito prático nos problemas;
  - Análise Estado de Arte: plataformas web, que permitem efetuar classificação de imagens (ImJoy, NiftyNet, e app's mobile);
  - Estudo teórico sobre técnicas de Imbalanced Data (Undersampling e Oversampling);
  - Estudo teórico "breve" sobre a abordagem "Ensemble";
  - Paperspace revela-se uma boa opção;-->
 
 <!--## Atualização 24/04:
  - Retificação de bugs na otimização com o PSO;
  - PSO já está a correr na Cloud, mas está a demorar bastante cerca de 40h e ainda não terminou o 1º script, acho que vou ter de reduzir as variáveis;
  - O dataset Colorectal Histopathology já foi estudado, preparados os dados e efetuada a sua pré-análise;
  - Já foi documentado o problema e ainda a pré-análise realizada;
  - Vou começar a desenvolver os modelos e a analisar os resultados;-->
  
 <!--## Atualização 30/04:
  - Tive problemas na definição da função objetivo do PSO, tive de reformular e voltar a executar o script que já tinha executado;
  - Foram corrigidos pequenos "bugs" identificados em alguns datasets;
  - Já obtive resultados alusivos à otimização do modelo AlexNet com o PSO (topologia em Roda) e tá a terminar a otimização do modelo VGGNet (também topologia em Roda);
  - Já conclui o estudo do Dataset Colorectal Histopathology, sendo que consegui obter bons resultados;
  - Já documentei toda a análise do dataset, inclusivé implementação da técnica ensemble. Faltando apenas documentar a otimização dos modelos com o PSO;
  - Neste momento estou a estudar a ferramenta Paperspace. De modo a verificar, se a mesma consegue dar resposta ao que pretendo.-->
  
 <!--## Atualização 04/05:
   - Tive problemas na "reprodutibilidade" de resultados no Breast Histopathology, e necessitei de refazer uma parte da documentação, e de aplicar e testar novamente os modelos;
   - Já obtive resultados da aplicação do PSO no dataset Breast Histopathology, nomeadamente AlexNet (Topologia em Roda) e VGGNet (ambas as topologias - Roda e Estrela), faltando apenas obter AlexNet topologia em Estrela;
   - Os resultados obtidos foram significativamente melhores na aplicação do PSO;
   - Os meus créditos no Google Cloud terminaram, e já procedi à passagem para o Paperspace;
   - Alguns "bugs" pontuais no código foram corrigidos;-->
 
 <!--## Atualização 08/05:
  - Analisada e criada arquitetura baseada na rede DenseNet;
  - Testada no 1º dataset - Breast Histopathology;
  - Reformulada a optimização de todas as arquiteturas (AlexNet, VGGNet, ResNet e DenseNet) - passei a considerar a otimização das suas arquiteturas também;
  - **Ainda estou a terminar a reformulação destes custom models;**
  - Servidor no Paperspace já está completamente funcional para dois dataset's - faltando apenas otimizar os modelos;
  - **A otimização que fiz previamente, já não irá ser considerada. Uma vez que antes não estava a otimizar a arquitetura dos modelos, enquanto que agora já estou (arquitetura, filtros, neurónios e batch size);**-->

<!--## Atualização 15/05:
  - Arquitetura DenseNet melhorada e já devidamente formulada em contexto com o paper original (adição de nova dimensão - compression rate);
  - Restantes modelos melhorados, isto é, a definição das suas arquiteturas e sua consequente otimização. ResNet em conformidade com o paper original (ResNet 18 e 34);
  - Melhoria de pequenos aspetos arquiteturais dos modelos AlexNet e VGGNet - mediante os seus papers também (AlexNet teve uma ligeira diferença no 1º dataset - dado o seu menor input (1º conv layer com stride=1, e não 2, para não limitar tanto a definição da arquitetura);
  - Projeto Django melhorado. Adição de modelos - Dataset e CNN models (relação 1-N). Criação de vistas e templates para dar suporte a criação de dataset, visualização de dataset (e aspetos relacionados com modelos), alteração de dataset;-->
 
 <!--## Atualização 02/06:
  - Melhoria na definição das arquiteturas, em conformidade com o conteúdo original;
  - Criação de um maior nº de templates na plataforma;
  - Layout geral da aplicação definido (responsivo);
  - Criação de Fluxos, a explicar a abordagem aplicada;
  - Definição dos layout's de CRUD definidos (à espera de confirmação);
  - Realização de apresentação do trabalho desenvolvido e a realizar;-->

## What is DiagnosisViewer and what is it for?

DiagnosisViewer is a web application designed using the Django framework, which aims to promote an intuitive and simple approach to sharing knowledge among the community of data scientists.

The platform promotes the submission and the use of convolutional models, created in response to multiple benchmarks, in the diagnosis of biomedical samples.

The user has total freedom to insert datasets (nominal definition only) and convolutional models in the platform, for consequent use in diagnosis.

The app is robust and fast, with diagnostic results being presented in a time interval of less than 10s. Unlike other applications, the models are not trained on the platform, i.e., they are compiled according to the base settings defined by the users, thus providing freedom for the submission of models with different development approaches, such as: splitting techniques, sampling, regularization, etc. This approach removes the hardware dependencies that are normally required in browser-based training of CNN networks.

The biggest advantage of the app, compared to the other apps, is that it allows the diagnostic functionality to be used in a high number of benchmarks, since the higher the number of models and benchmarks submitted the greater the offer available. The remaining app's focus exclusively on the study of 1-3 benchmarks.

The application also provides a diagnosis history, for this purpose provides interactively information about the most commonly used datasets and models by the community, and the most used by the logged-in user.

## Project Setup:

The steps required for the correct configuration of the platform are listed below.

1. You need to previously install the SGDB PostgreSQL in order to support database operations;
2. Clone this repository (root folder of project need to be Projeto_Mestrado, if you want to change this name you need to change some flags in settings.py files: STATIC_ROOT and DATASET_PATH with your root folder name);
3. Change settings.py file, in concordance with your PostgreSQL credentials (or you should create a secrets.py file with credentials and SECRET_KEY of project);
4. Install requirements: pip install -r requirements.txt;
5. Apply migrations to database (to create tables): python manage.py migrate;
    * If you have problems in this step, one workaround can be:
        1. Drop all migrations files;
        2. Run makemigrations command, in order to create migration files of all app's of project: python manage.py makemigrations;
        3. Now run again python manage.py migrate;

## Optimized models 

The results obtained for each optimized architecture are described below, in accordance with the problems being solved.
There are also available links to download the models.

### Results - Breast Histopathology:
| Model | Memory | Macro Average F1Score | Macro Average Recall | Accuracy | File | 
|---|---|---|---|---|---|
| AlexNet | 14,6 MB | 90.2% | 89.7% | 92.1% | [AlexNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Breast_Histopathology/alex_net_oficial.h5?raw=true) |
| VGGNet | 13,1 MB | 90.5% | 89.6% | 92.4% | [VGGNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Breast_Histopathology/vggnet_oficial.h5?raw=true) |
| ResNet | 29,9 MB |  90.4% |  90.2% | 92.2% | [ResNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Breast_Histopathology/resnet_oficial.h5?raw=true) |
| DenseNet | 10,3 MB | 89.8% |  89.4% | 91.7% | [DenseNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Breast_Histopathology/densenet_oficial.h5?raw=true) |
| Ensemble Average All Models | 22,8 MB | 91.1% | 90.7%  | 92.9% | [Ensemble h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Breast_Histopathology/ensemble_all.h5?raw=true) |

### Results - Skin Mnist:
| Model | Memory | Macro Average F1Score | Macro Average Recall | Accuracy | File | 
|---|---|---|---|---|---|
| AlexNet | 7,8 MB | 65.4% | 63.5% | 81.1% | [AlexNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Skin_MNIST/alexnet_gbest_oficial.h5?raw=true) |
| VGGNet | 12,9 MB | 64.8% | 62.3% | 80.8% | [VGGNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Skin_MNIST/vggnet_gbest_oficial.h5?raw=true) |
| ResNet | 39,8 MB |  66.5% |  64.2% | 81.3% | [ResNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Skin_MNIST/resnet_gbest_oficial.h5?raw=true) |
| DenseNet | 4,4 MB | 67.6% |  65.4% | 81.6% | [DenseNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Skin_MNIST/densenet_gbest_oficial.h5?raw=true) |
| Ensemble Average All Models | 21,8 MB | 68.5% | 65.2%  | 83.0% | [Ensemble All Models h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Skin_MNIST/ensemble_all.h5?raw=true) |
| Ensemble Average Alex + VGG + Dense | 17,5 MB | 69.2% | 66.5%  | 83.1% | [Ensemble Best Combination h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Skin_MNIST/ensemble_best.h5?raw=true) |

### Results - Colorectal Histopathology:
| Model | Memory | Macro Average F1Score | Accuracy | File | 
|---|---|---|---|---|
| AlexNet | 19,0 MB | 94.2% | 94.3% | [AlexNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Colorectal_Histopathology/alexnet_gbest_oficial.h5?raw=true) |
| VGGNet | 15,5 MB | 94.5% | 94.6% | [VGGNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Colorectal_Histopathology/vggnet_gbest_oficial.h5?raw=true) |
| ResNet | 11,4 MB |  95.5% | 95.7% | [ResNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Colorectal_Histopathology/resnet_gbest_oficial.h5?raw=true) |
| DenseNet | 17,9 MB | 96.0% | 96.1% | [DenseNet h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Colorectal_Histopathology/densenet_gbest_oficial.h5?raw=true) |
| Ensemble Average All Models | 21,4 MB | 95.5% | 95.6% | [Ensemble All Models h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Colorectal_Histopathology/ensemble_all.h5?raw=true) |
| Ensemble Average Res+ Dense | 9,9 MB | 96.6% | 96.6% | [Ensemble Best Combination h5 File](https://github.com/bundasmanu/ProjetoMestrado/blob/master/arquiteturas_otimizadas/Colorectal_Histopathology/ensemble_best.h5?raw=true) |

<!--## Link Diagrama de Classes Arquitetura Base para análises dos Dataset's:
 [Architecture Image](breast_Class_Diagram.png)-->

### Licence

GPL-3.0 License  
I am open to new ideas and improvements to the current repository. However, until the defense of my Project report, I will not accept pull request's.
