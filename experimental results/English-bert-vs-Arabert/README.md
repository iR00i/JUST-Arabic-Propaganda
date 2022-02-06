The following experiment investigates the performance of bert-base-cased on the original English version of the dataset and AraBERT-base (the best performing individual transformer) on the Arabic version of the dataset.
Both transformers were trained with the same partiitions of the dataset. The translation process was performed after the original dataset was partioned into train, validaition & test. For example, an English text sample **_x_** with index  **_i_** in the training dataset, had it's corresponding Arabic text **_y_** in the training dataset with index **_i_**.

Performance of the two:
|    Propaganda Techniques \ Models   | English-bert | AraBERT |
|:-----------------------------------:|:------------:|:-------:|
|         Appeal to authority         |      0.0     |   0.36  |
|       Appeal to fear-prejudice      |      0.0     |   0.40  |
|   Bandwagon, Reductio_ad_hitlerum   |      0.0     |   0.36  |
|       Black-and-white Fallacy       |      0.0     |   0.29  |
|      Casual Oversimplification      |      0.0     |   0.43  |
|                Doubt                |      0.0     |   0.61  |
|      Exaggeration, minimisation     |      0.0     |   0.50  |
|             Flag-waving             |      0.0     |   0.66  |
|           Loaded Language           |     0.50     |   0.78  |
|             Name Calling            |     0.24     |   0.70  |
|              Repetition             |     0.04     |   0.62  |
|                Slogan               |     0.11     |   0.58  |
|     Thought-terminating Cliches     |     0.00     |   0.31  |
| Whataboutism, strawman, red-herring |     0.00     |   0.36  |
|              Micro-avg              |     0.31     |   0.64  |
|              Macro-ave              |     0.06     |   0.50  |