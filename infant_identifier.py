class InfantIdentifier:
    def __init__(self):
        self.height_threshold = 1.2
        self.weight_threshold = 15
        self.movement_threshold = 0.1
        self.identifiers = set()

    def identify_infants(self, sensor_data):
        infants = []
        for data_point in sensor_data:
            identifier = f"{data_point.height}-{data_point.weight}-{data_point.movement}"
            if identifier not in self.identifiers:
                self.identifiers.add(identifier)
                if (data_point.height < self.height_threshold and
                        data_point.weight < self.weight_threshold and
                        data_point.movement < self.movement_threshold):
                    infants.append(data_point)
        return infants
