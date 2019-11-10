name: test suite
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: [2.7, 3.6, 3.7, 3.8]
      fail-fast: false
    steps:
    - uses: actions/checkout@v1
    - name: set up Python
      uses: actions/setup-python@v1
      with:
        python-version: ${{matrix.python}}
    - name: run tests
      run: |
        pip install pytest
        pytest -v test.py
