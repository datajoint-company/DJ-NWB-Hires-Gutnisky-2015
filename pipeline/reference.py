'''
Schema of subject information.
'''
import datajoint as dj

schema = dj.schema('ttngu207_reference',locals())


@schema
class BrainLocation(dj.Lookup):
    definition = """
    brain_location: varchar(24)
    ---
    brain_location_full_name: varchar(128)
    """
    contents = [
        ['Fastigial', 'Cerebellar fastigial nucleus'],
        ['ALM', 'Anteriror lateral motor cortex']
    ]

@schema
class Hemisphere(dj.Lookup):
    definition = """
    hemisphere: varchar(8)
    """
    contents = [['left'], ['right']]

@schema
class CoordinateReference(dj.Lookup):
    definition = """
    coordinate_ref: varchar(32)
    """
    contents = [['lambda'], ['bregma']]

@schema
class AnimalSource(dj.Lookup):
    definition = """
    animal_source: varchar(32)      # source of the animal, Jax, Charles River etc.
    """
    contents = [['JAX'], ['Homemade']]

@schema
class VirusSource(dj.Lookup):
    definition = """
    virus_source: varchar(64)
    """
    contents = [['UNC'], ['UPenn'], ['MIT'], ['Stanford'], ['Homemade']]

@schema
class ProbeSource(dj.Lookup):
    definition = """
    probe_source: varchar(64)
    ---
    number_of_channels: int
    """
    contents = [
        ['Cambridge NeuroTech', 64],
        ['NeuroNexus', 32]
    ]

@schema
class Virus(dj.Lookup):
    definition = """
    virus: varchar(64) # name of the virus
    ---
    -> VirusSource
    virus_lot_number="":  varchar(128)  # lot numnber of the virus
    virus_titer=null:       float     # x10^12GC/mL
    """
#    contents = [
#        {'virus_name': 'AAV2-hSyn-hChR2(H134R)-EYFP', 
#         'virus_source_name': 'UNC'
#        }
#    ]

@schema
class Experimenter(dj.Lookup):
    definition = """
    experimenter: varchar(64)
    """
    contents = [['Nuo Li']]

@schema
class Whisker(dj.Lookup):
    definition = """
    whisker_config: varchar(32)
    """
    contents = [['full'], ['C2']]
    
    
    
@schema
class BehavioralType(dj.Lookup):
    definition = """
    type: varchar(64)
    """    
    contents = [
            ['thetaAtBase'],
            ['ampitude'],
            ['phase'],
            ['setpoint'],
            ['thetafilt'],
            ['deltaKappa'],
            ['touch_onset'],
            ['touch_offset'],
            ['distance_to_pole'],
            ['pole_available'],
            ['beam_break_times']
            ]
    
@schema
class EphysType(dj.Lookup):
    definition = """
    type: varchar(64)
    """    
    contents = [
            ['voltage'],
            ['spike'],
            ]       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
