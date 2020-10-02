# RAKE-Keyword

[![made-with-python](https://img.shields.io/badge/language-python-blue)](https://www.python.org/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/u-prashant/RAKE.svg?logo=lgtm&logoWidth=18&color=blue)](https://lgtm.com/projects/g/u-prashant/RAKE/context:python)
[![Build Status](https://img.shields.io/travis/u-prashant/RAKE?color=blue)](https://travis-ci.com/u-prashant/RAKE)
[![GitHub license](https://img.shields.io/github/license/u-prashant/RAKE?color=blue)](https://github.com/u-prashant/RAKE/blob/master/LICENSE)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
![PyPI](https://img.shields.io/pypi/v/rake-keyword?color=blue)


RAKE-Keyword is a Python library that can extract keywords from any document or a piece of text. It is based on RAKE algorithm. Rapid Automatic Keyword Extraction (RAKE) is a keyword extraction method that is extremely efficient and operates on individual documents. It tries to determine the key phrases in a text by calculating the co-occurrences of every word in a key phrase and also its frequency in the entire text. [Link to Research Paper!](https://doi.org/10.1002/9780470689646.ch1)

## Installation
```
pip install rake
```

## Quick Start
```python
from rake import Rake

text = "Black grapes are famous for their use in making alcohol."

rake = Rake()

rake.exec(text)
# Returns keywords with scores in reverse sorted order: [('black grapes', 4.0), ('making alcohol', 4.0), ('famous', 1.0)]
```

## Development Setup
```
1. git clone https://github.com/u-prashant/RAKE.git
2. cd RAKE
3. pip install -r requirements.txt
4. make test-all
```
## Releases

[v0.0.1](https://pypi.org/project/rake-keyword/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Copyright (c) 2020 Prashant Upadhyay
