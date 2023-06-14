function isPalindrome(number){
    if(typeof number !== 'number') return '${number} is not a number';
    
    number = number.toString().split('');
    
    for(var i = 0; i < (number.length / 2); i++){
       if(number[i] !== number[number.length - 1 - i]){
        return false;
       } 
    }
    
    
  return true;
}

function largestPalindrome(){
    let largest = 0;

    for(let x = 999; x >= 100; x--){
      for(let y = 999; y >= 100; y--){
        let product = x * y;
        if(isPalindrome(product) && product > largest){
            largest = product;
      }
    }

}
 return largest;  
}

console.log(largestPalindrome());
