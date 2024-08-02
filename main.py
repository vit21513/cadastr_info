import json
import requests
import urllib3

urllib3.disable_warnings()

field = {"Кадастровый номер": "cn", " Статус": "statecd ", "Адрес": "address", "Форма собственности": "fp",
         "Тип площади": "area_type",
         "Единицы измерения площади": "area_unit", "Декларированная площадь": "area_value",
         "Кадастровая стоимость": "cad_cost",
         "Категория земель": "category_type", " Дата постановки на учет": "date_create",
         "Кадастровый квартал": "kvartal_cn",
         "Разрешенное использование по документу": "util_by_doc", "Разрешенное использование": "util_code",
         "Зарегистрированы права": "rights_reg", "Свободен от прав третьих лиц": "rifr"}






obj_total = dict


def get_info(typ_obj="1", cad_num="23:35:0523012:133"):
    def Normalize_num(cad_number):
        if cad_number[6] == "0":
            cad_number = cad_number[0:6] + cad_number[7:]
        if cad_number[3] == "0":
            cad_number = cad_number[0:3] + cad_number[4:]
        if cad_number[0] == "0":
            cad_number = cad_number[1:]
        return cad_number

    url = f'https://pkk.rosreestr.ru/api/features/{typ_obj}/{Normalize_num(cad_num)}'
    response = requests.get(url, verify=False)
    data = response.json()
    return data


def search_dict(res_response: dict, key: str):
    res = None
    for k, v in res_response.items():
        if k == key:
            res = v
            if res is not None:
                return res
        if isinstance(v, dict):
            res = search_dict(v, key)
            if res is not None:
                return res


temp = get_info("5","23:35:0524014:227")
print(temp)
total = field.copy()
for k, v in field.items():
    total[k] = search_dict(temp, v)
print(total)
