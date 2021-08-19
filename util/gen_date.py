"""
    Function to convert a date in string format 'Month, Day Year' to string format 'MM-DD-YYYY' 
    ('June 15, 2021' --> '06-15-2021')

"""
import re


def get_numerical_date(text_date: str):
    text_date = re.sub(',', '', text_date)
    split = text_date.strip().split(' ')

    # string to return
    num_date = ''

    # first, append numerical month from string
    if split[0] == 'January':
        num_date += '01'
    if split[0] == 'February':
        num_date += '02'
    if split[0] == 'March':
        num_date += '03'
    if split[0] == 'April':
        num_date += '04'
    if split[0] == 'May':
        num_date += '05'
    if split[0] == 'June':
        num_date += '06'
    if split[0] == 'July':
        num_date += '07'
    if split[0] == 'August':
        num_date += '08'
    if split[0] == 'September':
        num_date += '09'
    if split[0] == 'October':
        num_date += '10'
    if split[0] == 'November':
        num_date += '11'
    if split[0] == 'December':
        num_date += '12'

    # add dashes and numerical day and year
    num_date += '-'
    num_date += split[1]
    num_date += '-'
    num_date += split[2]

    return num_date
