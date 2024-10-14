from src.parser import parse_logs, save_to_csv # type: ignore

def main():
    # Parse logs and save to CSV
    log_file = 'logs/sfbios_log.txt'
    output_file = 'data/raw/sample_logs.csv'
    log_entries = parse_logs(log_file)
    save_to_csv(log_entries, output_file)
    
    print(f"Parsed {len(log_entries)} entries and saved to {output_file}.")

if __name__ == "__main__":
    main()
