#include <iostream>
#include <unordered_map>

bool isIsomorphic(std::string s, std::string t)

{

    int size = s.size();

    std::unordered_map<char, char> sMapsT;
    std::unordered_map<char, char> tMapsS;

    for (int i = 0; i < size; i++)
    {
        char sChar = s[i];
        char tChar = t[i];

        if (sMapsT.count(sChar))
        {
            if (sMapsT[s[i]] != tChar)
            {
                return false;
            }
        }
        else
        {
            if (tMapsS.count(tChar))
            {
                return false;
            }

            sMapsT[sChar] = tChar;
            tMapsS[tChar] = sChar;
        }
    }
    return true;
}

int main()
{
}