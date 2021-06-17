## SQL builder from YAML files

### How to start
1. Create venv
```
python3 -m venv new_env
```
2. Activate venv
```
source /new_env/bin/activate
```
3. Install requirements
```
pip install  -r requirements.txt
```
4. Run python script
```
python3 main.py
```

\
&nbsp;

Result:

```
File './queries/example1.yml'
SQL: SELECT "col1","col2","col3" FROM "table1"

File './queries/example2.yml'
SQL: SELECT "col1","col2","col3","col4","col5","col6" FROM "table2"
```