rmdir htmlcov /S /Q
del .coverage /Q
nosetests -w ./python/tests --with-xunit --with-coverage --cover-package ./python
coverage html -i
coverage report -m --skip-covered --omit="/*tests*/"
