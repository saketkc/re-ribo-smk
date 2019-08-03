import os
import sys

srp_ids = sys.argv[1:]
download_dir = '/staging/as/skchoudh/pysradb_downloads/'
dest_dir = '/staging/as/skchoudh/re-ribo-datasets/hg38/'
hg38_template = open('/home/cmb-panasas2/skchoudh/github_projects/re-ribo-smk/snakemake/configs/hg38_template.py').readlines()
for srp_id in srp_ids:
    if os.path.isdir(download_dir + srp_id):
        try:
            os.symlink(download_dir + srp_id, dest_dir + srp_id)
        except:
            pass
    with open('/home/cmb-panasas2/skchoudh/github_projects/re-ribo-smk/snakemake/configs/hg38_{}.py'.format(srp_id), 'w') as fh:
        for index, line in enumerate(hg38_template):
            line = line.strip()
            if index in [0,1]:
                line= line.rstrip("'")+srp_id + "'"
            fh.write('{}\n'.format(line))
