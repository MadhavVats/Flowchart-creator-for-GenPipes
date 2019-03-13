import pygraphviz as pgv
from func import *


class DnaSeqRaw:
    flag = 1

    """Pseudo functions created just for depiction"""
    @TraceCalls()  # Decorator for the function that needs to be traced.
    def picard_sam_to_fastq(self):
        pass

    @TraceCalls()
    def trimmomatic(self):
        pass

    @TraceCalls()
    def merge_trimmomatic_stats(self):
        pass

    @TraceCalls()
    def bwa_mem_picard_sort_sam(self):
        pass

    @TraceCalls()
    def picard_merge_sam_files(self):
        flag *= -1
        pass


k = DnaSeqRaw()
"""Functions called by the user. If we change the order or 
    which functions are called the same will reflect on the flowchart"""
k.picard_sam_to_fastq()
k.trimmomatic()
k.merge_trimmomatic_stats()
k.bwa_mem_picard_sort_sam()
k.picard_merge_sam_files()

#Flowchart creation
G = pgv.AGraph(strict=False, directed=True, landscape='true', ranksep='0.1')

total_steps = fun_called()
if len(total_steps) != 0:
    prev = total_steps[0]
    prev = "1. " + prev
    G.add_node(prev, shape='box', style='filled')
    """A bam is added before the execution of picard_sam_to_fastq"""
    if total_steps[0] == 'picard_sam_to_fastq':

        G.add_node('.bam', shape='diamond',
                   style='filled', fillcolor='white', fontcolor='black')
        G.add_edge('.bam', prev)
    """A fastq is added before the execution of trimmomatic"""
    if total_steps[0] == 'trimmomatic':

        G.add_node('.fastq', shape='diamond',
                   style='filled', fillcolor='white', fontcolor='black')
        G.add_edge('.fastq', prev)

for i in range(1, len(total_steps)):
    count = str(i+1) + ". "
    """Black fillcolor for Step on multiple readset/samples"""
    if total_steps[i] == 'picard_merge_sam_files':
        fillcolor = '#232426'
        fontcolor = 'white'
    else:
        """Grey fillcolor for Step per readset"""
        fillcolor = '#d1d3d6'
        fontcolor = 'black'

    G.add_node(count + total_steps[i], shape='box',
               style='filled', fillcolor=fillcolor, fontcolor=fontcolor)
    G.add_edge(prev, count + total_steps[i],
               len="5.0")
    if total_steps[i] == 'picard_sam_to_fastq':
        """A bam is added before the execution of picard_sam_to_fastq"""
        G.add_node('.bam', shape='diamond',
                   style='filled', fillcolor='white', fontcolor=black)
        G.add_edge('.bam', count + total_steps[i])
    if total_steps[i] == 'trimmomatic':
        """A fastq is added before the execution of trimmomatic"""
        G.add_node('.fastq', shape='diamond',
                   style='filled', fillcolor='white', fontcolor='black')
        G.add_edge('.fastq', count + total_steps[i])
    prev = count + total_steps[i]

G.layout(prog='dot')
G.draw('flowchart.png', format='png')
