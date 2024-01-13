import pandas as pd

class DataCollector:
    def __init__(self):
        self.data = {
            'total_production': [],
            'compliance_levels': [],
        }
    
    def collect(self, farmers):
        total_production = sum([farmer.production for farmer in farmers])
        compliance_levels = [farmer.compliance for farmer in farmers]
        self.data['total_production'].append(total_production)
        self.data['compliance_levels'].append(compliance_levels)

    def to_dataframe(self):
        return pd.DataFrame(self.data)
        
    def reset(self):
        self.data = {
            'total_production': [],
            'compliance_levels': [],
        }
