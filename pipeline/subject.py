'''
Schema of subject information.
'''
import datajoint as dj
from pipeline import reference

schema = dj.schema('ttngu207_subject',locals())


@schema
class Species(dj.Lookup):
    definition = """
    species: varchar(24)
    """
    contents = [['Mus musculus']]

@schema
class Strain(dj.Lookup):
    definition = """
    strain: varchar(24)
    """
    contents = [['000664'],['N/A']]

@schema
class Allele(dj.Lookup):
    definition = """
    allele_name: varchar(128)
    """
    contents = [
        ['L7-cre'],
        ['rosa26-lsl-ChR2-YFP']
    ]

@schema
class Subject(dj.Manual):
    definition = """
    subject_id: varchar(64)  # name of the subject
    ---
    -> Species
    -> Strain
    -> reference.AnimalSource
    sex = 'U': enum('M', 'F', 'U')
    date_of_birth = NULL: date
    """

@schema
class SubjectAllele(dj.Manual):
    definition = """
    -> Subject
    -> Allele
    ---
    zygosity:  enum('Homozygous', 'Heterozygous', 'Negative', 'Unknown')
    """
    
    
    
    
    
    
    
    
    
    