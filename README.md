git submodule update --init --recursive
vistualenv -p `which python3` venv
cd pslab-python
../venv/bin/python setup.py build
