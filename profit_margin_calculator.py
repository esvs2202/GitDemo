# script to compute the profit margin

class ProfitMarginCalculator:
    ''' Developed by Sriram ESV on March 20, 2024 '''
    def __init__(self, investment, revenue, operating_expenditure, tax):
        self.investment = investment
        self.revenue = revenue
        self.operating_expenditure = operating_expenditure
        self.tax = tax

    def compute(self):
        pm = (self.revenue - (self.investment + self.tax*self.revenue))*100/self.revenue

        np = self.revenue - (self.investment+self.operating_expenditure+self.tax*self.revenue)

        npm = (np*100)/self.revenue

        r1 = f"Your Gross profit margin = {round(pm,2)}%"
        r2 = f"Your Net profit in rupees = {round(np,2)}"
        r3 = f"So, your net profit margin = {round(npm,2)}%"

        return r1, r2, r3

