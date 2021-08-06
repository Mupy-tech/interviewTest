5. wrtie a function that takes in a string as input and returns true if it is a palingle or not
Answer:

var re = /[^A-Za-z0-9]/g; 
 str = str.toLowerCase().replace(re, '');


 var len = str.length; 
 
 for (var i = 0; i < len/2; i++) {
   if (str[i] !== str[len - 1 - i]) { 
       return false; 
   }
}
return true; 
}

palindrome("A man, a plan, a canal. Panama");