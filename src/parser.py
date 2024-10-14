import pandas as pd
import re
import random

def parse_logs(log_file):
    log_entries = []
    with open(log_file, 'r') as file:
        for line in file:
            # Example regex to extract timestamp
            match = re.match(r'(\S+\s+\S+)\s+\w+\s+(.*)', line)
            if match:
                timestamp = match.group(1)
                # Generate random feature values for demonstration
                feature1 = random.randint(10, 100)  # Random integer for feature1
                feature2 = random.randint(20, 200)  # Random integer for feature2
                log_entries.append((timestamp, feature1, feature2))
    return log_entries

def save_to_csv(log_entries, output_file):
    df = pd.DataFrame(log_entries, columns=['timestamp', 'feature1', 'feature2'])
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    log_file = 'logs/sfbios_log.txt'  # Path to your log file
    output_file = 'data/raw/sample_logs.csv'  # Output CSV file path
    log_entries = parse_logs(log_file)
    save_to_csv(log_entries, output_file)
    print(f"Parsed {len(log_entries)} entries and saved to {output_file}.")
