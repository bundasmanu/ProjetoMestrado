from .config import DATASCIENTIST_GROUP, HEALTH_CARE_GROUP

def getNameGroup(charGroup):
    try:
        if charGroup == "A":
            return "Admin"
        elif charGroup == "D":
            return DATASCIENTIST_GROUP
        elif charGroup == "H":
            return HEALTH_CARE_GROUP
        else:
            return None
    except:
        raise