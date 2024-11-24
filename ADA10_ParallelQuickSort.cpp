//Implementing Parallel Quick Sort

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <omp.h>

using namespace std;

class QSMultiThreading 
{
    private:
        int strt_;
        int end_;
        vector<int>& arr_;

    public:
        QSMultiThreading(int strt, int end, vector<int>& arr) 
            : strt_(strt), end_(end), arr_(arr) {}
        
        int partition(int strt, int end, vector<int>& arr) 
        {
            int i = strt;
            int j = end;

            int pivoted = rand() % (j - i + 1) + i;

            swap(arr[j], arr[pivoted]);
            j--;

            while (i <= j) 
            {
                if (arr[i] <= arr[end]) 
                {
                    i++;
                    continue;
                }
                if (arr[j] >= arr[end]) 
                {
                    j--;
                    continue;
                }
                swap(arr[i], arr[j]);
                j--;
                i++;
            }

            swap(arr[j + 1], arr[end]);

            return j + 1;
        }

        void operator() () 
        {
            if (strt_ >= end_) 
            {
                return;
            }

            int p = partition(strt_, end_, arr_);

            QSMultiThreading left(strt_, p - 1, arr_);
            QSMultiThreading right(p + 1, end_, arr_);

            #pragma omp parallel sections
            {
                #pragma omp section
                {
                    left();
                }
                #pragma omp section
                {
                    right();
                }
            }
        }

};

int main() 
{
    srand(time(NULL));

    int n;
    cout << "Enter num of elements: ";
    cin >> n;
    vector<int> arr(n);

    cout << "Enter elements: ";

    for (int i = 0; i < n; ++i) 
    {
        cin >> arr[i];
    }

    QSMultiThreading(0, n - 1, arr)();

    cout << "Sorted array: ";
    for (int i = 0; i < n; ++i) 
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
