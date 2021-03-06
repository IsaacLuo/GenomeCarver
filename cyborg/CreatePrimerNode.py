import psycopg2
import string
import json
import Nodes

def carver2(self):
    para = json.loads(self['Feature'])
    sequence = para["Sequence"]
    chromosome = para["Chromosome"]
    checkBoundary = para["CheckBoundary"]
    featureName = para["FeatureName"]
    if para["Species"] == "S.cerevisiae":
        species = "SC"
    elif para["Species"] == "A.thaliana":
        species = "AT"
    elif self['Species'] == "A.gossypii":
        species = "AG"
    else:
        species = self['Species']
    TargetPart = para["TargetPart"]


    std = self['Standard']
    stdDict = {'promotor5':'GGTC','promotor3':'CATC','orf5':'GATG','orf3':'GCTA','terminator5':'TAGC','terminator3':'GAGG'}
    cStr5 = stdDict[TargetPart+'5']
    cStr3 = stdDict[TargetPart+'3']
    srcStr5 = str(sequence)
    srcStr3 = str(srcStr5)[::-1]
    srcStr3 = srcStr3.translate(string.maketrans("AaTtCcGg","TtAaGgCc"))
    primerLength = int(self['PrimerLength'])
    if std == "GoldenGate":
        self['Primer5'] = ("GGTCTCg"+cStr5+srcStr5)[0:primerLength]
        self['Primer3'] = ("GGTCTCg"+cStr3+srcStr3)[0:primerLength]
    else:
        self['Primer5'] = "not support yet"
    
    self['Report'] = "http://genomecarver.cailab.org/carve/?species=%s&chromosomeName=%s&geneName=%s&checkBoundary=%s&standard=%s&carvePara=%s"%(species,chromosome,featureName,checkBoundary,self['Standard'],TargetPart)

carver2(self)



