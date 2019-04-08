class Proccess:
    procCount = 0

    def __init__(self, arrival_t, duration, name, priority):
        self.priority = priority
        self.arrival_t = arrival_t
        self.duration = duration
        self.name = name
        Proccess.procCount += 1

# an array of Proccess objects should be passed to each scheduler function
