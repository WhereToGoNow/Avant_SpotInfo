from __future__ import print_function

import googlemaps
import json

PATH_INPUT = 'input.txt'
PATH_OUTPUT = 'output.json'
API_KEY = 'AIzaSyAZ116sYwYampWa0lmH0Ypqn2vvAWtIXXA'

def read_input():
    print('Reading the names of the spots from %s... ' % PATH_INPUT, end='')

    with open(PATH_INPUT, 'rb') as p:
        lines = p.readlines()

    list_names = []

    for s in lines:
        if s and (s[0] == '-'):
            list_names.append(s[1:].strip())

    print('Success!')
    return list_names

def write_output(dict_info):
    print('Writing the data to %s... ' % PATH_OUTPUT, end='')

    with open(PATH_OUTPUT, 'wb') as p:
        json.dump(dict_info, fp=p, indent=4)

    print('Success!')

def retrieve(dc, key_1, key_2=None):
    value = dc.get(key_1)

    if (key_2 is not None) and value:
        return value.get(key_2)
    else:
        return value

def search_info(list_names):
    dict_info = {}
    client = googlemaps.Client(API_KEY)

    for name in list_names:
        print('Searching "%s"... ' % name, end='')

        # (1) simple info (including place id)
        response = client.places(name)

        if response['status'] != 'OK' or (not response['results']):
            print('Failed!')
            continue

        info_simple = response['results'][0]

        # (2) detail info (ex. opening hours)
        response_detail = client.place(info_simple['place_id'])

        if response_detail['status'] != 'OK':
            print('Failed!')
            continue

        info_detail = response_detail['result']

        # pack the values we need
        dict_info[name] = {
            'name': retrieve(info_simple, 'name'),
            'place_id': retrieve(info_simple, 'place_id'),
            'location': retrieve(info_simple, 'geometry', 'location'),
            'website': retrieve(info_detail, 'website'),
            'url': retrieve(info_detail, 'url'),
            'rating': retrieve(info_detail, 'rating'),
            'utc_offset': retrieve(info_detail, 'utc_offset'),
            'phone': retrieve(info_detail, 'international_phone_number'),
            'vicinity': retrieve(info_detail, 'vicinity'),
            'address': retrieve(info_detail, 'formatted_address'),
            'types': retrieve(info_detail, 'types'),
            'opening_hours': retrieve(info_detail, 'opening_hours', 'weekday_text'),
            'icon': retrieve(info_detail, 'icon')
        }

        print('Success!')

    return dict_info

def main():
    list_names = read_input()
    dict_info = search_info(list_names)
    write_output(dict_info)

if __name__ == '__main__':
    main()

