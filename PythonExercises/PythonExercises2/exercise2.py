# SER416 - Fall'25 B
# ndavispe
# exercise2.py

class Student : 
    # constants
    FRESHMAN_MAX = 24
    SOPHOMORE_MIN, SOPHOMORE_MAX = 25, 55
    JUNIOR_MIN, JUNIOR_MAX = 56, 86
    SENIOR_MIN = 87

    def __init__(self, first_name: str, last_name: str, initial_credits: int = 0) :
        self.first_name = first_name
        self.last_name = last_name
        self.credits = initial_credits

    # --- First Name --- #

    @property
    def first_name(self) -> str :
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) :
        self._first_name = value

    # --- Last Name --- #

    @property
    def last_name(self) -> str :
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) :
        self._last_name = value

    # --- Credits --- #

    @property
    def credits(self) -> int :
        return self._credits

    @credits.setter
    def credits(self, value: int) :
        self._credits = value
    
    def add_credits(self, additional_credits: int) :
        self.credits += additional_credits

    # --- Class Standing --- #

    def get_class_standing(self) -> str :
        if self.credits <= Student.FRESHMAN_MAX :
            return "Freshman"
        elif Student.SOPHOMORE_MIN <= self.credits <= Student.SOPHOMORE_MAX :
            return "Sophomore"
        elif Student.JUNIOR_MIN <= self.credits <= Student.JUNIOR_MAX :
            return "Junior"
        else :
            return "Senior"
    
    def __str__(self) -> str :
        return f"{self.first_name} {self.last_name}"

# --- Display  --- #

def display_class_standings(students: list[Student]) :
    # table headers
    headers = ["Student Name", "Credits", "Class Standing"]

    # table data
    table_data = [
        (str(student), student.credits, student.get_class_standing()) 
        for student in students
    ]

    # col width
    col_widths = [
        max(len(headers[i]), max(len(str(row[i])) for row in table_data))
        for i in range(len(headers))
    ]

    # format string
    format_str = " | ".join([f"{{:<{width}}}" for width in col_widths])

    # display table
    print("\n" + "=" * (sum(col_widths) + 3 * (len(headers) - 1)))
    print(format_str.format(*headers))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
    
    for row in table_data:
        print(format_str.format(*row))
    
    print("=" * (sum(col_widths) + 3 * (len(headers) - 1)) + "\n")

# --- Main Entry --- #

def main() :
    try : 
        # student instances
        students = [
            Student("Alice", "Johnson", 18),
            Student("Bob", "Smith", 32),
            Student("Carol", "Williams", 60),
            Student("David", "Brown", 90),
            Student("Eve", "Davis", 45)
        ]

        # add credits
        students[0].add_credits(5)  
        students[4].add_credits(15)

        display_class_standings(students)
    except Exception as e :
        print(f"Unexpected error: {e}")

if __name__ == "__main__" :
    main()