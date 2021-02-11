# Rainbow-Crack

# what is RainbowCrack ?

***RainbowCrack*** is a computer program which generates [rainbow tables](https://en.wikipedia.org/wiki/Rainbow_table) to be used in [password cracking](https://en.wikipedia.org/wiki/Password_cracking). RainbowCrack differs from "conventional" [brute force](https://en.wikipedia.org/wiki/Brute-force_attack) crackers in that it uses large pre-computed tables called rainbow tables to reduce the length of time needed to crack a password drastically.RainbowCrack was developed by Zhu Shuanglei, and implements an improved [time–memory tradeoff cryptanalysis](https://en.wikipedia.org/wiki/Time%E2%80%93memory_tradeoff) attack which originated in Philippe Oechslin's [Ophcrack](https://en.wikipedia.org/wiki/Ophcrack).

Some organizations have made RainbowCrack's rainbow tables available free over the internet.

***wikipedia source*** : [click here](https://en.wikipedia.org/wiki/RainbowCrack)
------

# some more info:

If someone hacks the x function, it will not reach your real password.

We have different functions for hash. Each hash function works in a specific form. (Note: All passwords are 4 digits and digits can be numbers from 0 to 9.

We also know that the sha256 algorithm is used for hashing.) So you are expected to be able to open this file and extract the file information Separate and specify the name and password associated with it. In fact, it is enough to write a for loop that works from 0-9999, for example.

Each time it encrypts the desired number with the above algorithm and returns a string and compares this string with the codes given in the file and if the number is equal to this string is stored as a password in the output.

-----

the input of the csv file is something like this :

`danial,99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974`

`elham,85432a9890aa5071733459b423ab2aff9f085f56ddfdb26c8fae0c2a04dce84c`

and the to output of the program should look like this : 

`danial,5104`

`elham,9770`
