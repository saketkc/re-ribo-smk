
######## Snakemake header ########
import sys; sys.path.append("/home/cmb-panasas2/skchoudh/software_frozen/anaconda27/envs/riboraptor/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00bams_srr_tx/SRR649753.bamq\x06X\x16\x00\x00\x00bams_srr/SRR649753.bamq\x07X\x1f\x00\x00\x00starlogs/SRR649753Log.final.outq\x08X\x1b\x00\x00\x00STARcounts/SRR649753.countsq\te}q\n(X\x05\x00\x00\x00txbamq\x0bh\x06X\x03\x00\x00\x00bamq\x0ch\x07X\x08\x00\x00\x00starlogsq\rh\x08X\x06\x00\x00\x00_namesq\x0e}q\x0f(h\x0bK\x00N\x86q\x10h\x0cK\x01N\x86q\x11h\rK\x02N\x86q\x12X\x06\x00\x00\x00countsq\x13K\x03N\x86q\x14uh\x13h\tubX\t\x00\x00\x00resourcesq\x15csnakemake.io\nResources\nq\x16)\x81q\x17(K\x01K\x10e}q\x18(X\x06\x00\x00\x00_nodesq\x19K\x01h\x0e}q\x1a(h\x19K\x00N\x86q\x1bX\x06\x00\x00\x00_coresq\x1cK\x01N\x86q\x1duh\x1cK\x10ubX\x06\x00\x00\x00configq\x1e}q\x1fX\x0b\x00\x00\x00config_pathq X\x19\x00\x00\x00configs/mm10_SRP017942.pyq!sX\x06\x00\x00\x00paramsq"csnakemake.io\nParams\nq#)\x81q$(X\x04\x00\x00\x00/tmpq%XT\x00\x00\x00/home/cmb-panasas2/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.intron.bedq&X?\x00\x00\x00/home/cmb-panasas2/skchoudh/genomes/mm10/fasta/mm10.chrom.sizesq\'e}q((X\x07\x00\x00\x00tmp_dirq)h%X\n\x00\x00\x00intron_bedq*h&h\x0e}q+(h)K\x00N\x86q,h*K\x01N\x86q-X\x0b\x00\x00\x00chrom_sizesq.K\x02N\x86q/uh.h\'ubX\x03\x00\x00\x00logq0csnakemake.io\nLog\nq1)\x81q2}q3h\x0e}q4sbX\x04\x00\x00\x00ruleq5X\x08\x00\x00\x00map_starq6X\x07\x00\x00\x00threadsq7K\x10X\x05\x00\x00\x00inputq8csnakemake.io\nInputFiles\nq9)\x81q:(X$\x00\x00\x00preprocessed/SRR649753_trimmed.fq.gzq;X7\x00\x00\x00/home/cmb-panasas2/skchoudh/genomes/mm10/star_annotatedq<e}q=(X\x02\x00\x00\x00R1q>h;X\x05\x00\x00\x00indexq?h<h\x0e}q@(h>K\x00N\x86qAh?K\x01N\x86qBuubX\t\x00\x00\x00wildcardsqCcsnakemake.io\nWildcards\nqD)\x81qEX\t\x00\x00\x00SRR649753qFa}qG(X\x06\x00\x00\x00sampleqHhFh\x0e}qIX\x06\x00\x00\x00sampleqJK\x00N\x86qKsubub.'); from snakemake.logging import logger; logger.printshellcmds = True
######## Original script #########
import os
import pandas as pd
import numpy as np
import tempfile
from riboraptor.helpers import path_leaf
from snakemake.shell import shell


def total_genome_size(chrom_sizes_file):
    """Return sum total of chromosome sizes"""
    df = pd.read_table(chrom_sizes_file, names=['chrom', 'sizes'])
    total = df['sizes'].sum()
    return total


def get_align_intro_params(intron_bed_file):
    df = pd.read_table(
        intron_bed_file,
        names=['chrom', 'start', 'end', 'name', 'score', 'strand'])
    lengths = df['end'] - df['start']

    ## Based on small genomes. See https://groups.google.com/forum/#!topic/rna-star/hQeHTBbkc0c
    alignintronNmin = max(4, lengths.min())
    alignintronNmax = lengths.max()
    return alignintronNmin, alignintronNmax


OUT_PREFIX = os.path.splitext(snakemake.output[0])[0]
TMP_DIR_SAMPLE = path_leaf(OUT_PREFIX)
STAR_LOGS_DIR = os.path.dirname(snakemake.output.starlogs)

ALIGN_INTRON_Nmin, ALIGN_INTRON_Nmax = get_align_intro_params(
    snakemake.params.intron_bed)
TOTAL_GENOME_SIZE = total_genome_size(snakemake.params.chrom_sizes)
SA_INDEX_Nbases = int(np.floor(min(14, np.log2(TOTAL_GENOME_SIZE) / 2.0 - 1)))

with tempfile.TemporaryDirectory(dir=snakemake.params.tmp_dir) as temp_dir:
    shell(r'''
            STAR --runThreadN {snakemake.threads}\
                --genomeDir {snakemake.input.index}\
                --outFilterMismatchNmax 2\
                --alignIntronMin {ALIGN_INTRON_Nmin}\
                --alignIntronMax {ALIGN_INTRON_Nmax}\
                --outFileNamePrefix {OUT_PREFIX}\
                --readFilesIn {snakemake.input.R1}\
                --readFilesCommand zcat\
                --quantMode TranscriptomeSAM GeneCounts\
                --outSAMtype BAM Unsorted\
                --outTmpDir {temp_dir}/{TMP_DIR_SAMPLE}_tmp\
                --outFilterType BySJout\
                --outFilterMatchNmin 16\
                --seedSearchStartLmax 15\
                --winAnchorMultimapNmax 200\
                && samtools sort -@ {snakemake.threads} {OUT_PREFIX}Aligned.out.bam -o {snakemake.output.bam} -T {temp_dir}/{TMP_DIR_SAMPLE}_sort\
                && mv {OUT_PREFIX}Aligned.toTranscriptome.out.bam {snakemake.output.txbam}\
                && samtools index {snakemake.output.bam}\
                && mv {OUT_PREFIX}ReadsPerGene.out.tab {snakemake.output.counts}\
                && mv {OUT_PREFIX}Log.final.out {OUT_PREFIX}Log.out {OUT_PREFIX}SJ.out.tab\
                {OUT_PREFIX}Log.progress.out {STAR_LOGS_DIR}
            ''')
