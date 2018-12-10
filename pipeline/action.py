'''
Schema of session information.
'''
import datajoint as dj
from pipeline import reference, subject

schema = dj.schema('ttngu207_action',locals())

@schema
class Weighing(dj.Manual):
    definition =  """
    -> subject.Subject
    ---
    weight_before: float   # in grams
    weight_after: float    # in grams
    """

@schema
class WhiskerConfig(dj.Manual):
    definition = """
    -> subject.Subject
    ---
    -> reference.Whisker
    """

@schema
class VirusInjection(dj.Manual):
    definition = """
    -> subject.Subject
    -> reference.Virus
    -> reference.BrainLocation
    -> reference.Hemisphere
    injection_date: date   
    ---
    injection_volume: float # in nL
    injection_coordinate_ap: float   # in mm, negative if posterior, positive if anterior
    injection_coordinate_ml: float   # in mm, always positive, larger number if more lateral
    injection_coordinate_dv: float   # in mm, always positive, larger number if more ventral (deeper)
    -> reference.CoordinateReference.proj(injection_coordinate_ref="coordinate_ref")
    """
