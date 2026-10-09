import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import ctypes
from PIL import Image

# CAMINHOS DAS TEXTURAS

TEXTURA_PAREDE = r"texturas/parede.jpg"
TEXTURA_TELHADO = r"texturas/telhado.jpg"
TEXTURA_PORTA = r"texturas/porta.jpg"
TEXTURA_JANELA = r"texturas/janela.jpg"
TEXTURA_MADEIRA = r"texturas/degraus.jpg"
TEXTURA_CHAMINE = r"texturas/chamine.jpg"

# SHADERS

VERTEX_SHADER = """
#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 TexCoord;

uniform mat4 MVP;

void main()
{
    gl_Position = MVP * vec4(aPos, 1.0);
    TexCoord = aTexCoord;
}
"""


FRAGMENT_SHADER = """
#version 330 core

in vec2 TexCoord;

out vec4 FragColor;

uniform sampler2D textura;

void main()
{
    FragColor = texture(textura, TexCoord);
}
"""

# CARREGAR TEXTURA

def carregar_textura(caminho):

    imagem = Image.open(caminho)

    imagem = imagem.transpose(
        Image.FLIP_TOP_BOTTOM
    )

    imagem = imagem.convert("RGBA")

    largura, altura = imagem.size

    dados = imagem.tobytes()

    textura = glGenTextures(1)

    glBindTexture(
        GL_TEXTURE_2D,
        textura
    )

    glTexParameteri(
        GL_TEXTURE_2D,
        GL_TEXTURE_MIN_FILTER,
        GL_LINEAR_MIPMAP_LINEAR
    )

    glTexParameteri(
        GL_TEXTURE_2D,
        GL_TEXTURE_MAG_FILTER,
        GL_LINEAR
    )

    glTexParameteri(
        GL_TEXTURE_2D,
        GL_TEXTURE_WRAP_S,
        GL_REPEAT
    )

    glTexParameteri(
        GL_TEXTURE_2D,
        GL_TEXTURE_WRAP_T,
        GL_REPEAT
    )

    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        largura,
        altura,
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        dados
    )

    glGenerateMipmap(
        GL_TEXTURE_2D
    )

    glBindTexture(
        GL_TEXTURE_2D,
        0
    )

    return textura

# PERSPECTIVA

def matriz_perspectiva(
    fov,
    aspecto,
    perto,
    longe
):

    f = 1.0 / np.tan(
        np.radians(fov) / 2.0
    )

    m = np.zeros(
        (4, 4),
        dtype=np.float32
    )

    m[0, 0] = f / aspecto
    m[1, 1] = f

    m[2, 2] = (
        (longe + perto)
        /
        (perto - longe)
    )

    m[2, 3] = (
        (2.0 * longe * perto)
        /
        (perto - longe)
    )

    m[3, 2] = -1.0

    return m

# TRANSLAÇÃO

def matriz_translacao(x, y, z):

    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ], dtype=np.float32)

# ESCALA

def matriz_escala(x, y, z):

    return np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

# ROTAÇÃO X

def matriz_rotacao_x(graus):

    c = np.cos(np.radians(graus))
    s = np.sin(np.radians(graus))

    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

# ROTAÇÃO Y

def matriz_rotacao_y(graus):

    c = np.cos(np.radians(graus))
    s = np.sin(np.radians(graus))

    return np.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)

# CUBO

def criar_cubo():

    vertices = np.array([

        # Frente
        -0.5, -0.5,  0.5, 0, 0,
         0.5, -0.5,  0.5, 1, 0,
         0.5,  0.5,  0.5, 1, 1,
        -0.5,  0.5,  0.5, 0, 1,

        # Trás
        -0.5, -0.5, -0.5, 1, 0,
         0.5, -0.5, -0.5, 0, 0,
         0.5,  0.5, -0.5, 0, 1,
        -0.5,  0.5, -0.5, 1, 1,

        # Esquerda
        -0.5, -0.5, -0.5, 0, 0,
        -0.5, -0.5,  0.5, 1, 0,
        -0.5,  0.5,  0.5, 1, 1,
        -0.5,  0.5, -0.5, 0, 1,

        # Direita
         0.5, -0.5, -0.5, 1, 0,
         0.5, -0.5,  0.5, 0, 0,
         0.5,  0.5,  0.5, 0, 1,
         0.5,  0.5, -0.5, 1, 1,

        # Superior
        -0.5,  0.5, -0.5, 0, 1,
         0.5,  0.5, -0.5, 1, 1,
         0.5,  0.5,  0.5, 1, 0,
        -0.5,  0.5,  0.5, 0, 0,

        # Inferior
        -0.5, -0.5, -0.5, 0, 0,
         0.5, -0.5, -0.5, 1, 0,
         0.5, -0.5,  0.5, 1, 1,
        -0.5, -0.5,  0.5, 0, 1

    ], dtype=np.float32)


    indices = np.array([

        0, 1, 2,
        2, 3, 0,

        4, 5, 6,
        6, 7, 4,

        8, 9, 10,
        10, 11, 8,

        12, 13, 14,
        14, 15, 12,

        16, 17, 18,
        18, 19, 16,

        20, 21, 22,
        22, 23, 20

    ], dtype=np.uint32)

    return vertices, indices

