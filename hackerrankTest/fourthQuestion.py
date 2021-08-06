4.  write a function that takes an array and integer as input. return any two numbers in the array that 
when sum up will be equal to the value of the integer
Answer:

function amountTotal(amount) {
    var total = 0;
    for (i = 0; i < amount.length; ++i) {
         total += amount[i];
    }
    return total;
}
