class Proccess:
    total_time = 0

    def __init__(self, arrival_t, duration, name, priority):
        self.priority = priority
        self.arrival_t = arrival_t
        self.duration = duration
        self.name = name
        Proccess.total_time += self.duration

# an array of Proccess objects should be passed to each scheduler function
