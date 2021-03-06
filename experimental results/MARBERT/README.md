```json
{
    "MODEL_ID": "UBC-NLP/MARBERT",
    "ArabertPreprocessor": false,
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
    "PATIENCE": 3,
    "EPOCHS": 15,
    "LEARNING_RATE": 0.00005,
    "PATH": "/content/drive/MyDrive/Grad/Grad Proj 2/Arabic_Prop/Transformers/",
    "NUM_LABELS": 14
}
```
Model epoch performance at training-time:
![performance.png](performance.png)

```txt
model name:  UBC-NLP/MARBERT 
Arabert_Prep: False 
Accuracy:  0.6041666666666666

                                    precision    recall  f1-score   support

               Appeal_to_Authority     0.5000    0.5625    0.5294        16
          Appeal_to_fear-prejudice     0.3611    0.3824    0.3714        34
    Bandwagon,Reductio_ad_hitlerum     0.3750    0.4286    0.4000         7
           Black-and-White_Fallacy     0.5000    0.3077    0.3810        13
         Causal_Oversimplification     0.3243    0.5217    0.4000        23
                             Doubt     0.7353    0.4464    0.5556        56
         Exaggeration,Minimisation     0.5000    0.5370    0.5179        54
                       Flag-Waving     0.6333    0.5938    0.6129        32
                   Loaded_Language     0.7449    0.7510    0.7480       245
             Name_Calling,Labeling     0.6667    0.6290    0.6473       124
                        Repetition     0.6267    0.6104    0.6184        77
                           Slogans     0.6667    0.4706    0.5517        17
       Thought-terminating_Cliches     0.2500    0.3333    0.2857         9
Whataboutism,Straw_Men,Red_Herring     0.1000    0.0769    0.0870        13

                         micro avg     0.6197    0.6042    0.6118       720
                         macro avg     0.4989    0.4751    0.4790       720
                      weighted avg     0.6300    0.6042    0.6124       720
                       samples avg     0.6042    0.6042    0.6042       720
```

Confusion Matrices:
![confusion_matrices.png](confusion_matrices.png)


