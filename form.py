# tap 1
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

filename = 'example.txt'  
print(f"Fayldakı söz sayı: {count_words(filename)}")
print()
# tap2
def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        return "Kopyalama tamamlandı."
    except FileNotFoundError:
        return "Mənbə fayl tapılmadı."

source_file = 'C:\\Users\\Ismay_cn01\\Documents\\example.txt'
destination_file = 'C:\\Users\\Ismay_cn01\\Documents\\copy_example.txt'
print(copy_file(source_file, destination_file))

# tap3
def count_occurrences(filename, search_word):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            return content.count(search_word.lower())
    except FileNotFoundError:
        return "Fayl tapılmadı."

filename = 'C:\\Users\\Ismay_cn01\\Documents\\example.txt'
search_word = input("Axtarmaq istədiyiniz sözü daxil edin: ")
print(f"Sözdəki təkrarlama sayı: {count_occurrences(filename, search_word)}")

# tap4

def remove_lines_containing(filename, word_to_remove, output_filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(output_filename, 'w') as file:
            for line in lines:
                if word_to_remove not in line:
                    file.write(line)
        return "Sətirlər silindi və yeni fayla yazıldı."
    except FileNotFoundError:
        return "Fayl tapılmadı."

filename = 'C:\\Users\\Ismay_cn01\\Documents\\example.txt'
word_to_remove = input("Silmək istədiyiniz sözü daxil edin: ")
output_file = 'C:\\Users\\Ismay_cn01\\Documents\\filtered_example.txt'
print(remove_lines_containing(filename, word_to_remove, output_file))

# tap5
def sum_numbers_from_file(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                total += sum(int(word) for word in line.split() if word.isdigit())
        return total
    except FileNotFoundError:
        return "Fayl tapılmadı."

filename = 'C:\\Users\\Ismay_cn01\\Documents\\example.txt'
print(f"Fayldakı rəqəmlərin cəmi: {sum_numbers_from_file(filename)}")

# tap6
def reverse_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        with open(output_filename, 'w') as file:
            for line in reversed(lines):
                file.write(line[::-1])
        return "Faylın məzmunu tərsinə çevrildi."
    except FileNotFoundError:
        return "Fayl tapılmadı."

input_file = 'C:\\Users\\Ismay_cn01\\Documents\\example.txt'
output_file = 'C:\\Users\\Ismay_cn01\\Documents\\reversed_example.txt'
print(reverse_file_content(input_file, output_file))




