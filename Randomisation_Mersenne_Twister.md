THE MERSENNE TWISTER

The Mersenne Twister is a general-purpose pseudorandom number generator (PRNG) developed in 1997 by Makoto Matsumoto [ja] (松本 眞) and Takuji Nishimura (西村 拓士). Its name derives from the fact that its period length is chosen to be a Mersenne prime.

The Mersenne Twister was designed specifically to rectify most of the flaws found in older PRNGs.

The most commonly used version of the Mersenne Twister algorithm is based on the Mersenne prime {\displaystyle 2^{19937}-1}{\displaystyle 2^{19937}-1}. The standard implementation of that, MT19937, uses a 32-bit word length. There is another implementation (with five variants) that uses a 64-bit word length, MT19937-64; it generates a different sequence.

Software
The Mersenne Twister is used as default PRNG by the following software:

Programming languages: 

Dyalog APL, IDL, R,Ruby, Free Pascal, PHP, Python (also available in NumPy, however the default was changed to PCG64 instead as of version 1.17), CMU Common Lisp, Embeddable Common Lisp, Steel Bank Common Lisp, Julia,
Linux libraries and software: GLib, GNU Multiple Precision Arithmetic Library, GNU Octave,GNU Scientific Library,
Other: Microsoft Excel, GAUSS, gretl, Stata., SageMath, Scilab, Maple,MATLAB,
It is also available in Apache Commons, in the standard C++ library (since C++11), and in Mathematica. Add-on implementations are provided in many program libraries, including the Boost C++ Libraries, the CUDA Library, and the NAG Numerical Library.

The Mersenne Twister is one of two PRNGs in SPSS: the other generator is kept only for compatibility with older programs, and the Mersenne Twister is stated to be "more reliable". The Mersenne Twister is similarly one of the PRNGs in SAS: the other generators are older and deprecated. The Mersenne Twister is the default PRNG in Stata, the other one is KISS, for compatibility with older versions of Stata.

  more->  https://en.wikipedia.org/wiki/Mersenne_Twister
