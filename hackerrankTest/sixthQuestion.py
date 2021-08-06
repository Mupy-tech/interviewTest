6.  write a function that takes in an array and returns true if the array contains any duplicate value or false otherwise

Answer;

function checkIfArrayIsUnique(myArray) 
    {
        for (var i = 0; i < myArray.length; i++) 
        {
            for (var j = 0; j < myArray.length; j++) 
            {
                if (i != j) 
                {
                    if (myArray[i] == myArray[j]) 
                    {
                        return true; 
                    }
                }
            }
        }
        return false; 
    }
