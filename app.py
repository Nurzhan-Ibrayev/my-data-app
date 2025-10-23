import pandas as pd

def average_age(file_path: str) -> float:
    """Считает средний возраст из CSV файла"""
    df = pd.read_csv(file_path)
    return round(df["age"].mean(), 2)

if __name__ == "__main__":
    avg = average_age("data.csv")
    print(f"Average age: {avg}")
