# Template repository for PH3010 Advanced Python

This is a template repository demonstrating how to package a python project. The directory is structured as follows:
```
template_project_PH3010_advanced_python/
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── .github/
│   └── workflows/
│              └── python_test.yml
├── docs/
│   └── ../
│   └── workflows/
├── src/
│   └── example_package/
│       ├── __init__.py
│       ├── command_line_interface.py
│       └── example.py
└── tests/
        └── test_example.py
```

Let's look at each element individually

* `.gitignore` contains files that should be ignored by git
* `LICENSE` the project license telling users who install your package the terms under which they can use your package
* `README.md` A [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) document telling users about the project
* `pyproject.toml` tells build tools (like pip and build) what is required to build your project.
* `requirements.txt` contains the requirements for the project, you can install these with `pip install -r requirements.txt`
* `docs/` contains the documentation - we won't discuss this further here.
* `.github/workflows/python_test.yml` contains a [YAML](https://yaml.org/) file which determined how github Action are run
* `src/` contains the python package itself
* `tests/` contains the tests of the python package
