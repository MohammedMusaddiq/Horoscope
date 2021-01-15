# importing necessary libraries
from datetime import date
import requests
from stringcolor import *
from tabulate import tabulate

# getting date from the date library
date = date.today().strftime('%d/%m/%y')

# creating a list to loop through to check for conditions
zodiac_sign = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra',
               'Scorpio', 'Sagittarius',
               'capricorn', 'aquarius', 'pisces', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
               'scorpio', 'sagittarius', ]


# our main function that takes uesrs input and fetch the result from the api
def get_horoscope():
    print('')
    horoscope_sign = input(cs('please enter your zodiac sign: ', '#55ff00'))
    if any(horoscope_sign in zodiac_sign for i in zodiac_sign):
        url = f'http://horoscope-api.herokuapp.com/horoscope/today/{horoscope_sign}'
        res = requests.get(url)
        horoscope = res.json()['horoscope']
        response = f'{horoscope}'
        print('')
        print(f'Today\'s date is {cs(date, "Black", "#ffff00")}')
        print('--------------------------')
        print(cs('your Horoscope for today is:', 'yellow2'))
        print(cs(response, "DarkViolet2", "lightgrey6"))
    else:
        print('')
        print(cs('Please enter correct Zodiac sign:', "yellow", "#ff0000"))
        get_horoscope()


# the program execution starts from here
if __name__ == '__main__':
    print('')
    print(cs('Do you know your zodiac-sign (Enter yes or no): ', "#e6e600"))
    confirmation = input()
    if confirmation == 'yes':
        get_horoscope()
    else:
        if confirmation == 'no':
            print('')
            print(bold('Please refer below table to get your zodiac signs').underline().cs("#e60000", "gold"))
            print('')
            print(cs(tabulate([['December 22 – January 20', 'Capricorn'],
                               ['January 21 – February 18', 'Aquarius'],
                               ['February 19 - March 20', 'Pisces'],
                               ['March 21 - April 20', 'Aries'],
                               ['April 21 – May 21', 'Taurus'],
                               ['May 22 – June 21', 'Gemini'],
                               ['June 22 – July 22', 'Cancer'],
                               ['July 23 – August 23', 'Leo'],
                               ['August 24 – September 22', 'Virgo'],
                               ['September 23 – October 23', 'Libra'],
                               ['October 24 – November 22', 'Scorpio'],
                               ['November 23 – December 21', 'Sagittarius'], ],
                              headers=['Date', 'Zodiac sign']), "DarkViolet2", "lightgrey6"))
            print('')
            get_horoscope()
