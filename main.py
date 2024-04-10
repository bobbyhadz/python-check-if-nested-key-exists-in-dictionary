# Check if a nested key exists in a Dictionary in Python

my_dict = {
    'address': {
        'country': 'Finland',
        'city': 'Oulu'
    }
}

try:
    city = my_dict['address']['city']
    print(city)  # 👉️ Oulu
except KeyError:
    print('The specified key does NOT exist')

# -------------------------------------------------

try:
    result = my_dict['not']['found']['key']
except KeyError:
    # 👇️ this runs
    print('The specified key does NOT exist')