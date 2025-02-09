class Game:
    def __init__(self, game_name):
        self.game_name = game_name
        self.score = 0
    
    def add_points(self, points):
        self.score += points
        print(f"+{points} points! Total: {self.score}")
    
    def game_over(self):
        print(f"Game Over! Final Score in {self.game_name}: {self.score}")
    
# Example usage
if __name__ == "__main__":
    battlement = Game("Battlement")
    battlement.add_points(10)
    battlement.add_points(5)
    battlement.game_over()
    
    trashcan = Game("TrashCan")
    trashcan.add_points(8)
    trashcan.add_points(3)
    trashcan.game_over()
