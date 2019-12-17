Framework for reinforcement learning
====================================

A framework for reinforcement learning based on the OpenAi environment and tensorflow 2.0.

Usage:
------

- Install Anaconda, I would also recommend to install pycharm.
- Create a virtual environment with ``conda create -n tf2 python=3.7``
- Activate it with ``conda activate tf2``, then install all required packages with ``pip install -r requirements.txt``


Roadmap
-------

Agents and roadmap
~~~~~~~~~~~~~~~~~~

- [ ] General framework outline
- [ ] Deep Q Learning (DQN)
- [ ] Double DQN
- [ ] n-step montecarlo
- [ ] Deep SARSA
- [ ] Asynchronous Advantage Actor-Critic (A3C) [



How to integrate your code on Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It will be hard for one person alone to beat the world at poker. That's
why this repo aims to have a collaborative environment, where models can
be added and evaluated.

To contribute do the following:

- Get Pycharm and build the virtual python environment. Use can do: ``pip install -r requirements.txt``
- If you want to use the 500x faster c++ based equity calculator, also install visual studio, but this is not necessary
- Clone your fork to your local machine. You can do this directly from pycharm: VCS --> check out from version control --> git
- Add as remote the original repository where you created the fork from and call it upstream (the connection to your fork should be called origin). This can be done with vcs --> git --> remotes
- Create a new branch: click on master at the bottom right, and then click on 'new branch'
- Make your edits.
- Ensure all tests pass. Under file --> settings --> python integrated tools switch to pytest (see screenshot). |image1| You can then just right click on the tests folder and run all tests. All tests need to pass. Make sure to add your own tests by simply naming the funtion test\_... \
- Make sure all the tests are passing. Best run pytest as described above (in pycharm just right click on the tests folder and run it). If a test fails, you can debug the test, by right clicking on it and put breakpoints, or even open a console at the breakpoint: https://stackoverflow.com/questions/19329601/interactive-shell-debugging-with-pycharm
- Commit your changes (CTRL+K}
- Push your changes to your origin (your fork) (CTRL+SHIFT+K)
- To bring your branch up to date with upstream master, if it has moved on: rebase onto upstream master: click on your branch name at the bottom right of pycharm, then click on upstream/master, then rebase onto. You may need to resolve soe conflicts. Once this is done, make sure to always force-push (ctrl+shift+k), (not just push). This can be done by selecting the dropdown next to push and choose force-push (important: don't push and merge a rebased branch with your remote)
- Create a pull request on your github.com to merge your branch with the upstream master.
- When your pull request is approved, it will be merged into the upstream/master.