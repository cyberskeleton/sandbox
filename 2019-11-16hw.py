def increment(self, key):
    if key not in self.keys():
        self[key] = 1
    else:
        self[key] += 1

tests = int(input('input test quantity: '))

results = []
for i in range(tests):
    vote_dict = {}
    votes = int(input('input vote quantity: '))
    for j in range(votes):
        number = input('input test #' + str(i) + ' vote #' + str(j) + ': ')
        increment(vote_dict, number)

    max_key = 1001
    max_val = 0
    for key, value in vote_dict.items():
        if value > max_val:
            max_val = value
            max_key = int(key)
        elif value == max_val and int(key) < max_key:
            max_key = int(key)
    results.append(max_key)

for i in range(len(results)):
    print(results[i])
