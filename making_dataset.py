import pandas as pd
import csv
from feature_selection import feature_selection
from pathlib import Path

def file_names(directory):
    folder = Path(directory)
    file_names = []
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith('.CEL'):
            file_names.append(file.name)
    return file_names

asthma_files = file_names('Asthma')
breast_cancer_files = file_names('Breast_Cancer')
hc_cancer_files = file_names('Hepatocellular_Carcinoma')
healthy_files = file_names('Healthy')
pulmonary_fibrosis_files = file_names('Pulmonary_Fibrosis')
bladder_cancer_files = file_names('Bladder_Cancer')
lung_cancer_files = file_names('Lung_Cancer')

print('Reading data')
columns = ['ID'];columns.extend(asthma_files)
asthma_data = pd.read_csv('Datasets/asthma_data.csv', usecols=columns)

columns = ['ID'];columns.extend(breast_cancer_files)
breast_cancer_data = pd.read_csv('Datasets/breast_cancer_data.csv', usecols=columns)

columns = ['ID'];columns.extend(bladder_cancer_files)
bladder_cancer_data = pd.read_csv('Datasets/bladder_data.csv', usecols=columns)

columns = ['ID'];columns.extend(hc_cancer_files)
hc_cancer_data = pd.read_csv('Datasets/hepatocellular_data.csv', usecols=columns)

columns = ['ID'];columns.extend(healthy_files)
healthy_data = pd.read_csv('Datasets/healthy_data.csv', usecols=columns)

columns = ['ID'];columns.extend(pulmonary_fibrosis_files)
pulmonary_fibrosis_data = pd.read_csv('Datasets/pulmonary_fibrosis_data.csv', usecols=columns)

columns = ['ID'];columns.extend(lung_cancer_files)
lung_cancer_data = pd.read_csv('Datasets/lung_cancer_data.csv', usecols=columns)



with open('final_dataset.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    gene_signatures = ['Sample_ID', 'Result', 'Status']
    gene_signatures.extend(feature_selection())
    writer.writerow(gene_signatures)
    gene_signatures.remove('Sample_ID');gene_signatures.remove('Result');gene_signatures.remove('Status')

    print('Running Asthma Samples')
    count = 0
    for sample in asthma_files:
        sample_val = f"asthma_{count}"
        count+=1
        sample_row = [sample_val, 'Asthma',1]
        for gene in gene_signatures:
            row_index = asthma_data.index[asthma_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = asthma_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)

    print('Running healthy')
    count=0
    for sample in healthy_files:
        sample_val = f"healthy_{count}"
        count+=1
        sample_row = [sample_val, 'Healthy',0]
        for gene in gene_signatures:
            row_index = healthy_data.index[healthy_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = healthy_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)
    print('Running Breast Cancer files')
    count = 0
    for sample in breast_cancer_files:
        sample_val = f"breast_cancer_{count}"
        count+=1
        sample_row = [sample_val, 'Breast_Cancer',2]
        for gene in gene_signatures:
            row_index =breast_cancer_data.index[breast_cancer_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = breast_cancer_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)

    print('Running Pulmonary Fibrosis')
    count=0
    for sample in pulmonary_fibrosis_files:
        sample_val = f"pulmonary_fibrosis_{count}"
        count+=1
        sample_row = [sample_val, 'Pulmonary Fibrosis',3]
        for gene in gene_signatures:
            row_index =pulmonary_fibrosis_data.index[pulmonary_fibrosis_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = pulmonary_fibrosis_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)
    
    print('Running Hepatocellular carcinoma')
    count=0
    for sample in hc_cancer_files:
        sample_val = f"hepatocellularcarcinoma_{count}"
        count+=1
        sample_row = [sample_val, 'Hepatocellular Carcinoma',4]
        for gene in gene_signatures:
            row_index =hc_cancer_data.index[hc_cancer_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = hc_cancer_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)

    print('Running Lung Cancer')
    count=0
    for sample in lung_cancer_files:
        sample_val = f"lung_cancer_{count}"
        count+=1
        sample_row = [sample_val, 'Lung Cancer',5]
        for gene in gene_signatures:
            row_index =lung_cancer_data.index[lung_cancer_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = lung_cancer_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)

    print('Running Bladder Cancer')
    count=0
    for sample in bladder_cancer_files:
        sample_val = f"bladder_cancer_{count}"
        count+=1
        sample_row = [sample_val, 'Bladder Cancer',6]
        for gene in gene_signatures:
            row_index =bladder_cancer_data.index[bladder_cancer_data['ID'] == gene].tolist()
            if row_index:
                row_index = row_index[0]
                cell = bladder_cancer_data.iloc[row_index][sample]
                sample_row.append(cell)
            else:
                sample_row.append('NA')
        writer.writerow(sample_row)