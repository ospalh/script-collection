#include <ctime>
#include <iostream>

int main()
{
   int size;
   size = sizeof(time_t);
//  printf("time_t ist %d bytes lang.\n",size);
   std::cout << "time_t ist " << size << " chars lang.\n";
   if (size == 4)
   {
      std::cout << "Das Ende naht!\n";
   }
   else if (size == 8)
   {
      std::cout <<  "Keine Panik!\n";
   }
   else
   {
      std::cout << "Huch!\n";
   }

   return 0;
}