# PIRÂMIDE DO TELHADO

def criar_telhado():

    vertices = np.array([

        # Frente
        -0.5, 0.0,  0.5, 0, 0,
         0.5, 0.0,  0.5, 1, 0,
         0.0, 0.65, 0.0, 0.5, 1,

        # Direita
         0.5, 0.0,  0.5, 0, 0,
         0.5, 0.0, -0.5, 1, 0,
         0.0, 0.65, 0.0, 0.5, 1,

        # Trás
         0.5, 0.0, -0.5, 0, 0,
        -0.5, 0.0, -0.5, 1, 0,
         0.0, 0.65, 0.0, 0.5, 1,

        # Esquerda
        -0.5, 0.0, -0.5, 0, 0,
        -0.5, 0.0,  0.5, 1, 0,
         0.0, 0.65, 0.0, 0.5, 1,

        # Base
        -0.5, 0.0, -0.5, 0, 0,
         0.5, 0.0, -0.5, 1, 0,
         0.5, 0.0,  0.5, 1, 1,

        -0.5, 0.0, -0.5, 0, 0,
         0.5, 0.0,  0.5, 1, 1,
        -0.5, 0.0,  0.5, 0, 1

    ], dtype=np.float32)


    indices = np.arange(
        18,
        dtype=np.uint32
    )

    return vertices, indices

# BUFFERS

def criar_buffers(
    vertices,
    indices
):

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(
        GL_ARRAY_BUFFER,
        VBO
    )

    glBufferData(
        GL_ARRAY_BUFFER,
        vertices.nbytes,
        vertices,
        GL_STATIC_DRAW
    )

    glBindBuffer(
        GL_ELEMENT_ARRAY_BUFFER,
        EBO
    )

    glBufferData(
        GL_ELEMENT_ARRAY_BUFFER,
        indices.nbytes,
        indices,
        GL_STATIC_DRAW
    )

    passo = 5 * vertices.itemsize


    # Posição

    glVertexAttribPointer(
        0,
        3,
        GL_FLOAT,
        GL_FALSE,
        passo,
        ctypes.c_void_p(0)
    )

    glEnableVertexAttribArray(0)


    # Coordenada UV

    glVertexAttribPointer(
        1,
        2,
        GL_FLOAT,
        GL_FALSE,
        passo,
        ctypes.c_void_p(
            3 * vertices.itemsize
        )
    )

    glEnableVertexAttribArray(1)

    glBindVertexArray(0)

    return VAO

# DESENHAR OBJETO

def desenhar_objeto(
    shader,
    VAO,
    quantidade,
    textura,
    projecao,
    view,
    model,
    loc_mvp,
    loc_tex
):

    MVP = (
        projecao
        @ view
        @ model
    )

    glUniformMatrix4fv(
        loc_mvp,
        1,
        GL_FALSE,
        np.ascontiguousarray(
            MVP.T,
            dtype=np.float32
        )
    )

    glActiveTexture(
        GL_TEXTURE0
    )

    glBindTexture(
        GL_TEXTURE_2D,
        textura
    )

    glUniform1i(
        loc_tex,
        0
    )

    glBindVertexArray(
        VAO
    )

    glDrawElements(
        GL_TRIANGLES,
        quantidade,
        GL_UNSIGNED_INT,
        None
    )

# MAIN

