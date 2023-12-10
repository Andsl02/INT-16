import re
def title(input_string):
    def custom_capitalize(word):
        # Преобразовать первую букву слова в верхний регистр, если слово состоит из букв
        return word[0].upper() + word[1:] if word.isalpha() else word
    
    # Используем регулярное выражение для разделения строки на слова
    words = re.split(r'(\s+)', input_string)
    
    # Преобразовать каждое слово с использованием custom_capitalize
    capitalized_words = [custom_capitalize(word) for word in words]
    
    # Объединить слова обратно в строку
    result_string = ''.join(capitalized_words)
    return result_string

# Пример использования:
input_str = "тесТОвое задание     для  pt"
result = title(input_str)
print(input_str, '->',result)