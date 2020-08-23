# README ThreeSum

This repository is meant as a skeleton to experimentally analyse different algorithms.
The example is the 3-sum problem, i.e., given a list of integers, are there 3 different positions whose values add to 0
(cf. Sedgewick Wayne, Chapter 1.4).

You are invited to use this skeleton to make sure your toolchain is ready to do similar experiments. Please check the installation guide in the `software.md` file.

Here are some tasks:

- Fork (or duplicate, I am not sure what is better) this repository
- Clone your duplicate to your local machine (or your cloud server or whatever machine you play with)
- Compile the LaTeX source with `pdflatex report-threesum.tex`.  This checks your LaTeX installation.
- Add yourself as an author (attributing the original source).
- Rerun the experiments with `python3 experiment.py`.  For this to  work, you need `python3` and a java installation (at least). Furthermore, we use the `algs4` library from the Sedgewick/Wayne book. Please refer to `software.md` for a full installation guide.
- The current time limit for stopping an experiment is 30 seconds.  For the purpose of playing with the script, recduce it to 3
  Every time you run the `experiment.py` script, it creates a new folder.  
  Once you are happy with the experiment (for a start: it does not fail, only installed software is used)
- Recompile the LaTeX source (don't forget to adjust the tables directory)
- adjust the constant factors at the helper lines in the plot to reflect your machine
- Implement a variant, let's say the version with binary search and include it into the experiments

We will use the first exercise slot to help you setting up the tool chain on your machine.
