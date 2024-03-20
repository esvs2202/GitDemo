# script to compute the profit margin

class ProfitMarginCalculator:
    def __init__(self, investment, revenue, operating_expenditure):
        self.investment = investment
        self.revenue = revenue
        self.operating_expenditure = operating_expenditure
        
    def compute(self):
        pm = (self.revenue - self.investment)*100/self.revenue 

        np = self.revenue - (self.investment+self.operating_expenditure)

        npm = (np*100)/self.revenue

        r1 = f"Your Gross profit margin = {round(pm,2)}%"
        r2 = f"Your Net profit in rupees = {np}"
        r3 = f"So, your net profit margin = {round(npm,2)}%"

        return r1, r2, r3
