class BoutResult:
    def __init__(self, fencer_name: str, score: tuple[int, int], opponent: str, victory: bool, is_pool: bool):
        self.name = fencer_name
        self.score = score
        self.opponent = opponent
        self.victory = victory
        self.is_pool = is_pool

    def swap_order(self):
        first, second = self.score
        self.score = (second, first)
        fencer = self.name
        opponent = self.opponent
        self.name = opponent
        self.opponent = fencer


class TotalResult:
    def __init__(self, name: str):
        self.name = name
        self.pool_bouts = []
        self.de_bouts = []

    def add_pool(self, bout: BoutResult):
        self.pool_bouts.append(bout)

    def add_de(self, bout: BoutResult):
        self.de_bouts.append(bout)
