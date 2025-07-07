function solution(num_list) {
    const product = num_list.reduce((acc, cur) => acc * cur, 1);
    const sum = num_list.reduce((acc, cur) => acc + cur, 0);
    
    if (product < sum*sum) {
        return 1;
    }
    return 0;
}