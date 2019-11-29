// try {
//     setTimeout(function(){
//         var err = new Error('example')
//         throw err
//     }, 1000)
// }
// catch (err) {
//     // Example error won't be caught here... crashing our app
//     // hence the need for domains
// }



var validateObject = function (obj) {
    if (typeof obj !== 'obj') {
        throw new Error('Invalid object');
    }
};

try {
    validateObject('123');
}
catch (err) {
    console.log('Thrown: ' + err.message);
}