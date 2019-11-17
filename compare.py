from simulation import Simulation

select_roulette_population_record   = []
select_tournament_population_record = []
iteration = 50
population_size = 3000
individual_size = 35
cross_points = 1
delta = 0.005

print("Roulette")
for _ in range(0, iteration):
    print(_)
    simu = Simulation(
        population_size, 
        individual_size, 
        cross_points, 
        delta, 
        selection_mode=Simulation.SELECTION_ROULETTE
    )
    simu.run_simulation()
    print(simu.population.get_global_fitness(True))
    select_roulette_population_record.append(simu.generation)

print("Tournament")
for _ in range(0, iteration):
    print(_)
    simu = Simulation(population_size,
        individual_size,
        cross_points,
        delta,
        selection_mode=Simulation.SELECTION_TOURNAMENT
    )
    simu.run_simulation()
    print(simu.population.get_global_fitness(True))
    select_tournament_population_record.append(simu.generation)

print(select_roulette_population_record)
print(select_tournament_population_record)
