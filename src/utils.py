import os
import csv
import json

from pathlib import Path

_BASE_DATA_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent / 'data'


def convert_csv_to_json_and_get_license_organ(csv_file, json_file=None, csv_file_dir=_BASE_DATA_DIR, encoding='UTF-8') -> list:
    ret = list()
    csv_list = list()

    if not json_file:
        json_file = csv_file.split('.')[0] + '.json'

    with open(csv_file_dir / csv_file, 'r', encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for csv_row in csv_reader:
            csv_list.append(csv_row)
            ret.append(csv_row.get('licenseOrgan'))

    with open(csv_file_dir / json_file, 'w', encoding=encoding) as json_file:
        json.dump(csv_list, json_file, ensure_ascii=False)

    return ret

