# Casa no Paintbrush com PyAutoGUI

Automação em Python que abre o Paintbrush e desenha uma casa colorida usando o mouse e o teclado.

## Requisitos

- macOS com Paintbrush instalado.
- Python e [uv](https://docs.astral.sh/uv/) instalados.

## Preparar o ambiente

No terminal, dentro da pasta do projeto:

1. Crie o ambiente virtual (apenas na primeira vez):

   ```sh
   uv venv
   ```

2. Ative o ambiente virtual:

   ```sh
   source .venv/bin/activate
   ```

3. Instale a dependência:

   ```sh
   uv pip install pyautogui
   ```

O ambiente fica na pasta `.venv`. Ative-o novamente sempre que abrir um novo terminal para executar os arquivos. O módulo `time` já faz parte do Python e não precisa ser instalado.

## Executar

Com o ambiente virtual ativo:

```sh
python paintbrush_house.py
```

Para capturar as coordenadas do mouse:

```sh
python capture_position.py
```

As coordenadas foram ajustadas para a tela usada no desenvolvimento. Em outro computador ou ao mover as janelas, capture as posições novamente e ajuste o script.

Durante a execução, deixe o script controlar o mouse e o teclado. Para interromper a automação, leve o ponteiro ao canto superior esquerdo da tela principal; mantenha o `FAILSAFE` habilitado.

Para sair do ambiente virtual:

```sh
deactivate
```
