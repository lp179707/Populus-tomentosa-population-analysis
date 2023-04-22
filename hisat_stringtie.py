import os
import sys
print('conda_environment')
print('###hisat, samtools, GTF/GFF###')
args=sys.argv
hisatgenome=args[1]
samtoolgenome=args[2]
gff=args[3]
prefix=args[4]
fastq1=args[5]
if not os.path.exists('sort.bam_file'):
    os.system('mkdir sort.bam_file')
if len(args)>6:
    fastq2=args[6]
    os.system('/share_bio/software/hisat2-2.1.0/hisat2 -p 10 --dta -x {} -1 {} -2 {} | /share_bio/software/samtools/samtools-1.9/bin/samtools view -bhS -t {}  -@ 10 | /share_bio/software/samtools/samtools-1.9/bin/samtools sort -@ 10  -o sort.bam_file/{}.sort.bam'.format(hisatgenome,fastq1,fastq2,samtoolgenome,prefix))
else:
    os.system('/share_bio/software/hisat2-2.1.0/hisat2 -p 10 --dta -x {} -U {} | /share_bio/software/samtools/samtools-1.9/bin/samtools view -bhS -t {}  -@ 10 | /share_bio/software/samtools/samtools-1.9/bin/samtools sort -@ 10  -o sort.bam_file/{}.sort.bam'.format(hisatgenome, fastq1,samtoolgenome, prefix))
print(' sort_bam')
if not os.path.exists('gtf_file'):
    os.system('mkdir gtf_file')
print('stringtie_c')
os.system('/home/lip/genome.2022.01.11/resequencing/zhuanlu/stringtie-2.0.4.Linux_x86_64/stringtie -p 10 -e -G {} -o gtf_file/{}.gtf -l {} sort.bam_file/{}.sort.bam'.format(gff,prefix,prefix,prefix))
if not os.path.exists('list.file'):
    os.system('touch list.file')
os.system('echo -e "{}\tgtf_file/{}.gtf" >> list.file'.format(prefix,prefix))
#os.system('python prepDE.py3 -i list.file')
