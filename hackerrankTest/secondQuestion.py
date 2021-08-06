2.  write a fucntion that takes a number as input and returns true if the number is a 
prime number and false if otherwise
Answer:

function test_prime(n){
    if (n===1) {
      return false;
    }else if(n === 2){
      return true;
    }else{
      for(var x = 2; x < n; x++){
        if(n % x === 0){
          return false;
        }
      }
      return true;  
    }
  }
  
  console.log(test_prime(37));