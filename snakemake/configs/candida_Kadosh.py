

RAWDATA_DIR ='/home/qcb-panasas/skchoudh/rna/July_07_2018_Kadosh_Flu_Film_Planktonic_merged/bams'
OUT_DIR ='/home/qcb-panasas/skchoudh/rna/July_07_2018_Kadosh_Flu_Film_Planktonic_merged_riboraptor'
GENOME_FASTA = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.fasta'
CHROM_SIZES = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.sizes'
STAR_INDEX = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/star_mrna_index'
GTF = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + 'C_albicans_SC5314_version_A22-s07-m01-r27_features.gtf'
GENE_BED = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r27_features.bed12'
STAR_CODON_BED = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r50_features.encode.gffutils.start_codon.bed'
STOP_CODON_BED = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r50_features.encode.gffutils.stop_codon.bed'
CDS_BED = '/home/qcb-panasas/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + '/C_albicans_SC5314_version_A22-s07-m01-r27_features.gtfTogenePred.genePredToBed6'
UTR5_BED = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR5.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
UTR3_BED = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR3.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
INTRON_BED = '/home/qcb-panasas/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR5.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
