# Disease Classification Model

## Practical Bioinformatics Course Project

### Authors:
- Aditya Jagadale
- Hemanth Dindigallu
- Het Shah
- Muthuraj Vairamuthu
- Noel Tiju
- Rishi Pendyala

### Course Details:
- **Course:** Practical Bioinformatics
- **Semester:** Winter 2024
- **Instructor:** Dr. Tavpritesh Sethi
- **Institute:** Indraprastha Institute of Information Technology, Delhi

---

## Problem Statement
**Disease Classification:** Collect patients’ gene information obtained through differential gene expression analysis and classify genes associated with a particular disease using a machine learning model.

## Dataset
**GEO Datasets from NCBI:** Downloaded .CEL files related to various diseases on the platform GPL570. The datasets can be accessed via the following link: [GEO Datasets](https://drive.google.com/drive/folders/1L_n9SBWKo4LMoqeZANiwzeD5poxCMnr6?usp=sharing).

## Normalization and Differential Gene Expression
We start by initializing essential R packages including `BiocManager`, `oligo`, `GEOquery`, and `limma`, among others, required to handle and analyze microarray data. Subsequently, disease-specific microarray datasets are imported and preprocessed using the `oligo::rma()` function, a method known for its efficiency in background correction, normalization, and summarization of probe intensities into expression values.

Following data preparation, the code undertakes differential gene expression analyses through linear modeling and empirical Bayes statistics provided by the `limma` package. Each disease dataset is arranged into cancerous and non-cancerous groups, and a linear model is used to note genes exhibiting significant expression variations between these groups. The outcomes of these analyses are stored in CSV files, documenting key gene expression details such as identifiers, log fold changes, average expression levels, statistical test values, and adjusted p-values.

## Machine Learning Model
An ML model is used to classify the genes associated with a particular disease. This begins by loading the dataset and preprocessing it. Subsequently, the data is standardized and split into training and testing sets.

The training set is then utilized to train a Convolutional Neural Network (CNN) model implemented using TensorFlow's Keras API. The model architecture comprises convolutional layers followed by max-pooling layers, dense layers, and a softmax output layer. Training progress is monitored through epochs, with validation set accuracy and loss also evaluated.

Post-training, the model's performance is assessed using the testing set, and accuracy metrics are printed. Additionally, a plot displaying the training and validation loss curves over epochs is generated for visualization.

Following CNN modeling, feature selection is performed using an XGBoost classifier to identify the most influential features for disease classification. The selected features are then utilized to train a new XGBoost classifier, and its accuracy on the testing set is evaluated.

Lastly, the code generates a pair plot visualization using seaborn, displaying pairwise scatter plots colored by target disease labels, providing insights into the distribution and relationships among features across different disease categories.
