Attempt to create a Python implementation of the Simulink engine (graphical features are low development priorities).


# scipy-sim

Originally taken from https://code.google.com/p/scipy-sim/:

ScipySim is a very early prototype of a graphical block-diagram tool for modelling and simulating heterogeneous systems using Python and Scipy. The current prototype has the core simulation engine in place, and allows simulation models to be constructed by writing Python scripts that connect together blocks that represent different component behaviours. Graphical definition of models isn't yet supported though.

For an overview of the design of ScipySim, and where things may be headed in the future, see our TMS/DEVS 2011 conference paper:

Allan McInnes and Brian Thorne, "ScipySim: Towards Distributed Heterogeneous System Simulation for the SciPy Platform", Proc. TMS/DEVS 2011.
The ScipySim project is inspired by the Ptolemy project. However, we are taking a slightly different approach to implementing the simulation engine: we are exploring the idea, originally suggested by Benveniste et al., of implementing the simulator as a Kahn-like network of actors that communicate via tagged-signals. In addition to being a more faithful representation of the tagged-signal model for heterogeneous systems, this approach appears to hold some promise for easy implementation of parallel and distributed simulations. It has also opened up some interesting new research directions in the area of discrete-event simulation.

See also http://bitsofpy.blogspot.com/2009/12/scipy-simulator.html
