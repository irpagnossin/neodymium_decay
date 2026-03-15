# Decaimento do Netúnio (Np)

O objetivo deste projeto é simular o decaimento radioativo do Netúnio, Neodímio etc. Inicialmente, vamos usar cadeias de Markov e, a partir daí, estimar os espectros de emissão beta e de radiação eletromagnética. Também a abundância de cada estado acessível no decaimento.

## Dependências

- Python 3.12 ou superior

Opcional:

- [uv](https://docs.astral.sh/uv/)

## Utilização

O arquivo [main.py](./main.py) apresenta um exemplo de como executar a simulação para o Netúnio, cuja configuração está em [cases/Np.py](./cases/Np.py). Basta executá-lo:

```shell
uv run main.py
```

Se preferir não usar o `uv`, crie seu ambiente Conda, venv etc com as dependências listadas em [pyproject.toml](./pyproject.toml), e execute o arquivo [main.py](./main.py).
