"""
Data Processor - Clean, analyze & visualize any dataset
Author: Maheen | AI & ML Engineer
"""

import csv
import json
import os
from collections import Counter


def load_csv(filepath):
    """Load CSV file and return data as list of dicts"""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def clean_data(data):
    """Remove empty rows and strip whitespace"""
    cleaned = []
    for row in data:
        clean_row = {k: v.strip() for k, v in row.items() if v and v.strip()}
        if clean_row:
            cleaned.append(clean_row)
    print(f"Cleaned: {len(data)} → {len(cleaned)} rows")
    return cleaned


def get_stats(data, column):
    """Get basic statistics for a column"""
    values = [row.get(column, "") for row in data if row.get(column)]
    
    try:
        nums = [float(v) for v in values]
        return {
            "count": len(nums),
            "min": min(nums),
            "max": max(nums),
            "average": round(sum(nums) / len(nums), 2),
            "total": round(sum(nums), 2)
        }
    except ValueError:
        freq = Counter(values)
        return {
            "count": len(values),
            "unique": len(freq),
            "top_5": freq.most_common(5)
        }


def convert_csv_to_json(csv_path, json_path="output.json"):
    """Convert CSV file to JSON"""
    data = load_csv(csv_path)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Converted to {json_path}")


if __name__ == "__main__":
    filepath = input("Enter CSV file path: ")
    data = load_csv(filepath)
    print(f"\nLoaded {len(data)} rows")
    print(f"Columns: {list(data[0].keys())}")
    
    data = clean_data(data)
    
    col = input("\nEnter column name for stats: ")
    stats = get_stats(data, col)
    for k, v in stats.items():
        print(f"  {k}: {v}")
