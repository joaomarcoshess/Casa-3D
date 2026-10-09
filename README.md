# 🏠 Casa 3D com Python e OpenGL

Para criar a casa 3D em Python, utilizei as bibliotecas numpy, GLFW, PyOpenGL e Pillow. O numpy foi utilizado para trabalhar com as matrizes e coordenadas dos objetos, enquanto o GLFW foi responsável pela criação da janela e pelos controles do teclado. Já o PyOpenGL foi utilizado para desenhar os objetos em três dimensões, e o Pillow para carregar as imagens que serão utilizadas como texturas.

Ao pensar na matemática por trás da casa, devemos analisar primeiro suas partes. Temos o corpo principal, o telhado, a porta, as janelas, a varanda, os degraus, as caixas de flores e a chaminé. Cada parte foi criada a partir de objetos geométricos, principalmente cubos e uma pirâmide, posicionados de forma que, juntos, formassem uma única construção.

A parte principal da matemática fica nas funções responsáveis pelas matrizes de translação, rotação e escala. A escala é utilizada para modificar o tamanho das peças, a rotação altera sua direção e a translação define sua posição no espaço. Dessa forma, foi possível deixar o corpo da casa mais largo, criar um telhado maior que as paredes e posicionar os demais elementos em seus respectivos lugares.

Para o telhado, foi utilizada uma pirâmide com base quadrada, enquanto o corpo da casa e os elementos decorativos foram construídos com cubos. A porta e as janelas foram posicionadas na parte frontal, e a varanda recebeu degraus para deixar a construção mais detalhada. Também foram adicionadas caixas de flores e uma chaminé, dando à casa uma aparência própria.

As transformações são combinadas por meio da multiplicação das matrizes, formando a transformação final de cada objeto. Além disso, foi utilizada uma matriz de perspectiva para dar profundidade à cena e o teste de profundidade da OpenGL para controlar quais partes ficam visíveis durante a renderização.

Para as texturas, foram preparadas coordenadas UV nos vértices de cada objeto. Essas coordenadas permitem mapear as imagens sobre as superfícies da casa, possibilitando utilizar texturas diferentes para as paredes, o telhado, a porta, as janelas e os elementos de madeira. Os caminhos das imagens ficam definidos no início do código, facilitando sua substituição.

Por fim, foram implementados controles pelas setas do teclado, permitindo girar a casa nos eixos X e Y e visualizar diferentes ângulos da construção. Tudo foi organizado na função main para inicializar a janela, carregar as texturas, configurar os objetos e executar a renderização continuamente.
