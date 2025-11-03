import pandas as pd
import sqlite3
from pathlib import Path
from typing import Optional

def import_to_database(csv_file: str, db_file: str) -> None:
    """
    Imports data for Student1, Student2, and Student3 from a CSV file into an SQLite database.

    """
    # read CSV data
    df = read_csv_file(csv_file)
    
    # only Student1, Student2, and Student3
    target_students = ["Student 1", "Student 2", "Student 3"]
    filtered_df = df[df["Name"].isin(target_students)].copy()
    
    # connect to SQLite database and import data
    try :
        with sqlite3.connect(db_file) as conn :
            # Create table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS StudentData (
                Name TEXT PRIMARY KEY,
                Quizzes INTEGER,
                Homework INTEGER,
                "Team Project" INTEGER,
                "Final Exam" INTEGER
            )
            """
            conn.execute(create_table_query)
            
            # Insert or replace data for the target students
            filtered_df.to_sql(
                "StudentData", 
                conn, 
                if_exists="replace", 
                index=False
            )
            
            # Verify the import
            result = conn.execute("SELECT COUNT(*) FROM StudentData").fetchone()

    except sqlite3.Error as e :
        raise sqlite3.Error(f"db operation failed : {e}")

def read_csv_file(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame.

    """
    try :
        df = pd.read_csv(file_path)

        return df
    
    except FileNotFoundError :
        raise FileNotFoundError(f"file not found: {file_path}")
    
    except Exception as e :
        raise ValueError(f"Error : {e}")

def combine_data(db_file: str, csv_file: str) -> pd.DataFrame:
    """
    Combines data from an SQLite database and a CSV file into a DataFrame.

    """
    combined_data = []
    
    # read data from SQLite database
    try :
        with sqlite3.connect(db_file) as conn:
            db_df = pd.read_sql_query("SELECT * FROM StudentData", conn)
            combined_data.append(db_df)
    except sqlite3.Error as e :
        raise sqlite3.Error(f"Error reading from database {db_file}: {e}")
    
    # read data from additional CSV file
    csv_df = read_csv_file(csv_file)
    combined_data.append(csv_df)
    
    # combine all data
    result_df = pd.concat(combined_data, ignore_index=True)
    
    return result_df

def calculate_final_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the final scores for all students based on the provided weights.

    """
    # validate required columns
    required_columns = ["Name", "Quizzes", "Homework", "Team Project", "Final Exam"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns :
        raise ValueError(f"missing required columns: {missing_columns}")
    
    # Create a copy to avoid modifying the original DataFrame
    result_df = df.copy()
    
    try :
        # Calculate final grade using weighted sum
        result_df["Final Grade"] = (
            result_df["Quizzes"] * 0.20 +
            result_df["Homework"] * 0.30 +
            result_df["Team Project"] * 0.20 +
            result_df["Final Exam"] * 0.30
        ).round(2)  # round to 2 decimal places
        
        return result_df
        
    except (TypeError, ValueError) as e :
        raise ValueError(f"Error calculating final scores: {e}")
    
def save_results(df: pd.DataFrame, output_file: str) -> None:
    """
    Saves the final results to a CSV file.

    """
    try  :
        df.to_csv(output_file, index=False)
    except Exception as e :
        raise Exception(f"Error saving results to {output_file}: {e}")


def main():
    """
    The main function, used to grab the data and pass it to
    your answer functions. You are not expected to edit this
    as part of the assignment. Feel free to edit it if needed
    while testing, but remember that the graders will be using
    this exact version when grading your answers.
    :return:
    """
    # File paths in the project directory
    first_csv_file = "Python-HW-WeightedSums-Data.csv"
    second_csv_file = "StudentA_B_Data.csv"
    db_file = "StudentData.db"

    try :
        import_to_database(first_csv_file, db_file)
        combined_data = combine_data(db_file, second_csv_file)
        final_results = calculate_final_scores(combined_data)
        save_results(final_results, "FinalStudentGrades.csv")

        # Display the final results
        print("Final Grades:\n")
        print(final_results.to_string(index=False))
    except FileNotFoundError as e :
        print(f"Error: {e.filename} not found.")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
