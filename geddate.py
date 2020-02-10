"""
SSW555DSYZ-geddate by Yuning Sun
17:47 2020/2/10
Module documentation: Datetime operations used in gedparser.py
"""
import datetime


def get_age(birt, deat=None, date_format='%Y-%m-%d'):
    """
    Calculate age
    @param birt: birthday
    @param deat: death day
    @param date_format: date format
    @return: age
    """
    year_birt = datetime.datetime.strptime(birt, date_format).year
    if deat:
        year_end = datetime.datetime.strptime(deat, date_format).year
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
