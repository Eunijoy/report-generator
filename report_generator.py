import pandas as pd
import os
import json
import logging
from data_fetcher import DataFetcher


#Setup logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReportGenerator:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)

    def load_config(self):
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            logging.info("Configuration loaded successfully.")
            return config
        except FileNotFoundError:
            logging.error(f"Config file {self.config_file} not found.")
            raise
    
    def generate_data(self):
        if self.config.get("use_api"):
            fetcher = DataFetcher()
            data = fetcher.fetch_data(self.config.get("rows", 10))
        else:
            #Generate Dummy data
            data = []
            for i in range(1, self.config.get("rows", 10) + 1):
                row = {col: f"{col}_{i}" for col in self.config.get("columns", [])}
                data.append(row)
        return data
    
    def save_csv(self, data):
        df = pd.DataFrame(data)
        filename = f"{self.config.get('report_name', 'report')}.csv"
        filepath = os.path.join(self.output_dir, filename)
        df.to_csv(filepath, index=False)
        logging.info(f"CSV report saved at {filepath}")
        return filepath
    
    def run(self):
        data = self.generate_data()
        self.save_csv(data)
