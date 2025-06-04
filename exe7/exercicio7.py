"""
Exercicio 7:
Utilize os Datasets e DataLoaders do pytorch criados para o
DryBeamDataset em conjunto com elementos do keras para resolver a
tarefa de classificação correspondente. Resolva também o mesmo problema sem
o uso de Datasets e DataLoaders do pytorch, usando apenas o keras.
"""
import numpy as np 
import torch
from ucimlrepo import fetch_ucirepo
import pandas as pd
import os 
os.environ["KERAS_BACKEND"] = "torch" 
import keras

class DryBeamDataset(torch.utils.data.Dataset):
    """
    Dataloader feito em pytorch para o dataset Dry Beam 
    """
    def __init__(self):
        dry_bean = fetch_ucirepo(id=602)
        dffeatures = dry_bean.data.features
        dffeatures= (dffeatures-dffeatures.mean())/dffeatures.std()
        self.X = dffeatures.values.astype(np.float32)
        cat = pd.Categorical(dry_bean.data.targets['Class'])
        self.y = cat.codes.astype(int)
        self.nsamples = self.y.shape[0]
        self.nclasses = dry_bean.data.targets['Class'].unique().shape[0]
        print(f'DryBeamDataset has {self.nsamples} of {self.nclasses} classes.')

    def __len__(self):
        return self.nsamples

    def __getitem__(self, idx):
        sample = (torch.from_numpy(self.X[idx,:]),
        torch.tensor(self.y[idx]))
        return sample
    
def train_test_split_pytorch(batch_size:int = 16, p_train:float = 0.7, p_test:float = 0.3):
    """
    Divide as amostras do dataset em treino e teste, com base no dataloader feito em pytorch
    """
    dbeamdset = DryBeamDataset() 

    generator1 = torch.Generator().manual_seed(42)
    traindset,testdset = torch.utils.data.random_split(dbeamdset, [p_train, p_test],
    generator=generator1)

    traindataloader = torch.utils.data.DataLoader(traindset, batch_size=batch_size,
    shuffle=True)
    testdataloader = torch.utils.data.DataLoader(testdset, batch_size=batch_size,
    shuffle=True)
    return traindataloader, testdataloader

def keras_model(num_classes:int = 7, input_shape:tuple = (16,), verbose = True):
    """
    implementação do modelo utilizando a API KERAS
    """

    model = keras.Sequential(
        [
            keras.layers.InputLayer(shape = input_shape),
            keras.layers.Dense(512),
            keras.layers.ReLU(),
            keras.layers.Dense(128),
            keras.layers.ReLU(),
            keras.layers.Dense(num_classes),
            
        ])
    if verbose is True:
        model.summary()
    
    return model

def train_dataloader_pytorch(batch_size:int = 16, epochs:int = 5, lr:float = 1e-3):
    """
    Treina o modelo utilizando o dataloader feito em pytorch
    """
    
    train, test = train_test_split_pytorch(batch_size = batch_size)
    model = keras_model(verbose = False)
    
    model.compile(loss = keras.losses.SparseCategoricalCrossentropy(),
                  optimizer=keras.optimizers.Adam(learning_rate=lr),
                  metrics = [
                      keras.metrics.SparseCategoricalAccuracy(name="acc"),
                  ])
    
    hist = model.fit(train,
              validation_data = test, 
              batch_size = batch_size, 
              verbose = True, 
              epochs = epochs)
    
    return hist

def keras_train(batch_size:int = 16, epochs:int = 5, lr:float = 1e-3):
    """
    Treina o modelo apenas utilizando a API KERAS, sem depender do dataloader feito em pytorch
    """
   
    # Carregamento e pré-processamento do dataset
    dry_bean = fetch_ucirepo(id=602)
    dffeatures = dry_bean.data.features
    dffeatures= (dffeatures-dffeatures.mean())/dffeatures.std()
    X = dffeatures.values.astype(np.float32)
    cat = pd.Categorical(dry_bean.data.targets['Class'])
    y = cat.codes.astype(int)
    
    nsamples = y.shape[0]
    nclasses = dry_bean.data.targets['Class'].unique().shape[0]
    print(f'DryBeamDataset has {nsamples} of {nclasses} classes.')

    # Divide em treino (70%) e teste (30%) com shuffle
    np.random.seed(42)
    indices = np.random.permutation(nsamples)
    train_size = int(0.7 * nsamples)
    train_idx = indices[:train_size]
    test_idx = indices[train_size:]

    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    model = keras_model()

    model.compile(loss = keras.losses.SparseCategoricalCrossentropy(),
                  optimizer=keras.optimizers.Adam(learning_rate=lr),
                  metrics = [
                      keras.metrics.SparseCategoricalAccuracy(name="acc"),
                  ])
    
    hist = model.fit(X_train, y_train,
              validation_data =(X_test, y_test), 
              batch_size = batch_size, 
              verbose = True, 
              epochs = epochs)
    
    return hist
