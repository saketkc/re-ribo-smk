#!/bin/bash
#conda activate ribopod
snakemake --snakefile Snakefile.ribotricer.fastq\
    --config config_path=configs/$1.py\
    --js $PWD/jobscript.sh\
    --printshellcmds\
    --cluster-config $PWD/cluster.yaml\
    --jobname "{rulename}.{jobid}.$1"\
    --keep-going\
    --stats $PWD/stats/$1.riboraptor.stats\
    --rerun-incomplete\
    -j 200\
    --cluster 'sbatch --partition={cluster.partition} --ntasks={cluster.cores} --mem={cluster.mem} --time={cluster.time} -o {cluster.logout} -e {cluster.logerror}'
