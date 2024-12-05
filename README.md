# DESAFIO BW

Esse projeto contém 3 pastas no qual cada uma contém um código em Python e testes referente a regras de neǵocio especificas:

- reconcile_accounts: tem como objetivo fazer um batimento de contas entre dois csv's
- last_lines: ler um arquivo utilizando stream a mostrando no final as linhas em ordem reversa, similiar ao comando tac do Linux
- computed_property: criar uma proprerty e ser utilizada por classes para calculo, cache e outras tratativas

## Configurando ambiente e instalação de dependências

1.  Configurando a versão do Python
    ```bash
    conda create -y -n myenv python=3.9
    conda activate myenv
    ```

2.  Instalando dependências
    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

## Rodando os scripts

### reconcile_accounts

1. Rode
```bash
python reconcile_accounts/main.py 
```

2. Saída esperada:
```
[['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket', 'FOUND'],
 ['2020-12-04', 'Jurídico', '60.00', 'LinkSquares', 'FOUND'],
 ['2020-12-05', 'Tecnologia', '50.00', 'AWS', 'MISSING']]
[['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket', 'FOUND'],
 ['2020-12-05', 'Tecnologia', '49.99', 'AWS', 'MISSING'],
 ['2020-12-04', 'Jurídico', '60.00', 'LinkSquares', 'FOUND']]
```

Essa saída é esperada com base no arquivos **.csv** que estão na pasta, caso queira testar com outro arquivo recomendo sobrescrever com o mesmo nome que estão dentro da pasta.

### last_lines

1. Nesse script é possível passar opcionalmente `--file` e `--buffer_size`, que respectivamente significa qual arquivo quer ser processado e o tamanho do buffer.
```bash
python last_lines/main.py --file=my_file.txt --buffer_size=1
```

2. Exemplo da saída para o arquivo **my_file.txt** esperada:
```
'And this is line 3\n'
'This is line 2\n'
'This is a file\n'
```

### computed_property

1. Foram criados 3 arquivos que fazem o uso da propriedade com base no que foi solicitado
```bash
python computed_property/vector.py 
python computed_property/circle.py
python computed_property/circle_docstring.py 
```

## Testes

### Executando os testes

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute os testes com `pytest`:
```bash
pytest
```

Exemplo de saída esperada:

```
=========== test session starts ===========
platform linux -- Python 3.9.20, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/user/projects/challenge_bw
collected 10 items                                                                                                                                                      

computed_property/computed_property_test.py ...          [ 30%]
last_lines/last_lines_test.py ....                       [ 70%]
reconcile_accounts/reconcile_accounts_test.py ...        [100%]

=========== 10 passed in 0.01s ============
```