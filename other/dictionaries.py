def app():
    person = {
        'keyname': 'namevalue',
        'keysurname': 'surnamevalue'
    }

    print('\n1. Dict')
    print('\n' + str(person))
    print('\n' + person['keyname'])
    print('\n' + person['keysurname'])

    print('\n2. Keys')
    for key in person.keys():
        print('\n' + key)

    print('\n3. Values')
    for val in person.values():
        print('\n' + val)

    print('\n4. Keys + Values')
    for key, val in person.items():
        print('\n' + key + ' ' + val)


if __name__ == '__main__':
    app()
