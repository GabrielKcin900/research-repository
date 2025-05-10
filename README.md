This repository brings together all the codes and jupyter notebooks used to carry out the research "From Code to Field: Evaluating the Robustness of Convolutional Neural Networks for Disease Diagnosis in Mango Leaves".

# Research pipeline summary

A brief summary of what was done in the research: We took a dataset of mango leaves ([MangoLeafDB](https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset/data)), applied the Data Augmentation technique through corruptions and severities and created MangoLeadDB-C, where C is for Corrupted. We implement and validate the CNNs that we will use (ResNet50, ResNet101, VGG-16, Xception and LCNN) (Note: I used Keras for implementation). After validating the models, we submit them to an F1-Score evaluation for each network on top of MangoLeafDB-C. And then we see some results. Then we calculated the mCE and Relative mCE metrics, which are metrics to evaluate network robustness, and we obtained results. We concluded that specific models can be better than generalist models. And in our case, the LCNN was the one that performed best and is a small specialist model that was proposed by the article [Nosin Ibna Mahbub](https://ieeexplore.ieee.org/document/10101648).

This project makes use of Dan Hendrycks [robustness](https://github.com/hendrycks/robustness) repository.

The research pipeline consists of:
* 1º - Data acquisition
* 2º - Manipulation
* 3º - Creation of MangoLeafDB-C
* 4º - Reorganizing database for F1-Score evaluation
* 5º - Model validation
* 6º - Evaluating models with MangoLeafDB-C (analysis based on F1-Score)
* 7º - Reorganizing database for CE, mCE and Relative mCE evaluation
* 8º - Evaluating models with MangoLeafDB-C (error, Corruption Error, mCE, Relative mCE)

Note 1: Remember to change the variables of where the data is on your computer.

Note 2: Remember that in one part of the pipeline it is necessary to use this website https://www.convertcsv.com/csv-viewer-editor.htm (It is in the F1-Score evaluation part) (When it is time to use it, it will be commented in the Jupyter notebooks)

Note 3: Remember to create a folder to store the results.

# Data acquisition

The dataset used was [MangoLeafDB](https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset/data).

# Manipulation

And then I downloaded it from Kaggle and extracted the zip file. Where I placed it in a folder on my computer. (Note: this folder is important in every pipeline, remember to adjust the variables that are in the code and in the Jupyter notebook when reproducing)

# Creating MangoLeafDB-C

In the structure of this repository we have: A folder called "external" where all the codes I used from my references are.

It is important to say that to carry out my research I used the repository "robustness (https://github.com/hendrycks/robustness)" by Dan Hendrycks. Where I used part of his repository, and made modifications to the file make_imagenet_c.py, where I adapted it to create MangoLeafDB-C, which would be MangoLeafDB but corrupted.

To create MangoLeafDB-C you must open the file external\ImageNet-C\create_c\make_imagenet_c.py. Before running, define the location where MangoLeafDB is and the location where MangoLeafDB-C will be. And run.

#Reorganizing database for F1-Score evaluation

Run the code scripts\reorganizarPasta.py. Remember to change the variables "origin" and "destination".

(When running this code, the output folder of make_imagenet_c.py will have its structure intact, however, the files will no longer be there)

And then run the code scripts\renomeandoPastasParaAvaliacao.py to rename the folders expected by the pipeline. (Remember to update the variable with the folder that is the output of scripts\reorganizarPasta.py)

# Validating the models

In the folder "notebooks\validacao-e-avaliacao-F1score-com-bancosCorrompidos" the validation

# Evaluating models with MangoLeafDB-C (analysis based on F1-Score)

In the folder "notebooks\validacao-e-avaliacao-F1score-com-bancosCorrompidos" in addition to the validation there is also the evaluation in relation to F1-Score. And also part of the results are in notebooks\ResultadosEmConjuntoDasRedes.ipynb.

# Reorganizing database for evaluation CE, mCE and Relative mCE

Run the code scripts\esseCodigoFoiCriadoParaCriarANovaEstruturaDePastasParaCalcularOMceEORelative.py and make the necessary changes in base_path and new_base_path. (This code will generate the MangoLeafDB-C structure needed for the notebook notebooks\calculando-metricas-mce-e-relative\Gerando-mCE-e-Relative_mCE.ipynb)

# Evaluating models with MangoLeafDB-C (error, Corruption Error, mCE, Relative mCE)

Run the notebook "notebooks\calculando-metricas-mce-e-relative\Gerando-mCE-e-Relative_mCE.ipynb"
