GENOMES_DIR = '/home/qcb-panasas/skchoudh/genomes'
OUT_DIR = '/staging/as/skchoudh/rna/Apr_04_2019_Kadosh_C_albicans_Biofilm_replicate2_riboraptor'

SRC_DIR = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/scripts'
#RAWDATA_DIR ='/home/cmb-06/as/skchoudh/dna/Apr_04_2019_Kadosh_C_albicans_Biofilm_replicate2/Kadosh_D_04022019'
RAWDATA_DIR = '/staging/as/skchoudh/rna/Apr_04_2019_Kadosh_C_albicans_Biofilm_replicate2/mapped_mRNA_only_collapsed/bams'
GENOME_BUILD = 'C_albicans_SC5314'
GENOME_FASTA = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.fasta'
RRNA_FASTA = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_other_features_no_introns.fasta'
STAR_INDEX = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/star_mrna_index_star27f'
RRNA_INDEX = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/star_rrna_index_star27f'
GTF = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + 'C_albicans_SC5314_version_A22-s07-m01-r27_features.gtf'

GENE_NAMES = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + GENOME_BUILD+'_gene_names_stripped.tsv'
GENE_LENGTHS = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r27_features.gtfTogenePred.genePred'
DESIGN_FILE = RAWDATA_DIR + '/' + 'design.txt'
HTSEQ_STRANDED = 'yes'
FEATURECOUNTS_S = '-s 1'
GENE_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.24.genes.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
FEATURECOUNTS_T = 'CDS'
HTSEQ_MODE = 'intersection-strict'
GTF = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + 'C_albicans_SC5314_version_A22-s07-m01-r27_features.gtf'
GENE_BED = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + '/C_albicans_SC5314_version_A22-s07-m01-r27_features.bed12'
UTR5_BED = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR5.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
UTR3_BED = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR3.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
CDS_BED = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + '/C_albicans_SC5314_version_A22-s07-m01-r27_features.gtfTogenePred.genePredToBed6'
SRC_DIR = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/scripts'
GENOME_FASTA = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.fasta'
CHROM_SIZES = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.sizes'
PYTHON2ENV = 'python2'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
