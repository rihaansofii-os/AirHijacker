import itertools
import random

def generate_wordlist(details, special_chars, output_file="wordlist.txt", num_words=10000):
    wordlist = set()
    
    structured_list = []
    for detail in details:
        structured_list.append(detail)
        for other_detail in details:
            if detail != other_detail:
                structured_list.append(detail + other_detail)
                structured_list.append(detail + "_" + other_detail)
                structured_list.append(detail + "-" + other_detail)
                structured_list.append(detail.capitalize() + other_detail.capitalize())
                structured_list.append(detail.lower() + other_detail.lower())
                structured_list.append(detail.upper() + other_detail.upper())
    
    temp_list = []
    for word in structured_list:
        for num in range(10):
            temp_list.append(word + str(num))
            temp_list.append(word + str(num) * 2)
    structured_list.extend(temp_list)
    
    if special_chars:
        temp_list = []
        for word in structured_list:
            for char in special_chars:
                temp_list.append(word + char)
                temp_list.append(word + char * 2)
        structured_list.extend(temp_list)
    
    wordlist = list(set(structured_list))
    if len(wordlist) > num_words:
        wordlist = random.sample(wordlist, num_words)
    
    with open(output_file, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")
    
    print(f"Wordlist generated: {output_file} ({len(wordlist)} words)")

if __name__ == "__main__":
    first_name = input("Enter First Name (or press Enter to skip): ")
    surname = input("Enter Surname (or press Enter to skip): ")
    partners_name = input("Enter Partner's Name (or press Enter to skip): ")
    pet_name = input("Enter Pet Name (or press Enter to skip): ")
    company = input("Enter Company Name (or press Enter to skip): ")
    birth_year = input("Enter Birth Year (or press Enter to skip): ")
    favorite_color = input("Enter Favorite Color (or press Enter to skip): ")
    favorite_number = input("Enter Favorite Number (or press Enter to skip): ")
    
    add_special = input("Do you want to add special characters (@!# etc.) at the end? (y/n): ").lower()
    special_chars = "@!#$_&" if add_special == "y" else ""
    
    add_keywords = input("Do you want to add extra keywords about the user? (y/n): ").lower()
    other = input("Enter Additional Keywords (comma separated, or press Enter to skip): ") if add_keywords == "y" else ""
    
    other_keywords = other.split(",") if other else []
    details = [first_name, surname, partners_name, pet_name, company, birth_year, favorite_color, favorite_number] + other_keywords
    
    
    details = [d.strip() for d in details if d.strip()]
    
    file_name = input("Enter the filename to save the wordlist (default: wordlist.txt): ") or "wordlist.txt"
    
    generate_wordlist(details, special_chars, output_file=file_name)
