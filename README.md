# Mareasbilbao - Get to know the tides of Bilbao
With mareasbilbao, you can know the low tide and high tide of each day in Bilbao in python with a single line of code. You only have to specify the date of the day you want to get information.

## Usage
### Getting it
To download mareasbilbao, do a fork of this github repo or just use Pypi via pip.

```sh
$ pip install mareasbilbao
```

### Using it
Mareasbilbao was programmed with ease-of-use in mind.

First, import mareasbilbao from mareasbilbao.

```Python
from mareasbilbao import mareasbilbao
```

Then, simply choose the date of the day you want to get tide information. It should be year, month and day all in a row. It can be in string or integer.

```Python
marea = mareasbilbao('20221030')
or
marea = mareasbilbao(20221030)
```

Finally, the only thing left to do is to show the result. To do this, put the following:

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
