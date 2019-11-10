# genetic
Basic genetic algorithm

# Dependencies

Be sure to have matplotlib installed. If you don't, you can install it like that :

```shell
python -m pip install matplotlib
```

# Usage

```shell
python genetic.py [options]
```

You can specify the following options : 

    -p, --population-size [integer]:
        The size of the population that will be use in the genetic algorithm.
    -u, --individual-size [integer]
        The number of gene of each individual member of the population.
    -d, --delta [float]
        A value for the convergence detection. The less this value will be, the longer the algorithm will take to stop but the greater the average fitness value will be.
        This value must be less than 1.
