from app import average_age
import pandas as pd

def test_average_age(tmp_path):
    # Создаём временный CSV-файл для теста
    data = pd.DataFrame({"name": ["A", "B"], "age": [20, 40]})
    file_path = tmp_path / "test.csv"
    data.to_csv(file_path, index=False)

    result = average_age(file_path)
    assert result == 30.00
