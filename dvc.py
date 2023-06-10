import os


def main():
    os.system('cmd /k "dvc init"')
    os.system('cmd /k "dvc add ./models/best_model"')
    os.system('cmd /k "dvc add ./reports/log_training.pkl"')
    os.system('cmd /k "dvc add ./data/raw/Ethos_Dataset_Binary.csv"')
    os.system('cmd /k "dvc add ./data/processed/processed_data.csv"')
    os.system('cmd /k "dvc push"')
    return 0

if __name__ == '__main__':
    main
else:
    pass
