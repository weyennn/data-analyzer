from src import DataAnalyzer

if __name__ == "__main__":
    analyzer = DataAnalyzer("data/sample.csv")
    analyzer.clean_data()
    analyzer.plot_income_distribution()
    print(analyzer.get_summary())





