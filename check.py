#!/usr/bin/python

import unicodedata as ud

names = [
  'ใส่ชื่อในนี้เลย'
]

bad_chars_by_day = {
    'Sunday': ['ศ','ษ','ส','ห','ฬ','ฮ'],
    'Monday': [],
    'Tuesday': ['ก','ข','ค','ฆ','ง'],
    'Wednesday Day': ['จ','ฉ','ช','ซ','ฌ','ญ'],
    'Wednesday Night': ['บ','ป','ผ','ฝ','พ','ฟ','ภ','ม'],
    'Thursday': ['ด','ต','ถ','ท','ธ','น'],
    'Friday': ['ย','ร','ล','ว'],
    'Saturday': ['ฎ','ฏ','ฐ','ฑ','ฒ','ณ']
}


for name in names:

    print('*' * 50)
    print(name)
    print('*' * 50)

    for day, bad_chars in bad_chars_by_day.items():
        for char in bad_chars:
            if char in name:
                print('Not good for', day)
                break

    # check for Monday
    for c in name:
        if 'SARA ' in ud.name(c):
            print('Not good for Monday')
            break
