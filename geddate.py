"""
ssw555tmDSYZ2020spring-geddate by Yuning Sun
17:47 2020/2/10
Module documentation: Datetime operations used in gedparser.py
"""
import datetime


def check_date_valid(item, item_type, date_format='%d %b %Y'):
    if 'birt' not in item.__dict__.keys():
        pass
    else:
        if item_type == 'ind':
            try:
                datetime.datetime.strptime(item['birt'].value, date_format)
            except ValueError:
                raise ValueError(
                    f'ERROR: INDIVIDUAL: US42: {item["birt"].line}: {item["id"].value}: Date {item["birt"].value} is not valid date.')
            if 'deat' in item.__dict__.keys():
                try:
                    datetime.datetime.strptime(item['birt'].value, date_format)
                except:
                    raise ValueError(
                        f'ERROR: INDIVIDUAL: US42: {item["birt"].line}: {item["id"].value}: Date {item["deat"].value} is not valid date.')
        else:
            try:
                datetime.datetime.strptime(item['marr'].value, date_format)
            except ValueError:
                raise ValueError(
                    f'ERROR: INDIVIDUAL: US42: {item["marr"].line}: {item["id"].value}: Date {item["marr"].value} is not valid date.')
            if 'div' in item.__dict__.keys():
                try:
                    datetime.datetime.strptime(item['div'].value, date_format)
                except:
                    raise ValueError(
                        f'ERROR: INDIVIDUAL: US42: {item["div"].line}: {item["id"].value}: Date {item["div"].value} is not valid date.')


def get_age(birt_node, deat_node=None, date_format='%d %b %Y'):
    """
    Calculate age
    @param birt: birthday
    @param deat_node: death day
    @param date_format: date format
    @return: age
    """
    year_birt = datetime.datetime.strptime(birt_node.value, date_format).year
    if deat_node:
        year_end = datetime.datetime.strptime(deat_node.value, date_format).year
    else:
        year_end = datetime.date.today().year
    return year_end - year_birt


def date_transit(date_time):
    """
    transit date type
    @param date_time: old type
    @return: new type
    """
    return datetime.datetime.strptime(date_time, '%d %b %Y').strftime('%Y-%m-%d')
