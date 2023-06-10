import os
os.system('cmd /k "dvc init"')
os.system('cmd /k "dvc add .\models\best_model"')
os.system('cmd /k "dvc add .\reports\log_training.pkl"')
os.system('cmd /k "dvc add .\data\raw\Ethos_Dataset_Binary.csv"')
os.system('cmd /k "dvc add .\data\processed\processed_data.csv"')
