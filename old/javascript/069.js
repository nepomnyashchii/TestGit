function foo() {
    console.log('2000 milliseconds have passed since this demo started'); 
}
setTimeout(foo); 
foo();



function outerFunction(arg) { 
    var variableInOuterFunction = arg;
    function myValue() { 
       console.log(variableInOuterFunction);
    }
    myValue(); 
} 
outerFunction('hello closure!'); // logs hello closure! 