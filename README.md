### python API Automation framework

Hybrid custom framework to test the REST APIs
### Tech stack
1.python
2.Requests -HTTP Requests
3.Pytest-Testing Framework
4.Reporting -Allure Report,Pytest HTML
5.Test Data -CSV,EXCEL,JSON
6.Parrallel excution  - x distribution

### how to install packages
generate new folder in virtual environment
go to terminal ,ckeck ''pip list
''pip install requests pytest pytest-html faker allure-pytest jsonschema

### to freeze your python packages
''pip freeze > requirements.txt
### to install the Freeze version
''pip install -r requirements.txt

## howto run test case parallel
pip install pytest-xdist
pytest -n auto tests/integration_test/parallel.py

###read excel file
pip install openpyxl

### to work with json schema
'' pip install jsonschema





