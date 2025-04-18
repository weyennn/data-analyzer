import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def clean_data(self):
        """Hapus duplikat dan null"""
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)

    def get_summary(self):
        """Kembalikan ringkasan statistik"""
        return self.data.describe()

    def preview(self, n=5):
        return self.data.head(n)
    
    def plot_income_distribution(self):
        """Visualisasi distribusi pendapatan"""
        self.data['income'].hist(bins=10)
        plt.title("Distribusi Pendapatan")
        plt.xlabel("Income")
        plt.ylabel("Frekuensi")
        plt.show()







