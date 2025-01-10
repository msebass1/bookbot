symbols = list("$@%/_1234567890-=+&^%@!}|{,.><,:;?# *][()\n'"+'"')
defaultbook = "./books/frankenstein.txt"
def words_count (str):

    return len(str.split())

def character_count (str):
    dict = {}
    parsed_str = str.lower()
    for i in parsed_str:
        if i not in symbols:
            if i in dict :
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

def sort_on (dict):
    return dict["value"]


def dict_to_sorted_list(dict):
    new_list = []
    for d in dict:
        new_list.append({"char": d , "value": dict[d]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def print_list(list):
    for element in list:
        print(f'The "{element["char"]}" character was found {element["value"]}')

def main():
    with open(defaultbook) as f:
        file_contents = f.read()
        number_of_words = words_count(file_contents)
        dict_of_characters = character_count(file_contents)

        print(f'--- Report of the book {defaultbook} ---')
        print(f'{number_of_words} words found in the document\n')
        print_list(dict_to_sorted_list(dict_of_characters))
        print('\n --- end of report ---')


main()

# things to add.
#
# - path to x book as parameter
# - --most-found and --aphabethic-order
