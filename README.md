# genetic
Basic genetic algorithm

# Dependencies

Be sure to have matplotlib installed. If you don't, you can install it like that :

```shell
python3 -m pip install matplotlib
```

# Usage

```shell
python3 genetic.py [options]
```

You can specify the following options : 

    -v, --verbose:
        If specified the last population will be printed out in the terminal.
    -p, --population-size [integer]:
        The size of the population that will be use in the genetic algorithm.
    -u, --individual-size [integer]
        The number of gene of each individual member of the population.
    -d, --delta [float]
        A value for the convergence detection. The less this value will be, the longer the algorithm will take to stop but the greater the average fitness value will be.
        This value must be less than 1.
