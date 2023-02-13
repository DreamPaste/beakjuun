// 재귀의 귀재

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int cnt = 0;

int recursion(const char *s, int l, int r)
{
    cnt++;
    if (l >= r)
        return 1;
    else if (s[l] != s[r])
        return 0;
    else
        return recursion(s, l + 1, r - 1);
}

int isPalindrome(const char *s)
{
    
    return recursion(s, 0, strlen(s) - 1);
    
}

int main()
{

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cnt = 0;
        char s[1001];  //항상 문자열의 길이보다 1 길게
        cin >> s;

        cout << isPalindrome(s)<< " ";
        cout << cnt <<"\n";

    }
}
