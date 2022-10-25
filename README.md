# Mareasbilbao - Conoce las mareas de Bilbao
Con mareasbilbao, puedes saber la bajamar y la pleamar de cada día en Bilbao en python con una sola línea de código. Solo tienes que especificar la fecha del día que quieras obtener información.

## Uso
### Instalación
Para descargar mareasbilbao, haz un fork de este repo de github o simplemente usa Pypi vía pip.

```sh
$ pip install mareasbilbao
```

### Cómo usarlo
Mareasbilbao fue programado pensando en la facilidad de uso. Primero, importa mareasbilbao desde mareasbilbao.

```Python
from mareasbilbao import mareasbilbao
```
Después, simplemente elige la fecha del día que quieres obtener información sobre la marea. Debe ser año, mes y día todo seguido.

```Python
marea = mareasbilbao('20221030')
```

Para terminar, solo queda mostrar el resultado. Para ello, pon lo siguiente:

```Python
print(marea.horario())
```


License
----

MIT License

Copyright (c) 2022 Mikel Juarez and Ander Rodriguez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
