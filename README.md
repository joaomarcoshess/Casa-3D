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

*Os nomes dos arquivos de textura são exemplos e podem ser alterados conforme os arquivos utilizados.*

## 👨‍💻 Autor

Projeto desenvolvido como atividade acadêmica da disciplina de **Computação Gráfica**.
