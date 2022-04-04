"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):

    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums



def get_odd_indices(items):
    
    result = []

    for idx in items:
        if idx % 2 != 0:
            result.append(idx)
    return result


def print_as_numbered_list(items):

    i = 1

    for item in items:
        print(f'{i}. {item}')
        i+=1


def get_range(start, stop):

    nums = []


    for num in range(0,5):
        if num < 5:
            nums.append(num)

    return nums
print(get_range(0, 5))


def censor_vowels(word):
    
    char = []
    for letter in word:
        if letter in 'aeiou':
            char.append("*")
        else:
            char.append(letter)
    
    return ''.join(char)


print(censor_vowels("cute"))


def snake_to_camel(string):
    
    camel_case =[]

    for word in string.split("_"):
        camel_case.append(f"{word[0].upper()}{word[1:]}")
    return ''.join(camel_case)

print(snake_to_camel("hello_world"))


# // Given a string in snake case, return a string in upper camel case.
# //
# // Ex.:
# //   > snakeToCamel('hello_world');
# //   'HelloWorld'
# function snakeToCamel(string) {
#   const camelCase = [];

#   for (const word of string.split('_')) {
#     camelCase.push(`${word[0].toUpperCase()}${word.slice(1)}`);
#   }

#   return camelCase.join('');
# }








def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
