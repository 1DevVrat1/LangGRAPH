# Placeholder for custom memory logic
class SimpleMemory:
    def __init__(self):
        self.state = {}

    def get_state(self, key):
        return self.state.get(key, [])

    def update_state(self, key, value):
        self.state[key] = value
