let isPalindrome = function(s) {
  let validLetters = "abcdefghijklmnopqrstuvwxyz0123456789";
  let lettersOnlyStr = "";

  for(let char of s){
      if(validLetters.includes(char.toLowerCase())){
          lettersOnlyStr += char.toLowerCase();
      }
  }

  let left = 0;
  let right = lettersOnlyStr.length - 1;
  while(left < right ){
      if(lettersOnlyStr[left] !== lettersOnlyStr[right]){
          return false
      }
      left++;
      right--;
  }

  return true;

};