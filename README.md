# Casa 3D com Python e OpenGL

## 📌 Sobre o projeto

Este projeto consiste na criação de uma casa tridimensional utilizando Python e OpenGL, como parte da atividade de Computação Gráfica. A construção é formada por diferentes objetos geométricos que, juntos, representam as partes de uma casa.

O objetivo é aplicar conceitos de **transformações geométricas, projeção 3D, texturização e interação com o teclado**.

## ✨ Funcionalidades

* Construção de uma casa em 3D.
* Utilização de cubos e pirâmide para formar a estrutura.
* Aplicação de transformações geométricas: translação, rotação e escala.
* Suporte à aplicação de texturas nas superfícies dos objetos.
* Projeção em perspectiva para visualizar a profundidade.
* Rotação da casa pelos eixos X e Y utilizando as setas do teclado.
* Elementos decorativos, como porta, janelas, varanda, degraus, caixas de flores e chaminé.

## 🛠️ Tecnologias utilizadas

* **Python:** linguagem utilizada no desenvolvimento.
* **NumPy:** manipulação de matrizes e coordenadas.
* **GLFW:** criação da janela e captura das entradas do teclado.
* **PyOpenGL:** renderização dos objetos tridimensionais.
* **Pillow:** carregamento das imagens utilizadas como texturas.

## 📐 Conceitos de Computação Gráfica

Para construir a casa, foram utilizadas matrizes de **translação, rotação e escala**. A escala modifica o tamanho dos objetos, a rotação altera sua orientação e a translação define suas posições no espaço.

As transformações são combinadas por meio da multiplicação de matrizes, formando a transformação final de cada objeto. Também são utilizadas projeção em perspectiva e teste de profundidade para representar corretamente a cena tridimensional.

Para aplicar as texturas, são utilizadas coordenadas UV nos vértices dos objetos, permitindo mapear imagens sobre suas superfícies.

## 🔧 Funções implementadas

### `carregar_textura(caminho)`

Responsável por carregar as imagens que serão utilizadas como texturas dos objetos. A função abre a imagem com a biblioteca Pillow, inverte sua orientação vertical, converte-a para RGBA e envia os dados para a OpenGL. Também configura os parâmetros de filtragem e repetição da textura.

### `matriz_perspectiva(fov, aspecto, perto, longe)`

Cria a matriz de projeção em perspectiva, responsável por representar a profundidade da cena tridimensional. Seus parâmetros definem o campo de visão, a proporção da janela e os limites de distância de visualização.

### `matriz_translacao(x, y, z)`

Cria uma matriz de translação utilizada para posicionar os objetos no espaço tridimensional. Os parâmetros definem o deslocamento nos eixos X, Y e Z.

### `matriz_escala(x, y, z)`

Cria uma matriz de escala para modificar as dimensões dos objetos. Cada parâmetro controla o tamanho nos respectivos eixos, permitindo deixar as peças mais largas, altas ou profundas.

### `matriz_rotacao_x(graus)`

Cria uma matriz de rotação em torno do eixo X, permitindo inclinar os objetos para frente ou para trás. O ângulo de rotação é informado em graus.

### `matriz_rotacao_y(graus)`

Cria uma matriz de rotação em torno do eixo Y, permitindo girar os objetos para os lados e visualizar diferentes ângulos da construção.

### `criar_cubo()`

Define os vértices, as coordenadas de textura e os índices que formam um cubo. Essa geometria é reutilizada para construir o corpo da casa e os elementos adicionais, como a porta, as janelas, a varanda, os degraus e a chaminé.

### `criar_telhado()`

Define os vértices e os índices utilizados para construir a geometria do telhado em formato de pirâmide de base quadrada. As coordenadas de textura permitem mapear uma imagem sobre suas faces.

### `criar_buffers(vertices, indices)`

Cria e configura os buffers da OpenGL responsáveis por armazenar os dados dos vértices e dos índices dos objetos. Também configura os atributos de posição e as coordenadas UV utilizadas no mapeamento das texturas.

### `desenhar_objeto(shader, VAO, quantidade, textura, projecao, view, model, loc_mvp, loc_tex)`

Responsável por desenhar cada objeto na tela. A função combina as matrizes de projeção, visualização e modelo para calcular a matriz MVP, envia essa matriz ao shader, seleciona a textura correspondente e executa o desenho da geometria.

### `main()`

É a função principal do programa. Inicializa o GLFW, cria a janela, configura o shader, prepara as geometrias e carrega as texturas. Em seguida, executa o loop principal, verifica as teclas pressionadas, aplica as rotações e desenha cada parte da casa até que a janela seja fechada.


## 🎨 Texturas

As texturas são carregadas a partir dos caminhos definidos no início do arquivo `casa_3d.py`, permitindo utilizar imagens diferentes para as paredes, o telhado, a porta, as janelas e os elementos decorativos.

Os caminhos podem ser configurados de acordo com a organização dos arquivos do projeto.

## ⚙️ Instalação

Certifique-se de ter o Python instalado. Em seguida, instale as dependências necessárias executando:

```bash
python -m pip install numpy glfw PyOpenGL Pillow
```

## ▶️ Como executar

1. Clone o repositório:

   ```bash
   git clone URL_DO_REPOSITORIO
   ```

2. Entre na pasta do projeto:

   ```bash
   cd NOME_DO_REPOSITORIO
   ```

3. Configure os caminhos das texturas no arquivo `casa_3d.py`.

4. Execute o programa:

   ```bash
   python casa_3d.py
   ```

## 🎮 Controles

| Tecla | Ação                 |
| ----- | -------------------- |
| `↑`   | Rotacionar no eixo X |
| `↓`   | Rotacionar no eixo X |
| `←`   | Rotacionar no eixo Y |
| `→`   | Rotacionar no eixo Y |

## 📂 Estrutura do projeto

```text
casa-3d/
├── casa_3d.py
├── README.md
└── texturas/
    ├── parede.jpg
    ├── telhado.jpg
    ├── porta.jpg
    ├── janela.jpg
    ├── madeira.jpg
    └── tijolo.jpg
```


## 👨‍💻 Autor

João Marcos Silva Hess. 
Projeto desenvolvido como atividade acadêmica da disciplina de **Computação Gráfica**.
