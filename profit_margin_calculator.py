# script to compute the profit margin

class ProfitMarginCalculator:
    def __init__(self, investment, revenue):
        self.investment = investment
        self.revenue = revenue 
        
    def compute(self):
        pm = (self.revenue - self.investment)*100/self.revenue 
        
        s = f"Your profit margin is {round(pm,2)}%"
        return s
