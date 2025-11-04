def num_words(text):
    word_array = text.split()
    word_count = len(word_array)
    return word_count

def count_char(text):
    char_dict = {}
    for word in text:
        for c in word:
            c = c.lower()
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    
    return char_dict
def sort_on(items):
    return items["num"]
def sorted_dict(dict):
    list_of_dict = []
    for key,val in dict.items():
        list_of_dict.append({"char": key, "num": val})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
   


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
#        print(file_contents)
        return file_contents

