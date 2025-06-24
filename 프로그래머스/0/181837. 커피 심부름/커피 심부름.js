function solution(order) {
    
  const PRICE = {
        americano: 4500,
        cafelatte: 5000,
     };

  const result =  order.reduce((total, menu) => {
    
    if (menu === 'anything') {
      return total + PRICE.americano;
      }
      
    if (menu.includes('americano')) {
      return total + PRICE.americano;
      }
      
    return total + PRICE.cafelatte;
  }, 0);
    
  return result;
    
}