# SER416 - Fall'25 B
# ndavispe
# exercise1.py

def read_strings(filename) :
    # read strings from a file and return as list
    with open(filename) as f :
        return [line.strip() for line in f]


def sort_strings(strings) :
    # sort strings alphabetically (case-insensitive
    return sorted(strings, key=str.lower)


def write_strings(filename, strings) :
    # write strings to a file, each on a new line
    with open(filename, 'w') as f :
        f.write('\n'.join(strings))


def main() :
    # main function to execute the string sorting process
    input_file = 'strings.txt'
    output_file = 'sorted_strings.txt'
    
    # read strings from input file
    strings = read_strings(input_file)
    
    # sort the strings
    sorted_strings = sort_strings(strings)
    
    # write sorted strings to output file
    write_strings(output_file, sorted_strings)
    
    print(f"sorted strings")

if __name__ == "__main__" :
    main()