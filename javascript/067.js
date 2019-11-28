var myData = 123; 
if (true) { 
    (function () { // create a new scope 
        var myData = 456;
     })(); 
} 
console.log(myData); // 123; 


var myData = 123; 
if (true) {
   var myData = 456; 
} 
console.log(myData); // 456; 