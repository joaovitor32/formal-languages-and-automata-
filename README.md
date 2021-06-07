<h4>Códigos desenvolvidos para a matéria Linguagens Formais e Automatos</h4>
<h3>Máquina de Estados Finitos e Simulador de Turing</h3>

##### Como Utilizar Este Repositório

Para utilizar este repositório é necessário que se tenha instalado python >= 3.6. Os comandos abaixo farão o necessário para a instalação das dependências e execução do programa.

Versão do Python utilizada: 3.6<br>
Versão Ubuntu utilizada: 18.04.1

```
git clone https://github.com/joaovitor32/Linguagens-Formais-e-Automatos
cd ./formal-languages-and-automata-
```

MEF:

```
cd ./MEF
python3.9 setup.py install --prefix="/home/{verify the path}"
python3.9 src/__init__.py
```

To execute tests:
```
python3.9 tests/test.py 
```

Turing_Simulator:

```
cd ./Turing_Simulator
python3.9 setup.py install --prefix="/home/{verify the path}"
python3.9 src/__init__.py
```

To execute tests:
```
python3.9 tests/test.py 
```