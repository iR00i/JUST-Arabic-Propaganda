```json
{
    "MODEL_ID": "aubmindlab/bert-base-arabertv02",
    "HIDDEN_SIZE": 768,
    "DEVICE": "cuda",
    "MAX_LEN": 200,
    "TRAIN_BATCH_SIZE": 32,
    "VALID_BATCH_SIZE": 16,
    "TRAIN_VALID_TEST_SPLIT":
    [
        0.8,
        0.1,
        0.1
    ],
    "EPOCHS": 15,
    "LEARNING_RATE": 0.00008,
    "MODEL_PATH": "/content/drive/MyDrive/Grad/Grad Proj 2/Arabic_Prop/model.bin",
    "NUM_LABELS": 14,
    "ArabertPreprocessor": true
}
```
Model epoch performance at training-time:
![performance.png](performance.png)

```txt
Accuracy:  0.625

                                    precision    recall  f1-score   support

               Appeal_to_Authority     0.5714    0.5000    0.5333        16
          Appeal_to_fear-prejudice     0.4000    0.2353    0.2963        34
    Bandwagon,Reductio_ad_hitlerum     0.4286    0.4286    0.4286         7
           Black-and-White_Fallacy     0.1250    0.0769    0.0952        13
         Causal_Oversimplification     0.4091    0.3913    0.4000        23
                             Doubt     0.6250    0.5357    0.5769        56
         Exaggeration,Minimisation     0.5610    0.4259    0.4842        54
                       Flag-Waving     0.7143    0.6250    0.6667        32
                   Loaded_Language     0.7680    0.7837    0.7758       245
             Name_Calling,Labeling     0.6791    0.7339    0.7054       124
                        Repetition     0.6190    0.6753    0.6460        77
                           Slogans     0.4500    0.5294    0.4865        17
       Thought-terminating_Cliches     0.1250    0.1111    0.1176         9
Whataboutism,Straw_Men,Red_Herring     0.3750    0.2308    0.2857        13

                         micro avg     0.6503    0.6250    0.6374       720
                         macro avg     0.4893    0.4488    0.4642       720
                      weighted avg     0.6370    0.6250    0.6280       720
                       samples avg     0.6250    0.6250    0.6250       720
```

Confusion Matrices:
![confusion_matrices.png](confusion_matrices.png)


