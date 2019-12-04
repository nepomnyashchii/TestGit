let arr = [1, 2, 3, 4, 5];

arr.forEach(item => {
    if(item == 3) {
        arr.shift();
    }
    console.log(item);
});