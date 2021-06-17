import glob
import yaml
from pypika import Query, Table, Field


def read_yml(yml_path):
    content = open(yml_path).read()
    data = yaml.safe_load(content)
    # json_str = json.dumps(data, indent=2)
    return data


def sql_builder(data):
    if "settings" not in data.keys():
        raise Exception("no settings in yml content")

    content = data["settings"]
    table_ = None
    columns_ = None

    for section in content:
        if "table" in section.keys():
            table_ = section["table"]
        elif "columns" in section.keys():
            columns_ = [column.replace(' ', '') for column in section["columns"].split(",")]

    if table_ is None:
        raise Exception("no table field in yml content")

    if columns_ is None:
        raise Exception("no columns field in yml content")

    q = Query.from_(table_)
    for column_ in columns_:
        q = q.select(column_)

    return q.get_sql()


def main(path):
    yml_content = read_yml(yml_path=path)
    sql_ = sql_builder(data=yml_content)
    print(f"File '{path}'\nSQL: {sql_}\n")


if __name__ == "__main__":
    path = "queries/example1.yml"
    for file in glob.glob("./queries/*.yml"):
        main(file)
