from report_generator import ReportGenerator

def main():
    try:
        generator = ReportGenerator("config.json")
        generator.run()
        print("CSV report generated successfully!")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()