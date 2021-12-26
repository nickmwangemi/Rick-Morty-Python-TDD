from rick import Rick


class Citadel(object):
    def __init__(self):
        self._residents = []

    def get_all_residents(self):
        return self._residents

    def add_resident(self, resident):
        self._residents.append(resident)

    def pickle_ricks_with_morties(self):
        for resident in self._residents:
            if isinstance(resident, Rick):
                if resident.morty:
                    resident.is_pickle = True
