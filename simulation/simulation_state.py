class SimulationState:
    def __init__(self):
        self.active = False  # Indicates if the simulation is active

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def reset(self):
        self.active = False
        # Logic to reset the simulation's internal state was here

# We instantiate a global state object to be shared across modules
simulation_state = SimulationState()
