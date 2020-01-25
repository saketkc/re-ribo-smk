#!/bin/bash
snakemake --snakefile Snakefile.kallisto.se\
    --config config_path=kallisto-configs/$1.py\
    --js $PWD/jobscript.sh\
    --printshellcmds\
    --cluster-config $PWD/cluster.yaml\
    --jobname "{rulename}.{jobid}.$1"\
    --keep-going\
    --stats $PWD/stats/$1.riboraptor.stats\
    --rerun-incomplete\
    -j 200\
    --cluster 'sbatch --partition={cluster.partition} --nodes=1 --ntasks={cluster.cores} --mem={cluster.mem} --time={cluster.time} -o {cluster.logout} -e {cluster.logerror}'