def main():

    if not glfw.init():
        return


    janela = glfw.create_window(
        900,
        700,
        "Casinha 3D - Computacao Grafica",
        None,
        None
    )

    if not janela:

        glfw.terminate()
        return


    glfw.make_context_current(
        janela
    )

    glfw.swap_interval(1)

    glEnable(
        GL_DEPTH_TEST
    )

    # SHADER

    shader = OpenGL.GL.shaders.compileProgram(

        OpenGL.GL.shaders.compileShader(
            VERTEX_SHADER,
            GL_VERTEX_SHADER
        ),

        OpenGL.GL.shaders.compileShader(
            FRAGMENT_SHADER,
            GL_FRAGMENT_SHADER
        )
    )

    # GEOMETRIA

    vertices_cubo, indices_cubo = (
        criar_cubo()
    )

    vertices_telhado, indices_telhado = (
        criar_telhado()
    )


    VAO_CUBO = criar_buffers(
        vertices_cubo,
        indices_cubo
    )

    VAO_TELHADO = criar_buffers(
        vertices_telhado,
        indices_telhado
    )

    # TEXTURAS

    textura_parede = carregar_textura(
        TEXTURA_PAREDE
    )

    textura_telhado = carregar_textura(
        TEXTURA_TELHADO
    )

    textura_porta = carregar_textura(
        TEXTURA_PORTA
    )

    textura_janela = carregar_textura(
        TEXTURA_JANELA
    )

    textura_madeira = carregar_textura(
        TEXTURA_MADEIRA
    )

    textura_chamine = carregar_textura(
        TEXTURA_CHAMINE
    )

    # PROJEÇÃO

    projecao = matriz_perspectiva(
        45.0,
        900 / 700,
        0.1,
        100.0
    )


    view = matriz_translacao(
        0,
        -0.2,
        -6.5
    )

    # UNIFORMS

    loc_mvp = glGetUniformLocation(
        shader,
        "MVP"
    )

    loc_tex = glGetUniformLocation(
        shader,
        "textura"
    )

    # ROTAÇÃO

    rot_x = 18.0
    rot_y = -25.0

    velocidade = 2.0

    # LOOP

    while not glfw.window_should_close(
        janela
    ):

        glfw.poll_events()

        # SETAS

        if glfw.get_key(
            janela,
            glfw.KEY_RIGHT
        ) == glfw.PRESS:

            rot_y += velocidade


        if glfw.get_key(
            janela,
            glfw.KEY_LEFT
        ) == glfw.PRESS:

            rot_y -= velocidade


        if glfw.get_key(
            janela,
            glfw.KEY_DOWN
        ) == glfw.PRESS:

            rot_x += velocidade


        if glfw.get_key(
            janela,
            glfw.KEY_UP
        ) == glfw.PRESS:

            rot_x -= velocidade

        # LIMPAR TELA

        glClearColor(
            0.55,
            0.80,
            1.0,
            1.0
        )

        glClear(
            GL_COLOR_BUFFER_BIT |
            GL_DEPTH_BUFFER_BIT
        )

        glUseProgram(
            shader
        )

        # ROTAÇÃO DA CASA

        rotacao = (
            matriz_rotacao_x(rot_x)
            @
            matriz_rotacao_y(rot_y)
        )

        # CORPO DA CASA

        modelo = (
            rotacao
            @
            matriz_translacao(
                0,
                0,
                0
            )
            @
            matriz_escala(
                2.7,
                1.35,
                2.3
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_parede,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # TELHADO GRANDE

        modelo = (
            rotacao
            @
            matriz_translacao(
                0,
                0.65,
                0
            )
            @
            matriz_escala(
                3.05,
                1.45,
                2.65
            )
        )

        desenhar_objeto(
            shader,
            VAO_TELHADO,
            len(indices_telhado),
            textura_telhado,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # PORTA

        modelo = (
            rotacao
            @
            matriz_translacao(
                0,
                -0.25,
                1.18
            )
            @
            matriz_escala(
                0.55,
                0.95,
                0.10
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_porta,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # JANELA ESQUERDA

        modelo = (
            rotacao
            @
            matriz_translacao(
                -0.85,
                0.25,
                1.18
            )
            @
            matriz_escala(
                0.55,
                0.55,
                0.10
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_janela,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # JANELA DIREITA

        modelo = (
            rotacao
            @
            matriz_translacao(
                0.85,
                0.25,
                1.18
            )
            @
            matriz_escala(
                0.55,
                0.55,
                0.10
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_janela,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # VARANDA

        modelo = (
            rotacao
            @
            matriz_translacao(
                0,
                -0.78,
                1.35
            )
            @
            matriz_escala(
                1.45,
                0.12,
                0.65
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_madeira,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # DEGRAU 1

        modelo = (
            rotacao
            @
            matriz_translacao(
                0,
                -0.88,
                1.65
            )
            @
            matriz_escala(
                0.9,
                0.25,
                0.35
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_madeira,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # DEGRAU 2

        modelo = (
            rotacao
            @
            matriz_translacao(
                0,
                -1.02,
                1.85
            )
            @
            matriz_escala(
                1.1,
                0.22,
                0.35
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_madeira,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # CAIXINHA DE FLOR ESQUERDA

        modelo = (
            rotacao
            @
            matriz_translacao(
                -0.85,
                -0.12,
                1.30
            )
            @
            matriz_escala(
                0.65,
                0.18,
                0.20
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_madeira,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # CAIXINHA DE FLOR DIREITA

        modelo = (
            rotacao
            @
            matriz_translacao(
                0.85,
                -0.12,
                1.30
            )
            @
            matriz_escala(
                0.65,
                0.18,
                0.20
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_madeira,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # CHAMINÉ

        modelo = (
            rotacao
            @
            matriz_translacao(
                0.75,
                1.45,
                -0.25
            )
            @
            matriz_escala(
                0.40,
                0.8,
                0.40
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_chamine,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )

        # TOPO DA CHAMINÉ

        modelo = (
            rotacao
            @
            matriz_translacao(
                0.75,
                1.75,
                -0.25
            )
            @
            matriz_escala(
                0.52,
                0.15,
                0.52
            )
        )

        desenhar_objeto(
            shader,
            VAO_CUBO,
            len(indices_cubo),
            textura_madeira,
            projecao,
            view,
            modelo,
            loc_mvp,
            loc_tex
        )


        glfw.swap_buffers(
            janela
        )


    glfw.terminate()

if __name__ == "__main__":
    main()