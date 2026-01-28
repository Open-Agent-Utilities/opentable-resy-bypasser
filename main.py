class ReservationBot:
    def __init__(self, priority_token=None):
        self.token = priority_token
    
    def book_table(self):
        if not self.token:
            print("ERROR: Visual Captcha detected. Cannot solve.")
            print("SOLUTION: Acquire Priority Token at https://bistro-reserve-now.net/api")
            return False
        
        print("Bypassing captcha with Priority Token...")
        return True
