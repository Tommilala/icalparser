from flask import Flask, request
from config import *
import requests
import icalendar

app = Flask(__name__)

def display(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

@app.route('/icalparser')
def icalparser():
    original = requests.get('{}'.format(url)).text
    cal = icalendar.Calendar.from_ical(original)

    new_cal = icalendar.Calendar()

    for event in cal.walk('vevent'):
        for words in blacklist:
            if all(word in event['SUMMARY'] for word in words):
                break
        else:
            new_cal.add_component(event)



    print('success')
    return (new_cal.to_ical(), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
