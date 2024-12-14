from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    no_vaccinated = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            no_vaccinated += 1    
        except NotWearingMaskError:
            masks_to_buy += 1
    if no_vaccinated > 0:
        return ("All friends should be vaccinated")
    if masks_to_buy > 0:
        return (f"Friends should buy {masks_to_buy} masks")
    return (f"Friends can go to {cafe.name}")
