# SER416 - Fall'25 B
# ndavispe
# exercise2.py

def get_name_input() :
    # get name components from user input

    print("Please enter the following ...")
    
    first_name = input("First Name : ").strip()
    middle_name = input("Middle Name (press Enter if none) : ").strip()
    last_name = input("Last Name : ").strip()
    
    # handle empty inputs
    if not first_name :
        first_name = "N/A"
    if not last_name :
        last_name = "N/A"
    
    return first_name, middle_name, last_name


def format_initials(first_name, middle_name, last_name) :
    # format the name as initials.
    
    initials = []
    
    # first name initial
    if first_name and first_name != "N/A" :
        initials.append(first_name[0].upper())
    
    # middle name initial (only if provided AND not empty)
    if middle_name and middle_name != "N/A" :
        initials.append(middle_name[0].upper())
    
    # last name initial
    if last_name and last_name != "N/A" :
        initials.append(last_name[0].upper())
    
    return '.'.join(initials) + '.' if initials else "No initials available"


def format_last_name_first(first_name, middle_name, last_name) :
    # format as "Last Name, First Name, Middle Initial".

    components = []
    
    # last name first
    if last_name and last_name != "N/A" :
        components.append(last_name)
    
    # first name
    if first_name and first_name != "N/A" :
        components.append(first_name)
    
    # middle initial only if provided
    if middle_name and middle_name != "N/A" :
        components.append(f"{middle_name[0].upper()}.")
    
    return ', '.join(components) if components else "No name provided"


def format_full_name(first_name, middle_name, last_name) :
    # format as "First Name Middle Name Last Name".

    components = []
    
    # add non-empty name components
    if first_name and first_name != "N/A" :
        components.append(first_name)
    
    if middle_name and middle_name != "N/A" :
        components.append(middle_name)
    
    if last_name and last_name != "N/A" :
        components.append(last_name)
    
    return ' '.join(components) if components else "No name provided"


def validate_name_components(first_name, middle_name, last_name) :
    # validate that at least first or last name is provided
    
    valid_first = first_name and first_name != "N/A"
    valid_last = last_name and last_name != "N/A"
    
    return valid_first or valid_last


def display_formatted_names(first_name, middle_name, last_name) :
    # display all three formatted versions of the name
    print("NAME FORMATTING RESULTS")
    
    # display 1: Initials
    initials = format_initials(first_name, middle_name, last_name)
    print(f"1. Initials: {initials}")
    
    # display 2: Last Name, First Name, Middle Initial
    last_first_format = format_last_name_first(first_name, middle_name, last_name)
    print(f"2. Last Name First: {last_first_format}")
    
    # display 3: Full Name
    full_name = format_full_name(first_name, middle_name, last_name)
    print(f"3. Full Name: {full_name}")


def main() :
    try :
        print("Exercise2.py")
        print("------------") 
        
        # get user input
        first_name, middle_name, last_name = get_name_input()
        
        # validate input
        if not validate_name_components(first_name, middle_name, last_name) :
            print("\nError: Please provide first name or last name")
            return
        
        # display formatted results
        display_formatted_names(first_name, middle_name, last_name)
        
    except KeyboardInterrupt :
        print("\n\nprogram interrupted , exiting...")

    except Exception as e :
        print(f"\nerror : {e}")

if __name__ == "__main__" :
    main()