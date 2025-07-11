class train:

    def __init__(self, trainNo):
        self.trainNo= trainNo

    def BookTicket(self):
        print(f"Ticket is booked in train no. {self.trainNo}")


    def get_status(self):
        seats=50
        print(f"No. of seats available in train no. {self.trainNo} is {seats}")

    def get_fare(self,fro,to):
        p=1000
        print(f"fare of ticket {p} in train no. {self.trainNo} from {fro} to {to}")

T = train(12399)
T.BookTicket()
T.get_status()
T.get_fare("jaipur","delhi")