import tomllib

with open('example.toml', 'rb') as file:
    tom_file = tomllib.load(file)
    for row in tom_file:
        print(row)