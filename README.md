# data-visualisation

A proof of concept for data-visualisation using D3.js

Check it out at https://sqbl.github.io/data-visualisation/



# Hand waving explanation of data acquisition.

Imagine having a huge pile of timber-wood (imagine the pile to be really huge, like 6.023 x 10^23-huge). Your task is to attach exactly two nails to every individual piece of timber. 
There are nails enough – they are supplied to you in a steady stream, so that we have always a few nails around.
Now, imagine that the timbers can only be “nailed” in four different positions. Two of these are markedly more likely to be nailed than the remaining two places. (let’s call the timber “Backbone” (BB), and the four possible mono-nailed timbers “NA”, “NB”, “K1” and “K2”. K1 and K2 are assumed to be >10-times more likely compared to NA and NB)

Now, let a blindfolded carpenter start hitting nails in timbers at random, we assume that the carpenter cannot know if a particular timber already contains a nail.
For how long should the carpenter be allowed to entertain this madness in order to end with the highest percentage of dual-nailed timbers?

For the mathematically inclined reader, we could describe the speed of nailing by a constant for each of the four positions multiplied by the availability of the timber and the nails.

speed = rate-constant * [timber] * [nails]

Because of the assumption of nails being constantly present in a small surplus, we can omit [nails] from above when comparing speeds of different nail-positions. As such, the speed for producing the K1-mono nailed timber at any time is:

speed(K1) = rate-constant(K1) * [timber(Backbone)]

yet, the K1-mono-nailed timber is also consumed by the blind carpenter. So the overall rate of change of the current amount of this species is given as the sum of its production (above) with the negated sum of its consuming “reactions” (e.g. when the blind carpenter takes a K1-mono nailed timber to add another nail).
This leads to a large number of coupled differential equations in which the concentration of all different types of timbers (with various degrees of nailed-ness) is calculated for the timescale of the nail-madness. Solving these equations by fitting the data to real world observations gives the individual rate-constants.
The approach with solving differential equations can be describes as the blind carpenters point of view (or lack of same…) in which all types of timbers interconvert in a set speed.



An alternative approach is by the use of transition probability. In other words: Now, we observe the probability of a specific piece of timber to be picked up by the carpenter and the probability of the carpenter to nail a specific position of the specific piece of timber. Framed in these words, it is highly likely for a piece of timber to NOT be picked up at any specific time. Should a timber be picked up it is slightly more likely to be nailed in these positions in descending order: K1>K2>NB>NA (Note that not all products can be made from all timbers, i.e. an un-nailed timber cannot produce a dual-nailed timber in one operation).
When the timber is nailed it is thrown back into the pile of timbers to wait for its chance to be picked up again.
These probabilities can be modelled over observed data to give a transition probability matrix describing the probability of all species to be transformed into any of the other species (many of which are 0). 

If we now assume that the carpenter is still in supply of nails and that he is nailing timbers at a constant pace, we can simulate the life of a specific piece of timber. We consider the multinomial distribution given by the current state of the timber in the transition probability matrix and determine whether the timber is picked up and in that case, in which position the nail is placed (Search for “Random Walk” or “Markov Chain”).

By performing 1000 of these simulations, we can visualise the blind carpenters work.

Code for solving differential equations and building/using a transition probability matrix is made in Python. Plotting is performed with D3.js.

(
Fitting of diff equa: http://adventuresinpython.blogspot.com/2012/08/fitting-differential-equation-system-to.html
Using transition probability: https://martin-thoma.com/python-markov-chain-packages/
Animation: https://flowingdata.com/2015/12/15/a-day-in-the-life-of-americans/ 
)

