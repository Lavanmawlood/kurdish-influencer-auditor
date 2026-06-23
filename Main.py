# Kurdish Influencer Auditor (Kurdistan Market Dynamic Model)

market_data = [
    {"username": "payam.shexazerd", "followers": 233000, "likes": 42290, "comments": 1476},
    {"username": "soma_a_mustafa_", "followers": 87500, "likes": 15360, "comments": 842},
    {"username": "kurd_hitech", "followers": 66000, "likes": 21580, "comments": 1500}
]

class MarketAuditor:
    def __init__(self, username, followers, total_likes, total_comments):
        if followers <= 0:
            raise ValueError("Followers must be positive.")
        self.username = username
        self.followers = followers
        self.avg_likes = total_likes / 10
        self.avg_comments = total_comments / 10
        self.er = 0.0
        self.investment_safety = ""

    def run_audit(self):
        total_interaction = self.avg_likes + self.avg_comments
        self.er = (total_interaction / self.followers) * 100
        
        if self.er < 3.0:
            self.investment_safety = "🚨 RISK (Low Interaction)"
        elif 3.0 <= self.er <= 6.0:
            self.investment_safety = "✅ SAFE (Good Engagement)"
        else:
            self.investment_safety = "🔥 PREMIUM (High Conversion)"

    def generate_row(self):
        bar_len = int(self.er * 2)
        visual_bar = "🟩" * bar_len if bar_len > 0 else "⬜"
        return f"@{self.username:<17} | ER: {self.er:>5.2f}% | {self.investment_safety:<26} | {visual_bar}"


if __name__ == "__main__":
    print("\n" + "="*85)
    print("📋            INFLUENCER AUDIT REPORT (KURDISTAN MARKET)            ")
    print("="*85)
    
    for item in market_data:
        auditor = MarketAuditor(item["username"], item["followers"], item["likes"], item["comments"])
        auditor.run_audit()
        print(auditor.generate_row())
        
    print("="*85 + "\n")
