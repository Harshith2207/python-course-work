from my_programs import *

def main():
    while True:
        print("\n" + "=".rjust(53, "="))
        print("\n\t~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~")
        print("\n" + "=".rjust(53, "="))
        print("\n<--- Functions You Didn’t Know You Needed --->")
        print("     -------------------------------------")
        print("\nrev_spell   → Reverse a String")
        print("freq_potion   → Character Frequency Counter")
        print("cleanse_list  → Remove Duplicates from List")
        print("shared_runes  → Find Common Elements")
        print("dict_fuse     → Merge Dictionaries")
        print("calc_charm    → Simple Calculator")
        print("sort_glyphs   → Sort Tuples by Second Element")
        print("unfold_scroll → Flatten Nested List")
        print("lost_number   → Find Missing Number")
        print("mirror_words  → Check if Strings are Anagrams")
        print("exit_spell    → Exit the Spellbook")

        choice = input("\nType your magic key: ").strip().lower()

        if choice == 'rev_spell':
            reverse_string()
        elif choice == 'freq_potion':
            char_frequency()
        elif choice == 'cleanse_list':
            remove_duplicates()
        elif choice == 'shared_runes':
            common_elements()
        elif choice == 'dict_fuse':
            merge_dictionaries()
        elif choice == 'calc_charm':
            simple_calculator()
        elif choice == 'sort_glyphs':
            sort_tuples_by_second()
        elif choice == 'unfold_scroll':
            flatten_nested_list()
        elif choice == 'lost_number':
            missing_number()
        elif choice == 'mirror_words':
            check_anagram()
        elif choice == 'exit_spell':
            print("The spellbook closes... Farewell, wizard!")
            break
        else:
            print("Unknown spell. Try again!")

main()
