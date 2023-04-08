class Turing_Machine:
    def __init__(self, delta, q0, qa, qr, input):
        """Turing Machine class where we assume all input is of the correct type."""
        self.q0 = q0
        self.qa = qa
        self.qr = qr
        self.delta = delta  # delta : Q x Gamma -> Q x Gamma x {L, R}
        # TODO: Turn configuration into array instead of string
        self.configuration = f"fff{q0}{input}_"
        self.currState = "q00"
        self.head = 3
        self.q_len = 3 # We define our states to be of the form q followed by a 2 digit number

    def make_move(self):
        (q_, gamma_, lr) = self.delta(self.currState, self.configuration[self.head])
        if (lr == 'L'):
            self.move_left(q_, gamma_)
        else:
            self.move_right(q_, gamma_)
        self.print_config
        if self.currState == self.qa:
            return 'accept'
        if self.currState == self.qr:
            return 'reject'

    def move_left(self, q_, gamma_):
        if (self.head == 0):
            print("Already at edge of tape")
        else:
            self.configuration[self.head + self.q_len] = gamma_
            self.configuration[self.head + self.q_len - 1] = self.configuration[self.head - 1]
            self.configuration[self.head - 1: self.head + self.q_len - 1] = q_
            self.currState = q_
            self.head -= 1
            
    def move_right(self, q_, gamma_):
        pass

    def print_config(self):
        print(self.configuration)


def mock_delta(x, y):
    return ("q00", "_", 'L')


M = Turing_Machine(mock_delta, "q00", "qaa", "qrr", "Hello world")
M.print_config()
M.make_move()
