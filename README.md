These are my solutions to the implementations proposed in the ["The Elements of Computing Systems"](https://mitpress.mit.edu/books/elements-computing-systems) book.

The following table lists the total number of Nand gates and D flip-flops used by the current implementation of the chips. (calculated using the [gate_counter.py](https://github.com/ronaldotd/tecs/blob/master/gate_counter.py) script)

|Chip|Nand count|DFF count|Total|
|---|--:|--:|--:|
|Not|1|0|1|
|And|2|0|2|
|Or|3|0|3|
|DMux|5|0|5|
|Mux|8|0|8|
|Xor|9|0|9|
|Bit|8|1|9|
|HalfAdder|11|0|11|
|DMux4Way|15|0|15|
|Not16|16|0|16|
|Or8Way|21|0|21|
|FullAdder|25|0|25|
|And16|32|0|32|
|DMux8Way|35|0|35|
|Or16|48|0|48|
|Mux16|128|0|128|
|Register|128|16|144|
|Mux4Way16|384|0|384|
|Add16|400|0|400|
|Inc16|400|0|400|
|Mux8Way16|896|0|896|
|ALU|1294|0|1294|
|RAM8|1955|128|2083|
|RAM64|16571|1024|17595|
|RAM512|133499|8192|141691|
|RAM4K|1068923|65536|1134459|
|RAM16K|4276091|262144|4538235|
