def feature_selection():
    import pandas as pd
    final_feature_set = []
    asthma_data = pd.read_csv('Differential_Analysis/differential_analysis_asthma.csv', usecols=['Gene_ID'])
    breast_cancer_data = pd.read_csv('Differential_Analysis/differential_analysis_breast_cancer.csv', usecols=['Gene_ID'])
    hepatocellular_carcinoma_data = pd.read_csv('Differential_Analysis/differential_analysis_hepatocellular_carcinoma.csv', usecols=['Gene_ID'])
    pulmonary_fibrosis_data = pd.read_csv('Differential_Analysis/differential_analysis_pulmonary_fibrosis.csv', usecols=['Gene_ID'])
    lung_cancer_data = pd.read_csv('Differential_Analysis/differential_analysis_lung_cancer.csv', usecols=['Gene_ID'])
    bladder_cancer_data = pd.read_csv('Differential_Analysis/differential_analysis_bladder_cancer.csv', usecols=['Gene_ID'])
    healthy_data = pd.read_csv('Datasets/healthy_data.csv', usecols=['ID'])

    asthma_probes = set(asthma_data['Gene_ID'])
    cancer_probes = set(breast_cancer_data['Gene_ID'])
    healthy_probes = set(healthy_data['ID'])
    hc_probes = set(hepatocellular_carcinoma_data['Gene_ID'])
    pf_probes = set(pulmonary_fibrosis_data['Gene_ID'])
    lc_probes = set(lung_cancer_data['Gene_ID'])
    bc_probes = set(bladder_cancer_data['Gene_ID'])

    feature_set_common = list(asthma_probes & cancer_probes & healthy_probes & hc_probes & pf_probes & lc_probes & bc_probes)[:10]

    return feature_set_common

print(feature_selection())